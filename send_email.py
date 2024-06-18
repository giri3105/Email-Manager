from simplegmail import Gmail
import csv
gmail = Gmail()
with open("todays_email.csv",'r') as f:
    emails = csv.reader(f)
    for email in emails :
        params = {
        "to": "me22b2004@iiitdm.ac.in",
        "sender": "girimanikandan3105@gmail.com",
        
        "subject": email[2],
        "msg_plain": email[5] + "sent by : " + email[1]
        #"attachments": ["path/to/something/cool.pdf", "path/to/image.jpg", "path/to/script.py"],
          # use my account signature
        }
        message = gmail.send_message(**params)  # equivalent to send_message(to="you@youremail.com", sender=...)


'''         "Recipient: " + message.recipient,
            "Sender: " +message.sender,
            "Subject: " + message.subject,
            "Date: " + message.date,
            "Preview: " + message.snippet,
            "Message Body: " + message.plain'''