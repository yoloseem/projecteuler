fn is_palindrome(x: i32) -> bool {
    let xstr = x.to_string();
    let xforward = xstr.chars().take(xstr.len());
    let xbackward = xstr.chars().rev().take(xstr.len());
    return xforward.zip(xbackward).all(|(a, b)| (a == b))
}

fn main() {
    let mut largest_palindrome = 0;
    for x in (100..1000) {
        for y in (100..1000) {
            let num = x * y;
            if is_palindrome(num) && num > largest_palindrome {
                largest_palindrome = num;
            }
        }
    }
    println!("{}", largest_palindrome);
}
