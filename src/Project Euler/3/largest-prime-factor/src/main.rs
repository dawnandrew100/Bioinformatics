fn main() {
    let number: u64 = 600_851_475_143;
    let mut n = number;
    let mut factor = 2_u64;
    let mut last_factor = 1;
    let mut prime_factors: Vec<u64> = Vec::new();

    while factor * factor <= n {
        if n % factor == 0 {
            last_factor = factor;
            // divides out all multiples therefore n % factor == 0 will only happen for primes
            while n % factor == 0 {
                prime_factors.push(factor);
                n /= factor;
            }
        }
        factor += if factor == 2 { 1 } else { 2 }; // Skip even numbers after 2
    }

    if n > 1 {
        last_factor = n; // n itself is prime
        prime_factors.push(n)
    }

    println!("The prime factors of {number} are {:?}", prime_factors);
    println!("Largest prime factor: {}", last_factor);
}

fn _old_implementation() {
    // This was my original solution but finding all of the primes up to the square root took
    // FOREVER
    let number: f64 = 600851475143.0;
    let mut primes: Vec<usize> = (2..=number.sqrt() as usize).collect();
    let number = number as usize;
    let mut i = 0;

    // This does produce a valid answer but it takes A WHILE to find all the primes
    while i < primes.len() {
        let num = primes[i];
        primes = primes
            .iter()
            .cloned()
            .filter(|&n| n == num || n % num != 0)
            .collect();
        i = i + 1;
    }
    println!("{:?}", primes);

    // This part was nearly instantaneous
    let mut res = number;
    let mut prime_factors: Vec<usize> = Vec::new();
    for prime in primes {
        if res == 1 {
            break;
        }
        while res % prime == 0 {
            prime_factors.push(prime);
            res = res / prime;
        }
    }
    if res != 1 {
        prime_factors.push(res);
    }

    println!("{:?}", prime_factors);
    println!("{}", prime_factors.last().unwrap());
}
