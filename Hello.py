import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to my try on a (dockerized) Streamlit app ! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Don't try to find any links between all the pages, this is just
    a test to see how Streamlit works. You can find enclosed in my Github repository
    (https://github.com/CharlesDc9/Streamlit-and-Docker-basics) the code ! 

    Have fun ! 🎉
"""
)
