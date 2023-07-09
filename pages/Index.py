import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from time import sleep
st.set_page_config("Earn By Complete","🧑‍💻",initial_sidebar_state="collapsed",menu_items=None)
def link_css():
    with open("style.css","r") as f:
        style_ = f.read()
    st.markdown(f"""
                <style> 
                {style_}
                </style>""",unsafe_allow_html=True)
    
# -----------------------------------------
st.header("INDEX HERE")

# ___________________________________________
link_css()