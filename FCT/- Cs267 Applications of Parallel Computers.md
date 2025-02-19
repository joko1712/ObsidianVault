
## Lecture 1

![[Pasted image 20250219005002.png]]

### Shared Memory (SMP) or Multicore: 
A shared memory multiprocessor (SMP*) by connecting multiple processors to a single memory system A multicore processor contains multiple processors (cores) on a single chip. 

### High PerformanceComputing (HPC) or Distributed Memory: 
A distributed memory multiprocessorhas processors with their own memoriesconnected by a high speed network. Also called a cluster. A high performance computing (HPC) system contains 100s or 1000s of such processors (nodes)

### Single Instruction Multiple Data (SIMD):
A Single Processor Multiple Data(SIMD) computer has multiple processors(or functional units) that perform the same operation on multiple data elements at once. Most single processors have SIMD units with ~2-8 way parallelism. Graphics processing units (GPUs) usethis as well



## Performance = parallelism
## Efficiency = locality


## Concurrency vs. Parallelism
Concurrency: multiple tasks are logically active at one time.
Parallelism: multiple tasks are actually active at one time.

![[Pasted image 20250219005520.png]]

## Parallel Computer vs. Distributed System
A distributed system is inherently distributed, i.e., serving clients at different locations
![[Pasted image 20250219005632.png]]

