
## Structured Parallel Programming: Patterns for Efficient Computation; Chapter 1
[[01 - Structured Parallel Programming - Cap 1.pdf]]

To do parallel is to (1) learn to recognize serial traps, some of which we examine throughout the remainder of this section, and (2) program in terms of parallel patterns that capture best practices and use efficient implementations of these patterns.

First of all, computation may not be the bottleneck. Frequently, access to memory or (equivalently) communication may constrain performance. Second, the potential for scaling perfor- mance on a parallel computer is constrained by the algorithm’s span. The span is the time it takes to perform the longest chain of tasks that must be performed sequentially. Such a chain is known as a critical path, and, because it is inherently sequential, it cannot be sped up with parallelism, no matter how many parallel processors you have.

The locality model asserts that memory accesses close together in time and space (and communication between processing units that are close to each other in space) are cheaper than those that are far apart.

When designing a parallel algorithm, it is actually important to pay attention to three things: 
	• The total amount of computational work. 
	• The span (the critical path). 
	• The total amount of communication (including that implicit in sharing memory).

Load balancing is the problem of ensuring that all processors are doing their fair share of the work.

