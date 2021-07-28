fn main() {
    // string
    let s1: String = String::from("Hello, World!");
    let s2: &str = &s1; // String -> &str
    let s3: String = s2.to_string(); // &str -> String

    println!("{}", s3);
}
