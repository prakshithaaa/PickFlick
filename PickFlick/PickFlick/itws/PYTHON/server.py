import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Start TLS for security
server.starttls()

#Authentication
sender_email = "prakshithaa1d@gmail.com"
password = ""

server.login(sender_email, password)

#Message details
receiver_email = "prakshithapradeep24bcs0163@iiitkottayam.ac.in"
message = """\
Subject