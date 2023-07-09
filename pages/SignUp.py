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
#____________________________________
st.header("Sign Up..")
st.divider()

def new_reg():
    return False


with st.form(key='Sign up') as form:
    username = st.text_input('Username')
    password = st.text_input('Password')
    signed_up = st.columns(5)[2].form_submit_button('SignUp')
    if signed_up:
        if new_reg():
            st.success("Successfully created! 👏")
            sleep(2)            
            switch_page("Index")
        else:
            st.error("User already registered! Please login ")
            sleep(2)
            switch_page("Login")

        


link_css()