import os
import win32com.client
from datetime import datetime, timedelta

################################################################
# OS
################################################################

##
# Print folder tree
##
def printFolderTree(path):
    root = os.path.join(path)
    for directory, subdir_list, file_list in os.walk(root):
        print('Directory:', directory)
        for name in subdir_list:
            print('Subdirectory:', name)
        for name in file_list:
            print('File:', name)


################################################################
# WIN32
################################################################

##
# Print emails Function
##
def listFolders(directoryFolders):
    for folder in directoryFolders.Folders: 
        print(folder.Name)
##
# Print messages details
##
def displayMessages(messages):
    for message in list(messages):
        print(message.subject)
##
# Filtering emails by sender / recieved dt
##
def emailListFilteredBySenderRecievedDt(sender='',daysago=1):
    outlook = win32com.client.Dispatch('outlook.application')
    mapi = outlook.GetNamespace("MAPI")
    inbox = mapi.GetDefaultFolder(6)
    messages = inbox.Items
    received_dt = datetime.now() - timedelta(days=daysago)
    received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')
    messages = messages.Restrict("[ReceivedTime] >= '" + received_dt + "'")
    if len(sender)!=0:
        print(sender)
        messages = messages.Restrict("[SenderEmailAddress] = '{}'".format(sender))
    return messages