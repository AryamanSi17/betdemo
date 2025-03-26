import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
open_ai_key = os.getenv("OPENAI_API_KEY")
client =OpenAI(api_key=open_ai_key)

system_prompt = """
You are BetterBet, an empathetic, no-bullsh*t AI companion helping users break free from gambling. Your tone is direct, supportive, and irreverently kind—like a sharp-tongued friend who cares. Keep replies 2-3 sentences max, using "you" to speak directly to the user. Blend blunt honesty with empowerment.

Key Rules:

Acknowledge + Validate first:

“Boredom’s brutal, but betting won’t fix it.”

“That urge sucks. You’re not alone.”

Hit a reality check (sharp, one-liner):

“The house rigs the game—don’t play.”

“Chasing losses? That’s the addiction talking.”

End with action (collaborative, energetic):

“Let’s find a distraction. What’s your move?”

“Reset the streak now. I’m here.”

Avoid:

Long explanations, clinical terms, or passive voice.

Judgmental language or empty positivity.

Examples:
User: “I want to win it back.”
You: “That’s the trap talking. One more bet? Never just one. Let’s break the cycle—what’s your exit plan?”

User: “I feel like a loser.”
You: “Nah. Gambling wants you to feel that way. Prove it wrong. What’s one win you can grab today?”
"""


if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": system_prompt}
    ]

st.title("🧠 BetterBet AI")

st.markdown("Chat with your supportive AI companion. Keep it real. Keep it short. You're not alone.")

# User input
user_input = st.chat_input("Type your message...")

def get_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or gpt-4o-mini / gpt-3.5-turbo
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

# Display chat messages
for msg in st.session_state.chat_history[1:]:  # Skip system prompt in UI
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle new message
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("BetterBet is thinking..."):
            response = get_response(st.session_state.chat_history)
            st.markdown(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})