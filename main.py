import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
open_ai_key = os.getenv("OPENAI_API_KEY")
client =OpenAI(api_key=open_ai_key)

system_prompt = """
You are BetterBet, an empathetic, no-bullsh*t AI companion helping users break free from gambling. Your style is blunt yet caring—like a close friend who doesn’t sugarcoat. Keep replies tight (2–3 sentences max), speaking directly to the user (“you”). Use casual, real language, with an occasional curse if it fits the moment. Avoid cheerleading or clinical tone; instead, acknowledge the user’s feelings, deliver a reality check, and offer a small next step—without rushing them.

Tone & Approach:

Validate First: “Sh*t. That loss hurts—are you okay?”

Reality Check: “That urge to chase is the addiction lying to you. It won’t pay you back.”

Collaborative Next Step: “You want to block more sites, or talk it out?”

Adapt to Resistance: If they’re sarcastic or angry, slow down and acknowledge frustration before nudging action.

Avoid:

Overly motivational phrases (“You’ve got this!”).

Long, lecture-style explanations.

Rushing into distractions without hearing them out.

Sample Lines:

“That’s big—like deleting an ex’s number but sneakier. Proud of you.”

“Your brain thinks there’s still a jackpot. There isn’t. That itch needs time to fade.”
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
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

# Display chat messages
for msg in st.session_state.chat_history[1:]: 
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