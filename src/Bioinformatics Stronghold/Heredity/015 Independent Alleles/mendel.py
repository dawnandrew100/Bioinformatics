def main():
    generation = 7
    min_threshold = 35
    probability = independent_alleles(generation, min_threshold)
    print(round(probability, 3))

def independent_alleles(k: int, N: int) -> float:
    """
    :param k: N-th generation
    :param N: Threshold individuals in N-th generation
    :return: Probability at least N individuals have a heterogenous genotype in the k-th generation
    """
    if N > 2**k:
        raise ValueError("Expected number of minimum individuals is greater than total number of offspring possible for this generation!")
    if N == 0:
        N = 1 # This prevents division by 0 problems
    if N < 0 or k < 0:
        raise ValueError("Both parameters must be positive!")
    max_pop = 2**k
    binom_coeff = 1  # This corresponds to C(max_pop, N) when N = 0
    if N > 1:
        for i in range(1, N):
            #allows for next for loop to start at correct coefficient
            binom_coeff = binom_coeff * (max_pop - i + 1) // i
    solution = 0
    for i in range(N, max_pop + 1)
        #calculated incrementally instead of calculating the factorial for each interation
        binom_coeff = binom_coeff * (max_pop - i + 1) // i
        """
        All the ways you can choose N individuals from max population at N-th generation
        multiplied by the probability exactly i individuals will be heterogenous
        multiplied by the probability that exactly everyone else will not be heterogenous
        """
        solution += binom_coeff * (0.25 ** i) * (0.75 ** (max_pop - i))
    return solution

if __name__ == "__main__":
    main()
