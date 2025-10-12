# Representations and Basic Algorithms

def validate_dna(dna_seq):
    """ Checks if DNA sequence is valid. Returns True is sequence is
    valid, or False otherwise. """
    seqm = dna_seq.upper()
    valid = seqm.count("A") + seqm.count("C") + seqm.count("G") + \
            seqm.count("T")
    if valid == len(seqm): return True
    else: return False

def frequency(seq):
    """ Calculates the frequency of each symbol in the sequence.
        Returns a dictionary. """
    dic = {}
    for s in seq.upper():
        if s in dic: dic[s] += 1
        else: dic[s] = 1
    return dic

def gc_content(dna_seq):
    """ Returns percentage of G and C nucleotides in a DNA sequence."""
    gc_count = 0
    for s in dna_seq:
        if s in "GCgc": gc_count += 1
    return gc_count / len(dna_seq)

def gc_content_subseq(dna_seq , k=100):
    """ Returns GC content of non−overlapping sub−sequences of size k.
        The result is a list. """
    res = []
    for i in range(0, len(dna_seq)-k+1, k):
        subseq = dna_seq[i:i+k]
        gc = gc_content(subseq)
        res.append(gc)
    return res


# Transcription and Reverse Complement

def transcription(dna_seq):
    """ Function that computes the RNA corresponding to the
        transcription of the DNA sequence provided. """
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    return dna_seq.upper().replace("T","U")

def reverse_complement(dna_seq):
    """ Computes the reverse complement of the DNA sequence. """
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    comp = ""
    for c in dna_seq.upper():
        if c == "A":
            comp = "T" + comp
        elif c == "T":
            comp = "A" + comp
        elif c == "G":
            comp = "C" + comp
        elif c == "C":
            comp = "G" + comp
    return comp


# Translate

def translate_codon(cod):
    """Translates a codon into an aminoacid using an internal
       dictionary with the standard genetic code."""
    tc = {"GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
          "TGT":"C", "TGC":"C",
          "GAT":"D", "GAC":"D",
          "GAA":"E", "GAG":"E",
          "TTT":"F", "TTC":"F",
          "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",
          "CAT":"H", "CAC":"H",
          "ATA":"I", "ATT":"I", "ATC":"I",
          "AAA":"K", "AAG":"K",
          "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
          "ATG":"M", "AAT":"N", "AAC":"N",
          "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
          "CAA":"Q", "CAG":"Q",
          "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
          "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S",
          "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
          "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
          "TGG":"W",
          "TAT":"Y", "TAC":"Y",
          "TAA":"_", "TAG":"_", "TGA":"_"}
    if cod in tc: return tc[cod]
    else: return None

def translate_seq(dna_seq , ini_pos = 0):
    """ Translates a DNA sequence into an aminoacid sequence. """
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    seqm = dna_seq.upper()
    seq_aa = ""
    for pos in range(ini_pos , len(seqm)-2,3):
        cod = seqm[pos:pos+3]
        seq_aa += translate_codon(cod)
    return seq_aa

def codon_usage(dna_seq , aa):
    """Provides the frequency of each codon encoding a given
       aminoacid, in a DNA sequence."""
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    seqm = dna_seq.upper()
    dic = {}
    total = 0
    for i in range(0, len (seqm)-2, 3):
        cod = seqm[i:i+3]
        if translate_codon(cod) == aa:
            if cod in dic: dic[cod] += 1
            else: dic[cod] = 1
            total += 1
    if total >0:
        for k in dic:
            dic[k] /= total
    return dic


# Input Output

def sequence_from_keyboard():
    """Reads a DNA sequence from keyboard. Verify validity. Compute
       transcription, reverse complement, gc content and translation"""
    seq = input ("Insert DNA sequence: ")
    if validate_dna(seq):
        print("Valid sequence")
        print("Transcription: ", transcription(seq))
        print("Reverse complement:", reverse_complement(seq))
        print("GC content (global):", gc_content(seq))
        print("Direct translation:" , translate_seq(seq))
    else: print("DNA sequence is not valid")

def read_seq_from_file(filename):
    """ Reads a sequence from a multi−line text file. """
    fh = open(filename , "r")
    lines = fh.readlines()
    seq = ""
    for l in lines:
        seq += l.replace("\n","")
    fh.close()
    return seq

def write_seq_to_file(seq, filename):
    """ Writes a sequence to file. """
    fh = open(filename , "w")
    fh.write(seq)
    fh.close()

def sequence_from_file():
    """Reads a DNA sequence from file. Verify validity. Compute
       gc content. Write transcription, reverse complement and
       translation to new files. """
    fname = input("Insert input filename:")
    seq = read_seq_from_file(fname)
    if validate_dna(seq):
        print("Valid sequence") 
        print("GC content (global):", gc_content(seq))
        write_seq_to_file(transcription(seq), "trs-" + fname)
        write_seq_to_file(reverse_complement(seq), "rc-" + fname)  
        write_seq_to_file(translate_seq(seq), "trl-" + fname)
    else: print("DNA sequence is not valid")

