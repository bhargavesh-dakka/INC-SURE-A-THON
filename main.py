import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.set_page_config("Earn By Complete","🧑‍💻",initial_sidebar_state="collapsed",menu_items=None)
def link_css():
    with open("style.css","r") as f:
        style_ = f.read()
    st.markdown(f"""
                <style> 
                {style_}
                </style>""",unsafe_allow_html=True)

# -----------------------------------------
st.header("WELCOME !👋")
st.divider()
st.text("""This website will help you in Earning by completing the projects.
        - You require to sign in to the portal.
        - You can select the project you want.
            NOTE : Resources are provided if you would like to learn.
        - Once you complete the project then your Bank details will be asked to
          provide the money directly to your bank account.""")
st.columns(3)
st.columns(3)
st.columns(3)
st.columns(3)
st.columns(3)
st.columns(3)
if st.columns(3)[1].button("Get Started"):
    switch_page("SignUp")



# _______LINKING STYLESHEET
link_css()