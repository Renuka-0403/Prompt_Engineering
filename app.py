import streamlit as st
from llm import generate_response
from prompt_templates import build_prompt
st.set_page_config(
    page_title="Qwen Prompt Lab",
    page_icon="🤖",
    layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

if "answer" not in st.session_state:
    st.session_state.answer = ""

if "final_prompt" not in st.session_state:
    st.session_state.final_prompt = ""

st.markdown("""
<style>
.stApp {
    background-color: #EFF6FF;
}
.main-title {
    text-align: center;
    color: #174A7E;
    font-size: 38px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: #52677D;
    font-size: 16px;
}
div.stButton > button {
    background-color: #1976D2;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: #12599E;
    color: white;
}
.response-box {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #C9DDF2;
}
</style>
""", unsafe_allow_html=True)
st.markdown(
    '<div class="main-title">Qwen Prompt Lab</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Explore and compare different LLM prompting techniques using Qwen.</div>',
    unsafe_allow_html=True
)
st.write("")
with st.sidebar:
    st.header("About the Project")
    st.write(
        "This application demonstrates six "
        "prompt engineering techniques using Qwen."
    )
    st.divider()
    st.subheader("Available Techniques")
    st.write("1. Zero-shot")
    st.write("2. One-shot")
    st.write("3. Few-shot")
    st.write("4. Chain of Thought")
    st.write("5. Manual CoT")
    st.write("6. Tree of Thought")
    st.divider()
    st.caption("Powered by Qwen LLM")
st.subheader("Prompt Configuration")

samples = {
    "Select an example": "",
    "Artificial Intelligence": "Explain how Artificial Intelligence is used in healthcare.",
    "Machine Learning": "Explain the difference between supervised and unsupervised learning.",
    "Python Programming": "Write a Python program to check whether a number is prime.",
    "Environment": "Suggest five practical ways to reduce plastic pollution.",
    "Cybersecurity": "Explain how phishing attacks work and how to prevent them."
}
sample = st.selectbox(
    "Try a sample task",
    list(samples.keys())
)
default_task = samples[sample]
task = st.text_area(
    "Enter your task",
    value=default_task,
    height=120,
    placeholder="Enter your question or task here..."
)
word_count = len(task.split())
st.caption(f"Word count: {word_count}")
col1, col2 = st.columns(2)
with col1:
    technique = st.selectbox(
        "Select Prompting Technique",
        [
            "Zero-shot",
            "One-shot",
            "Few-shot",
            "CoT",
            "Manual CoT",
            "ToT"
        ]
    )

with col2:
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.2,
        step=0.1
    )
max_tokens = st.slider(
    "Maximum Tokens",
    min_value=100,
    max_value=1000,
    value=500,
    step=100
)
generate_col, clear_col = st.columns(2)
with generate_col:
    generate = st.button(
        "Generate Response",
        use_container_width=True
    )
with clear_col:
    clear = st.button(
        "Clear",
        use_container_width=True
    )
if clear:
    st.session_state.answer = ""
    st.session_state.final_prompt = ""
    st.rerun()
if generate:
    if not task.strip():
        st.warning("Please enter a task.")
    else:
        try:
            final_prompt = build_prompt(
                technique,
                task
            )
            st.session_state.final_prompt = final_prompt
            with st.spinner("Qwen is generating your response..."):
                answer = generate_response(
                    final_prompt,
                    temperature,
                    max_tokens
                )
            st.session_state.answer = answer
            st.session_state.history.insert(
                0,
                {
                    "technique": technique,
                    "task": task,
                    "answer": answer
                }
            )
            st.success("Response generated successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
if st.session_state.final_prompt:
    st.divider()
    st.subheader("Generated Prompt")
    with st.expander("View the complete prompt", expanded=False):
        st.code(
            st.session_state.final_prompt,
            language="text"
        )
if st.session_state.answer:
    st.divider()
    st.subheader("Generated Response")
    st.markdown(
        f'<div class="response-box">{st.session_state.answer}</div>',
        unsafe_allow_html=True
    )
    st.write("")
    st.download_button(
        label="Download Response",
        data=st.session_state.answer,
        file_name="qwen_response.txt",
        mime="text/plain"
    )
    st.caption(
        f"Response words: {len(st.session_state.answer.split())}"
    )
st.divider()
st.subheader("Compare Prompting Techniques")
st.write(
    "Generate responses using multiple prompting techniques "
    "for the same task."
)
comparison_techniques = st.multiselect(
    "Choose techniques to compare",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "CoT",
        "Manual CoT",
        "ToT"
    ],
    default=["Zero-shot", "Few-shot"]
)
if st.button("Compare Responses", use_container_width=True):
    if not task.strip():
        st.warning("Please enter a task first.")
    elif not comparison_techniques:
        st.warning("Select at least one technique.")
    else:
        for selected_technique in comparison_techniques:
            try:
                comparison_prompt = build_prompt(
                    selected_technique,
                    task
                )
                with st.spinner(
                    f"Generating {selected_technique} response..."
                ):
                    comparison_answer = generate_response(
                        comparison_prompt,
                        temperature,
                        max_tokens
                    )
                with st.expander(
                    f"{selected_technique} Response",
                    expanded=True
                ):
                    st.write(comparison_answer)
            except Exception as e:
                st.error(
                    f"{selected_technique} failed: {e}"
                )
st.divider()
st.subheader("Prompt History")
if st.session_state.history:
    for index, item in enumerate(st.session_state.history):
        with st.expander(
            f"{index + 1}. {item['technique']} - {item['task'][:50]}"
        ):
            st.write("**Task:**")
            st.write(item["task"])
            st.write("**Response:**")
            st.write(item["answer"])

else:
    st.info("Your generated responses will appear here.")