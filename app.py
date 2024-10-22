import streamlit as st
from PIL import Image
import os
from dotenv import load_dotenv
from frontend.styles import apply_styles
import base64
from firebase_admin import firestore
from groq import Groq
import firebase_admin
from firebase_admin import credentials, firestore, auth
from frontend.themes import themes, get_theme_css
import streamlit.components.v1 as components
import json


# Load environment variables
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

# Define ROOT_DIR
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Get the current script's directory
current_dir = ROOT_DIR

# Construct the path to the service account key file
service_account_path = os.path.join(current_dir, 'config', 'serviceAccountKey.json')

# Initialize Firebase if it hasn't been initialized yet
if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)

# Create Firestore client
db = firestore.client()

# Firebase authentication functions
def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except:
        return None

def create_user(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return user
    except:
        return None

def store_user_data(user):
    user_ref = db.collection('users').document(user['localId'])
    user_ref.set({
        'email': user['email'],
        'last_login': firestore.SERVER_TIMESTAMP
    })




def main():
    st.set_page_config(page_title="AI Assistant", layout="wide")
    
    # Apply custom styles
    apply_styles()

    # Theme selector in sidebar
    with st.sidebar:
        selected_theme = st.selectbox("Choose a theme", list(themes.keys()), key="theme_selector")
        
    # Apply the selected theme
    st.markdown(f"<style>{get_theme_css(themes[selected_theme])}</style>", unsafe_allow_html=True)

    # Initialize the Groq client
    groq_client = Groq(api_key="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")

    # Session state for user authentication
    if 'user' not in st.session_state:
        st.session_state.user = None

    # Login/Signup in the sidebar
    with st.sidebar:
        if st.session_state.user is None:
            choice = st.radio("Login/Signup", ["Login", "Sign Up"])
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if choice == "Login":
                if st.button("Login"):
                    user = login_user(email, password)
                    if user:
                        st.session_state.user = user
                        store_user_data(user)
                        st.success("Logged in successfully!")
                    else:
                        st.error("Invalid credentials")
            else:
                if st.button("Sign Up"):
                    user = create_user(email, password)
                    if user:
                        st.session_state.user = user
                        store_user_data(user)
                        st.success("Account created and logged in successfully!")
                    else:
                        st.error("Failed to create account")
        else:
            st.write(f"Logged in as: {st.session_state.user['email']}")
            if st.button("Logout"):
                st.session_state.user = None
                st.experimental_rerun()

    # Create a container for the fixed elements
    st.markdown('<div class="fixed-container">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown('<p class="big-font">I am Sarah</p>', unsafe_allow_html=True)
        
        # Display the animated robot image
        st.markdown(
            f'<img src="data:image/gif;base64,{base64.b64encode(open(os.path.join(ROOT_DIR, "static", "images", "animated_robot.gif"), "rb").read()).decode()}" alt="Animated Robot" style="width:150px;">',
            unsafe_allow_html=True
        )

        st.markdown('<p class="medium-font">Hello! How Can I assist you today....</p>', unsafe_allow_html=True)

        # Search bar with LLM functionality and send button
        user_input = st.text_input("", placeholder="Ask me anything...")
        send_button = st.button("Send")

    st.markdown('</div>', unsafe_allow_html=True)

    # Create a container for the scrollable content
    st.markdown('<div class="scrollable-content">', unsafe_allow_html=True)
    
    if send_button and user_input:
        with st.spinner("Thinking..."):
            chat_completion = groq_client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="llama3-groq-70b-8192-tool-use-preview",
            )
            response = chat_completion.choices[0].message.content
        
        # Create a unique ID for this response
        response_id = f"response-{hash(response)}"
        
        # Inject the JavaScript function and call it
        st.markdown(f"""
        <div id="{response_id}" class="response-box"></div>
        <script>
        function typeWriter(text, elementId, speed) {{
            let i = 0;
            const element = document.getElementById(elementId);
            if (!element) {{
                console.error(`Element with id "${{elementId}}" not found`);
                return;
            }}
            function type() {{
                if (i < text.length) {{
                    element.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(type, speed);
                }}
            }}
            element.innerHTML = ''; // Clear existing content
            type();
        }}
        
        typeWriter({json.dumps(response)}, "{response_id}", 20);
        </script>
        """, unsafe_allow_html=True)

        st.write(f"Debug - Response: {response}")

    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown('<p class="small-font" style="position: fixed; bottom: 10px; right: 10px;">Driven by RAJ SINGH</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
