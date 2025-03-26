import streamlit as st
from groq import Groq 

groq_api_key = "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"  # Replace with your actual API key
client = Groq(api_key=groq_api_key)

st.title("Better Bet AI")


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


def generate_betterbet_response(user_text):

    if not groq_api_key:
        return "Error: OpenAI API key not found. Please set OPENAI_API_KEY as an environment variable."

    try:
        
        messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ]
        # Call OpenAI's ChatCompletion
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {e}"
    
def main():


    user_text = st.text_input("What's on your mind?", value="", max_chars=200)

    if st.button("Get Support") or user_text:
        with st.spinner("Thinking..."):
            response = generate_betterbet_response(user_text)
        st.write("### BetterBet:")
        st.success(response)

if __name__ == "__main__":
    main()