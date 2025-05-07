
## Database System Concepts Chapter 12
[[Abraham Silberschatz, Henry Korth and S. Sudarshan - Database System Concepts. 7-McGraw-Hill Education (2020).pdf]]
[[Abraham Silberschatz, 12.pdf]]

This chapter focuses on various types of physical storage media and techniques for efficiently managing data storage in database systems, emphasizing performance, reliability, and cost-effectiveness.

**Key Storage Media:**

1. **Cache**: Fastest, most expensive, volatile, and managed by hardware. Primarily used for temporary storage.
    
2. **Main Memory**: Volatile memory used directly by the CPU, with moderate cost and speed. Large enough for enterprise databases but limited for extensive databases due to cost and volatility.
    
3. **Flash Memory (SSDs)**: Non-volatile, faster than magnetic disks, and moderately priced. Widely used in consumer electronics, increasingly popular as storage media in computers and servers due to higher speed, lower power consumption, and reliability, despite higher costs compared to magnetic disks.
    
4. **Magnetic Disks (HDDs)**: Non-volatile, lower cost per byte, primary medium for large-scale persistent storage. Disks consist of platters with magnetic surfaces, read-write heads, and are prone to mechanical failures. Typical capacities range from gigabytes to multiple terabytes.
    
5. **Optical Storage**: Includes DVDs and Blu-ray, non-volatile and reliable for archival purposes but slow for active data access.
    
6. **Tape Storage**: Non-volatile, inexpensive, high capacity, used mainly for backups and archival storage. Tapes offer sequential access (slower) but are suitable for long-term data preservation.
    

**Storage Interfaces:**

- **SATA and SAS**: Common interfaces for connecting disks to computers.
    
- **NVMe (PCIe-based)**: High-performance interface optimized for SSDs, providing extremely fast data transfer rates.
    
- **Storage Area Networks (SAN)** and **Network Attached Storage (NAS)**: Allow multiple servers to share storage, with SAN appearing as a large logical disk and NAS providing file-level access.
    

**Magnetic Disks Detailed:**

- Comprised of rotating platters divided into tracks and sectors, data access involves seek time (disk arm movement) and rotational latency (waiting for data sector alignment). Performance measured by capacity, access times, data-transfer rates, and Mean Time To Failure (MTTF).
    
- Controllers manage data integrity through checksums and remapping bad sectors.
    

**Flash Memory (SSDs) Detailed:**

- Faster random access, lower latency, and higher transfer rates compared to magnetic disks.
    
- Write operations require special handling due to limitations on overwriting and finite erase cycles, managed by wear leveling and flash translation layers (FTL).
    

**RAID (Redundant Arrays of Independent Disks):**

RAID techniques improve data storage reliability and performance by distributing data across multiple disks, using mirroring and parity to handle disk failures:

- **RAID Level 0**: Block striping without redundancy (high performance, no reliability).
    
- **RAID Level 1**: Mirroring disks, high reliability, but costly (double storage required).
    
- **RAID Level 5**: Block-level striping with distributed parity, balances reliability, cost, and performance for read-intensive applications.
    
- **RAID Level 6**: Advanced redundancy, tolerating two simultaneous disk failures, ideal for critical systems.
![[Pasted image 20250429154858.png]]

**Choice of RAID Level**

§ Factors in choosing RAID level
	• Monetary cost
	• Performance: Number of I/O operations per second, and bandwidth during normal operation
	• Performance during failure
	• Performance during rebuild of failed disk
		§ Including time taken to rebuild failed disk
		
§ RAID 0 is used only when data safety is not important
	• E.g. data can be recovered quickly from other sources
	
§ RAID 1 provides much better write performance than level 5
	• Level 5 requires at least 2 block reads and 2 block writes to write a single block, whereas Level 1 only requires 2 block writes
§ RAID 1 had higher storage cost than level 5

§ Level 5 is preferred for applications where writes are sequential and large (many blocks), and need large amounts of data storage

§ RAID 1 is preferred for applications with many random/small updates

§ RAID 6 gives better data protection than RAID 5 since it can tolerate two disk (or disk block) failures
	• Increasing in importance since latent block failures on one disk, coupled with a failure of another disk can result in data loss with RAID 1 and RAID 5.

RAID configurations also support hot swapping, hardware and software implementations, and specialized recovery strategies to minimize downtime and data loss.

§ Software RAID: RAID implementations done entirely in software, with no special hardware support
§ Hardware RAID: RAID implementations with special hardware
	• Use non-volatile RAM to record writes that are being executed
	• Beware: power failure during write can result in corrupted disk
		§ E.g. failure after writing one block but before writing the second in a mirrored system
		§ Such corrupted data must be detected when power is restored
			• Full scan of disk may be required!
			• NV-RAM helps to efficiently detected potentially corrupted blocks

**Disk-Block Access Optimization:**

Efficient data access methods are vital for performance:

- **Buffering** and **Read-ahead**: Reduce latency by prefetching and caching blocks.
    
- **Scheduling (Elevator algorithm)**: Minimizes arm movement by ordering disk access requests.
    
- **File Organization and Defragmentation**: Ensure sequential file blocks are stored contiguously to minimize seeks.
    
- **Non-volatile Write Buffers**: Temporarily store data to protect against power failures and improve write performance.
    

**Conclusion:**

The chapter emphasizes the critical role of physical storage management in database performance and reliability, providing an extensive overview of current technologies, their characteristics, and best practices for optimizing data storage systems.

## Database System Concepts Chapter 13
[[Abraham Silberschatz, Henry Korth and S. Sudarshan - Database System Concepts. 7-McGraw-Hill Education (2020).pdf]]
[[Abraham Silberschatz, 13.pdf]]
### Overview:

This chapter addresses methods of organizing and managing data storage in database systems, focusing on how data is physically structured and accessed on various storage media, such as magnetic disks and SSDs.

### Key Concepts:

### 1. Database Storage Architecture:

- **Non-volatile Storage:** Databases use block-structured storage devices (magnetic disks, SSDs).
    
- **Intermediate Layers:** Databases often utilize operating system files as intermediate storage layers but remain block-aware for efficiency and recovery purposes.
    
- **Data Dictionary:** Stores metadata essential for locating data and managing schema.
    

### 2. File Organization:

Data is logically structured into files, which are sequences of records mapped onto blocks. Files may have fixed-length or variable-length records.

- **Fixed-Length Records:**
    
    - Records fit within single blocks.
        
    - Easy insertions/deletions using a "free-list" for reusing deleted record space.
	    - There are 3 ways for deletion: 
		    - 1 move all data points after i back one space (if I delete row 10 row 11-10, 12-11, 13-12 and so on)
		    - Move new record on top of deleted row so that it replaces the whole row
		    - Do not move records, but link all free records on a free list


- **Variable-Length Records:**
![[Pasted image 20250502120612.png]]
    - Use slotted-page structure to manage variable-sized records within blocks efficiently.
    -
    - Each record contains fixed-length metadata (offset and length) and variable-length attributes separately.


- **Storing Large Objects (LOBs):**
    
    - Objects like multimedia files are stored separately due to size constraints.
        
    - Database systems store pointers to these large objects, either within the database or externally in file systems.
        

### 3. Organization of Records in Files:

Several strategies exist for organizing records within database files, chosen based on data access patterns:

- **Heap File Organization:**
    
    - No particular order of records.
        
    - Uses free-space maps to manage available storage efficiently.
        
- **Sequential File Organization:**
    
    - Records stored physically in a sorted order based on a key attribute, supporting efficient sequential reads.
        
    - Overflow blocks handle insertions; however, frequent reorganization is needed due to inefficiencies over time.
        
- **Multitable Clustering:**
    
    - Stores related records from multiple relations within the same blocks to improve join operation efficiency.
        
    - Effective for frequent join operations but less optimal for individual relation access.
        
- **Partitioning:**
    
    - Splits relations into smaller segments based on attributes like date ranges, optimizing access and storage management (e.g., current year on SSD, past years on magnetic disks).
        

### 4. Data Dictionary Storage:

- Metadata is stored in a data dictionary or system catalog.
    
- Contains relational schemas, attribute details, integrity constraints, views, and index information.
    
- Stored typically as a relational structure itself within the database for efficiency.
    

### 5. Database Buffer:

The database buffer is main memory space dedicated to storing blocks temporarily fetched from disk, managed by the buffer manager to minimize costly disk I/O operations.

- **Buffer Manager Functions:**
    
    - Manages block fetching and eviction, ensuring data integrity and concurrency via pinning and locking mechanisms.
        
    - Replacement policies include Least Recently Used (LRU), Most Recently Used (MRU), and specialized strategies (e.g., toss-immediate for sequential reads).
        
- **Buffer Replacement Strategies:**
    
    - Optimized using database knowledge about access patterns (e.g., frequently accessed metadata or indices).
        
- **Reordering Writes and Recovery:**
    
    - Journaling file systems and logs ensure consistency after crashes despite write-order reordering.
        
    - Database systems use logging (discussed in later chapters) to ensure recovery capabilities.
        

### 6. Column-Oriented Storage:

- Stores data column-wise rather than row-wise, significantly beneficial for analytical workloads.
    
- Advantages:
    
    - Reduced disk I/O for queries accessing few attributes.
        
    - Improved CPU cache usage and compression efficiency.
        
    - Supports vectorized processing for performance gains in analytics.
        
- Limitations:
    
    - Increased cost for reconstructing complete tuples, costly updates/deletes.
        
    - Ideal for read-heavy, analytical databases, not optimal for transaction processing.
        
- **Hybrid Storage Systems:**
    
    - Some systems (e.g., SAP HANA) use both column and row storage, migrating data between them based on usage patterns.
        

### 7. Storage in Main-Memory Databases:

- Entire database fits in RAM, allowing significant performance optimization.
    
- Removes need for buffer management, supports direct memory pointers for fast data access.
    
- Optimizations leverage direct data access and eliminate traditional disk-oriented overheads.
    

---

### Conclusion:

Chapter 13 comprehensively covers database data organization, presenting various strategies for file and record management, storage efficiency techniques, buffer management practices, and specialized storage formats like columnar and main-memory databases. This knowledge enables effective optimization of database systems to meet specific performance and application needs.

## Database System Concepts Chapter 14
[[Abraham Silberschatz, Henry Korth and S. Sudarshan - Database System Concepts. 7-McGraw-Hill Education (2020).pdf]]
[[Abraham Silberschatz, 14.pdf]]
### Overview:

Indexes significantly improve the efficiency of database query processing by allowing quick access to specific records without scanning entire files. Indexing mechanisms are crucial for performance, especially in large databases.

### Basic Concepts of Indexing:

- **Indexes** function similarly to book indexes, allowing rapid lookup of data using keys.
    
- Without indexing, finding specific records would require scanning entire files, causing inefficiency.
    
- Two primary types of indexes:
    
    - **Ordered Indices:** Maintain sorted order of search keys.
        
    - **Hash Indices:** Distribute keys across buckets using a hash function.
        

### Evaluation Criteria for Indexes:

When selecting indexing techniques, database systems consider:

- **Access Types:** Support for exact match or range queries.
    
- **Access Time:** Speed of data retrieval.
    
- **Insertion and Deletion Times:** Cost of maintaining the index when records change.
    
- **Space Overhead:** Extra storage space required for maintaining indexes.
    

---

## Ordered Indices:

### Types of Ordered Indices:

- **Dense Index:**
    
    - Index entry exists for every search-key value.
        
    - Fast lookups, higher space usage.
        
- **Sparse Index:**
    
    - Index entry only for some search-key values, typically one per block.
        
    - Lower space overhead but slightly slower search due to sequential scans after initial block lookup.
        

### Multi-level Indices:

- Large indices use multi-level indexing to reduce disk reads, organizing the index into hierarchical levels.
    
- Outer indices are sparse and point to inner indices, which in turn point to the actual data.
    

### Primary (Clustering) vs. Secondary (Non-clustering) Indices:

- **Primary (Clustering) Index:**
    
    - Determines the physical order of records.
        
    - Typically sparse.
        
- **Secondary Index:**
    
    - Used for attributes that do not determine the file's physical order.
        
    - Must be dense because records are physically unordered.
        

---

## B⁺-Tree Index Structures:

### B⁺-Tree Overview:

- **B⁺-trees** are balanced, multi-level index structures that maintain efficiency despite frequent updates.
    
- They have nodes with multiple keys and pointers, making them broad and shallow compared to binary trees.
    

### B⁺-Tree Properties:

- All leaf nodes are at the same level (balanced).
    
- Nodes contain multiple pointers, optimizing disk I/O operations.
    
- Leaf nodes are linked for efficient sequential access.
    

### Operations on B⁺-Trees:

- **Search:** Efficient traversal from root to leaf for locating records.
    
- **Range Queries:** Efficient due to sequential access at leaf level.
    
- **Insertion:**
    
    - Nodes split when full, with middle keys moved upwards, possibly creating new levels.
        
- **Deletion:**
    
    - Nodes may merge or redistribute entries to maintain balance.
        

### Handling Non-Unique Keys:

- Non-unique keys handled either by appending unique identifiers to keys or by storing multiple pointers per key.
    

---

## Index Update Cost and Efficiency:

- Index insertions and deletions have logarithmic complexity related to tree height (number of levels).
    
- Updates may trigger node splits or merges, but typically only involve minimal disk I/O operations due to shallow tree structure.
    
- Efficient buffer management ensures frequently accessed nodes (especially higher-level nodes) remain in memory.
    

---

## Secondary Indices and Composite Keys:

- **Secondary indices** significantly speed up queries involving attributes that do not physically order the data, despite added overhead for updates.
    
- **Composite keys** use multiple attributes for indexing, providing efficient queries on combined attribute conditions.
    

---

### Conclusion:

Indexes are essential database structures for fast data retrieval, enabling efficient query processing. B⁺-trees stand out as the preferred indexing method due to their balanced structure, support for fast insertion/deletion, and optimization for disk storage. Database designers carefully select and manage indices considering query types, maintenance costs, and storage overhead to ensure database efficiency.

## Database System Concepts Chapter 15
[[Abraham Silberschatz, Henry Korth and S. Sudarshan - Database System Concepts. 7-McGraw-Hill Education (2020).pdf]]
[[Abraham Silberschatz, 15.pdf]]
### Overview

Query processing involves converting high-level database queries (like SQL) into efficient, executable query plans. The process is typically broken down into three main steps:

1. **Parsing and Translation**
    
2. **Optimization**
    
3. **Evaluation**
    

### Steps of Query Processing:

- **Parsing and Translation**:
    
    - Converts SQL queries into a relational algebra form or an internal representation.
        
    - Checks syntax, validates relation names, and constructs a parse tree, replacing views with their definitions.
        
- **Optimization**:
    
    - Determines the most cost-effective query execution plan.
        
    - Considers different equivalent relational algebra expressions and execution strategies.
        
- **Evaluation**:
    
    - Executes the optimized query plan and returns the query results.
        

### Query Evaluation Plans:

- A query-execution plan specifies precisely how each relational algebra operation is executed.
    
- Annotated with algorithms and indices used, forming a detailed evaluation strategy.
    

### Measures of Query Cost:

- Essential for choosing optimal query execution plans.
    
- Typically measured by resources consumed (disk I/O, CPU usage, memory).
    
- Historically focused heavily on disk I/O; recent hardware improvements (e.g., SSDs, large RAM) have shifted emphasis to also include CPU and memory usage.
    
- Commonly measured by:
    
    - Number of blocks transferred (I/O cost).
        
    - Number of seeks and transfers (seek time and transfer time).
        

### Evaluation of Relational Operations:

#### 1. **Selection Operation**

- **Linear Search:** Scans all tuples, expensive if many tuples.
    
- **Index Scan:** Efficient if relevant indices exist, particularly B⁺-tree indices:
    
    - Clustering indices (efficient for range searches, equality on key).
        
    - Non-clustering indices (efficient for single-record lookups, potentially expensive for multiple records due to extra seeks).
        
- Complex selections (conjunctions, disjunctions, negations) implemented using combinations of indexes and set operations (intersection, union).
    

#### 2. **Sorting**

- Essential for operations like joins and ordered output.
    
- **External Sort-Merge Algorithm**:
    
    - Handles data too large for main memory.
        
    - Two stages: initial sorting into runs, and multi-pass merging of sorted runs.
        
    - Cost: dependent on available memory (buffers), number of passes, block transfers, and seeks.
        

#### 3. **Join Operation**

- A crucial and expensive operation in query processing. Several strategies include:
    
    - **Nested-loop Join**:
        
        - Compares every tuple pair; simple but inefficient for large datasets.
            
    - **Block Nested-loop Join**:
        
        - Improved version reading blocks of tuples, significantly reducing disk I/O.
            
    - **Indexed Nested-loop Join**:
        
        - Uses an index on the inner relation for efficient access, significantly improving performance for selective joins.
            
    - **Merge Join (Sort-Merge Join)**:
        
        - Requires sorted inputs, efficient for large joins.
            
        - Performs a simultaneous scan of sorted relations, merging matching tuples.
            
    - **Hash Join**:
        
        - Uses hashing to partition relations into buckets.
            
        - Efficient, particularly with large relations, but requires careful memory management and can face hash-table overflow or skewed partitions.
            

### Advanced Optimization Techniques:

- **Hybrid Algorithms** (e.g., bitmap index scan): Combines linear and index-based scans to adaptively handle unpredictable selection conditions.
    
- **Pipelined Operations**: Avoids writing intermediate results to disk by passing results between operations as soon as they are generated, improving query execution speed.
    

---

### Conclusion

Query processing systematically transforms high-level queries into efficient, executable plans. Key aspects include careful cost estimation, algorithm selection for operations like selections, sorting, and joins, and adapting to modern hardware capabilities. Effective query processing significantly improves database performance and user experience.