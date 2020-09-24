def DNA_strand(dna):
    new_dna = ''
    for i in dna:
        if i == 'A':
            new_dna += 'T'
        if i == 'T':
            new_dna += 'A'
        if i == 'C':
            new_dna += 'G'
        if i == 'G':
            new_dna += 'C'

    return new_dna

print (DNA_strand('AAATTT'))












# new_items = [x if x % 2 else None for x in items]
