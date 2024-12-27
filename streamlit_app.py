import streamlit as st
from streamlit.components.v1 import html

# Set page configuration
st.set_page_config(
    page_title="Flamingo Dance Party",
    page_icon="🦩",
    layout="wide",
)

# CSS and Flamingo Dance Animation
flamingo_css = """
<style>
@keyframes dance {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(-20deg); }
    50% { transform: rotate(20deg); }
    75% { transform: rotate(-20deg); }
    100% { transform: rotate(0deg); }
}
.flamingo {
    animation: dance 2s infinite;
    width: 150px;
    margin: 0 auto;
    display: block;
}
</style>
"""

flamingo_html = """
<div style="text-align: center;">
    <img src="https://i.imgur.com/4ZK6EEN.png" alt="Dancing Flamingo" class="flamingo">
</div>
"""

# Header
st.title("🦩 Flamingo Dance Party")
st.markdown(
    """
    Welcome to the **Flamingo Dance Party!**  
    🎮 Play games, interact with dancing flamingos, and have fun!
    """
)

# Flamingo Dance Display
html(flamingo_css + flamingo_html, height=300)

# Sidebar Navigation
st.sidebar.title("Menu")
menu = st.sidebar.radio("Choose a section:", ["Home", "Flamingo Facts", "Leaderboard"])

# Main Page Sections
if menu == "Home":
    st.header("Home: Let the Party Begin!")
    st.write("Enjoy this adorable dancing flamingo!")
elif menu == "Flamingo Facts":
    st.header("🦩 Fun Flamingo Facts")
    st.write("""
    - Flamingos are social birds that live in colonies.
    - They get their pink color from their diet of shrimp and algae.
    - Flamingos can dance! They perform group rituals that look like dances.
    """)
elif menu == "Leaderboard":
    st.header("🏆 Leaderboard")
    st.write("This section will show top scorers for future flamingo games.")

# Footer
st.markdown("---")
st.markdown("Built with 💖 for flamingo lovers.")
