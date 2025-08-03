import streamlit as st
import about as ab
import steering as sg
import developers as de
import shooter as sh

if "page" not in st.session_state:
    st.session_state.page = 'web'

st.set_page_config(
    page_title="Cam-X",
    page_icon=":video_game:",
    layout="centered",
    initial_sidebar_state="expanded",  
)
def web():
    st.sidebar.title("Cam-X Controller :video_game:")
    About_button=st.sidebar.button("About Project",use_container_width=True)
     
    dev_button=st.sidebar.button("About Developers",use_container_width=True)
    
    if About_button:
        st.session_state.page="about"
        st.rerun()
    if dev_button:
        st.session_state.page="developers"
        st.rerun()

    # Use st.markdown to render the custom HTML and CSS for video background

    st.markdown("<center><h1>Cam-X Controller</h1></center>", unsafe_allow_html=True)
    st.markdown("""---""")
    col1,col2 = st.columns(2)
    st.markdown("""
                <style>
        div.stButton > button {
            height: 70px;
            font-size: 30px;
        }
        </style>""", unsafe_allow_html=True)
    with col1:
        st.subheader("Virtual Wheel:")
        wheel_button=st.button("Start Virtual Wheel", type="primary",use_container_width=True)
        if wheel_button:
            st.session_state.page="steering"
            st.rerun()
        st.markdown("""<p>Take control with our virtual steering
                    wheel, crafted using advanced technology
                    like OpenCV and MediaPipe. Navigate
                    through digital realms effortlessly
                    as you steer through immersive
                    experiences with intuitive
                    gestures.</p>""",unsafe_allow_html=True)
        

    with col2:
        st.markdown("<div style='text-align: right;'><h3>:Virtual Gun</h3></div>", unsafe_allow_html=True)
        shooter_button=st.button("Start Virtual Gun", type="primary",use_container_width=True)
        st.markdown("""<p>Step into the action with our virtual gun,
                    leveraging the latest in OpenCV and MediaPipe technology.
                    Immerse yourself in dynamic gameplay as you wield
                    virtual firepower with precision and realism, bringing gaming
                    to a whole new level of immersion.</p>""",unsafe_allow_html=True)
        if shooter_button:
            st.session_state.page="shooter"
            st.rerun()
if st.session_state.page == 'web':
    web()
        
if st.session_state.page=="about":
    ab.about()


if st.session_state.page=="steering":
    sg.steering()

if st.session_state.page=="developers":
    de.dev()

if st.session_state.page=="shooter":
    sh.shooter()
