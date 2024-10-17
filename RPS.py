import streamlit as st
import random

# Initialize session state variables
if "round_number" not in st.session_state:
    st.session_state.round_number = 1
    st.session_state.user_score = 0
    st.session_state.comp_score = 0
    st.session_state.num_rounds = 0
    st.session_state.game_started = False
    st.session_state.result_message = ""
    st.session_state.comp_choice = ""

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

# Function to determine the winner
def determine_winner(user, comp):
    if user == comp:
        return "It's a Draw! How boring! Better luck next time.", 0
    elif (user == 'rock' and comp == 'scissor') or \
         (user == 'scissor' and comp == 'paper') or \
         (user == 'paper' and comp == 'rock'):
        return f"{user.capitalize()} wins over {comp}!", 1  # User wins
    else:
        return f"{comp.capitalize()} wins over {user}!", -1  # Computer wins

# User input for the number of rounds
if not st.session_state.game_started:
    st.title("Welcome to the Rock-Paper-Scissors App!")
    st.session_state.num_rounds = st.number_input(
        "How many rounds would you like to play?", 
        min_value=1, max_value=10, step=1
    )
    if st.button("Start Game"):
        st.session_state.game_started = True

# Main game logic
if st.session_state.game_started and st.session_state.round_number <= st.session_state.num_rounds:
    st.subheader(f"Round {st.session_state.round_number}")

    # User selects their move
    user_choice = st.selectbox(
        "Pick your move:", 
        ["rock", "paper", "scissor"], 
        key=f"user_choice_{st.session_state.round_number}"
    )

    # When the user clicks "Submit", play the round
    if st.button("Submit"):
        st.session_state.comp_choice = get_computer_choice()
        result_message, result = determine_winner(user_choice, st.session_state.comp_choice)

        # Update scores
        if result == 1:
            st.session_state.user_score += 1
        elif result == -1:
            st.session_state.comp_score += 1

        st.session_state.result_message = result_message
        st.session_state.round_number += 1

# Display the result of the current round
if st.session_state.result_message:
    st.write(f"Player: {user_choice}")
    st.write(f"Computer: {st.session_state.comp_choice}")
    st.write(st.session_state.result_message)
    st.write(f"Current Score -> PLAYER: {st.session_state.user_score} COMPUTER: {st.session_state.comp_score}")

# Display the final results when all rounds are completed
if st.session_state.round_number > st.session_state.num_rounds:
    st.write("## Final Game Results:")
    st.write(f"Rounds Played: {st.session_state.num_rounds}")
    st.write(f"Player Score: {st.session_state.user_score}")
    st.write(f"Computer Score: {st.session_state.comp_score}")

    if st.session_state.user_score > st.session_state.comp_score:
        st.success('User wins the game!')
    elif st.session_state.user_score < st.session_state.comp_score:
        st.error('Computer wins the game!')
    else:
        st.info("It's a draw!")

    st.balloons()  # Display balloons animation for the end of the game

    # Reset the game state to allow replay
    if st.button("Play Again"):
        st.session_state.round_number = 1
        st.session_state.user_score = 0
        st.session_state.comp_score = 0
        st.session_state.game_started = False
        st.session_state.result_message = ""
        st.session_state.comp_choice = ""
