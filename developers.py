import streamlit as st

def dev():
    
    st.markdown("""
        <style>
            div.stButton > button {
                height: 70px;
                font-size: 30px;
            }
            .transparent-box {
                border: 1px solid rgba(52, 152, 219, 0.5); /* Black border with 50% transparency */
                height: 200px;
                width: 100%;
                text-align: center;
                background-color: rgba(255, 255, 255, 0.8); /* White with 80% transparency */
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .transparent-box h5, .transparent-box p, .transparent-box a {
                color: black;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.sidebar.title("Cam-X Controller :video_game:")
    home_button = st.sidebar.button("Home", use_container_width=True, type="primary")
    about_button = st.sidebar.button("About Project", use_container_width=True)
    
    if home_button:
        st.session_state.clear()
        st.rerun()
    
    if about_button:
        st.session_state.page = "about"
        st.rerun()
    
    st.title("About Developers:")

    # Create two columns with equal width
    col1, col2 = st.columns(2)

    # First container in the first column
    with col1:
       
        st.text("")
        st.markdown("""
        <div class="transparent-box">
            <h5>Mohammed Abdul Moyeed</h5>
            <p>Lords Institute of Engineering and Technology </p>
            <a href="https://github.com/abdulmoyeed28">Github</a>
        </div>
        """, unsafe_allow_html=True)
    # Second container in the second column
    with col2:
        
        st.text("")
        st.markdown("""
        <div class="transparent-box">
            <h5>Shaik Addeeb Ahmed</h5>
            <p>Lords Institute Of <br>Engineering</p>
            <a href="https://github.com/Shaikaddeeb">Github</a>
        </div>
        """, unsafe_allow_html=True)


