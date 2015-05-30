fn main() {
    let mut sieve: Vec<bool> = vec![true; (1000000 + 1) as usize];
    let mut n = 0;
    let mut nth_prime = 0;
    for i in (2..1000000) {
        if sieve[i as usize] == true {
            nth_prime = i;
            n = n + 1;
            if n == 10001 { break }
            for j in (2..(1000000 / i + 1) as i32) {
                sieve[(i * j) as usize] = false;
            }
        }
    }
    println!("{}", nth_prime);
}
