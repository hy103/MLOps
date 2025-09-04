import streamlit as st
from Movie_guesser.main import analyze_comment

st.title("🧠 Comment Analyzer: Emotion & Toxicity Detector")
st.write("Enter a comment to analyze its **emotion** and **toxicity/hate speech** levels.")

user_input = st.text_area("💬 Your Comment", height=150)

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter a comment.")
    else:
        result = analyze_comment(user_input)

        st.subheader("🎭 Emotion Classification")
        for item in result["emotion"]:
            st.write(f"**{item['label']}**: {item['score']:.3f}")

        st.subheader("☣️ Toxicity / Hate Speech Classification")
        for item in result["toxicity"]:
            st.write(f"**{item['label']}**: {item['score']:.3f}")
