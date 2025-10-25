# main.py

import streamlit as st
import streamlit.components.v1 as components
import os
import base64 # Used to encode the image

# --- PAGE CONFIG ---
st.set_page_config(layout="wide")

# --- HELPER FUNCTIONS ---

def read_file(path):
    """Reads a file and returns its content."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"File not found: {path}")
        return ""
    except Exception as e:
        st.error(f"Error reading {path}: {e}")
        return ""

def get_image_base64(path):
    """Returns a base64 encoded string of an image."""
    try:
        with open(path, "rb") as img_file:
            # Read the file and encode it
            b64_string = base64.b64encode(img_file.read()).decode()
        # Return the Data URI
        return f"data:image/png;base64,{b64_string}"
    except FileNotFoundError:
        st.error(f"Image not found: {path}")
        return ""
    except Exception as e:
        st.error(f"Error processing image {path}: {e}")
        return ""

# --- 1. LOAD ASSETS ---

# Read HTML, CSS, and JS
html_content = read_file("index.html")
css_content = read_file("style.css")
js_content = read_file("script.js")

# Get the secure API key
try:
    api_key = st.secrets["gmaps_api_key"]
except (KeyError, FileNotFoundError):
    st.error("API key not found. Please add 'gmaps_api_key = \"YOUR_KEY\"' to .streamlit/secrets.toml")
    st.stop()

# Get the base64-encoded image
image_base64 = get_image_base64("images/watermelon.png")

# --- 2. INJECT CONTENT INTO HTML ---

# Check if all files were loaded
if html_content and css_content and js_content and api_key and image_base64:
    
    # Inject CSS
    html_content = html_content.replace(
        "", 
        f"<style>{css_content}</style>"
    )
    
    # Inject JavaScript
    html_content = html_content.replace(
        "", 
        f"<script>{js_content}</script>"
    )
    
    # Inject the Google Maps API Key
    html_content = html_content.replace(
        "YOUR_API_KEY_PLACEHOLDER", 
        api_key
    )

    # Inject the Base64 Image
    html_content = html_content.replace(
        "",
        image_base64
    )

    # --- 3. RENDER THE FINAL HTML ---
    components.html(html_content, height=800, scrolling=True)

else:
    st.error("Could not load all necessary files (HTML, CSS, JS, Image) or API key.")