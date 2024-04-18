use regex::Regex;
use std::collections::{HashMap, HashSet};
use std::fs;
use std::io;
use std::io::BufRead;
use std::process;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let matches = clap::Command::new("preq")
        .version("0.1.0")
        .author("Antonio Braz <antoniomtbraz@gmail.com>")
        .about("Generates requirements.txt for Python projects.")
        .arg(
            clap::Arg::new("FILE")
                .help("Sets the input file to use")
                .required(true)
                .index(1),
        )
        .get_matches();

    let filename = matches.get_one::<String>("FILE").unwrap(); // Safe to unwrap because it's required
    let imports = get_imports_from_file(&filename);
    let packages = map_imports_to_packages(&imports);
    println!("{}", packages.join("\n"));
    Ok(())
}

fn read_fallback_stdlib() -> Vec<String> {
    let file_path = "./assets/stdlib";
    let file = fs::File::open(file_path);

    match file {
        Ok(file) => {
            let buf_reader = io::BufReader::new(file);
            buf_reader.lines().filter_map(Result::ok).collect()
        }
        Err(e) => {
            // Now printing the specific error message
            println!(
                "Failed to read fallback data file '{}'; Error: {}; returning empty list.",
                file_path, e
            );
            Vec::new()
        }
    }
}

fn get_imports_from_file(file_path: &str) -> Vec<String> {
    let file = fs::File::open(file_path);
    let stdlib = get_python_stdlib();
    let import_regex = Regex::new(r"^\s*(from\s+[\w\.]+|import\s+[\w\.]+)").unwrap();

    let mut modules = HashSet::new();

    match file {
        Ok(file) => {
            let buf_reader = io::BufReader::new(file);
            buf_reader
                .lines()
                .filter_map(Result::ok)
                .filter(|line| import_regex.is_match(line))
                .for_each(|line| {
                    let parts: Vec<&str> = line.split_whitespace().collect();
                    if let Some(module) = parts.get(1) {
                        // TODO: handle namespace packages
                        let module_name = module.trim().to_string();
                        if !stdlib.contains(&module_name) && !module_name.is_empty() {
                            modules.insert(module_name);
                        }
                    }
                });

            // Convert HashSet to Vec for a consistent return type or further processing
            modules.into_iter().collect()
        }
        Err(_) => {
            println!("Failed to read file '{}'; returning empty list.", file_path);
            Vec::new()
        }
    }
}

fn map_imports_to_packages(imports: &Vec<String>) -> Vec<String> {
    let import_package_map = get_import_package_map();
    imports
        .iter()
        .filter_map(|import| {
            if let Some(packages) = import_package_map.get(import) {
                Some(packages.join(" "))
            } else {
                println!("No package found for import '{}'", import);
                None
            }
        })
        .collect()
}

fn find_python_command() -> Option<String> {
    let commands = ["python3", "python", "py"];
    for &command in commands.iter() {
        if process::Command::new(command)
            .arg("--version")
            .output()
            .is_ok()
        {
            return Some(command.to_string());
        }
    }
    None
}

fn get_python_stdlib() -> Vec<String> {
    let python_command = find_python_command().unwrap_or_else(|| {
        println!("Python interpreter not found. Ensure Python is installed and in your PATH.");
        "python".to_string() // Default to "python" if neither found
    });

    let python_code = "from sys import builtin_module_names as b, stdlib_module_names as s; print('\\n'.join(sorted(set(b) | s)))";
    let output = process::Command::new(python_command)
        .arg("-c")
        .arg(python_code)
        .output();

    match output {
        Ok(output) if output.status.success() => match String::from_utf8(output.stdout) {
            Ok(stdlib_str) => stdlib_str.lines().map(|s| s.to_string()).collect(),
            Err(_) => {
                println!("Error converting Python command output to UTF-8; using file fallback.");
                read_fallback_stdlib()
            }
        },
        _ => {
            println!("Python command failed or encountered an error; using file fallback.");
            read_fallback_stdlib()
        }
    }
}

fn get_import_package_map() -> HashMap<String, Vec<String>> {
    let python_command = find_python_command().unwrap_or_else(|| {
        println!("Python interpreter not found. Ensure Python is installed and in your PATH.");
        "python".to_string() // Default to "python" if neither found
    });

    let python_code = "import importlib.metadata as i;print(i.packages_distributions())";
    let output = process::Command::new(python_command)
        .arg("-c")
        .arg(python_code)
        .output();

    if let Ok(output) = output {
        if let Ok(stdout) = String::from_utf8(output.stdout) {
            let cleaned_json = stdout.trim_end().replace("'", "\"");
            if let Ok(map) = serde_json::from_str::<HashMap<String, Vec<String>>>(&cleaned_json) {
                return map;
            }
        }
    }

    println!("Command failed to run or output was invalid.");
    HashMap::new() // Return an empty HashMap if there was an error
}
