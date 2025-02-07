# WhatsApp Mental Health Chatbot

The WhatsApp Mental Health Chatbot is an AI-driven conversational assistant designed to provide evidence-based mental health support. Leveraging GPT-4 for empathetic conversations, LlamaIndex for document retrieval, and sentiment analysis for early distress detection, this chatbot offers Cognitive Behavioral Therapy (CBT)-based guidance, workplace stress management, and self-assessments through WhatsApp.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [Acknowledgements](#acknowledgements)

---

## Features

- **Conversational AI & Therapy Support**  
  - Provides CBT-based therapy sessions, mindfulness exercises, and stress management techniques.
  - Generates empathetic, context-aware responses using GPT-4.

- **Mental Health Assessments**  
  - Delivers validated self-assessments for stress, anxiety, and burnout.
  - Tracks user progress over time.

- **Document Retrieval with LlamaIndex**  
  - Retrieves HR-approved mental health and wellness documents.
  - Enhances responses with evidence-based context.

- **Sentiment Analysis**  
  - Analyzes user messages for emotional tone using VADER.
  - Flags messages indicating high distress for proactive intervention.

- **WhatsApp Integration via Twilio**  
  - Seamlessly handles incoming and outgoing messages on WhatsApp.
  - Supports proactive messaging and check-ins.

- **Subscription Management**  
  - Offers tiered access for individuals (B2C) and businesses (B2B).
  - Includes support for free trials, individual, small business, and enterprise plans.

---

## Tech Stack

- **Backend Framework:** Flask
- **Database:** SQLAlchemy (SQLite for development; configurable for production)
- **APIs:**
  - [GPT-4](https://openai.com/api/) – for generating therapy-based responses.
  - [Twilio](https://www.twilio.com/) – for WhatsApp messaging integration.
- **Utilities:**
  - [LlamaIndex](https://gpt-index.readthedocs.io/) – for document indexing and retrieval.
  - [VADER Sentiment](https://github.com/cjhutto/vaderSentiment) – for sentiment analysis.
- **Environment Management:** Python-dotenv

---

## Folder Structure

```plaintext
whatsapp-mental-health-chatbot/
├── app/
│   ├── __init__.py         # Initializes the Flask app and loads configurations/extensions
│   ├── config.py           # Application configuration (API keys, DB URIs, etc.)
│   ├── routes.py           # Flask endpoints (including /whatsapp webhook)
│   ├── models.py           # Database models (e.g., User, Subscription)
│   └── utils/
│       ├── __init__.py     # Makes utils a package
│       ├── gpt4.py         # Functions for interacting with the GPT-4 API
│       ├── llama_index.py  # Functions for building and querying the document index
│       ├── sentiment.py    # Functions for sentiment analysis using VADER
│       └── subscription.py # Utilities for managing user subscriptions and access control
├── tests/                  # Unit and integration tests
├── docs/                   # Project documentation (e.g., architecture.md)
├── .env.example            # Example environment variables file
├── requirements.txt        # Python dependencies
├── Procfile                # Procfile for deployment (e.g., Heroku)
├── Dockerfile              # Dockerfile for containerized deployment (optional)
├── README.md               # This file
└── run.py                  # Application entry point


Getting Started
Prerequisites
Python 3.8+
pip
Virtualenv or Conda
A Twilio account with a WhatsApp Sandbox or Business number
OpenAI API key for GPT-4 access
Installation
Clone the Repository:

bash
Copy
git clone https://github.com/your-username/whatsapp-mental-health-chatbot.git
cd whatsapp-mental-health-chatbot
Create and Activate a Virtual Environment:

bash
Copy
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install Dependencies:

bash
Copy
pip install -r requirements.txt
Set Up Environment Variables:

Copy .env.example to .env:

bash
Copy
cp .env.example .env
Edit the .env file to include your API keys and configuration details:

dotenv
Copy
SECRET_KEY=your_secret_key_here
DATABASE_URI=sqlite:///app.db
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
OPENAI_API_KEY=your_openai_api_key
Usage
Run the Application Locally:

bash
Copy
python run.py
The Flask app will start on http://127.0.0.1:5000/.

Expose Localhost (Optional):

Use ngrok to expose your local server for Twilio webhook testing:

bash
Copy
ngrok http 5000
Configure Twilio Webhook:

Log into your Twilio Console.
Set the webhook URL for WhatsApp messages to your ngrok URL, e.g., https://<ngrok-id>.ngrok.io/whatsapp.
Interact with the Chatbot:

Send a WhatsApp message to your Twilio Sandbox number to start interacting with the chatbot.

Testing
Tests are provided for various components of the application.

Run all tests using:

bash
Copy
pytest
Testing Folders:

tests/test_routes.py for endpoint testing.
tests/test_gpt4.py for GPT-4 API interaction.
tests/test_llama_index.py for document indexing and retrieval.
tests/test_sentiment.py for sentiment analysis.
tests/test_subscription.py for subscription management logic.
Deployment
Deploying to Heroku
Create a Heroku App:

bash
Copy
heroku create your-app-name
Push the Code:

bash
Copy
git push heroku main
Set Environment Variables on Heroku:

bash
Copy
heroku config:set SECRET_KEY=your_secret_key_here
heroku config:set DATABASE_URI=your_database_uri_here
heroku config:set TWILIO_ACCOUNT_SID=your_twilio_account_sid
heroku config:set TWILIO_AUTH_TOKEN=your_twilio_auth_token
heroku config:set OPENAI_API_KEY=your_openai_api_key
Scale the App:

bash
Copy
heroku ps:scale web=1
Docker Deployment
A Dockerfile is provided for containerized deployments. To build and run the Docker container:

bash
Copy
docker build -t whatsapp-mental-health-chatbot .
docker run -p 5000:5000 whatsapp-mental-health-chatbot
Future Enhancements
Advanced AI Risk Detection: Improve sentiment analysis and add crisis detection capabilities.
Multi-Platform Integration: Extend support to Slack, Microsoft Teams, etc.
Subscription Automation: Integrate a payment gateway for automated subscription management.
HR Dashboard: Develop an analytics dashboard for HR to monitor employee well-being trends.
Enhanced User Experience: Refine conversational flows and add multilingual support.
Contributing
Contributions are welcome! If you would like to contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.
Please make sure to follow the Code of Conduct and write tests for your contributions.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
OpenAI for GPT-4.
Twilio for WhatsApp messaging APIs.
LlamaIndex for document indexing.
VADER Sentiment for sentiment analysis.
All contributors and the open source community for their invaluable support.

