import streamlit as st
import random
import json
import time
from pathlib import Path
from datetime import datetime
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FlamingoGame:
    def __init__(self):
        self.setup_streamlit()
        self.load_game_state()
        
    def setup_streamlit(self):
        """Configure Streamlit page settings"""
        try:
            st.set_page_config(
                page_title="Dancing Flamingos",
                page_icon="🦩",
                layout="wide",
                initial_sidebar_state="expanded"
            )
            st.title("🦩 Dancing Flamingos")
        except Exception as e:
            logger.error(f"Error setting up Streamlit: {e}")
            st.error("There was an error setting up the game. Please refresh the page.")

    def load_game_state(self):
        """Load or initialize game state"""
        try:
            if 'flamingos' not in st.session_state:
                st.session_state.flamingos = []
            if 'coins' not in st.session_state:
                st.session_state.coins = 100
            if 'dance_moves' not in st.session_state:
                st.session_state.dance_moves = ['Salsa', 'Ballet', 'Hip Hop', 'Tap']
        except Exception as e:
            logger.error(f"Error loading game state: {e}")
            st.error("Unable to load game state. Starting with default values.")
            self.reset_game_state()

    def reset_game_state(self):
        """Reset game state to default values"""
        st.session_state.flamingos = []
        st.session_state.coins = 100
        st.session_state.dance_moves = ['Salsa', 'Ballet', 'Hip Hop', 'Tap']

class Flamingo:
    def __init__(self, name: str):
        self.name = name
        self.happiness = 100
        self.energy = 100
        self.dance_skill = 1
        self.favorite_move = random.choice(st.session_state.dance_moves)
        self.last_interaction = datetime.now()

    def dance(self) -> tuple[int, str]:
        """Make flamingo dance and return rewards"""
        try:
            if self.energy < 20:
                return 0, "Too tired to dance! Please rest your flamingo."
            
            skill_bonus = random.randint(1, self.dance_skill)
            coins_earned = skill_bonus * 5
            self.energy -= 10
            self.happiness += 5
            self.dance_skill += 0.1
            
            return coins_earned, f"{self.name} earned {coins_earned} coins dancing!"
        except Exception as e:
            logger.error(f"Error during dance action: {e}")
            return 0, "Something went wrong during the dance!"

    def rest(self) -> str:
        """Rest the flamingo to recover energy"""
        try:
            energy_recovery = min(30, 100 - self.energy)
            self.energy += energy_recovery
            return f"{self.name} recovered {energy_recovery} energy!"
        except Exception as e:
            logger.error(f"Error during rest action: {e}")
            return "Unable to rest right now."

def main():
    try:
        game = FlamingoGame()
        
        # Sidebar for game stats and actions
        with st.sidebar:
            st.header("Game Stats")
            st.write(f"Coins: {st.session_state.coins}")
            
            # Add new flamingo
            if st.button("Adopt New Flamingo (Cost: 50 coins)"):
                if st.session_state.coins >= 50:
                    name = f"Flamingo_{len(st.session_state.flamingos) + 1}"
                    st.session_state.flamingos.append(Flamingo(name))
                    st.session_state.coins -= 50
                    st.success(f"Welcome {name} to your flock!")
                else:
                    st.error("Not enough coins!")

        # Main game area
        if not st.session_state.flamingos:
            st.info("Adopt your first flamingo to start playing!")
        else:
            cols = st.columns(len(st.session_state.flamingos))
            
            for idx, flamingo in enumerate(st.session_state.flamingos):
                with cols[idx]:
                    st.subheader(flamingo.name)
                    st.progress(flamingo.energy/100, "Energy")
                    st.progress(flamingo.happiness/100, "Happiness")
                    st.write(f"Dance Skill: {flamingo.dance_skill:.1f}")
                    st.write(f"Favorite Move: {flamingo.favorite_move}")
                    
                    if st.button(f"Dance!", key=f"dance_{idx}"):
                        coins, message = flamingo.dance()
                        st.session_state.coins += coins
                        st.success(message)
                    
                    if st.button(f"Rest", key=f"rest_{idx}"):
                        message = flamingo.rest()
                        st.success(message)

    except Exception as e:
        logger.error(f"Critical game error: {e}")
        st.error("An unexpected error occurred. Please refresh the page.")
        if st.button("Reset Game"):
            game.reset_game_state()

if __name__ == "__main__":
    main()
