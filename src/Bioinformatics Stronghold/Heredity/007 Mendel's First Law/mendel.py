def main():
    print(f"{find_mendel_prob(23,20,15)=}\n")
    print(f"{find_mendel_prob(24,22,24)=}\n")
    print(f"{find_mendel_prob(2,2,2)=}\n")
    print(f"{find_mendel_prob(28,24,18)=}\n")

def find_mendel_prob(k: int, m: int, n: int) -> float:
    """
    :param k: number of homozygous dominant individuals
    :param m: number of heterozygous individuals
    :param n: number of homozygous recessive individuals
    :return: probability offspring of two randomly selected individuals will have a dominant gene
    """
    N = float(k+m+n)
    #(k(k-1)+km+kn+mk+0.75m(m-1)+0.5mn+nk+0.5mn)/N(N-1)
    #(k^2-k+2km+2kn+0.75m^2-0.75m+mn)/N(N-1)
    return (k**2-k+2*k*m+2*k*n+0.75*m*m-0.75*m+m*n)/(N**2-N)

if __name__ == "__main__":
    main()
