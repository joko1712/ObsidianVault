
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

Algorithm strategy patterns have two parts: semantics and implementation. The semantics describe how the pattern is used as a building block of an algorithm, and consists of a certain arrangement of tasks and data dependencies. The semantic view is an abstraction that intentionally hides some details, such as whether the tasks making up the pattern will actually run in parallel in a particular implementation. The semantic view of a pattern is used when an algorithm is designed. However, patterns also need to be implemented well on real machines. 
**The key point is that different implementation choices may lead to different performances, but not to different semantics.**

Three patterns deserve special mention: nesting, map, and fork–join. 
	- Nesting means that patterns can be hierarchically composed. Nesting is extensively used in serial programming for composability and information hiding, but is a challenge to carry over into parallel programming. The key to implementing nested parallelism is to specify optional, not mandatory, parallelism. 
	- The map pattern divides a problem into a number of uniform parts and represents a regular parallelization. This is also known as embarrassing parallelism. The map pattern is worth using whenever possible since it allows for both efficient parallelization and efficient vectorization. 
	- The fork–join pattern recursively subdivides a problem into subparts and can be used for both regular and irregular parallelization. It is useful for implementing a divide-and-conquer strategy.
These three patterns also emphasize that in order to achieve scalable parallelization we should focus on data parallelism: the subdivision of the problem into subproblems, with the number of subproblems able to grow with the overall problem size.

To achieve portable parallel programming you should you should avoid vector intrinsics that map directly onto vector instructions and instead use array operations. You should also avoid using threads directly and program in terms of a task abstraction. Tasks identify only opportunities for parallelism, not the actual parallel execution mechanism. Programming should focus on the decomposition of the problem and the design of the algorithm rather than the specific mechanisms by which it will be parallelized.

Using abstractions for specifying vectorization rather than vector intrinsics avoids dependencies on the peculiarities of a particular vector instruction set, such as the number of elements in a vector.
The reasons for avoiding direct threading are more subtle, but basically a task model has less overhead, supports better composability, and gives the system more freedom to allocate resources. In particular, tasks support the specification of optional parallelism.

## Structured Parallel Programming: Patterns for Efficient Computation; Chapter 2
[[02 - Structured Parallel Programming - Cap 2.pdf]]


## The Art of Multiprocessor Programming; Chapter 2
[[ch02 - The Art of Multiprocessor Programming, 2nd Edition.pdf]]