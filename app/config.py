# app/config.py
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Third-party API keys
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
