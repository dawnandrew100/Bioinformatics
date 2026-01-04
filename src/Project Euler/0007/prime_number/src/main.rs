fn main() {
    let target = 10001;
    println!("{}", inefficient_nth_prime_finder(target));
}

fn inefficient_nth_prime_finder(nth_prime: usize) -> usize {
    let mut primes: Vec<usize> = Vec::new();
    let mut curr = 2;
    'main_loop: loop {
        if primes.len() == nth_prime {
            break;
        }
        for i in &primes {
            if curr % i == 0 {
                curr += 1;
                continue 'main_loop;
            }
        }
        primes.push(curr);
        curr += 1;
    }
    return primes[primes.len() - 1];
}
