
print("hello")

import streamlit as st

# Initialize session state
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # To store the chat messages

# Define chatbot questions
questions = [
    "What's your name?",
    "How are you feeling today?",
    "Let's talk about this year 2024.",
    "How was your year?",
    "What is the most amazing memory of this year of yours?",
    "What is the one learning you got from this year?",
    "What is the one thing you liked the most about yourself this year?",
    "Have you captured the best memories of your life with you? If yes, I can give a suggestion to you.",
    "If you get a chance to write a book regarding the philosophy of living life, what would be the title?",
    "Do you pay gratitude to the higher for all the opportunities in your life?",
    "What one advice do you want to give yourself to be happier in life?"
]

# Suggestion for Question 7
suggestion = "Please convert them to physical copies; otherwise, you might lose them due to storage issues."

# Layout configuration
st.set_page_config(page_title="DATE TO MEMORIES (2024 Edition)", layout="wide")

# Header styling
st.markdown(
    """
    <div style="background-color:orange; padding:20px; border-radius:10px; text-align:center;">
        <h1 style="color:white; margin:0;">DATE TO MEMORIES (2024 Edition)</h1>
        <h3 style="color:white; margin:0;">Reliving Moments, Creating Memories</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# Chat container
st.write("### Chat Conversation")
chat_area = st.container()

# Input area
user_input = st.text_input("Type your response below and press Enter:")

# Helper function to render chat
def display_chat():
    """Render the chat history dynamically."""
    for message in st.session_state.chat_history:
        if message["sender"] == "bot":
            st.markdown(
                f"""
                <div style="text-align:left; margin:10px;">
                    <div style="display:inline-block; padding:10px; background-color:#f0f0f0; border: 1px solid red; border-radius:10px; max-width:60%; font-family:sans-serif;">
                        <b>Bot:</b> {message['text']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div style="text-align:right; margin:10px;">
                    <div style="display:inline-block; padding:10px; background-color:#e1ffc7; border-radius:10px; max-width:60%; font-family:sans-serif; font-weight:bold;">
                        {message['text']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# Main logic for handling chat
if user_input:
    # Record user response
    st.session_state.chat_history.append({"sender": "user", "text": user_input})

    # Get the current question
    current_index = st.session_state.current_question_index
    if current_index < len(questions):
        # Save the bot's next question
        bot_response = questions[current_index]
        st.session_state.chat_history.append({"sender": "bot", "text": bot_response})
        st.session_state.current_question_index += 1

        # Add suggestion for Question 7
        if current_index == 7:
            st.session_state.chat_history.append({"sender": "bot", "text": suggestion})
    else:
        # End of conversation
        user_name = st.session_state.chat_history[0]["text"]
        thank_you_message = (
            f"Thank you for your responses, {user_name}! I appreciate your thoughtful answers and wish you the best for the future."
        )
        st.session_state.chat_history.append({"sender": "bot", "text": thank_you_message})

    # Clear the input box for the next response
    st.experimental_rerun()

# Display chat history
with chat_area:
    display_chat()
