def correspond(motif, chaine, position):
    if len(motif) > len(chaine):
        return False
    for i in range(len(motif)):
        if chaine[position + i] != motif[i]:
            return False
    return True


def est_inclus(brin, gene):
    taille_gene = len(gene)
    taille_brin = len(brin)
    for i in range(taille_gene - taille_brin + 1):
        if correspond(brin, gene, i):
            return True
    return False

# Tests

assert correspond("AA", "AAGGTTCC", 4) is False
assert correspond("AT", "ATGCATGC", 4) is True

assert est_inclus("AATC", "GTACAAATCTTGCC") is True
assert est_inclus("AGTC", "GTACAAATCTTGCC") is False
assert est_inclus("AGTC", "GTACAAATCTTGCA") is False
assert est_inclus("AGTC", "GTACAAATCTAGTC") is True
