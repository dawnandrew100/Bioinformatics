fn main() {
    let nums: usize = (1..1000)
        .filter(|&n| n % 3 == 0 || n % 5 == 0)
        .collect::<Vec<usize>>()
        .iter()
        .sum();
    println!(
        "The sum of all even numbers divisible by 3 and 5 up to 1000 is {}",
        nums
    );
}
