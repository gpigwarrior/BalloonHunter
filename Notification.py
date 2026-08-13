# imports for text
from twilio.rest import Client
import twilio
from requests.models import Response

# Email imports
import smtplib
from email.mime.text import MIMEText

# Slack imports
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv, dotenv_values


# Others:
from requests.api import request
import json
import requests

important = open("pass.json")
important = json.load(important)
print("Notification online")


def text_me(msg):
    client = Client(important["account_sid"], important["auth_token"])
    message = client.messages.create(
        body=msg,  # Message you send
        from_=important["from#"],  # Provided phone number
        to=important["to#"],
    )  # Your phone number
    print("TXT msg sid" + message.sid)


def email_me(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = important["email_sender"]
    msg["To"] = ", ".join([important["email_to"]])
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.login(important["email_sender"], important["email_app_password"])
    smtp_server.sendmail(
        important["email_sender"], [important["email_to"]], msg.as_string()
    )
    smtp_server.quit()


# client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))


def slack_everyone(channel_id, message):

    load_dotenv()
    client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
    # print(client)
    try:
        response = client.chat_postMessage(channel=channel_id, text=message)
        print(f"Message sent to {channel_id}: {response['message']['text']}")
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")


"""
subject = "Email Test Subject"
body = "This is the body of the text message"
email_me(subject, body)
"""
