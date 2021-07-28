fn main() {
    // string
    let s1: String = String::from("Hello, World!");
    let s2: &str = &s1; // String -> &str
    let s3: String = s2.to_string(); // &str -> String

    println!("{}", s3);

    // tuple
    let mut t = (1, "2");
    t.0 = 2;
    t.1 = "3";

    println!("{:?}", t);

    // array
    let mut a: [i32; 3] = [0, 1, 2];
    let b: [i32; 3] = [0; 3];
    a[1] = b[1];
    a[2] = b[2];

    println!("{:?}", &a[1..3]);

    // struct
    #[derive(Debug)]
    struct Person {
        name: String,
        age: u32,
    }

    let p = Person {
        name: String::from("John"),
        age: 8,
    };

    println!("{:?}", p);
}
