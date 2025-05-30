fn main() {
    let option = "1101";
    // Implement thing to generate 3 digit * 3 digit products
    let is_palindrome = check_is_palindrome(option);

    println!("{is_palindrome}");
}

fn check_is_palindrome(word: &str) -> bool {
    let mut l = 0 as usize;
    let mut r = word.len() - 1;
    let mut is_palindrome = true;
    let word_vec: Vec<char> = word.to_lowercase().chars().collect();

    while l < r {
        if word_vec[l] != word_vec[r] {
            is_palindrome = false;
            break;
        }
        l += 1;
        r -= 1;
    }
    return is_palindrome;
}
