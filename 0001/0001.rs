fn main() {
    // Find the sum of all the multiples of 3 or 5 below 1000.
    let sum = (1..1000).filter(|&x| x % 3 == 0 || x % 5 == 0)
                       .fold(0, |sum, x| sum + x);
    println!("{}", sum);
}
