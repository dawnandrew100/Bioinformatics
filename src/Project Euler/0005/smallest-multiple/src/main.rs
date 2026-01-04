fn main() {
    let upper_limit = 20;
    let primes = sieve_of_eratosthenes(upper_limit);
    // Instead of dividing by every number from 2 to 20
    // dividing by the highest power of each prime within the limit
    // speeds up computations because of fewer comparisons
    let divisors: Vec<usize> = primes
        .iter()
        .cloned()
        .map(|n| {
            let mut x = n;
            while x * n < upper_limit {
                x *= n;
            }
            return x;
        })
        .collect();
    // Started at the product of all primes because the lcm must be divisible
    // by all primes at a minimum
    // (number produced is still low enough to not overshoot true answer)
    let mut curr: usize = primes.iter().product();

    'outer: loop {
        curr += 1;
        for i in &divisors {
            if curr % i != 0 {
                continue 'outer;
            }
        }
        /* Target answer when upper_limit == 20 */
        // assert_eq!(curr, 232792560);
        break;
    }
    println!("{curr}");
}

fn sieve_of_eratosthenes(limit: usize) -> Vec<usize> {
    if limit < 2 {
        return Vec::new();
    }

    let mut is_prime = vec![true; limit + 1];
    is_prime[0] = false;
    is_prime[1] = false;

    let sqrt_limit = (limit as f64).sqrt() as usize;

    for i in 2..=sqrt_limit {
        if is_prime[i] {
            for j in (i * i..=limit).step_by(i) {
                is_prime[j] = false;
            }
        }
    }

    is_prime
        .iter()
        .enumerate()
        .filter_map(|(i, &prime)| if prime { Some(i) } else { None })
        .collect()
}
