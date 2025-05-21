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