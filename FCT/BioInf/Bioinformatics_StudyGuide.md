
# 🧬 Bioinformatics 2025/2026 — Study Guide

## 📘 Course Info
- **Instructor**: André Lamúrias (a.lamurias@fct.unl.pt)
- **Lectures**: Thursdays 9–11
- **Labs**: Thursdays 11–13
- **Platforms**: 
  - Moodle: https://moodle.fct.unl.pt/course/view.php?id=9786
  - CLIP: https://clip.fct.unl.pt/
  - Rosalind: https://rosalind.info/classes/enroll/e678b99afb/

---

## 🧬 Lecture 1: Introduction to Bioinformatics
### Course Structure
- **Assessment**
  - Theory Tests (2): 60%
  - Projects (2): 40%
- **Passing Requirement**: ≥9.5/20 on each component

### Objectives & Topics
- Understand algorithms for biological data
- Analyze sequence alignment, genome assembly, motif discovery
- Applications in genomics and medicine

### Interdisciplinary Areas
- Biology + Computer Science + Statistics
- Key areas: Sequence analysis, Ontologies, Systems biology

---

## 🧪 Lecture 2: Biomolecules & Biological Concepts
### Biomolecules
- **DNA**: Double-stranded (A-T, G-C)
- **RNA**: Single-stranded (A-U, G-C)
- **Proteins**: Made of 20 amino acids

### Processes
- **Replication**: DNA duplication
- **Transcription**: DNA → mRNA
- **Translation**: mRNA → Protein

---

## 🧬 Lecture 3: Processing Biological Sequences
- DNA/RNA represented by ACGT/U
- Codon translation (triplets → amino acids)
- Reverse complements & transcription
- Basic algorithms: GC content, k-mer counts
- Python class: `MySeq`

---

## 🔍 Lecture 4: Finding Patterns in DNA
- **Frequent Words / k-mers**
- **Clump Finding**
- **Skew Diagrams** to locate oriC
- **Hamming Distance** for approximate matches

---

## 🧬 Lecture 5: Pairwise Sequence Alignment (1)
- Global, Local, Semi-global alignments
- **Needleman-Wunsch** algorithm
- Match = +1, Mismatch = -1, Gap = -2
- Dot plots for visual comparison

---

## 🧬 Lecture 6: Pairwise Sequence Alignment (2)
- **Smith-Waterman** for local alignment
- **Affine gap penalties** = open + extension
- Useful for domain-level sequence comparison

---

## 🧬 Lecture 7: Multiple Sequence Alignment (MSA)
- **Progressive alignment** (e.g., ClustalW)
- **Scoring**: Sum-of-Pairs, Consensus sequences
- **PSSMs**: position-specific scoring matrices

---

## 🌳 Lecture 8: Phylogenetic Trees
- Tree parts: leaves = sequences, internal = ancestors
- **Newick format**
- Construction methods:
  - Distance-based (UPGMA, Neighbor-Joining)
  - Maximum Parsimony
  - Maximum Likelihood

---

## 🧬 Lecture 9: Distance-Based Phylogeny
### UPGMA
- Assumes constant mutation rate
- Clusters closest nodes iteratively

### Neighbor-Joining
- Allows variable mutation rates
- Uses Q-matrix for merging decisions

---

## 🧬 Lecture 10: MSA with Genetic Algorithms
- Heuristic search using evolution metaphor
- **Population** of alignments → **fitness** score
- **Crossover/Mutation** to evolve MSAs
- Keep alignments valid (equal length, no all-gap columns)

---

## 🔍 Lecture 11: Motif Finding (1)
- Find conserved k-mers in DNA sequences
- **(k, d)-motifs**: k-mers with ≤d mismatches
- **Profile Matrix** & **Consensus**
- Algorithms:
  - Brute force
  - Median String
  - Branch and Bound
  - Heuristic Consensus

---

## 🧬 Lecture 12: Motif Finding (2)
- **Greedy Search** with pseudocounts
- **Randomized Motif Search**: iterate from random k-mers
- **Gibbs Sampling**: updates one k-mer at a time
- Handles local optima better with multiple runs

---

## 📚 Recommended Reading
- Compeau & Pevzner (Ch. 2)
- Rocha (Ch. 8, 10, 11)
- Notredame & Higgins, *SAGA: Sequence Alignment by Genetic Algorithm*

---

## 🧠 Practice Topics
- Implementing alignment algorithms
- Pattern finding using k-mers
- Phylogenetic tree construction
- MSA evaluation and scoring
- Motif discovery with heuristics and randomness
