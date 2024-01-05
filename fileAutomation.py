import os
from shutil import move
from os.path import exists, join

#source folder
source = '/Users/paulcrouch/Downloads'

#destination folders
destinationPictures = '/Users/paulcrouch/Library/Mobile Documents/com~apple~CloudDocs/Downloaded Pictures'
destinationVideos = '/Users/paulcrouch/Library/Mobile Documents/com~apple~CloudDocs/Downloaded Videos'
destinationDocuments = '/Users/paulcrouch/Documents'

#image types
imageExtensions = ['.jpeg', '.jpg', '.png', '.heic']

#video types
videoExtensions = ['.mp4', '.wav']

#document types
documentExtensions = ['.pdf', '.docx', '.xlsx', '.xls', '.ppt', '.pptx', '.txt']

def main():

     with os.scandir(source) as entries:
          for entry in entries:
               name = entry.name
               if checkPictures(entry, name):
                    continue
               elif checkVideos(entry, name):
                    continue
               elif checkDocuments(entry, name):
                    continue



#function to move a file
def moveFile(entry, name, destination):

     counter = 1
     #check if file exists
     while exists(f'{destination}/{entry.name}'):
          fileName, extension = os.path.splitext(entry) #splits the file from the extension
          oldName = join(fileName, extension)
          tempName = f'{fileName}({str(counter)}){extension}'
          newName = join(destination, tempName)

          print(f'BEFORE:\nOld Name: {oldName}; type: {type(oldName)},\nNew Name: {newName}; type: {type(newName)}\nFile Name: {entry.name}')
          os.rename(entry, newName)
          print(f'AFTER:\nOld Name: {oldName}; type: {type(oldName)},\nNew Name: {newName}; type: {type(newName)}\nFile Name: {entry.name}\n')
          counter += 1
          
     #move(file, destination)

     #if it does, add a number to the end and check if THAT exists

     #if it does NOT, move the file

#checks picture files
def checkPictures(entry, name):
     for extension in imageExtensions:
          if name.endswith(extension) or name.endswith(extension.upper()):
               print(f'Picture: {name}')
               moveFile(entry, destinationPictures)
               return True


#checks video files
def checkVideos(entry, name):
     for extension in videoExtensions:
          if name.endswith(extension) or name.endswith(extension.upper()):
               print(f'Video: {name}')
               moveFile(entry, destinationVideos)
               return True                

#checks document files
def checkDocuments(entry, name):
     for extension in documentExtensions:
          if name.endswith(extension) or name.endswith(extension.upper()):
               print(f'Document: {name}')
               moveFile(entry, name, destinationDocuments)
               return True

if __name__ == '__main__':
    main()