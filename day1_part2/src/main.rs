use aho_corasick::AhoCorasick;
use std::fs::read_to_string;

fn find_number(l_input: &str, pattern: [(&str, u8); 18]) -> (u8, u8) {
    let mut matches = vec![];
    for mat in AhoCorasick::builder()
        .ascii_case_insensitive(true)
        .build(pattern.iter().map(|x| x.0).collect::<Vec<_>>())
        .unwrap()
        .find_overlapping_iter(l_input)
    {
        matches.push((mat.start() as u8, pattern[mat.pattern()].1));
    }
    (matches[0].1, matches[matches.len() - 1].1)
}

fn main() {
    let patterns = [
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
    ];
    let mut total: u32 = 0;
    for line in read_to_string("problem_input").unwrap().lines() {
        let digits = find_number(line, patterns);
        total += format!("{}{}", digits.0, digits.1).parse::<u32>().unwrap();
    }
    println!("{total}"); // Prints 54706 which is the correct answer
}
