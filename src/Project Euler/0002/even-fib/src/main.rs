fn main() {
    let limit = 4_000_000;
    let fib = fib_to_limit(limit);

    let even_fib_sum: usize = fib.iter().filter(|&n| n % 2 == 0).sum();
    println!(
        "The sum of all even fibonacci numbers up to 4,000,000 is {}",
        even_fib_sum
    );
}

fn fib_to_limit(upper: usize) -> Vec<usize> {
    let mut fibonacci: Vec<usize> = Vec::new();
    let mut a = 0;
    let mut b = 1;
    let mut num = 0;
    while num <= upper {
        num = a + b;
        if num > upper {
            break;
        }
        fibonacci.push(num);
        a = b;
        b = num;
    }
    return fibonacci;
}
