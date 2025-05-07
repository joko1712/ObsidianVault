# [[SBD - Notes]]

## Chapter 12: Physical Storage Systems

### Summary:

Chapter 12 covers different types of storage systems and storage media. Key concepts include:

- **Storage Hierarchy:** differentiating between volatile (cache, RAM), nonvolatile storage (SSD, magnetic disks), and tertiary storage (tape).
    
- **Magnetic Disks:** Organization into platters, tracks, sectors, and the concept of disk controllers.
    
- **Performance Measures:** Access time (seek time, rotational latency), data transfer rates, IOPS (Input/Output Operations per Second).
    
- **Flash Storage (SSD):** NAND vs. NOR flash, SSD advantages (no seek or rotation), limitations (wear leveling).
    

### Exercises for Practice:

1. Describe and compare volatile storage, nonvolatile storage, and tertiary storage in terms of access speed and typical usage scenarios.
    
2. Explain the components of a magnetic disk and their roles in data storage.
    
3. Calculate the average access time for a magnetic disk given the seek time and rotational latency.
    
4. Discuss wear leveling in SSD storage, explaining why it is essential.
    

---

## Chapter 13: Data Storage Structures

### Summary:

This chapter explores file organization and storage structures in databases, including:

- **File Organization:** Fixed-length and variable-length records, heap file organization, sequential file organization, and clustering.
    
- **Slotted Page Structure:** Management of variable-length records on disk.
    
- **Large Object Storage (BLOBs/CLOBs):** PostgreSQL TOAST technique.
    
- **Partitioning:** Splitting a table across multiple storage structures for efficiency.
    

### Exercises for Practice:

1. Compare heap, sequential, and clustering file organizations. Provide scenarios where each would be optimal.
    
2. Explain how the slotted page structure works, and discuss its advantages and disadvantages.
    
3. Given a database with records larger than a disk page, what storage strategies could you use?
    
4. Discuss the advantages and disadvantages of partitioning a database table.
    

---

## Chapter 14: Indexing

### Summary:

Indexing is crucial for efficient data retrieval. Key topics covered include:

- **Ordered Indices:** Clustering (primary) and nonclustering (secondary) indices.
    
- **Dense vs. Sparse Indices:** Efficiency and maintenance trade-offs.
    
- **Multilevel Indices:** Managing large indices by structuring them hierarchically.
    
- **B+ Trees:** Properties, operations (insert, delete, search), advantages in ordered indexing.
    
- **Hash Indices:** Direct addressing of data using hash functions.
    
- **Write-optimized indices:** Handling high volumes of updates efficiently (LSM trees).
    

### Exercises for Practice:

1. Describe the difference between dense and sparse indices. In what scenario would each be most appropriate?
    
2. Explain the structure and key operations (search, insert, delete) of a B+ tree. Illustrate with a simple example.
    
3. Discuss why B+ trees are preferable over binary search trees for indexing in databases.
    
4. Compare hashing and indexing for data retrieval. When would you prefer one over the other?
    

---

## Chapter 15: Query Processing

### Summary:

This chapter addresses how queries are parsed, optimized, and executed, including:

- **Basic Steps in Query Processing:** Parsing, translation into relational algebra, optimization, and evaluation.
    
- **Measures of Query Cost:** Estimation using disk I/O, seek time, and block transfer metrics.
    
- **Selection Operations:** Linear and index scans.
    
- **Join Operations:** Nested-loop joins, block nested-loop joins, indexed nested-loop joins, merge joins, and hash joins.
    
- **Sorting and Other Operations:** Techniques for efficient execution of sorting and aggregation.
    

### Exercises for Practice:

1. Describe the three basic steps in query processing.
    
2. Given tables `R` (1,000 blocks) and `S` (200 blocks), calculate the cost of performing a block nested-loop join if the memory can hold 51 blocks.
    
3. Explain different algorithms for performing joins. Provide examples of situations where one join algorithm outperforms another.
    
4. Discuss how query costs are estimated in a DBMS and why accurate estimation is critical for performance.
    

---

## Example Test Questions:

### Chapter 12 (Physical Storage Systems):

- Given a disk with an average seek time of 5 ms and rotational latency of 4 ms, calculate the average access time.
    

### Chapter 13 (Data Storage Structures):

- Can slotted pages handle records larger than a single page? Why or why not, and what alternatives exist?
    

### Chapter 14 (Indexing):

- Why might a secondary index on a non-key attribute be very costly to maintain?
    

### Chapter 15 (Query Processing):

- Calculate the cost of executing an index nested-loop join for two relations R (200 blocks, 10000 tuples) and S (100 blocks, 5000 tuples) given certain B+ tree heights and transfer times.


---


# Formulas & Explanations

## Chapter 12: Physical Storage Systems

### Formulas & Explanations:

**1. Average access time of a magnetic disk:**

![[Pasted image 20250502114801.png]]

- **Seek Time:** Time to position disk head over the correct track.
    
- **Rotational Latency:** Waiting time for the desired sector to rotate under the head (average is half a rotation).
    
- **Transfer Time:** Time needed to transfer data from disk to memory.
    

### Exercise:

Calculate the average access time given:

- Average seek time = 5 ms
    
- Disk rotation = 7200 RPM
    
- Transfer rate = 200 MB/s
    
- Data block size = 4 KB.
    

---

## Chapter 13: Data Storage Structures

### Formulas & Explanations:

**2. Blocking Factor:**

![[Pasted image 20250502114844.png]]

- Measures how many records fit in a single block.
    

**3. Number of Blocks needed for a relation:**

![[Pasted image 20250502114913.png]]
### Exercise:

Given a database block size of 4096 bytes and a record size of 128 bytes, calculate:

- The blocking factor.
    
- The number of blocks required to store 10,000 records.
    

---

## Chapter 14: Indexing

### Formulas & Explanations:

**4. Height of a B+ Tree:** For a B+ Tree of order nnn with KKK search-key values:
![[Pasted image 20250502114928.png]]

- Determines how deep the tree structure is, which affects the number of disk accesses.
    

### Exercise:

Calculate the maximum height of a B+ tree given:

- Order n=200n = 200n=200
    
- Number of search-key values K=106K = 10^6K=106.
    

---

## Chapter 15: Query Processing

### Formulas & Explanations:

**5. Cost of Block Nested-Loop Join (worst case):**

![[Pasted image 20250502114943.png]]

- brb_rbr​ is the number of blocks in the outer relation.
    
- bsb_sbs​ is the number of blocks in the inner relation.
    

**6. Cost of Block Nested-Loop Join (best case with sufficient memory MMM):**

![[Pasted image 20250502115000.png]]

**7. Cost of Index Nested-Loop Join:**

![[Pasted image 20250502115010.png]]

- nrn_rnr​ = Number of tuples in the outer relation.
    
- ccc = Cost to access one tuple via index (typically height of the B+ tree plus one).
    

**8. Cost of External Merge-Sort:** With a memory buffer of MMM blocks, sorting NNN blocks:

![[Pasted image 20250502115023.png]]

### Exercises:

1. Calculate the cost of a block nested-loop join given two tables RRR and SSS:
    
    - RRR has 500 blocks, SSS has 200 blocks.
        
    - Buffer has 100 blocks available.
        
2. Calculate the cost of an external merge-sort given:
    
    - Relation size N=10,000N = 10,000N=10,000 blocks
        
    - Memory buffer size M=101M = 101M=101 blocks.
        

