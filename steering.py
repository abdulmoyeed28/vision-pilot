import math
import keyinput  # Assuming keyinput is correctly implemented elsewhere
import cv2
import mediapipe as mp
import streamlit as st
import numpy as np

# Initialize session state variables
if "start_wheel" not in st.session_state:
    st.session_state.start_wheel = False
if "result" not in st.session_state:
    st.session_state.result = None

def steering():
    st.markdown("""
                <style>
        div.stButton > button {
            height: 70px;
            font-size: 30px;
        }
        </style>""", unsafe_allow_html=True)
    st.sidebar.title("Cam-X Controller :video_game:")
    home_button=st.sidebar.button("Home",use_container_width=True,type="primary")
     

    if home_button:
        st.session_state.page="web"
        st.rerun()
    
    st.title("Virtual Steering Wheel")
    st.session_state.start_wheel = False
    st.session_state.result=None
    btn_ph=st.empty()
    # Button to start the virtual wheel
    if not st.session_state.start_wheel:
        start_wheel = btn_ph.button("Start Virtual Wheel", type="primary", use_container_width=True)

    if start_wheel:
        st.session_state.start_wheel = True
        btn_ph.empty()
        home_button=st.button("Exit Controller",type="primary",use_container_width=True)
        
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_hands = mp.solutions.hands

        font = cv2.FONT_HERSHEY_SIMPLEX

        cap = cv2.VideoCapture(0)

        frame_placeholder = st.empty()
        result_placeholder = st.empty()

        with mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    st.write("Ignoring empty camera frame.")
                    continue

                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image)
                imageHeight, imageWidth, _ = image.shape

                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                co = []
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style()
                        )
                        for point in mp_hands.HandLandmark:
                            if str(point) == "HandLandmark.WRIST":
                                normalizedLandmark = hand_landmarks.landmark[point]
                                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                                    normalizedLandmark.x,
                                    normalizedLandmark.y,
                                    imageWidth, imageHeight
                                )

                                try:
                                    co.append(list(pixelCoordinatesLandmark))
                                except:
                                    continue

                if len(co) == 2:
                    xm, ym = (co[0][0] + co[1][0]) / 2, (co[0][1] + co[1][1]) / 2
                    radius = 150
                    try:
                        m = (co[1][1] - co[0][1]) / (co[1][0] - co[0][0])
                    except:
                        continue
                    a = 1 + m ** 2
                    b = -2 * xm - 2 * co[0][0] * (m ** 2) + 2 * m * co[0][1] - 2 * m * ym
                    c = xm ** 2 + (m ** 2) * (co[0][0] ** 2) + co[0][1] ** 2 + ym ** 2 - 2 * co[0][1] * ym - 2 * co[0][1] * co[0][0] * m + 2 * m * ym * co[0][0] - 22500
                    xa = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
                    xb = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
                    ya = m * (xa - co[0][0]) + co[0][1]
                    yb = m * (xb - co[0][0]) + co[0][1]
                    if m != 0:
                        ap = 1 + ((-1 / m) ** 2)
                        bp = -2 * xm - 2 * xm * ((-1 / m) ** 2) + 2 * (-1 / m) * ym - 2 * (-1 / m) * ym
                        cp = xm ** 2 + ((-1 / m) ** 2) * (xm ** 2) + ym ** 2 + ym ** 2 - 2 * ym * ym - 2 * ym * xm * (-1 / m) + 2 * (-1 / m) * ym * xm - 22500
                        try:
                            xap = (-bp + (bp ** 2 - 4 * ap * cp) ** 0.5) / (2 * ap)
                            xbp = (-bp - (bp ** 2 - 4 * ap * cp) ** 0.5) / (2 * ap)
                            yap = (-1 / m) * (xap - xm) + ym
                            ybp = (-1 / m) * (xbp - xm) + ym
                        except:
                            continue

                    cv2.circle(img=image, center=(int(xm), int(ym)), radius=radius, color=(195, 255, 62), thickness=15)
                    # l = (int(math.sqrt((co[0][0] - co[1][0]) ** 2 * (co[0][1] - co[1][1]) ** 2)) - 150) // 2
                    cv2.line(image, (int(xa), int(ya)), (int(xb), int(yb)), (195, 255, 62), 20)
                    if co[0][0] > co[1][0] and co[0][1] > co[1][1] and co[0][1] - co[1][1] > 65:
                        if st.session_state.result != ":orange[turning left]":
                            st.session_state.result = ":orange[turning left]"
                        keyinput.release_key('s')
                        keyinput.release_key('d')
                        keyinput.press_key('a')
                        cv2.putText(image, "Turn left", (50, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
                        cv2.line(image, (int(xbp), int(ybp)), (int(xm), int(ym)), (195, 255, 62), 20)
                    elif co[1][0] > co[0][0] and co[1][1] > co[0][1] and co[1][1] - co[0][1] > 65:
                        if st.session_state.result != ":orange[turning left]":
                            st.session_state.result = ":orange[turning left]"
                        keyinput.release_key('s')
                        keyinput.release_key('d')
                        keyinput.press_key('a')
                        cv2.putText(image, "Turn left", (50, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
                        cv2.line(image, (int(xbp), int(ybp)), (int(xm), int(ym)), (195, 255, 62), 20)
                    elif co[0][0] > co[1][0] and co[1][1] > co[0][1] and co[1][1] - co[0][1] > 65:
                        if st.session_state.result != ":orange[turning right]":
                            st.session_state.result = ":orange[turning right]"
                        keyinput.release_key('s')
                        keyinput.release_key('a')
                        keyinput.press_key('d')
                        cv2.putText(image, "Turn right", (50, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
                        cv2.line(image, (int(xap), int(yap)), (int(xm), int(ym)), (195, 255, 62), 20)
                    elif co[1][0] > co[0][0] and co[0][1] > co[1][1] and co[0][1] - co[1][1] > 65:
                        if st.session_state.result != ":orange[turning right]":
                            st.session_state.result = ":orange[turning right]"
                        keyinput.release_key('s')
                        keyinput.release_key('a')
                        keyinput.press_key('d')
                        cv2.putText(image, "Turn right", (50, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
                        cv2.line(image, (int(xap), int(yap)), (int(xm), int(ym)), (195, 255, 62), 20)
                    else:
                        if st.session_state.result != ":green[moving forward]":
                            st.session_state.result = ":green[moving forward]"
                        keyinput.release_key('s')
                        keyinput.release_key('a')
                        keyinput.release_key('d')
                        keyinput.press_key('w')
                        cv2.putText(image, "Keep straight", (50, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
                        if ybp > yap:
                            cv2.line(image, (int(xbp), int(ybp)), (int(xm), int(ym)), (195, 255, 62), 20)
                        else:
                            cv2.line(image, (int(xap), int(yap)), (int(xm), int(ym)), (195, 255, 62), 20)

                if len(co) == 1:
                    if st.session_state.result != ":red[moving back]":
                        st.session_state.result = ":red[moving back]"
                    keyinput.release_key('a')
                    keyinput.release_key('d')
                    keyinput.release_key('w')
                    keyinput.press_key('s')
                    cv2.putText(image, "Keep back", (50, 50), font, 1.0, (0, 255, 0), 2, cv2.LINE_AA)

                # Convert image to RGB for Streamlit display
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = cv2.flip(image, 1)
                frame_placeholder.image(image, channels="RGB")

                # Display result text outside the loop
                result_placeholder.markdown(st.session_state.result, unsafe_allow_html=True)

                # Break the loop if 'q' is pressed
                if cv2.waitKey(5) & home_button:
                    st.session_state.page="web"
                    break
        
        cap.release()
        
        if st.session_state.page=="web":
            st.rerun()
        
        
