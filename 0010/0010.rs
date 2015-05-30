fn main() {
    let mut sieve: Vec<bool> = vec![true; (2000000 + 1) as usize];
    let mut sum_of_primes: i64 = 0;
    for i in (2..2000000) {
        if sieve[i as usize] == true {
            sum_of_primes += i;
            for j in (2..(2000000 / i + 1) as i64) {
                sieve[(i * j) as usize] = false;
            }
        }
    }
    println!("{}", sum_of_primes);
}
