#!/usr/bin/python

import smtplib

#sender is a string literal 
#recivers is a list of strings 
class Send_Email:
	def __init__ (self , sender , recivers, speech_data):

		self.sender = sender
		self.receivers = recivers

		self.message = "From: From Office Phone <%s> \n To: To Person <%s> \n Subject: SMTP e-mail test\n"  % (self.sender, self.recivers)+ speech_data

	def send ()
		try:
			smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465 )
				smtpObj.ehlo()
			#how do we decide we are loginig in some type of config? 
			#login here
			smtpObj.sendmail(sender, receivers, message)         
			print "Successfully sent email"
		except:
			print "Error: unable to send email"
   
# http://www.tutorialspoint.com/python/python_sending_email.htm
