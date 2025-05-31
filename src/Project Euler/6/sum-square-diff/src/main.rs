fn main() {
    let upper_limit = 100;
    let nat_vec: Vec<usize> = (1..=upper_limit).collect();
    let sum_of_squares: usize = nat_vec.iter().map(|n| n * n).sum();
    println!(
        "The sum of squares from 1 to {upper_limit} is {}.",
        sum_of_squares
    );
    let square_of_sums: usize = {
        let sum = nat_vec.iter().sum::<usize>();
        sum * sum
    };
    println!(
        "The square of sums from 1 to {upper_limit} is {}.\n",
        square_of_sums
    );
    println!(
        "The absolute difference is {}",
        square_of_sums - sum_of_squares
    );
}
