themes = {
    "Default": {
        "background": "linear-gradient(to bottom, #000000, #434343)",
        "text": "#FFFFFF",
        "accent": "#eb1313"
    },
    "Ocean": {
        "background": "linear-gradient(to bottom, #1a2980, #26d0ce)",
        "text": "#FFFFFF",
        "accent": "#FFD700"
    },
    "Forest": {
        "background": "linear-gradient(to bottom, #134E5E, #71B280)",
        "text": "#FFFFFF",
        "accent": "#FF6B6B"
    }
}

def get_theme_css(theme):
    return f"""
    .stApp {{
        background: {theme['background']};
    }}
    .big-font, .medium-font, .small-font, .response-box {{
        color: {theme['text']};
    }}
    .big-font {{
        text-shadow: 0 0 10px {theme['accent']};
    }}
    .stButton > button {{
        background-color: {theme['accent']};
        color: {theme['text']};
    }}
    """
