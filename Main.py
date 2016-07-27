#!/usr/bin/python
import pyttsx, pyaudio, IMAPClient

import fetch_email.py
import speech_to_text.py
import send_email.py

from twisted.internet import task
from twisted.internet import reactor

timeout = 60.0 #time is in 
####
def is_phone_up():
        if89  phone_is_up == 1: 
		return 1
	else: 
		return 0 
######		 
class Email:
	def __init__(self, Message):
		self.e = Message

	def Read_Message (self, is_phone_up):
		if(is_phone_up == 1):
			engine = pyttsx.init() 
			engine.say(self.e)
			engine.runAndWait()

#####
def sweep():
        if (fetch_email.new() != 0):
                
        
        x = Email(fetch_email.fetch())
        x.Read_Message(is_phone_up())

        
        pass


l = task.LoopingCall(sweep)
l.start(timeout) #run every "timeout"

reactor.run()


