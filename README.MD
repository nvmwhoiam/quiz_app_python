# Python Quiz Application

This Python application simulates a simple quiz where users are presented with multiple-choice questions, select answers, and receive a score at the end.

## Features

- Displays a welcome message to the user.
- Shows a series of multiple-choice questions (loaded from `quiz_data.json`).
- Allows the user to select an answer for each question.
- Calculates the user's score based on correct answers.
- Displays the total score and a message based on the user's performance.
- Ensures valid input by validating user answers.
- Thanks the user for taking the quiz upon completion.

## Project Structure

The project consists of the following files:

- `app.py`: The main Python script that runs the quiz application.
- `quiz_data.json`: JSON file containing quiz questions, options, and answers.

## Installation and Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nvmwhoiam/quiz_app_python.git
   cd quiz_app_python
   ```

2. **Install dependencies (none required):**

This project does not require any external dependencies.

3. **Run the quiz:**

Ensure quiz_data.json is in the same directory as app.py.

```bash
python app.py
```

4. **Follow on-screen instructions:**

Ensure quiz_data.json is in the same directory as app.py.

- Answer each question by entering the number corresponding to your choice.
- At the end of the quiz, your total score will be displayed along with a thank you message.

## Example Question Format

Each question in `quiz_data.json` is represented as follows:

```json
{
  "question": "What is the capital of France?",
  "options": ["Berlin", "Madrid", "Paris", "Rome"],
  "answer": "Paris"
}
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- nvmwhoiam
- GitHub: <a href="https://github.com/nvmwhoiam">Your GitHub Profile</a>
