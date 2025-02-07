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
- [Contributing](#contributing)
- [License](#license)
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
