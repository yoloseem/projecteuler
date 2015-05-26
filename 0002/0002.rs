fn main() {
    let mut first = 0;
    let mut second = 1;
    let mut sum = 0;
    while second <= 4000000 {
        if second % 2 == 0 { sum = sum + second }
        let third = first + second;
        first = second;
        second = third;
    }
    println!("{}", sum)
}
