# Text To Math Problem Solver and Data Search Assistant

This project is an AI-powered text-to-math problem solver that helps users solve mathematical queries by interpreting natural language input. It leverages advanced mathematical tools and reasoning capabilities to offer detailed solutions to a variety of mathematical questions.

## Features

- **Mathematical Expression Evaluation**: Handles various mathematical symbols such as factorial (`!`), square root (`√`), pi (`π`), Euler's number (`e`), modulus (`%`), and more.
- **Trigonometric and Logarithmic Functions**: Supports common functions like `sin`, `cos`, `tan`, `log`, and `log10`.
- **LLM-based Reasoning**: Uses Groq’s `Gemma2-9b-It` model for logical reasoning and complex problem-solving.
- **Wikipedia Integration**: Leverages Wikipedia for retrieving relevant information when solving logic-based questions.
- **Streamlit Interface**: Offers an interactive user interface for question input and real-time response generation.

## How It Works

1. **User Input**: The user can enter any math-related question in natural language.
2. **Expression Preprocessing**: The app preprocesses mathematical symbols and functions, transforming them into a Python-compatible format using the `math` library.
3. **Evaluation**: The mathematical expression is evaluated safely using Python’s `eval` function.
4. **Reasoning Engine**: The reasoning engine powered by the Groq LLM provides logical explanations and step-by-step solutions.
5. **Wikipedia Search**: If the question requires external information, the assistant will use Wikipedia to fetch and display relevant content.

## Supported Symbols and Functions

- **Factorial**: `!` (e.g., `5!`)
- **Square Root**: `√` (e.g., `√16`)
- **Exponentiation**: `^` (e.g., `2^3` becomes `2**3`)
- **Trigonometric Functions**: `sin`, `cos`, `tan` (e.g., `sin(π/2)`)
- **Logarithms**: `log` for natural log, `log10` for base-10 log
- **Modulus**: `%` (e.g., `10 % 3`)
- **Pi**: `π` (e.g., `π * r^2`)
- **Euler’s Number**: `e` (e.g., `e^x` becomes `math.e**x`)

## Technologies Used

- **Python**
- **LangChain**
- **Groq's Gemma2-9b-It Model**
- **Streamlit** for UI
- **WikipediaAPIWrapper** for Wikipedia searches
- **Google Generative AI** for additional logical reasoning

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    https://github.com/VivekSuryavanshi03/MathsGPT.git
    ```

2. Set up the virtual environment:
    ```bash
    conda create -p env python==3.10 -y
    env\Scripts\activate # For Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

- After starting the app, you'll be prompted to enter your Groq API key to access the model.
- Enter any math question or natural language problem, and the assistant will respond with a detailed solution.
- The app will also suggest relevant resources if your question is more logic-based or theoretical.

## Example Questions

- `What is 5! + √16?`
- `How do you calculate π * r^2 for a circle?`
- `What is log(100)?`
- `Solve 12!/(6! * 6!)`

## Contact

For any inquiries or issues, feel free to contact me:

- **Name**: Vivek Kumar
- **Email**: [vivek.2022ug3014@iiitranchi.ac.in](mailto:vivek.2022ug3014@iiitranchi.ac.in)

## License

This project is licensed under the MIT License.
