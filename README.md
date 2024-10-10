# MathsGPT
# Text To Math Problem Solver and Data Search Assistant

This Streamlit application allows users to solve complex mathematical problems and search for general information using Wikipedia. It integrates the power of Groq's `Gemma 2` model for natural language understanding and problem-solving, along with LangChain for handling logical reasoning and computations. Users can input queries related to math, logic, or general topics, and the app provides detailed solutions and explanations.

## Features

- Solve complex mathematical expressions.
- Answer logic-based questions with step-by-step reasoning.
- Fetch information from Wikipedia about a variety of topics.
- Seamless user interaction through a chat interface.

## Demo

<img src="https://i.imgur.com/zNm7XTx.gif" alt="Demo GIF" width="600"/>

## How to Use

1. Enter your Groq API key in the sidebar to authenticate.
2. Ask a math-related question, and the app will calculate the answer using the `Calculator` tool.
3. For general knowledge queries, the app uses Wikipedia as a source of information.
4. The chatbot displays responses step by step, ensuring clarity in explanations.

## API Key

This app requires a Groq API key. You can input your API key through the Streamlit sidebar before using the app.

## Tech Stack

- **Streamlit**: For building an interactive web app.
- **LangChain**: To power the logical reasoning and LLM-based tools.
- **Groq's Gemma 2**: LLM used to understand and answer queries.
- **Wikipedia API**: For fetching information about general topics.

## Example Usage

- **Math Problem**: 
   - **Question**: "What is the derivative of x^2 + 3x + 2?"
   - **Response**: "The derivative of x^2 + 3x + 2 is 2x + 3."

- **General Knowledge**: 
   - **Question**: "Tell me about Albert Einstein."
   - **Response**: "Albert Einstein was a theoretical physicist who developed the theory of relativity..."

## Requirements

- Python 3.10+
- Streamlit
- LangChain
- LangChain-Groq
- WikipediaAPIWrapper
- StreamlitCallbackHandler

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/math-problem-solver.git
   cd math-problem-solver
