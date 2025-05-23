Implementation of the k-means with threading better to first split the points into blocks to then distribute to the threads.

Based on - [[ParalizeKmeans.pdf]] we have:

- **Parallelization Approach:**
    
    - Implemented in **C language** using **POSIX threads** (pthreads).
        
    - The dataset is partitioned into blocks; each thread processes one block.
        
    - Parallelized parts:
        
        - **Initialization of cluster centroids:** Used a method by Katsavounidis et al., choosing centroids far apart initially.
            
        - **Assignment step:** Assign data points to the nearest centroid.
            
        - **Update step:** Compute new centroids based on assigned points.
            
- **Implementation Highlights:**
    
    - The dataset was structured as a matrix, with two extra columns to store distances and cluster IDs.
        
    - Parallel threads divided data evenly, ensuring workload balance.


OMP_NUM_THREADS=8 ./src/kmeans_omp_Parallel \
    test_files/input100D.inp \
    32 \                             # K: 32 clusters
    1000 \                           # Max iterations
    0.1 \                            # 0.1% change threshold (very strict)
    0.00001 \                        # Very small centroid movement threshold
    output_omp_100D_K32_T1000.txt

OMP_NUM_THREADS=14 ./src/kmeans_omp_Parallel test_files/input100D.inp 500 2000000 0.0001 0.000000001 output_K500_T2000000.txt