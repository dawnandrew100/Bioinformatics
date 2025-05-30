fn main() {
    let upper_lim = 999*999;
    let lower_lim = 100*100;
    let target_count = 3;
    println!("{}", largest_palindrome(upper_lim, lower_lim, target_count));
}

fn largest_palindrome(max_num: usize, min_num: usize, t_count: usize) -> usize {
    let mut option: usize = max_num;
    
    while option > min_num {
        let opt = option.to_string();
        let is_palindrome = check_is_palindrome(opt);
        if is_palindrome == false {
            option -= 1;
            continue;
        }
        let factors = gen_all_factors(option);
        
        let n_chars: Vec<usize> = factors.iter()
                            .cloned()
                            .filter(|&n| n.to_string().chars().count() == t_count)
                            .collect();
        if factors.len() % 2 != 0 {
            let mid = factors.len() / 2;
            if factors[mid] * factors[mid] == option && factors[mid].to_string().chars().count() == t_count {
                println!("{}", factors[mid]);
                return option;
            }
        }
        if n_chars.len() > 0 {
            let (equal, fact_vec) = factors_eq_palindrome(&n_chars, option);
            if equal {
                println!("{:?}", fact_vec);
                return option;
            }
        }
        option -= 1;
    }
    return 0;
}

fn check_is_palindrome(word: String) -> bool {
    let mut l = 0 as usize;
    let mut r = word.len() - 1;
    let mut num_is_palindrome = true;
    let word_vec: Vec<char> = word.to_lowercase().chars().collect();

    while l < r {
        if word_vec[l] != word_vec[r] {
            num_is_palindrome = false;
            break;
        }
        l += 1;
        r -= 1;
    }
    return num_is_palindrome;
}

fn gen_all_factors(target: usize) -> Vec<usize> {
    let sqrt_n = (target as f64).sqrt() as usize;
    let mut factors = Vec::new();
    
    for i in 1..=sqrt_n {
        if target % i == 0 {
            factors.push(i);
            if i != target / i {
                factors.push(target / i);
            }
        }
    }
    factors.sort();
    return factors;
}

fn factors_eq_palindrome(factors: &Vec<usize>, target: usize) -> (bool, Vec<usize>) {
    let mut l: usize = 0;
    let mut r: usize = l + 1;
    let mut fac_vec: Vec<usize> = Vec::new();
    
    if factors.len() == 1 {
        if factors[0] * factors [0] == target {
            fac_vec.push(factors[0]);
            return (true, fac_vec);
        }
        return (false, fac_vec);
    }
    loop {
        if r >= factors.len() {
            l += 1;
            r = l + 1;
            if r == factors.len(){
                break;
            }
        }
        let opt = &factors[l] * &factors[r];
        if opt == target {
            fac_vec.push(factors[l]);
            fac_vec.push(factors[r]);
            return (true, fac_vec);
        }
        r += 1;
    }
    return (false, fac_vec);
}
