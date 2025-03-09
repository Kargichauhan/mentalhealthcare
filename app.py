import streamlit as st
import openai

# Load API key from secrets
if "OPENAI_API_KEY" not in st.secrets:
    st.error("OpenAI API Key is missing. Please add it in Streamlit Secrets.")
    st.stop()

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Set the API key globally
openai.api_key = OPENAI_API_KEY

st.title("AI Mental Health Counselor")
st.write("Enter problem, and I will generate guidance.")

user_input = st.text_area("Describe your problem:", "")

if st.button("Get Advice"):
    if user_input.strip():
        with st.spinner("Loading response..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an experienced mental health counselor providing compassionate, "
                                "evidence-based support. Your goal is to offer guidance that is empathetic, "
                                "non-judgmental, and solution-oriented."
                            )
                        },
                        {"role": "user", "content": user_input}
                    ]
                )
                st.subheader("Advice:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a description before submitting.")
