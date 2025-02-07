
import openai
import os

# Set the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_gpt_response(user_message):
    """
    Generates a response from the GPT-4 API based on the provided user message.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a compassionate mental health support assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print("GPT-4 API error:", e)
        return "I'm sorry, I encountered an error while processing your request. Please try again later."
