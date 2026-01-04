fn main() {
    let upper_lim = 2_000_000;
    let prime_sum = (2..upper_lim)
        .filter(|&n| !(2..=((n as f64).sqrt() as usize)).any(|i| n % i == 0))
        .sum::<usize>();

    println!("{prime_sum}");
}
