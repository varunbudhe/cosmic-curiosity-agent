import streamlit as st
from agent import ask_cosmic_agent

st.set_page_config(
    page_title="Cosmic Curiosity Agent",
    page_icon="🪐",
    layout="wide"
)

st.title("🪐 Cosmic Curiosity Agent")
st.caption("Ask wild universe questions. Get science + imagination.")

question = st.text_area(
    "Ask your universe question:",
    value="What if Earth had rings like Saturn?",
    height=120
)

examples = [
    "What if Jupiter became a star?",
    "What if the Moon disappeared?",
    "Can humans live on Titan?",
    "What if Earth had two suns?",
    "What happens if you fall into a black hole?"
]

st.write("### Try examples")

cols = st.columns(5)

for i, example in enumerate(examples):
    with cols[i]:
        if st.button(example):
            question = example

if st.button("Ask Cosmic Agent", type="primary"):
    with st.spinner("Thinking like a space scientist..."):
        answer = ask_cosmic_agent(question)
        st.markdown(answer)