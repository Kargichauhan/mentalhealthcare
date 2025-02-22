import streamlit as st
import openai

# Set the API key directly on the openai module
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("AI Mental Health Counselor")
st.write("Enter problem, and I will generate guidance :) ")

user_input = st.text_area("Describe your problem:", "")

if st.button("Legacy Advice's: "):
    if user_input:
        with st.spinner("Loading response... please wait."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": (
                            "You are an experienced mental health counselor providing compassionate, "
                            "evidence-based support. Your goal is to offer guidance that is empathetic, "
                            "non-judgmental, and solution-oriented."
                        )},
                        {"role": "user", "content": user_input}
                    ]
                )

                st.subheader("Legacy Advices:")
                st.write(response.choices[0].message.content)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("⚠️ Please enter a description.")
