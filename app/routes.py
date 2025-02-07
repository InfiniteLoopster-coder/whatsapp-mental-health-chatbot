# app/routes.py
from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

# Import utility functions
from app.utils.gpt4 import generate_gpt_response
from app.utils.llama_index import get_relevant_info
from app.utils.sentiment import analyze_sentiment
from app.utils.subscription import check_subscription

# Create a Blueprint for our main routes
main = Blueprint("main", __name__)

@main.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    # Extract sender and message content
    user_id = request.values.get('From', '')
    user_message = request.values.get('Body', '')

    # Check subscription status (dummy logic for demonstration)
    if not check_subscription(user_id):
        response = MessagingResponse()
        response.message("Your subscription is inactive. Please subscribe to continue receiving personalized support.")
        return str(response)

    # Analyze sentiment from the user message
    sentiment = analyze_sentiment(user_message)
    if sentiment.get('compound', 0) < -0.5:
        # Here you could add additional logic for high-distress alerts
        print(f"High distress detected for user {user_id}: {sentiment}")

    # Retrieve additional context from indexed documents
    additional_context = get_relevant_info(user_message)

    # Combine the user message with additional context for GPT-4 processing
    final_prompt = f"{user_message}\nAdditional context: {additional_context}"
    gpt_response = generate_gpt_response(final_prompt)

    # Prepare the Twilio response message
    response = MessagingResponse()
    response.message(gpt_response)
    return str(response)
