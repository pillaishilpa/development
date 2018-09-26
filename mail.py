
import smtplib
server = "outlook.td.teradata.com"
FROM   = "sp186090@Teradata.com"
to= [FROM]
sub="jenkins"
TEXT="""Hi this is a message from jenkins \n
Goodmorning Shilpa, have a nice day"""
msg = """"From: %s\r\nTo: %s\r\nSubject: %s\r\n\
        %s\n""" % (FROM, ", ".join(to),sub,TEXT)
server = smtplib.SMTP(server)
server.sendmail(FROM,to,msg)
server.quit()