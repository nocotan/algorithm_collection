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

    // enum
    #[derive(Debug)]
    enum Event {
        Quit,
        KeyDown(u8),
        MouseDown { x: i32, y: i32 },
    }

    let e1 = Event::Quit;
    let e2 = Event::KeyDown (1);
    let e3 = Event::MouseDown { x: 10, y: 10};

    println!("{:?}", e1);
    println!("{:?}", e2);
    println!("{:?}", e3);

    // result
    let result: Result<i32, String> = Ok(200);
    match result {
        Ok(code) => println!("code: {}", code),
        Err(err) => println!("Err: {}", err),
    };

    let result: Result<i32, String> = Ok(200);
    if let Ok(code) = result {
        println!("code: {}", code);
    }

    let result: Result<i32, String> = Ok(200);
    println!("code: {}", result.unwrap_or(-1));
    let result: Result<i32, String> = Err("error".to_string());
    println!("code: {}", result.unwrap_or(-1));

    fn func(code: i32) -> Result<i32, String> {
        println!("code: {}", code);
        Ok(100)
    }
    let result: Result<i32, String> = Ok(200);
    let next_result = result.and_then(func);
    println!("{:?}", next_result);
    let result: Result<i32, String> = Err("error".to_string());
    let next_result = result.and_then(func);
    println!("{:?}", next_result);

    fn error_handling(result: Result<i32, String>) -> Result<i32, String> {
        let code = result?;
        println!("code: {}", code);
        Ok(100)
    }
    let result: Result<i32, String> = Err("error".to_string());
    let next_result = error_handling(result);
    println!("{:?}", next_result);

    // Vec
    let v1 = vec![1, 2, 3, 4, 5];
    let v2 = vec![0; 5];
    println!("{:?}", v1);
    println!("{:?}", v2);

    let v = vec![1, 2, 3, 4, 5];
    println!("{}", v[0]);

    let v = vec![1, 2, 3, 4, 5];
    for element in &v {
        println!("{}", element);
    }

    // Box
    fn print(s: Box<[u8]>) {
        println!("{:?}", s);
    }

    let byte_array = [b'h', b'e', b'1', b'1', b'o'];
    print(Box::new(byte_array));
}
