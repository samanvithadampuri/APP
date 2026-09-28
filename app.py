import streamlit as st

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

        st.chat_message("user").write(question)

        # Simple response without Ollama
        response = "You entered: " + question

        list.append({
            "role": "assistant",
            "content": response
        })

        with st.chat_message("assistant"):
            st.write(response)

if st.button("Exit"):
    st.session_state.list = []
    st.info("Exiting the chat...")
