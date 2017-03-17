def check_DNA(seq1, seq2):
    seq2 = seq2[::-1]
    pairs = {'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A'}
    seq1_conj = ''.join([pairs[base] for base in seq1])
    return (seq1_conj in seq2) or (seq2 in seq1_conj)
