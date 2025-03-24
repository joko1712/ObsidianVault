![[Screenshot 2025-03-24 at 15.28.20.png]]
## Solution:
Peterson's algorithm ensures that a thread A that wants to enter the critical section sets itself as the victim and waits only if another thread is interested. This design guarantees that at most one other thread can overtake thread A once it expresses interest. Thus, Peterson’s algorithm indeed provides **1-bounded waiting**. The value r=1r = 1r=1 since no thread can be overtaken more than once.

![[Pasted image 20250324153048.png]]
**Solution:**  
We must define a doorway section explicitly rather than relying on the first instruction because the first instruction of `lock()` might not establish a meaningful ordering due to concurrency issues:
- **If the first instruction is a read:** The reading order alone doesn't necessarily reflect the threads' order, as reads might occur simultaneously or out-of-order relative to other operations.
- **If the first instruction is a write:** Concurrent writes can overwrite each other, making the order ambiguous.
Thus, to meaningfully establish ordering, we designate a doorway section that's short and bounded, clearly and explicitly establishing ordering.

![[Pasted image 20250324153356.png]]
- **Rationale:**  
    This exercise is particularly insightful because it tests understanding of:
    - Recursive composition of simpler synchronization primitives (Peterson’s Lock).
    - Analysis of properties like mutual exclusion, deadlock, starvation, and performance.
    - Evaluating hierarchical synchronization structures (Binary Trees).
- **Summary of Exercise:**  
    Given a binary-tree structure composed of Peterson's locks:
    - Prove whether the composite structure satisfies:
        1. Mutual exclusion,
        2. Freedom from deadlock,
        3. Freedom from starvation,
    - Determine if there's an upper bound on lock acquisition attempts.
### Solution:
**1. Mutual Exclusion:**
- Holds. At every node, Peterson’s algorithm ensures mutual exclusion between the two competing threads. A thread can only enter the critical section after acquiring the Peterson lock at every node up to the root. Thus, only one thread at a time can hold the lock at the root, ensuring mutual exclusion globally.
**2. Freedom from Deadlock:**
- Holds. Threads acquire locks from leaves upwards in a strictly hierarchical order, preventing circular dependencies. Hence, no deadlock can occur.
**3. Freedom from Starvation:**
- Holds. Peterson's algorithm at each node guarantees starvation-freedom. Thus, a thread that reaches a node will eventually pass through. Combined with the finite height of the tree, every thread eventually acquires the global lock.
**Upper bound on acquisition attempts:**
- Yes. A thread can be overtaken at most once per node along its path, thus the upper bound on the number of times the lock can be acquired and released by others is O(log n) for n threads.


![[Pasted image 20250324153604.png]]
- **Rationale:**  
    This question provides practical insights into generalizing synchronization primitives beyond simple mutual exclusion, involving:
    - Modifying existing algorithms (Filter lock).
    - Understanding of fairness and synchronization when multiple threads enter critical sections simultaneously.
    - Real-world scenarios where multiple threads (limited number) can safely coexist in critical sections.
- **Summary of Exercise:**  
    Modify the Filter lock algorithm to handle ℓ threads simultaneously in the critical section, ensuring ℓ-exclusion and ℓ-starvation-freedom.
### Solution:
**Modification Sketch (Filter Lock):**
- Instead of only allowing a single thread at the final level, allow up to ℓ threads simultaneously.
- Introduce an atomic counter at the final level, initialized to ℓ.
- When a thread reaches the final level, it decrements the counter if it’s positive and enters; otherwise, it waits.
- Upon exiting the critical section, the thread increments the counter, allowing another waiting thread to proceed.
**Properties:**
- **ℓ-exclusion:** Ensured by the counter limiting the number of threads in the critical section.
- **ℓ-starvation-freedom:** Each waiting thread eventually proceeds as threads leaving the critical section increment the counter, making room for others.
![[Pasted image 20250324153747.png]]
- **Rationale:**  
    This exercise tests the understanding of:
    - Timestamping and ordering mechanisms.
    - Concurrency complications and race conditions that occur even with carefully designed labeling systems.
    - Identifying subtle flaws through counterexamples.
- **Summary of Exercise:**  
    Provide a counterexample demonstrating that the sequential timestamp system T³ does not maintain a total ordering when used concurrently by three threads. The solution requires demonstrating a concrete scenario showing unordered states.

### Solution:
**Counterexample Explanation:**
- Consider three threads A, B, and C concurrently performing label assignments on T³. Each picks a timestamp from distinct T² subgraphs simultaneously.
- Thread A picks a timestamp from the first T² subgraph, thread B picks from the second, and thread C from the third, without observing the others clearly.
- Due to concurrency, it’s possible to obtain a cycle of dominance relations between the chosen timestamps, resulting in no clear ordering.
**Implication:**
- This shows that sequential timestamp systems such as T³ do not trivially generalize to concurrent use cases because concurrent assignments break the total ordering required by mutual exclusion algorithms.

![[Pasted image 20250324153847.png]]
![[Pasted image 20250324153927.png]]
- **Rationale:**  
    This problem challenges students to:
    - Analyze minimalistic synchronization algorithms.
    - Formally prove critical properties (mutual exclusion, deadlock-freedom).
    - Understand and reason about lower bounds and theoretical optimality in synchronization algorithms.
- **Summary of Exercise:**  
    Prove that the OneBit mutual exclusion algorithm (using exactly n bits for n threads):
    - Satisfies mutual exclusion,
    - Is deadlock-free.

### Solution:
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