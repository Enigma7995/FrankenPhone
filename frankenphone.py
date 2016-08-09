#!/usr/bin/python

import smtplib
from datetime import date
import imapclient
#import speech_recognition as sr

from os import path

# return email login information stored in config file as a dictionary ['username': username, 'password': password]
def getLoginCredentials():
    credentials = {'username': '', 'password': ''}

    with open('config.txt', 'r') as confFile:
        credList = confFile.readline().strip().split(':')
        credentials['username'] = credList[0]
        credentials['password'] = credList[1]
    
    return credentials



def getNewUIDs(username, password):
    old_UID = None

    with open('uids.txt', 'r') as uidFile:
        old_UID =  uidFile.readline()
    
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imapObj.login(username, password)
    imapObj.select_folder('INBOX', readonly=True)
    new_UID = imapObj.search([u'SINCE', date.today()])

    with open('uids.txt', 'w') as uidFile:
        if (len(new_UID) > 0 and ( old_UID == '' or new_UID[-1] > old_UID ) ):
            uidFile.write(str(new_UID[-1]))

    return new_UID



def send (username, password, sender, receivers, message):
    try:
        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465 )
        smtpObj.ehlo()
        smtpObj.login(username, password)
        smtpObj.sendmail(sender, receivers, message)         
        print "Successfully sent email"
    except:
        print "Error: unable to send email"



def listen():

	# obtain path to "english.wav" in the same folder as this script
	AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "agnew_nabobs.wav")

	# use the audio file as the audio source
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source) # read the entire audio file 

	# recognize speech using Sphinx
	try:
		print("Sphinx thinks you said: \n" + r.recognize_sphinx(audio))
	except sr.UnknownValueError:
		print("Sphinx could not understand audio")
	except sr.RequestError as e:
		print("Sphinx error; {0}".format(e))
		
	return recognize_sphinx(audio)


