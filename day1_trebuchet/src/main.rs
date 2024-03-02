use std::fs::read_to_string;

fn main() {
    let lines = read_lines("problem_input");
    let mut final_value = 0;
    for line in lines {
        let first = find_number(line.clone());
        let last = find_number(line.chars().rev().collect());
        final_value += first + last;
    }
    println!("Final number: {}", final_value)
}

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

// Function that returns the first number in a string, without using Option
fn find_number(s: String) -> i32 {
    for c in s.chars() {
        if c.is_digit(10) {
            // Turn the character into a number and return it
            return c.to_string().parse().unwrap();
        }
    }
    0
}
