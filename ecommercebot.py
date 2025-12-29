import streamlit as st
from google import genai

# -----------------------------
# API KEY
# -----------------------------
API_KEY = "GOOGLE_API_KEY"

client = genai.Client(api_key=API_KEY)

# -----------------------------
# SYSTEM PROMPT
# -----------------------------
SYSTEM_PROMPT = """
You are an AI customer support assistant for an e-commerce platform.

Your role is strictly limited to EXPLAINING:
- Product return eligibility rules
- Return request workflow
- Inspection and approval stages
- Refund timelines and delays

You must NOT:
- Initiate returns
- Process refunds
- Ask for order IDs
- Modify customer accounts
- Perform transactions

If users request actions, politely state that you can only explain the process.

Respond clearly, step-by-step, in simple customer-friendly language.
"""

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="Return & Refund Explainer Bot", page_icon="🛒")
st.title("🛒 E-Commerce Return & Refund Explainer Bot")

user_query = st.text_input("Ask your question")

if st.button("Get Explanation"):
    if user_query.strip():
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[
                SYSTEM_PROMPT,
                user_query
            ]
        )
        st.write(response.text)
    else:
        st.warning("Please enter a question")
