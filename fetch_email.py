
import imapclient

with open('config.txt', 'r') as confFile:
    username = confFile.readline().strip().split(':')[-1]
    password = confFile.readline().strip().split(':')[-1]
    print username
    print password
    
def fetch():

    with open('uids.txt', 'r+') as uidFile:
    
        old_UID =  uidFile.readline()
        imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
        imapObj.login(username, password)
        imapObj.select_folder('INBOX', readonly=True)
        new_UID = imapObj.search('SINCE 05-Jul-2016')
        if (new_UID > old_UID):
            uidFile.write(str(UIDs[-1]))
            return new_UID
        else:
            return 0

        

        






    

	


	
