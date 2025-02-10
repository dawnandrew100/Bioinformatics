def main():
    n, m = 83, 19
    rabbit_per_month, Solution = rabbit_recur(n, m)
    rabbit_dict = {i:rabbit for i, rabbit in enumerate(rabbit_per_month, 1)}
    print(f"{rabbit_dict}\n\n{Solution = }")

def rabbit_recur(months: int, mortality: int) -> tuple[list[int], int]:
    """
    :param months: number of months
    :param mortality: number of months that each rabbit lives
    :return: number of rabbits alive by the specified month 
    rtype: tuple[list[int], int]
    """
    rabbits = []
    for i in range(months):
        if i == 0 or i == 1:
            #initialises first two positions of array
            rabbits.append(1)
            continue
        if i < mortality:
            #normal fib sequence when no rabbit dies
            rabbits.append(rabbits[-1] + rabbits[-2])
            continue
        if i == mortality:
            #the first rabbit dies when mortality equals the current number of months
            rabbits.append(rabbits[-1] + rabbits[-2] - 1)
            continue
        #after mortality is reached, all the rabbits born n+1 months before current month die
        rabbits.append(rabbits[-1] + rabbits[-2] - rabbits[-(mortality+1)])
    return rabbits, rabbits[-1]

if __name__ == "__main__":
    main()
