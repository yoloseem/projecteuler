fn main() {
    let num: i64 = 600851475143;
    let factor_limit = (num as f64).sqrt() as i32;
    let mut sieve: Vec<i32> = vec![0; (factor_limit + 1) as usize];
    let mut largest_prime_factor = 0;
    for factor in (2..factor_limit) {
        if sieve[factor as usize] == 0 {
            if num % (factor as i64) == 0 {
                largest_prime_factor = factor;
            }
            for i in (2..(factor_limit / factor + 1) as i32) {
                sieve[(factor * i) as usize] = 1;
            }
        }
    }
    println!("{}", largest_prime_factor);
}
