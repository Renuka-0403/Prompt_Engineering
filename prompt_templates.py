def build_prompt(technique, task):
    if technique == "Zero-shot":
        prompt = f"""
You are a helpful AI assistant.

Complete the following task accurately.

Task:
{task}

Provide a clear and relevant answer.
"""

    elif technique == "One-shot":

        prompt = f"""
You are a helpful AI assistant.

Example:

Task: What is photosynthesis?

Answer: Photosynthesis is the process by which
green plants use sunlight, water and carbon dioxide
to produce food and oxygen.

Now complete the following task using a similar format.

Task:
{task}

Answer:
"""
    elif technique == "Few-shot":

        prompt = f"""
You are a helpful AI assistant.

Study the following examples.

Example 1:
Task: Define AI.
Answer: AI enables machines to perform tasks
that normally require human intelligence.

Example 2:
Task: Define ML.
Answer: Machine Learning is a branch of AI
that allows computers to learn from data.

Example 3:
Task: Define Deep Learning.
Answer: Deep Learning uses neural networks
to learn complex patterns from large datasets.

Now follow the same style.

Task:
{task}

Answer:
"""
    elif technique == "CoT":

        prompt = f"""
You are a helpful AI assistant.

Solve the following task carefully.
Break the solution into clear, logical steps
and provide a concise explanation of the approach.

Task:
{task}

Answer:
"""
    elif technique == "Manual CoT":

        prompt = f"""
You are an AI assistant.

Follow these instructions:

1. Understand the given task.
2. Identify the important information.
3. Organize the solution into logical steps.
4. Check the result for accuracy.
5. Present the final answer clearly.

Task:
{task}

Provide the final answer with a brief explanation.
"""
    elif technique == "ToT":

        prompt = f"""
You are a helpful AI assistant.

Explore multiple possible approaches to the task.

1. Identify three possible approaches.
2. Briefly explain the advantages of each.
3. Compare the approaches.
4. Select the most suitable approach.
5. Present the final answer with a concise explanation.

Task:
{task}

Answer:
"""
    else:
        prompt = task
    return prompt