import streamlit as st

def about():
    st.markdown("""
                <style>
        div.stButton > button {
            height: 70px;
            font-size: 30px;
        }
        </style>""", unsafe_allow_html=True)
    st.sidebar.title("Cam-X Controller :video_game:")
    home_button=st.sidebar.button("Home",use_container_width=True,type="primary")
     
    dev_button=st.sidebar.button("About Developers",use_container_width=True)

    if home_button:
        st.session_state.page="web"
        st.rerun()
    
    if dev_button:
        st.session_state.page="developers"
        st.rerun()
    st.title("About Project")
    st.subheader("Cam-X Controller")
    st.markdown("""
    <p>
                Virtual Controller Project<br>
This project utilizes OpenCV and MediaPipe to create a versatile virtual controller system. It features two distinct controller types: a virtual steering wheel and a shooter controller.<br>

<h4>Virtual Steering Wheel</h4><br>
The virtual steering wheel leverages hand tracking to detect and interpret hand movements, allowing users to control the direction of a virtual vehicle. Using the camera feed, the system tracks the positions of the user's hands and translates them into steering commands, providing a realistic and immersive driving experience.<br>

<h4>Shooter Controller</h4><br>
The shooter controller uses similar hand tracking technology to create an interactive shooting mechanism. Users can aim and shoot by moving and gesturing with their hands, simulating a real-life shooting experience. The system accurately detects hand positions and gestures to control aiming and firing actions in a virtual environment.<br>

<h4>Key Features</h4><br>
Hand Tracking: Utilizes MediaPipe for precise hand landmark detection.<br>
Real-Time Processing: Implements OpenCV for real-time video capture and processing.<br>
Immersive Controls: Provides an intuitive and engaging user experience through natural hand movements.<br>
Versatile Applications: Can be adapted for various interactive applications, such as gaming or virtual simulations.<br>
</p>
    """,unsafe_allow_html=True)