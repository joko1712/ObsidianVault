## Lectures 1-4: 
Basacly intro into dna and such only migningfull information is:
- Reading frames (ORFs) - +/-
- Codon translation table and an aminoacid - +
- The \#G-\#C skew diagram - ++

### Lecture 5 Is about global alignment
- Global Alignment 
	-  Needleman-Wunsch Algorithm - +/-

### Lecture 6 continues the global alignment
- Local Sequence Alignment (Smith-Waterman Algorithm) 
- Semi-global Alignment 
- Affine Gap Penalty
study (Rocha and Ferreira Chapter 6 • Compeau and Pevzner Chapter 5)

### Lecture 7 Fasta and Blast
- FASTA is a fast algorithm for finding similar sequences 
	- It is not an optimal alignment algorithm.
	- The heuristics make the computation faster but do not guarantee optimality • 
	- Focuses on the best matching stretches of the sequence 
	- then builds an alignment that follows these stretches within a limited window, thus reducing the computational demands.
- BLAST (Basic Local Alignment Search Tool) 
	- currently the most used to perform searches over DNA or protein sequence databases. 
	- similar to FASTA, but around 100 times faster 
	- It gains this advantage by skipping the alignment step and focusing on high-scoring pairs HSPs (also known as maximal segment pairs MSPs)
		- The main steps of the BLAST algorithm are: 
		1. Remove regions of low complexity (e.g. sequence repeats) from the sequence (may compromise the quality of the alignment) 
		2. Obtain all possible “words” of size w, i.e. sub-sequences of length w occurring in the query sequence; 
		3. For each word from the previous step, compile the list of all possible words of size w that can be defined in the allowable alphabet, whose alignment score (no gaps, using SM) is higher than a threshold T; 
		4. Search in the database for all occurrences of the words collected in the last step, which represent matches (hits) of size w between the query and one of the database sequences; 
		5. Extend all hits from the last step, in both directions, while the score follows a given criterion (typically, the criterion is dependent on the size of the extension); 
		6. Select the alignments in the previous step with highest scores, normalized for its size (these are named the high-scoring pairs-HSPs).
		
- BLASTN allows to optimize the search for highly similar sequences, allowing a faster search for longer sequences (using the megablast program). In BLASTN, there are a number of parameters that can be set including the word size w whose default value is 11, and the ones defining the scoring function, the match/mismatch scores (default 2 and −3) and the gap penalties for opening and extension (default values of −5 and −2). 
- BLASTP can be used to search for protein sequence databases, such as the nr, the non-redundant set of protein sequences, RefSeq, UniProt (curated sequences from the SwissProt database) or sequences from the PDB database. The set of adjustable parameters are similar to BLASTN, with different default values: w is set to 6, while the scoring function uses a substitution matrix (BLOSUM62 by default), and gap penalties for opening and extension (default values of −11 and −1). For protein alignments, there are alternative programs which are not covered in this book, such as PSI-BLAST, PHI-BLAST and DELTA-BLAST.
- BLASTX – takes a DNA sequence as query, but searches over protein sequences, and thus can be used to find potential protein products encoded by a nucleotide sequence;
- TBLASTN – takes a protein sequence as query, but searches over DNA sequence databases, thus trying to identify database sequences encoding proteins similar to the one in the query;
- TBLASTX – takes a DNA sequence as input, searching over DNA sequence databases, but in both cases the sequences are translated considering the 6 reading frames and the matches are searched over protein sequences (this leads to 36 comparisons);
- 
study (Rocha Chapter 7 • Jones Chapter 9 • Baxevanis Chapter 3)

### Lecture 8 
- Multiple Sequence Alignment (MSA) 
- Scoring Multiple Alignments 
- Heuristic Algorithms for Multiple Sequence Alignment 
	- Progressive 
	- Iterative 
	- Others
study (Ferreira Chapter 8 • Pevzner Chapter 9 • Compeau Chapter 5 (epilogue))

### Lecture 9
- Phylogenetic Trees 
- Methods for Computing Phylogenetic Trees 
	- Distance-based Methods: UPGMA, Neighbour-Joining 
	- Maximum Parsimony 
	- Maximum Likelihood
study Rocha Chapter 8

### Lecture 10
study (Cédric Notredame, Desmond G. Higgins, SAGA: Sequence Alignment by Genetic Algorithm, Nucleic Acids Research, Volume 24, Issue 8, 1 April 1996, Pages 1515– 1524, https://doi.org/10.1093/nar/24.8.1515 )

### Lecture 11
- Importance of Motif Finding 
- Scoring Motifs 
- Brute force search 
- Median String approach 
- Branch-and-bound 
- Heuristic Search 
study (Compeau Chapter 2 • Rocha Chapter 10)

### Lecture 12
- Greedy motif search 
	- Iterates profile matrix according to current best k-mers 
- Random search 
	- Initial positions are randomly sampled 
- Gibbs Sampling 
	- At each step, remove a sequence and update the motif with weighted sampled match
study (Compeau Chapter 2 • Rocha Chapter 11 • Greedy Search is called Expectation Maximization here)



# TO Study:

- [x] Rocha and Ferreira Chapter 6 • Compeau and Pevzner Chapter 5
- [x] Rocha and Ferreira Chapter 6 • Compeau and Pevzner Chapter 5
- [x] Rocha Chapter 7 • Jones Chapter 9 • Baxevanis Chapter 3
- [x] Ferreira Chapter 8 • Pevzner Chapter 9 • Compeau Chapter 5 (epilogue)
- [x] Rocha Chapter 8
- [ ] Cédric Notredame, Desmond G. Higgins, SAGA: Sequence Alignment by Genetic Algorithm, Nucleic Acids Research, Volume 24, Issue 8, 1 April 1996, Pages 1515– 1524, https://doi.org/10.1093/nar/24.8.1515 
- [ ] Compeau Chapter 2 • Rocha Chapter 10
- [ ] Compeau Chapter 2 • Rocha Chapter 11 • Greedy Search is called Expectation Maximization here






# TO solve:
## Exercises and Programming Projects Exercises (ROCHA)
Chapter 6
1. 
	1. a. Consider the application of the Smith-Waterman algorithm to the sequences: S1: ANDDR; S2: AARRD. The alignment parameters should be the BLOSUM62 sub- stitution matrix and the value of g = −8. Calculate (by hand); (i) the S matrix with the best scores; (ii) the trace-back matrix; (iii) the optimal alignment and its score. Check if there are any alternative optimal alignments. 
	2. b. Write a program in Python, using the functions defined in this chapter, that allows to confirm the results you obtained in the previous exercise. 
2. 
	1. a. Consider the application of the Needleman-Wunsch algorithm to the following DNA sequences: S1: TACT; S2: ACTA. The used parameters are the following: gap penalty (g): −3, match (equal characters): 3, mismatch: −1. Calculate (by hand); (i) the S matrix with the best scores; (ii) the trace-back matrix; (iii) the optimal align- ment and its score. Check if there are any alternative optimal alignments. 
	2. b. Write a program in Python, using the functions defined in this chapter, that allows to confirm the results you obtained in the previous exercise. 
3. Write and test a function that, given a binary matrix (with elements 0 or 1), coming from a function that creates dotplot matrices, identifies the largest diagonal containing ones (it can be the main diagonal or any other diagonal in the matrix). The result should be a tuple with: the size of the diagonal, the row where it begins, the column where it begins.
4. Consider the functions to calculate pairwise global alignments. Note that, in the case there are distinct alignments with the same optimal score, the functions only return one of them. Notice that these ties arise in the cases where, in the recurrence relation of the DP algorithm, there are at least two alternatives that return the same score. 
	1. a. Define a function needleman_Wunsch_with_ties, which is able to return a trace- back matrix (T ) with each cell being a list of optimal alternatives and not a single one. 
	2. b. Define a function recover_align_with_ties, which taking a trace-back matrix created by the previous function, can return a list with the multiple optimal alignments. 
5. Considering the functions to calculate pairwise local alignments, define similar functions to the previous exercise for the case of multiple optimal alignments. Note that, in this case, ties may also arise due to multiple equal scores in the S matrix (check the example from Figs. 6.7 and 6.8). 
6. Write and test a function that, given two lists of sequences (l1 and l2), searches for each sequence in the l1 the most similar sequence in l2 (considering similarity based on iden- tity, as defined above). The result will be a list with the size l1, indicating in each position i the index in l2 of the most similar sequence to the ith sequence in l1.
7. Write and test a function that, given two DNA sequences s1 and s2, searches for the best possible local alignment between a putative protein encoded by a reading frame from s1 and a putative protein encoded by a reading frame from s2 (check Section 4.4 for the de- tails on reading frame calculations). The result will be a tuple with the best alignment and its score. The parameters of the alignment should be passed as arguments to the function.
-----

Chapter 7

 1. Consider the function get_hits above. Create a variant that allows at most 1 character to be different between the sequence and the query words. 
 2. 
	 1. a. Write a function that given two sequences of the same length, determines if they have at most d mismatches (d is an argument of the function). The function returns True if the number of mismatches is less or equal to d, and False otherwise. 
	 2. b. Using the previous function find all approximate matches of a pattern p in a se- quence. An approximate match of the pattern can have at most d characters that do not match (d is an argument of the function). 
3. Search in the UniProt database the record for the human protein APAF (O14727). Save it in the FASTA format. Using BioPython perform the following operations: 
	1. a. Load the file and check that the protein contains 1248 aminoacids. 
	2. b. Using BLASTP, search for sequences with high similarity to this sequence, in the “swissprot” database. 
	3. c. Check which the global parameters were used in the search: the database, the substi- tution matrix, and the gap penalties. 
	4. d. List the best alignments returned, showing the accession numbers of the sequences, the E value of the alignments, and the alignment length. 
	5. e. Repeat the search restricting the target sequences to the organism S. cerevisiae (sug- gestion: use the argument entrez_query in the qblast function). Searching Similar Sequences in Databases 177 
	6. f. Check the results from the last operation, listing the best alignments, and checking carefully in each the start position of the alignment in the query and in the sequence. 
	7. g. What do you conclude about the existence of homologous genes in the yeast for the human protein APAF ?

-----

Chapter 8

1. Consider the following four sequences of DNA: 
	S1: ACATATCAT
	S2: AACAGATCT 
	S3: AGATATTAG 
	S4: GCATCGATT 
	Write a Python script, using the code developed in this chapter, to generate a multiple alignment of these sequences using the progressive algorithm implemented in class Mul- tipleAlignment. Consider the parameters to be: match score = 1, mismatch = −1, gap penalty g = −1. 
2. Implement a method calculating the score sum of pairs (SP) of a given alignment. The method should be included in the MultipleAlignment class, taking as input an alignment (object of class MyAlign). Notice that the parameters for the score are given in an inter- nal variable of the class (alignpars). 
3. 
	1. a. Consider the application of the Needleman-Wunsch algorithm to the protein se- quences: S1: APSC; S2: TAPT, using the BLOSUM62 matrix and g = −4. Calculate the optimal alignment. 
	2. b. Based on the result of the previous exercise, could the following alignment be pro- vided by the progressive algorithm implemented in this chapter? 
		-AP-SC 
		TAPT-- 
		TAT-S-  
	3. c. Calculate the SP score of the previous alignment. 
	4. d. Write a Python script, using the code developed in this chapter to confirm your re- sults. 
4. Write a method to add to the class MyAlign that, given an alignment (self ), returns the list of columns (indexes) in the alignment that are rich in polar basic aminoacids (R, H, or K). To be considered rich, the column needs to include at least half of the aminoacids in this group. 
5. Write a method to add to the class MyAlign that, given an alignment (self ), returns a string with a symbol for each column of the alignment, following these rules: ‘*’, if the column is fully conserved (it has all symbols equal and no gaps); ‘:’, if the column has at least half of the symbols equal; ‘.’: if the column does not match any of the previous, but has no gaps; ‘ ’, in all other cases. 
6. Write a method to add to the class MultipleAlign that, given an alignment (object of class MyAlign), identifies the columns where this alignment has high quality. In this case, a column is considered of high quality if the score of the alignment, calculated by the SP method is larger than 0. The method should return a list of indexes of the selected columns. 
7. Consider the following sequence of aminoacids: 
	MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTE DPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLG FLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQH MTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPE VGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGR DRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRE RFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD 
	1. a. Through the NCBI site, use the BLASTP application to search for similar sequences (alternatively use BioPython interface for this purpose) – see Chapter 7 for details. 
	2. b. From the result, select 10 to 12 matching sequences. Try to select different species and avoid sequences marked as “PREDICTED”. Save those into a file in the FASTA format. Keep as sequence identifiers (after the “>” in the first line) the species name, without spaces. 
	3. c. In the EBI site, use the Clustal Omega application to get a multiple sequence align- ment using the previous set of sequences. Save the alignment (in the “clustal” for- mat) and the guide tree in two different files. 
	4. d. Load the previous alignment using BioPython. 
	5. e. Calculate the consensus of the alignment. Suggestion: check the class AlignInfo in the BioPython documentation or implement a function yourself. 
	6. f. Calculate a list of positions where the alignment is conserved (i.e. all sequences have the same aminoacid and there are no gaps). Calculate the percentage of these posi- tions in the whole alignment.
	7. g. From the previous information, get the region of the alignment more conserved, i.e. the longest sequence of consecutive conserved positions from the list above.
## Exercises and Programming Projects Exercises (Compeau and Pevzner)
Chapter 5
Construct the alignment of ATGTTATA and ATCGTCC corresponding to the alignment path in Figure 5.6 (right). 