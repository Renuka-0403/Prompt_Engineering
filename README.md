# Prompt Engineering

## Qwen Prompt Lab – Exploring LLM Prompt Engineering Techniques

## Project Description

Qwen Prompt Lab is an interactive web application developed using Python and Streamlit to demonstrate different prompt engineering techniques using the Qwen Large Language Model (LLM).

The application allows users to enter tasks, select different prompting techniques, adjust model parameters, and generate AI responses. It also provides prompt previews, response comparisons, response downloads, and prompt history.

## Features

- **Zero-shot Prompting:** Generates responses using direct instructions without examples.
- **One-shot Prompting:** Uses one example to guide the model's response.
- **Few-shot Prompting:** Uses multiple examples to demonstrate the expected response format.
- **Chain of Thought (CoT):** Encourages structured, step-by-step explanations.
- **Manual Chain of Thought:** Uses explicitly defined instructions to organize the solution.
- **Tree of Thought (ToT):** Explores multiple approaches and compares possible solutions.
- **Prompt Preview:** Displays the generated prompt before execution.
- **Response Comparison:** Compares outputs from different prompting techniques.
- **Temperature Control:** Adjusts the creativity and randomness of responses.
- **Maximum Token Control:** Controls the maximum response length.
- **Sample Tasks:** Provides predefined examples for testing.
- **Download Response:** Allows users to download generated responses as text files.
- **Prompt History:** Displays previously generated tasks and responses.

## Technologies Used

- Python
- Streamlit
- Qwen 2.5 (3B)
- Ollama
- Requests

## Installation and Setup

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Install Ollama

Download Ollama from:

https://ollama.com/

### Step 3: Download the Qwen Model

Open the terminal and execute:

```bash
ollama pull qwen2.5:3b
```

### Step 4: Install Required Libraries

Open the project folder in the terminal and execute:

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

Execute the following command:

```bash
streamlit run app.py
```

The application will open automatically in your default web browser.

## How to Use

1. Open the Qwen Prompt Lab application.
2. Select a sample task or enter your own task.
3. Choose a prompting technique from the dropdown menu.
4. Adjust the temperature and maximum token settings.
5. Click the Generate Response button.
6. View the generated prompt and AI response.
7. Use the comparison feature to compare different prompting techniques.
8. Download the generated response if required.
9. View previously generated responses in the Prompt History section.

## Example Input

```text
A college wants to reduce food waste in its cafeteria.
Identify the main problems, suggest three possible solutions,
compare their advantages and disadvantages, and recommend
the most effective solution.
```

## Prompting Techniques Explained

### 1. Zero-shot Prompting

Zero-shot prompting generates an answer directly from the given instruction without providing examples.

### 2. One-shot Prompting

One-shot prompting provides one example to guide the model in understanding the expected response format.

### 3. Few-shot Prompting

Few-shot prompting provides multiple examples to help the model recognize patterns and generate relevant responses.

### 4. Chain of Thought (CoT)

Chain of Thought prompting encourages the model to organize its solution into logical steps and provide a structured explanation.

### 5. Manual Chain of Thought

Manual Chain of Thought uses explicitly written instructions to guide the model through understanding, organizing, and checking a task before presenting the answer.

### 6. Tree of Thought (ToT)

Tree of Thought prompting encourages the model to explore multiple possible approaches, compare them, and select a suitable solution.

## Applications

- Understanding different prompt engineering techniques.
- Experimenting with Large Language Models.
- Comparing AI-generated responses.
- Improving prompt design and instruction quality.
- Learning practical applications of Generative AI.
- Exploring structured AI problem-solving approaches.

## Future Enhancements

- Support for additional LLM models.
- Save and export prompt history.
- Advanced prompt optimization.
- Response evaluation and scoring.
- Additional prompting strategies.
- Improved response comparison and visualization.

## Conclusion

Qwen Prompt Lab provides a simple and interactive environment for exploring different prompt engineering techniques using a Large Language Model. It demonstrates how different prompting strategies influence AI-generated responses and helps users understand the practical importance of effective prompt design.

## Author

Developed as an LLM Prompt Engineering project using Python, Streamlit, Ollama, and Qwen 2.5.
