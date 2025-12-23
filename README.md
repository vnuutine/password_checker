# Password Checker

A simple command-line tool for evaluating password strength based on common security rules.  
It analyzes a password, assigns a strength score, and reports which requirements are missing.

This project is intentionally minimal and focuses on clean structure, readable logic, and a proper CLI interface.

---

## Features

- Evaluates password strength using multiple rules
- Produces a numeric score (0–5) and human-readable classification
- Reports exactly which rules are missing
- Command-line interface with built-in help
- Clean separation between analysis logic and output

---

## Password Rules

A password is evaluated against the following criteria:

- Minimum length of 8 characters
- Contains at least one digit
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one symbol from `!@#$%^&*`

Each satisfied rule contributes one point to the total score.

---

## Installation

Clone the repository and navigate into it:

```bash
git clone https://github.com/<your-username>/password_checker.git
cd password_checker
```

No external dependencies are required beyond Python 3.10+.

---

## Usage

Run the tool by passing the password as a positional argument:

```bash
python3 password_checker.py 'MyPassword123!'
```

### Example output

```text
Password score (0-5): 5
Password strength: Very strong
```

For a weaker password:

```text
Password score (0-5): 1
Password strength: Very weak
Missing rules:
- long enough
- has digits
- has uppercase
- has symbol
```

---

## Important Note on Quoting

If your password contains special characters such as `!`, you should wrap it in **single quotes** when running from the terminal:

```bash
python3 password_checker.py 'P@ssw0rd!'
```

This avoids shell interpretation issues.

---

## Help

You can view the built-in help message with:

```bash
python3 password_checker.py --help
```

---

## Project Structure

- `password_checker.py` — main CLI entrypoint and implementation
- Rule checks are implemented as small, focused functions
- Password analysis is separated from output formatting

This structure makes the logic easy to test and extend.

---

## License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

---