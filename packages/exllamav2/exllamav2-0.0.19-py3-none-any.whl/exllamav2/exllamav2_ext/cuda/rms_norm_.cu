#include "rms_norm.cuh"
#include "util.cuh"
#include "compat.cuh"

#if defined(USE_ROCM)
#define NUM_WARPS (512 / warpSize)
#define WARP_SIZE (warpSize)
#else
#define NUM_WARPS 8
#define WARP_SIZE 32
#endif

// y = x * w / sqrt(row_mean(x * x) + epsilon)

#define NUM_THREADS (NUM_WARPS * WARP_SIZE)

typedef void (*fp_rms_norm_kernel)
(
    const half*,
    const half*,
    half*,
    const float,
    const float,
    const int,
    const int
);

typedef struct __align__(16)
{
    half2 x;
    half2 y;
    half2 z;
    half2 w;
} half8;

template <int blocks_per_warp>
__global__ void rms_norm_kernel
(
    const half* __restrict__ x,
    const half* __restrict__ w,
    half* __restrict__ y,
    const float epsilon,
    const float r_dim,
    const int rows,
    const int dim
)
{
    int warp_id = threadIdx.x / WARP_SIZE;
    int lane_id = threadIdx.x % WARP_SIZE;
    int row = blockIdx.x;
    const half8* x_row = (const half8*) (x + row * dim);
    half8* y_row = (half8*) (y + row * dim);
    const half8* w8 = (const half8*) w;

    // Compute sum of squares for each block

    float sum = 0.0f;
    float itemf[blocks_per_warp][8];

    #pragma unroll
    for (int i = 0; i < blocks_per_warp; i++)
    {
        int column = warp_id * WARP_SIZE + lane_id + NUM_THREADS * i;
        if (column >= dim / 8) break;

        half8 x8;
        ((uint4*)&x8)[0] = ((uint4*)x_row)[column];

        itemf[i][0] = __half2float(__low2half(x8.x));
        itemf[i][1] = __half2float(__high2half(x8.x));
        itemf[i][2] = __half2float(__low2half(x8.y));
        itemf[i][3] = __half2float(__high2half(x8.y));
        itemf[i][4] = __half2float(__low2half(x8.z));
        itemf[i][5] = __half2float(__high2half(x8.z));
        itemf[i][6] = __half2float(__low2half(x8.w));
        itemf[i][7] = __half2float(__high2half(x8.w));
        sum = fma(itemf[i][0], itemf[i][0], sum);
        sum = fma(itemf[i][1], itemf[i][1], sum);
        sum = fma(itemf[i][2], itemf[i][2], sum);
        sum = fma(itemf[i][3], itemf[i][3], sum);
        sum = fma(itemf[i][4], itemf[i][4], sum);
        sum = fma(itemf[i][5], itemf[i][5], sum);
        sum = fma(itemf[i][6], itemf[i][6], sum);
        sum = fma(itemf[i][7], itemf[i][7], sum);
    }

    // Shuffle to sum across lanes

    __shared__ float sums[NUM_WARPS];

    for(int offset = warpSize / 2; offset > 0; offset /= 2) sum += __shfl_xor_sync(0xffffffff, sum, offset);
    if (lane_id == 0) sums[warp_id] = sum;
    __syncthreads();

    // Load partial sums from across warps, shuffle again across lanes

    sum = lane_id < NUM_WARPS ? sums[lane_id] : 0.0f;
    for(int offset = warpSize / 2; offset > 0; offset /= 2) sum += __shfl_xor_sync(0xffffffff, sum, offset);

    // Get norm

    float rmf = rsqrtf(sum * r_dim + epsilon);

    // Normalize x, scaling by w

    #pragma unroll
    for (int i = 0; i < blocks_per_warp; i++)
    {
        int column = warp_id * WARP_SIZE + lane_id + NUM_THREADS * i;
        if (column >= dim / 8) return;

        half8 w8_;
        ((uint4*)&w8_)[0] = ((uint4*)w8)[column];

        float n0 = itemf[i][0] * __half2float(__low2half(w8_.x)) * rmf;
        float n1 = itemf[i][1] * __half2float(__high2half(w8_.x)) * rmf;
        float n2 = itemf[i][2] * __half2float(__low2half(w8_.y)) * rmf;
        float n3 = itemf[i][3] * __half2float(__high2half(w8_.y)) * rmf;
        float n4 = itemf[i][4] * __half2float(__low2half(w8_.z)) * rmf;
        float n5 = itemf[i][5] * __half2float(__high2half(w8_.z)) * rmf;
        float n6 = itemf[i][6] * __half2float(__low2half(w8_.w)) * rmf;
        float n7 = itemf[i][7] * __half2float(__high2half(w8_.w)) * rmf;

        half8 y8_;
        y8_.x = __halves2half2(__float2half_rn(n0), __float2half_rn(n1));
        y8_.y = __halves2half2(__float2half_rn(n2), __float2half_rn(n3));
        y8_.z = __halves2half2(__float2half_rn(n4), __float2half_rn(n5));
        y8_.w = __halves2half2(__float2half_rn(n6), __float2half_rn(n7));

        ((uint4*)y_row)[column] = ((uint4*)&y8_)[0];
    }
}

fp_rms_norm_kernel pick_rms_norm_kernel(const int blocks_per_warp)
{
    if (blocks_per_warp == 1) return rms_norm_kernel<1>;
    if (blocks_per_warp == 2) return rms_norm_kernel<2>;
    if (blocks_per_warp == 3) return rms_norm_kernel<3>;
    if (blocks_per_warp == 4) return rms_norm_kernel<4>;
//    if (blocks_per_warp == 5) return rms_norm_kernel<5>;
//    if (blocks_per_warp == 6) return rms_norm_kernel<6>;
//    if (blocks_per_warp == 7) return rms_norm_kernel<7>;
//    if (blocks_per_warp == 8) return rms_norm_kernel<8>;
	return NULL;
}

void rms_norm_cuda
(
    const half* x,
    const half* w,
    half* y,
    const float epsilon,
    const int rows,
    const int dim
)
{
    dim3 blockDim, gridDim;
    blockDim.x = NUM_THREADS;
    blockDim.y = 1;
    gridDim.x = rows;
    gridDim.y = 1;

    float r_dim = 1.0f / (float) dim;

    int blocks_per_warp = DIVIDE(dim, NUM_THREADS * 8);
    fp_rms_norm_kernel kernel = pick_rms_norm_kernel(blocks_per_warp);
    kernel<<<gridDim, blockDim>>>(x, w, y, epsilon, r_dim, rows, dim);
}
