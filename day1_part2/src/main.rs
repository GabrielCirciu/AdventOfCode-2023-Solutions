use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn find_number(s: String) -> String {
    for c in s.chars() {
        if c.is_numeric() {
            return c.to_string();
        }
    }
    "0".to_string()
}

fn main() {
    let mut total = 0;
    for line in read_lines("problem_input") {
        total += (find_number(line.clone()) + &find_number(line.chars().rev().collect()))
            .parse::<i32>()
            .unwrap();
    }
    println!("{total}"); // Prints 55447, which is the correct answer
}
