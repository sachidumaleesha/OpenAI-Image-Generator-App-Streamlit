import streamlit as st

def show_sidebarInfo():
    st.subheader("Go to OpenAI Dashboard")
    link_to_api_dashboard = "https://platform.openai.com/"
    st.code(link_to_api_dashboard)

    st.subheader("Steps to get your API key 🔑")
    st.write("01. Then navigate to the API section on the left sidebar.")
    st.write("02. Click on Create New Secret Key.")
    st.write("03. Give it a name and click on Create.")
    st.write("04. Before closing the window, copy the API key becouse it can view only once.")

    st.subheader("Repository Link")
    link_to_repo = "https://github.com/sachidumaleesha/OpenAI-Image-Generator-App-Streamlit"
    st.code(link_to_repo)