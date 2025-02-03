def main():
    n, k = 32, 3
    Solution = rabbit_recur(n, k)
    print(f"{Solution = }")

def rabbit_recur(months: int, offspring: int) -> int:
    if months <= 0:
        return 0
    if months == 1:
        return 1
    return rabbit_recur(months-1, offspring)+(rabbit_recur(months-2, offspring)*offspring)

if __name__ == "__main__":
    main()
