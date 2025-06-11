## 🧠 Query Optimization (Class 06 - 2024/25)

### 📌 1. **Overview**

- Query optimization aims to determine the most efficient way to execute a given query by considering multiple execution plans and choosing the best based on cost.
    

---

### 🔍 2. **Query Block and Equivalence Rules**

- SQL queries are broken into blocks (SELECT-FROM-WHERE).
    
- Relational algebra is used to define **equivalent transformations** (e.g., `σc(σb(R)) ≡ σb∧c(R)`).
    

---

### ⚙️ 3. **Heuristic Optimization**

- Applies transformation rules to:
    
    - Move selections down the tree.
        
    - Combine selections and projections.
        
    - Push projections down the tree.
        
- Reduces the size of intermediate results.
    
- Often done before cost-based optimization.
    

---

### 📈 4. **Cost-Based Optimization**

- Considers multiple physical plans.
    
- Chooses the one with the **least cost** (I/O, CPU).
    
- Uses **dynamic programming** or **greedy algorithms** to search plan space.
    
- Cost models are based on:
    
    - Size estimation
        
    - Index availability
        
    - Join order and method
        

---

### 📚 5. **Estimating Query Size**

Key formulas:

- Selection:  
    If attribute `A` has `V(R, A)` distinct values,  
    `T(σA=c(R)) = T(R) / V(R, A)`
    
- Join:  
    `T(R ⨝ S) = T(R) * T(S) / max(V(R, A), V(S, A))` (assuming uniformity)
    

---

### 🔄 6. **Transformation Rules Examples**

- Commutativity: `R ⨝ S ≡ S ⨝ R`
    
- Associativity: `(R ⨝ S) ⨝ T ≡ R ⨝ (S ⨝ T)`
    
- Selection Pushdown: `σc(R ⨝ S) ≡ σc(R) ⨝ S` if `c` refers only to `R`
    

---

### 🪄 7. **Plan Generation**

- Logical → Physical Plan:
    
    - Choose access paths (index, full scan)
        
    - Choose join methods (nested loop, hash join, sort-merge)
        
- Cost is calculated recursively.
    

---

### 💡 8. **Join Strategies**

- **Nested-loop join**: Simple but expensive for large inputs.
    
- **Block nested-loop join**: Improves performance by reading blocks.
    
- **Index nested-loop join**: Uses index for inner relation.
    
- **Merge join**: Requires sorted inputs.
    
- **Hash join**: Good for equi-joins with large data.
    

---

### 🧮 9. **Statistics**

- Maintained to support cost estimates:
    
    - Number of tuples `T(R)`
        
    - Number of blocks `B(R)`
        
    - Distinct values `V(R, A)`
        
- Can be stored in system catalogs and updated periodically.
    

---

### 🧵 10. **Dynamic Programming for Join Order**

- Bottom-up approach:
    
    - Start with base tables
        
    - Combine smaller subplans
        
- Avoids recomputation by storing intermediate results
    

---

## Transactions (Class 07 - 2023/24)

### 📌 1. **What is a Transaction?**

- A transaction is a **logical unit of database work**.
    
- Must satisfy **ACID** properties:
    
    - **Atomicity**: All-or-nothing.
        
    - **Consistency**: Transitions DB from one valid state to another.
        
    - **Isolation**: Intermediate results are not visible to other transactions.
        
    - **Durability**: Once committed, effects persist even after failure.
        

---

### 🧾 2. **Transaction States**

1. **Active**: Transaction is executing.
    
2. **Partially Committed**: Last operation executed, waiting for commit.
    
3. **Committed**: Effects permanently recorded.
    
4. **Failed**: Errors occurred, must rollback.
    
5. **Aborted**: Rollback completed.
    

---

### 🧠 3. **Schedules**

- **Schedule**: Sequence of operations from a set of transactions.
    
- **Serial Schedule**: Transactions run one after another.
    
- **Concurrent Schedule**: Operations from multiple transactions interleave.
    

---

### ✅ 4. **Serializability**

- A schedule is **serializable** if its outcome is equivalent to some **serial** schedule.
    
- **Conflict-serializability**:
    
    - Swap **non-conflicting operations** (on different data or reads only).
        
    - Use **precedence graphs** to test for cycles.
        

---

### 🔁 5. **Recoverability**

- A schedule is **recoverable** if a transaction commits **only after** all transactions whose data it read have committed.
    
- Avoids **dirty reads** and **cascading aborts**.
    

---

### 🔒 6. **Cascadeless and Strict Schedules**

- **Cascadeless**: Transactions only read data from committed transactions.
    
- **Strict**: Transactions can neither read nor write to data modified by uncommitted transactions (most used in practice).
    

---

### 🛑 7. **Concurrency Problems**

- **Lost Update**: Two transactions overwrite each other’s changes.
    
- **Temporary Update (Dirty Read)**: Transaction reads uncommitted changes.
    
- **Unrepeatable Read**: Transaction reads same item twice and gets different values.
    
- **Phantom Read**: A query returns different number of rows if re-executed.
    

---

### 🧮 8. **View Serializability**

- Based on **what values are read** rather than order.
    
- More general than conflict serializability.
    
- Harder to test than conflict-serializability (NP-complete).
    

---

## Concurrency Control (Class 08 - 2023/24)

---

### 📌 1. **Why Concurrency Control?**

- Ensures **isolation** in concurrent transaction execution.
    
- Prevents anomalies like **lost updates, dirty reads, unrepeatable reads, and phantoms**.
    

---

### 🔐 2. **Lock-Based Protocols**

- Two types of locks:
    
    - **Shared (S)** – for read
        
    - **Exclusive (X)** – for write
        
- **Lock compatibility matrix** determines if new locks can be granted.
    

---

### ✌️ 3. **Two-Phase Locking (2PL)**

- **Growing phase**: acquire locks.
    
- **Shrinking phase**: release locks.
    
- **Strict 2PL**: holds all **X locks until commit/abort** → avoids cascading rollbacks.
    
- **Rigorous 2PL**: holds all locks (S and X) until commit/abort.
    

---

### 🔁 4. **Deadlocks**

- Occur when transactions wait for each other in a cycle.
    
- **Detection**: wait-for graph with cycles.
    
- **Prevention**:
    
    - **wait-die** (non-preemptive): older waits, younger rolls back.
        
    - **wound-wait** (preemptive): older rolls back younger.
        
    - **Timeouts**: abort after wait time.
        

---

### 🌲 5. **Tree Protocol**

- Applies a **partial order** to data items (tree).
    
- Only **X locks** used.
    
- Parent must be locked before child.
    
- Deadlock-free, but **not cascadeless or recoverable**.
    

---

### 🧱 6. **Multiple Granularity**

- Locks on different levels: **database > area > file > record**.
    
- Uses additional lock types:
    
    - **IS**: Intention Shared
        
    - **IX**: Intention Exclusive
        
    - **SIX**: Shared + Intention Exclusive
        
- Lock escalation: move from fine-grained to coarse-grained lock.
    

---

### 👻 7. **Phantom Problem**

- Occurs when a transaction reads a **set of tuples**, and another inserts/deletes a matching tuple.
    
- Solutions:
    
    - **Index locking**: Lock index pages, not just tuples.
        
    - **Next-key locking**: Locks index entries and the next key.
        

---

### ⏳ 8. **Timestamp-Based Protocols**

- Assign unique timestamp **TS(Ti)** to each transaction.
    
- Maintain:
    
    - **R-TS(Q)**: latest read TS
        
    - **W-TS(Q)**: latest write TS
        

**Rules:**

- If read/write is **out-of-order**, abort.
    
- **Thomas Write Rule**: ignore obsolete writes instead of aborting → allows **view-serializability**.
    

---

### 🔍 9. **Validation-Based (Optimistic) Protocol**

- No locking during execution.
    
- 3 phases:
    
    1. **Read**: execute and save writes locally.
        
    2. **Validation**: check if serializable.
        
    3. **Write**: apply changes if validated.
        
- Validation uses 3 timestamps:
    
    - Start, Validation, Finish.
        

---

### 🧬 10. **Multiversion Concurrency Control (MVCC)**

- Maintain **multiple versions** of data.
    
- **Reads never block.**
    
- Variants:
    
    - **Multiversion Timestamp Ordering**:
        
        - Selects version ≤ TS(Ti)
            
        - Write fails if read-TS > TS(Ti)
            
    - **Multiversion 2PL**:
        
        - Update txns use 2PL and versioning.
            
        - Read-only txns get snapshot.
            

---

### 📸 11. **Snapshot Isolation (SI)**

- Txn sees **snapshot** of committed data at start.
    
- Reads/modifies only its snapshot.
    
- Uses **first-committer-wins** rule to avoid write conflicts.
    

---

### ⚠️ 12. **SI Anomalies**

- **Write skew**: Txns write different data based on outdated reads.
    
- SI is **not always serializable**.
    
- **Serializable SI (SSI)**: tracks **read-write conflicts** + prevents cycles.
    

---

### 💡 13. **Weak Consistency Levels**

- **Read committed**: no dirty reads.
    
- **Repeatable read**: no update anomalies, but **phantoms allowed**.
    
- **Serializable**: no anomalies at all.
    

---

### 🧩 14. **Application-Level Concurrency**

- Use **version numbers** to detect conflicts on commit.
    
- Similar to optimistic concurrency control.
    

---

## Recovery (Class 09 - 2024/25)

---

### 🧠 1. **Why Recovery?**

- Protects against **system crashes**, **power failures**, and **software errors**.
    
- Goal: ensure **Atomicity** and **Durability** of transactions.
    

---

### 📦 2. **Types of Storage**

- **Volatile**: RAM (lost on crash).
    
- **Non-volatile**: Disk/SSD (persistent).
    
- **Stable Storage**: Idealized persistent storage assumed never to fail.
    

---

### 🧾 3. **Log-Based Recovery**

- Use a **log** to track all DB modifications.
    
- Log is stored on **stable storage**.
    

**Log Entries**:

- `<Ti start>` – transaction Ti has started.
    
- `<Ti, X, old, new>` – Ti updates X from old to new.
    
- `<Ti commit>` / `<Ti abort>`
    

**Write-Ahead Logging (WAL)**:

- Log must be written **before** actual data is updated.
    
- Commit record must be **flushed** to log before acknowledging success.
    

---

### ♻️ 4. **Undo and Redo**

- **Undo**: reverse effects of uncommitted txns.
    
- **Redo**: reapply effects of committed txns not written to DB.
    

---

### 🔄 5. **Recovery Procedure**

1. **Analysis**: identify committed/uncommitted txns.
    
2. **Redo**: repeat actions of committed txns from the log.
    
3. **Undo**: roll back actions of uncommitted txns.
    

---

### 📑 6. **Checkpoints**

- Periodically save DB + log state to reduce recovery time.
    

**Checkpoint Entry**:

- `<checkpoint(T1, T2, …)>`: lists active txns.
    
- Discard logs prior to checkpoint if no txn needs them.
    

---

### 🧬 7. **ARIES Recovery Algorithm**

**ARIES = Algorithm for Recovery and Isolation Exploiting Semantics**

- Core Concepts:
    
    1. **WAL** protocol
        
    2. **Repeating history** during redo
        
    3. **Logging undo operations** during rollback
        
- Each log entry has:
    
    - **LSN**: log sequence number
        
    - **prevLSN**: back pointer for per-txn log chain
        

---

### 🔁 8. **ARIES: Three Phases**

1. **Analysis**:
    
    - Construct transaction table and dirty page table.
        
    - Identify redo starting point (smallest recLSN).
        
2. **Redo**:
    
    - Reapply actions from earliest needed LSN.
        
    - Only redo if page is dirty and LSN not yet applied.
        
3. **Undo**:
    
    - Process loser transactions.
        
    - Undo actions in reverse using **compensation log records (CLRs)**.
        
    - CLRs describe undos and are **redoable** (idempotent).
        

---

### ⛑ 9. **Compensation Log Records (CLRs)**

- Written during undo to record the **undo of an update**.
    
- Help resume recovery if crash occurs during recovery itself.
    

---

### 🧼 10. **Force vs No-Force / Steal vs No-Steal**

- **Force**: write updated pages to disk on commit.
    
- **No-force**: defer writes (requires redo).
    
- **Steal**: write dirty pages before commit (requires undo).
    
- **No-steal**: don’t allow dirty writes before commit.
    

**ARIES uses**: **No-force + Steal**

---

### 🧪 11. **Shadow Paging (alternative method)**

- Avoids logging. Uses **page tables**.
    
- **Copy-on-write**: changes go to shadow copies.
    
- When committed, new pages replace old ones.
    

**Drawbacks**:

- Complicated garbage collection.
    
- Not flexible for fine-grained updates.
    

---

### 🗃 12. **Recovery from Media Failure**

- Use **periodic backups**.
    
- Apply **logs since last backup** to reconstruct DB.
    
- **Restore = backup + replay logs**
  
---

## Distributed Databases (Class 10 - 2024/25)

---

### 📌 1. **What is a Distributed Database (DDB)?**

- A collection of **logically interrelated databases** distributed over a **computer network**.
    
- Appears as a **single database** to users.
    

---

### 🗺 2. **Goals**

- **Location transparency**: users don’t need to know data location.
    
- **Replication transparency**: users unaware of multiple data copies.
    
- **Fragmentation transparency**: users unaware that data may be split across sites.
    

---

### 🧩 3. **Data Fragmentation**

Splitting relations into **smaller pieces** for distribution:

- **Horizontal fragmentation**: subsets of rows.
    
- **Vertical fragmentation**: subsets of columns + primary key.
    
- **Mixed**: both types combined.
    

**Reconstruction**:

- Horizontal: `R = R1 ∪ R2 ∪ ...`
    
- Vertical: `R = πA1,...,An(R1) ⨝ πAn+1,...,Am(R2)`
    

---

### 🔁 4. **Replication**

- Store copies of data across multiple sites.
    
- **Full replication**: copy of DB at each site.
    
- **Partial replication**: only some fragments are replicated.
    

**Pros**:

- Improved availability and performance.
    

**Cons**:

- Complicates updates → must maintain consistency.
    

---

### 🛠 5. **Distributed Query Processing**

Goals:

- Minimize:
    
    - **Communication cost**
        
    - **Number of sites accessed**
        
    - **Data transfer volume**
        

**Techniques**:

- **Semijoin**:
    
    - `R ⋉ S = πR_attributes(R ⨝ S)`
        
    - Reduces data sent across sites.
        
- **Query shipping**: move the query to the data.
    
- **Data shipping**: move the data to the query.
    

---

### 🔒 6. **Distributed Transactions**

- Must satisfy **ACID** across multiple sites.
    

**Two-Phase Commit Protocol (2PC)**:

1. **Prepare phase**:
    
    - Coordinator asks participants to prepare.
        
    - Participants write log and reply "yes"/"no".
        
2. **Commit phase**:
    
    - If all say "yes", coordinator sends "commit".
        
    - If any say "no", coordinator sends "abort".
        

**Log entries**: `<prepare>`, `<commit>`, `<abort>`

**Downside**: blocking – if coordinator crashes, participants may be stuck.

---

### 🧠 7. **Three-Phase Commit Protocol (3PC)**

- Adds extra phase to avoid blocking.
    
- More complex and assumes no network partition.
    

---

### 📡 8. **Concurrency Control in DDB**

Options:

- **Distributed 2PL**: lock manager per site.
    
- **Distributed timestamp ordering**: assigns timestamps globally.
    
- **Distributed validation-based**: validation happens across sites.
    

---

### 🧮 9. **Distributed Deadlock Handling**

- Use **wait-for graphs** per site.
    
- Exchange information periodically to detect **global deadlocks**.
    

---

### 🔁 10. **Distributed Recovery**

- Recovery steps must ensure **global consistency**.
    
- Participants may **resend votes** to help recovery if coordinator crashes.
    

---

### 📍 11. **Heterogeneous Systems**

- Databases using **different DBMSs, schemas, query languages**.
    
- Needs **middleware** for translation and coordination.



---

# To Write
![[Pasted image 20250611193547.png]]

ACID Properties
§ Atomicity. Either all operations of the transaction are properly reflected in
the database or none are.
§ Consistency. Execution of a transaction in isolation preserves the
consistency of the database.
§ Isolation. Although multiple transactions may execute concurrently, each
transaction must be unaware of other concurrently executing transactions.
Intermediate transaction results must be hidden from other concurrently
executed transactions.
• That is, for every pair of transactions Ti and Tj, it appears to Ti that
either Tj, finished execution before Ti started, or Tj started execution
after Ti finished.
§ Durability. After a transaction completes successfully, the changes it has
made to the database persist, even if there are system failures.



Transaction State
§ Active – the initial state; the transaction stays in this state while it is
executing
§ Partially committed – after the final statement has been executed.
§ Failed -- after the discovery that normal execution can no longer proceed.
§ Aborted – after the transaction has been rolled back and the database
restored to its state prior to the start of the transaction. Two options after it
has been aborted:
• Restart the transaction
§ Can be done only if no internal logical error
• Kill the transaction
§ Committed – after successful completion.


two-
phase locking is necessary for conflict
serializability in the following sense:
• Given a transaction Ti that does
not follow two-phase locking, we
can find a transaction Tj that uses
two-phase locking, and a schedule
for Ti and Tj that is not conflict
serializable

A schedule S is legal under a locking protocol if it can be generated
by a set of transactions that follow the protocol
• A protocol ensures serializability if all legal schedules under that
protocol are serializable


intention-shared (IS): indicates explicit locking at a lower level of the
tree but only with shared locks.
• intention-exclusive (IX): indicates explicit locking at a lower level with
exclusive or shared locks
• shared and intention-exclusive (SIX): the subtree rooted by that
node is locked explicitly in shared mode and explicit locking is being
done at a lower level with exclusive-mode locks.