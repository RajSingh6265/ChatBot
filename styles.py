import streamlit as st
import os

def apply_styles():
    # Get the directory of the current file (styles.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to main.css
    css_path = os.path.join(current_dir, '..', 'static', 'css', 'main.css')
    
    # Read and apply the CSS
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    # Add animated background and fixed container
    st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #000000, #434343);
        animation: stars 20s linear infinite;
        background-size: 200% 200%;
    }

    .fixed-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        background: linear-gradient(to bottom, #000000, #434343);
        padding: 20px 0;
    }

    /* Add twinkling stars */
    .stApp::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
            radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
            radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px);
        background-size: 550px 550px, 350px 350px, 250px 250px;
        background-position: 0 0, 40px 60px, 130px 270px;
        animation: twinkle 10s linear infinite;
    }

    @keyframes twinkle {
        0% {
            background-position: 0 0, 40px 60px, 130px 270px;
        }
        100% {
            background-position: -550px 0, -350px 60px, -250px 270px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
    )
