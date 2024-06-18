#!/usr/bin/env python3

from simplegmail import Gmail
from simplegmail.query import construct_query
import csv
gmail = Gmail()


query_params = {
    
    "newer_than" : (1,"day")
}

emails_data = []

messages = gmail.get_important_messages(query=construct_query(query_params))

for message in messages:
    if message.plain:
        email_data = [
            "Recipient: " + message.recipient,
            "Sender: " +message.sender,
            "Subject: " + message.subject,
            "Date: " + message.date,
            "Preview: " + message.snippet,
            "Message Body: " + message.plain
        ]
        emails_data.append(email_data)

with open("todays_email.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(emails_data)
f.close()

with open("todays_email.csv", 'r') as f:
    emails = csv.reader(f)
    for email in emails:
        print(email[2])
        print('\n')
f.close()
