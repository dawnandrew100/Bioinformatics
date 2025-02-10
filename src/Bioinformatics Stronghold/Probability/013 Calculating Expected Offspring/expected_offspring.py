def main():
    genotype_pairs = "17780 18274 17061 17308 18707 17881"
    genotype_pairs = [int(x) for x in genotype_pairs.split()]
    print(expected_offspring(genotype_pairs))

def expected_offspring(chrom_pairs: list[int]) -> float:
    """
    :param chrom_pairs: list of ints representing number of couples with each genotype pair
    :return: expected number of offspring
    """
    #Probabilities of posessing dominant genotype given:
    #0:AA-AA 1:AA-Aa 2:AA-aa 3:Aa-Aa 4:Aa-aa 5:aa-aa
    dom_prob = {0: 1, 1: 1, 2: 1, 3: 0.75, 4: 0.5, 5: 0}
    
    temp_prob = [x*dom_prob[i] for i, x in enumerate(chrom_pairs)]
    return sum(temp_prob)*2 #each individual gives birth to two offspring

if __name__ == "__main__":
    main()
