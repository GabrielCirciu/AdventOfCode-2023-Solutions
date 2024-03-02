use std::fs::read_to_string;

fn main() {
    let lines = read_lines("problem_input");
    let mut final_value = 0;
    for line in lines {
        final_value += (find_number(line.clone()) + &find_number(line.chars().rev().collect()))
            .parse::<i32>()
            .unwrap();
    }
    println!("{final_value}"); // Prints 55447, which is the correct answer
}

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
