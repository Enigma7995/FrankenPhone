#!/usr/bin/python

import pyttsx, smtplib, pyaudio
from datetime import date
import imapclient
import speech_recognition as sr

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

def fetchEmail (username, password, UID):
    Email_arr = []
    imapObold_UID =  uidFile.readline()
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imapObj.login(username, password)
    imapObj.select_folder('INBOX', readonly=True)
    uidFile.write(str(UIDs[-1]))
    rawMessage = imapObj.fetch([new_UID], ['BODY[]' , 'FLAGS'])
    message = pyzmail.PyzMessage.factory(rawMessages[new_UID]['BODY[]'])
    Email_arr.append(int(UIDs[-1]))
    Email_arr.append(message.get_addresses('from'))
    Email_arr.append(message.get_addresses('to')) 
    Email_arr.append(message.text_part.get_payload().decode(message.text_part.charset))

    return Email_arr
    
                         

def sendEmail (username, password, sender, receivers, message):
    try:
        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465 )
        smtpObj.ehlo()
        smtpObj.login(username, password)
        smtpObj.sendmail(sender, receivers, message)
        return 0
    except:
        return -1


def speechToText(wavFileName):

	# obtain path to "english.wav" in the same folder as this script
	AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), wavFileName)

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
		
	return r.recognize_sphinx(audio)
    
def textToSpeech(message) :
    engine = pyttsx.init() 
    engine.say(message)
    engine.runAndWait()


textToSpeech("h a book or other written or printed work, regarded in terms of its content rather than its physical formello mr.Robot you will see that i will not finnish") 
