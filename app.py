import streamlit as st
import ollama

st.set_page_config(page_title="AI Chat", page_icon="🤖")

st.title("🤖 Welcome to AI Chat")
st.write("Enter your prompt and click **Generate**.")


if "list" not in st.session_state:
    st.session_state.list = []

list = st.session_state.list


for i in list:
    if i["role"] == "user":
        st.chat_message("user").write(i["content"])
    else:
        st.chat_message("assistant").write(i["content"])

question = st.text_input("Enter your prompt:")

if st.button("Generate"):
    
    if not question.strip():
        st.error("Did not type anything")
    else:
        st.success("Success")

        list.append({
            "role": "user",
            "content": question
        })

        # Display the user's prompt again
        st.chat_message("user").write(question)

        # Generate AI response using the original Ollama logic
        with st.chat_message("assistant"):
            response = ollama.chat(
                model="llama3.2",
                messages=list
            )

            st.write(response["message"]["content"])
        list.append({
            "role": "assistant",
            "content": response["message"]["content"]
        })
if st.button("Exit"):
    st.session_state.list = []
    st.info("Exiting the chat...")
