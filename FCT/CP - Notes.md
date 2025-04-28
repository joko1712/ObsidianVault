
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

The best overall strategy for **scalable parallelism** is **data parallelism**. We define data parallelism as any kind of parallelism that grows as the data set grows or, more generally, as the problem size grows. Typically the data is split into chunks and each chunk processed with a separate task.

The opposite of data parallelism is **functional decomposition**, an approach that runs different program functions in parallel. At best, functional decomposition improves performance by a constant factor. For example, if a program has functions _f_, _g_, and _h_, running them in parallel at best triples performance, but only if all three functions take exactly the same amount of time to execute and do not depend on each other, and there is no overhead. Otherwise, the improvement will be less. Functional decomposition can be used to meet performance targets but it should not be the primary strategy, because it does not scale.

• **Regular parallelism:** The tasks are similar and have predictable dependencies.
• **Irregular parallelism:** The tasks are dissimilar in a way that creates unpredictable dependencies.

Various hardware mechanisms enable parallel computation. The two most important mechanisms are **thread parallelism** and **vector parallelism**:

• **Thread parallelism:** A mechanism for implementing parallelism in hardware using a separate flow of control for each worker. Thread parallelism supports both regular and irregular parallelism, as well as functional decomposition.
• **Vector parallelism:** A mechanism for implementing parallelism in hardware using the same flow of control on multiple data elements. Vector parallelism naturally supports regular parallelism but also can be applied to irregular parallelism with some limitations.

So what is performance? Usually it is about one of the following:

• Reducing the _total time_ it takes to compute a single result (**latency**)
• Increasing the _rate_ at which a series of results can be computed (**throughput**)
• Reducing the _power consumption_ of a computation

**Latency** is the time it takes to complete a task.
**Throughput** is the rate a which a series of tasks can be completed.

Two important metrics related to performance and parallelism are **speedup** and **efficiency**. Speedup compares the latency for solving the identical computational problem on one hardware unit **(“worker”)** versus on _P_ hardware units:

![[Screenshot 2025-03-17 at 14.49.58.png]]
where _T_1 is the latency of the program with one worker and _T__P_ is the latency on _P_ workers.

**Efficiency** is speedup divided by the number of workers:
![[Screenshot 2025-03-17 at 14.52.01.png]]
Efficiency measures return on hardware investment. Ideal efficiency is 1 (often reported as 100%).

## The Art of Multiprocessor Programming; Chapter 2
[[ch02 - The Art of Multiprocessor Programming, 2nd Edition.pdf]]

### Introduction to Mutual Exclusion

**Definition:** Mutual exclusion ensures only one thread accesses critical sections at a time to avoid conflicts and ensure data integrity. Crucially, this prevents race conditions, which could corrupt shared data.
### Key Concepts
#### Time and Events
- **Events**: Instantaneous state transitions within threads; crucial for understanding thread interaction.
- **Intervals**: Duration between two events, used to analyze concurrent execution.
- **Precedence Relation**: Denoted as →; essential for defining clear execution ordering among threads.
#### Critical Sections
- Code segments requiring exclusive access to prevent data inconsistencies.
- Implemented using **Lock objects** with methods:
    - `lock()`: Acquire exclusive access; threads must wait if unavailable.
    - `unlock()`: Release access to allow other waiting threads to proceed.
- **Lock Properties:**
    - **Mutual exclusion**: Only one thread can hold the lock, preventing concurrent access.
    - **Freedom from deadlock**: Ensures continuous system progress, eliminating permanent freezes.
    - **Freedom from starvation**: Guarantees fairness by ensuring all threads eventually gain access.
### Two-thread Lock Solutions
#### LockOne Class
- Uses two Boolean flags to control entry.
- Critical limitation: **Deadlock-prone** if both threads simultaneously set their flags.
#### LockTwo Class
- Employs a single "victim" variable, determining which thread yields.
- Critical limitation: Requires **concurrent execution** to avoid deadlock.
#### Peterson’s Algorithm
- Integrates flags and victim variables, achieving a robust balance.
- Crucially ensures both **mutual exclusion** and **starvation-freedom**, overcoming weaknesses of LockOne and LockTwo.
### Deadlocks and Livelocks
- **Deadlock**: Occurs when threads wait indefinitely for each other, halting progress.
- **Livelock**: Threads actively change states without making meaningful progress, continuously blocking each other.
#### Freedom from Deadlock
- Vital for system reliability; guarantees that the system never enters a permanent wait state, ensuring continuous operational progress.
#### Freedom from Starvation
- Essential for fairness; ensures that no thread is indefinitely postponed from entering the critical section, though delays can be unpredictable.
### Filter Lock (Generalization for N threads)
- Structured as an **N-level lock**, where threads sequentially pass through levels.
- Critically guarantees **mutual exclusion** and robustly prevents **starvation**, scalable to a large number of threads.
### Fairness
- **First-come-first-served (fairness)**: Prioritizes threads by arrival order to the lock.
- Lock method clearly divided into:
    - **Doorway** (bounded wait-free): Quick determination of entry order.
    - **Waiting section** (unbounded): Threads wait based on their determined order.
### Lamport’s Bakery Algorithm
- Highly regarded for fairness, inspired by bakery ticket systems.
- Crucially ensures orderly service via numbered tickets, guaranteeing fairness, and freedom from deadlock/starvation.
- Main limitation: Ticket numbers continuously increase, posing potential overflow issues.
### Bounded Timestamps
- Resolves Bakery algorithm’s overflow issue through bounded numbering schemes.
- Utilizes a structured graph-based system (T-graphs) to manage timestamps.
- Essential for maintaining proper dominance relations among competing threads
### Lower Bounds
- **Fundamental Limit**: Demonstrates critical theoretical constraint—minimum of n distinct memory locations needed for n-thread deadlock-free mutual exclusion using simple read/write operations.
- Important Implication: Highlights the theoretical optimality of Peterson’s and Bakery algorithms, and motivates exploration of advanced synchronization primitives for practical solutions.
### Chapter Summary
- Reinforces the importance of mutual exclusion in concurrent programming for data integrity.
- Early algorithms serve foundational conceptual roles, while real-world scenarios demand stronger primitives.
- Emphasizes the importance of rigorous algorithmic proofs (e.g., covering arguments) for deep comprehension and assurance of correctness.
### Important Algorithms
- **Peterson’s Algorithm:** Elegant foundational two-thread solution ensuring fairness and reliability.
- **Filter Lock:** Scalable for practical multi-thread environments, generalizing Peterson’s principles.
- **Bakery Algorithm:** Illustrative fairness model, highly instructive despite practical scalability concerns.

### Exercises 

# [[CP - Exercises]]

### Exercise 2.6 (Tree-lock)
**1. Mutual Exclusion:**
- Holds. At every node, Peterson’s algorithm ensures mutual exclusion between the two competing threads. A thread can only enter the critical section after acquiring the Peterson lock at every node up to the root. Thus, only one thread at a time can hold the lock at the root, ensuring mutual exclusion globally.
**2. Freedom from Deadlock:**
- Holds. Threads acquire locks from leaves upwards in a strictly hierarchical order, preventing circular dependencies. Hence, no deadlock can occur.
**3. Freedom from Starvation:**
- Holds. Peterson's algorithm at each node guarantees starvation-freedom. Thus, a thread that reaches a node will eventually pass through. Combined with the finite height of the tree, every thread eventually acquires the global lock.
**Upper bound on acquisition attempts:**
- Yes. A thread can be overtaken at most once per node along its path, thus the upper bound on the number of times the lock can be acquired and released by others is O(log n) for n threads.
**Hierarchical Locking Structure (Additional Note):**
- Tree-lock structures leverage simpler lock algorithms (like Peterson’s) combined hierarchically to efficiently manage mutual exclusion for large numbers of threads, facilitating parallelism while maintaining safety.
---
### Exercise 2.7 (ℓ-exclusion)
**Modification Sketch (Filter Lock):**
- Instead of only allowing a single thread at the final level, allow up to ℓ threads simultaneously.
- Introduce an atomic counter at the final level, initialized to ℓ.
- When a thread reaches the final level, it decrements the counter if it’s positive and enters; otherwise, it waits.
- Upon exiting the critical section, the thread increments the counter, allowing another waiting thread to proceed.
**Properties:**
- **ℓ-exclusion:** Ensured by the counter limiting the number of threads in the critical section.
- **ℓ-starvation-freedom:** Each waiting thread eventually proceeds as threads leaving the critical section increment the counter, making room for others.
**Generalized Exclusion (Additional Note):**
- Generalized (ℓ-)exclusion allows multiple threads (up to ℓ) to safely access the critical section concurrently, broadening the scope of synchronization from single-threaded mutual exclusion to controlled multi-threaded access.
---
### Exercise 2.11 (T³ Concurrent Counterexample)
**Counterexample Explanation:**
- Consider three threads A, B, and C concurrently performing label assignments on T³. Each picks a timestamp from distinct T² subgraphs simultaneously.
- Thread A picks a timestamp from the first T² subgraph, thread B picks from the second, and thread C from the third, without observing the others clearly.
- Due to concurrency, it’s possible to obtain a cycle of dominance relations between the chosen timestamps, resulting in no clear ordering.
**Implication:**
- This shows that sequential timestamp systems such as T³ do not trivially generalize to concurrent use cases because concurrent assignments break the total ordering required by mutual exclusion algorithms.
**Timestamp Concurrency Issues (Additional Note):**
- Sequential timestamp systems can fail in concurrent environments due to subtle concurrency-related issues, such as cyclical dependencies or insufficient total ordering, highlighting the importance of concurrency-aware designs.
---
### Exercise 2.14 (OneBit Algorithm)
**Proof of Mutual Exclusion:**
- Suppose two threads, A (with lower ID) and B, simultaneously attempt to enter.
- Thread B explicitly waits (lines 10-13) until thread A's flag is false (since A has a lower ID).
- A thus enters the critical section first; B enters only after A exits, setting its flag to false. Thus, mutual exclusion is guaranteed.
**Proof of Deadlock-freedom:**
- Consider threads ordered by their IDs. Each thread waits only for threads with smaller IDs.
- Since threads release their flags (set them to false upon exit), each thread eventually sees all lower-ID threads as not interested.
- Hence, no thread can wait indefinitely, ensuring deadlock-freedom.
**Conclusion:**
- The OneBit algorithm correctly achieves mutual exclusion and deadlock-freedom with minimal storage (exactly n bits for n threads), meeting the theoretical lower bound.
**Optimal Memory Usage (Additional Note):**
- Certain synchronization algorithms, like the OneBit algorithm, reach theoretical optimality by minimizing the required memory locations or bits, reflecting essential theoretical constraints and demonstrating efficiency in synchronization design.

## The Art of Multiprocessor Programming; Chapter 3
[[ch03 - The Art of Multiprocessor Programming, 2nd Edition.pdf]]

**Overview:**  
This chapter explores concurrent objects, focusing on the criteria used to define and verify their correctness and progress properties. It discusses how concurrency affects object behavior and introduces several formal correctness conditions, including sequential consistency, linearizability, and quiescent consistency. The chapter also defines various progress conditions like wait-freedom, lock-freedom, and obstruction-freedom, and evaluates their practical implications.
### Key Concepts:

#### 1. Concurrency and Correctness:

- Concurrent objects have methods invoked by multiple threads simultaneously, potentially overlapping in execution.
- Correctness of concurrent objects involves safety (correct behavior) and liveness (ongoing progress).
- Lock-based implementations ensure mutual exclusion but can limit concurrency due to sequential execution of method calls.

**Example:**
- A lock-based FIFO queue enforces correct behavior by using locks to prevent simultaneous access, maintaining sequential behavior.

#### 2. Sequential Objects:

- Traditional objects described by preconditions and postconditions assuming single-thread execution.
- Concurrent methods challenge this approach due to overlapping calls, making sequential specifications inadequate.

#### 3. Correctness Conditions:

##### **a. Sequential Consistency:**

- Method calls appear to take place in some sequential order consistent with program order (order of operations within a single thread).
- Does not require preserving real-time order between different threads’ operations.
- Nonblocking but not compositional (doesn't guarantee correctness when composed with other sequentially consistent components).

**Illustration:**

- Two threads concurrently enqueue and dequeue items might have ambiguous orders but must maintain program order internally within threads.

##### **b. Linearizability (stronger than Sequential Consistency):**

- Method calls appear to take effect instantaneously at a single point (linearization point) within their invocation and completion.
- Preserves real-time ordering, ensuring consistency even when composed.
- Compositional, making it suitable for complex systems built from individual linearizable components.

##### **c. Quiescent Consistency (weaker than Linearizability):**

- Enforces ordering only when the object is "quiescent" (no pending method calls).
- Does not preserve program order or real-time ordering, but is compositional.
- Suitable for high-performance systems where strict ordering is less critical.

#### 4. Formal Definitions and Properties:

##### Histories:

- The behavior of concurrent objects modeled as "histories," sequences of method invocation and response events.
- A sequential history is one without overlapping method calls.
- Legal histories match a sequential specification of the object.

##### Linearizability (formal definition):

- A concurrent history is linearizable if it can be reordered into a legal sequential history (linearization) that respects real-time ordering.
- Linearizability is compositional and nonblocking.

#### 5. Memory Consistency Models:

- Defines correctness for memory as a shared concurrent object.
- Sequential consistency was historically assumed but modern systems often reorder memory operations for performance, complicating programming and verification.

#### 6. Progress Conditions:

Define how methods of concurrent objects guarantee completion under various conditions:

##### Nonblocking Progress Conditions:

- **Wait-Freedom (maximal progress):** Every thread's method calls finish within a finite number of steps regardless of other threads’ behavior.
- **Lock-Freedom (minimal progress):** Guarantees progress for at least one thread's method call, potentially allowing starvation of others.
- **Obstruction-Freedom:** Guarantees progress if a method executes in isolation (no conflicting operations concurrently executed).

##### Blocking Progress Conditions:

- **Deadlock-Freedom (minimal progress):** Some method completes given fair scheduling; blocking by threads possible.
- **Starvation-Freedom (maximal progress):** Every method eventually completes if threads are fairly scheduled; still allows blocking.


### Choosing Conditions:

- Correctness and progress conditions depend on application requirements.
- **Correctness:**
    - Linearizability is most robust for complex, compositional systems.
    - Sequential consistency suitable for standalone systems.
    - Quiescent consistency suitable when high throughput outweighs strict order.

- **Progress:**
    
    - Wait-free/lock-free essential for real-time, interactive systems.        
    - Obstruction-free or blocking conditions suitable for applications tolerant to delays under specific scheduling assumptions.


## The Art of Multiprocessor Programming; Chapter 4
[[ch04 - The Art of Multiprocessor Programming, 2nd Edition.pdf]]

**Introduction and Context:**

Chapter 4 addresses the foundational aspects of concurrent computation in shared-memory systems, introducing and developing various abstract register models. It examines the progression from simple shared memory primitives to more sophisticated constructions and ultimately presents implementations of atomic registers and snapshots.

### Key Points and Main Ideas:

### 1. Concept of Shared Memory and Registers:

- Concurrent computing involves multiple threads interacting through shared memory.    
- Threads communicate by reading and writing shared locations called **registers**, implemented through simple shared memory primitives.
- Threads are asynchronous, running at unpredictable speeds and delays.

**Examples:**

- Registers may hold simple Boolean values, integers, or object references.

### 2. Types and Properties of Registers:

Registers are classified by their properties of **safety**, **regularity**, and **atomicity**, and by the number of allowed readers/writers:

- **Safe Register:**
    
    - Minimal guarantees: reads that overlap writes can return arbitrary values within the allowed range.
    - Weakest form of synchronization.
- **Regular Register:**
    - Intermediate strength: reads overlapping a write may return the new or old value, but no arbitrary values.
- **Atomic Register:**
    - Strongest guarantees: ensures linearizability, meaning each operation appears to happen instantaneously at some point between its start and finish times.

**Reader/Writer classifications:**

- Single-Reader Single-Writer (**SRSW**)
- Multi-Reader Single-Writer (**MRSW**)
- Multi-Reader Multi-Writer (**MRMW**)

### 3. Implementations and Constructions:

The chapter demonstrates systematic constructions, proving how complex registers can be built from simpler ones, typically using Boolean and timestamped registers. The sequence of constructions is:

- **Safe SRSW → Safe MRSW**  
- **Safe Boolean MRSW → Regular Boolean MRSW**
- **Regular Boolean MRSW → Regular M-valued MRSW**
- **Regular SRSW → Atomic SRSW**
- **Atomic SRSW → Atomic MRSW**
- **Atomic MRSW → Atomic MRMW**

Each step is carefully explained, including proofs of correctness, leveraging mechanisms like timestamps to order events and ensure linearizability.

### 4. Atomic Snapshots:

- A snapshot is an operation to atomically capture the values of multiple registers simultaneously.
- The chapter presents two snapshot implementations:
    - **Simple Snapshot (Obstruction-Free):**  
        Repeatedly performs a "double collect" (two consecutive reads of all registers) until it sees no changes, ensuring a consistent snapshot.
    - **Wait-Free Snapshot (Helping Mechanism):**  
        Uses the helping approach where each `update()` operation takes a snapshot before updating. Scanning threads adopt snapshots from threads that have moved twice, ensuring wait-freedom and atomicity even under heavy contention.

**Example Use Case:**

- Snapshots are beneficial for backups, checkpoints, and debugging concurrent algorithms.


### 5. Correctness and Progress Conditions:

- Emphasizes linearizability (strongest correctness criteria) and explains the difference from weaker consistency models like safe and regular.
- Discusses **wait-free** and **obstruction-free** progress properties:
    - **Wait-Free:** Every thread completes its operations in a finite number of steps independently of others.
    - **Obstruction-Free:** Operation completes only if it eventually executes without interruption.

### 6. Key Techniques Illustrated:

- **Timestamps:**  
    Used throughout for ordering concurrent events and establishing atomicity.

- **Helping Mechanisms:**  
    Threads help complete each other's operations to achieve wait-free implementations.

### 7. Practical and Theoretical Significance:

- Illustrates foundational knowledge essential for understanding concurrency.

- Emphasizes conceptual rigor over immediate practicality, focusing on the underlying principles rather than optimized performance.


### Summary of Core Results:

- Demonstrated equivalence and implementability of all register types from simple safe Boolean registers.

- Introduced practical methods (timestamps, helping) widely applicable in concurrent programming.

- Highlighted the importance of understanding memory consistency and synchronization in concurrent systems.



## The Art of Multiprocessor Programming; Chapter 5
[[ch05 - The Art of Multiprocessor Programming, 2nd Edition.pdf]]

**Chapter Overview:** This chapter investigates the relative power of synchronization primitives used in multiprocessor systems, specifically focusing on their ability to solve the consensus problem, an essential abstract synchronization task. It introduces and utilizes the concept of "consensus number" as a measure to determine and compare the power of different synchronization primitives and to establish a hierarchy of these primitives based on their consensus-solving capabilities.

### Key Concepts and Main Ideas:

### 1. Synchronization Primitives and Consensus:

- The main goal is identifying synchronization operations powerful enough to solve common synchronization problems in multiprocessor systems.
- **Consensus Problem**: A fundamental synchronization task where multiple threads must agree (decide) on a single value from their proposed inputs.
- **Consensus Protocol**: Defined through a single method, `decide()`, ensuring:
    - **Consistency**: All threads decide on the same value.
    - **Validity**: The decided value must be an input from one of the threads.

**Example:**

- Binary consensus involves two possible input values, typically 0 or 1.

### 2. Consensus Numbers:

- **Consensus Number**: Defined as the largest number of threads for which a class of synchronization primitives can solve the consensus problem using wait-free protocols.
- If a synchronization primitive can solve the consensus problem for an unlimited number of threads, it has an infinite consensus number.
- A synchronization primitive at a lower level cannot implement (using wait-free methods) a primitive at a higher consensus number.

### 3. Classification of Synchronization Primitives by Consensus Number:

#### Atomic Registers:

- **Consensus number = 1**
- Atomic read/write registers alone cannot solve consensus for two or more threads.

#### FIFO Queues, Stacks, Priority Queues, Lists, Sets:

- **Consensus number = 2**
- These data structures can solve consensus for exactly two threads but cannot handle consensus for three or more threads.

#### Multiple-Assignment Objects:

- An (m,n)-assignment object atomically assigns values to multiple memory locations simultaneously.
- An (m,n)-assignment has a consensus number greater than atomic registers but still limited. Specifically, (2,3)-assignments have a consensus number of at least 2, while general (n, n(n+1)/2)-assignments have consensus number at least n.
- Multiple assignment (writing multiple memory locations simultaneously) is strictly more powerful than atomic snapshots (reading multiple locations atomically).

#### Read-Modify-Write (RMW) Operations:

- Defined as methods that atomically read a memory location, apply a function to its value, and write back the result.
- Any nontrivial RMW register has at least consensus number 2.
- **Common2 class**: A subclass of RMW operations characterized by commuting or overwriting functions (e.g., `getAndSet`, `getAndIncrement`, and `getAndAdd`) have consensus number exactly 2, thus unable to achieve consensus for three or more threads.

#### CompareAndSet (CAS) Operations:

- **Consensus number = infinite**
- CAS registers can solve consensus problems for an unlimited number of threads.
- CAS operations are powerful synchronization primitives and form a "universal" synchronization operation, capable of building any wait-free concurrent object.

### 4. Bivalence Arguments and Critical States:

- Uses the notion of **bivalent (undecided)** and **univalent (decided)** states to prove the limitations of synchronization primitives.
- A **critical state** is a bivalent state where the next move of any thread makes the protocol state univalent (decided).
- These concepts are instrumental in proving impossibility results (e.g., atomic registers can't solve two-thread consensus).

### 5. Practical Implications:

- Hardware designers must provide synchronization primitives beyond atomic registers to build practical concurrent data structures.
- CAS emerges as a fundamentally important primitive for modern multiprocessor systems.

### Key Results and Implications:

- **Atomic registers alone cannot solve two-thread or greater consensus** (consensus number 1).
- **FIFO Queues and common data structures have limited synchronization power** (consensus number 2).
- **CAS operations are universally powerful**, capable of constructing any concurrent object in a wait-free manner (infinite consensus number).


## The Art of Multiprocessor Programming; Chapter 6

Lock-free does not allow starvation
Wait-free operation will eventually complete 

If a program is lock-free, it basically means that _at least one_ of its threads is guaranteed to make progress over an arbitrary period of time. If a program deadlocks, none of its threads (and therefore the program as a whole) cannot make progress - we can say it's not lock-free. Since lock-free programs are guaranteed to make progress, they are guaranteed to complete (assuming finite execution without exceptions).

Wait-free is a stronger condition which means that _every_ thread is guaranteed to make progress over an arbitrary period of time, regardless of the timing/ordering of thread execution; and so we can say that the threads finish independently. All wait-free programs are lock-free.

Obstruction-freedom is the weakest natural non-blocking progress guarantee. An algorithm is obstruction-free if at any point, a single thread executed in isolation (i.e., with all obstructing threads suspended) for a bounded number of steps will complete its operation. All lock-free algorithms are obstruction-free.