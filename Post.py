import uuid
import datetime
import Threads
import Service

class Post:
    def __init__(self, title, content):
        self.id = str(uuid.uuid4)
        self.title = title
        self.content = content 
        self.timeStamp = datetime.datetime.now()
        self.service = Service.Service()

    # Adding comments to the post
    def addComment(self, idList, text, author):
        self.service.addComment(idList, text, author)
        
    # Editing comment
    def editComment(self, idList, text):
        self.service.editComment(idList, text)

    # Method to delete the thread
    def deleteComment(self, idList):
        self.service.deleteComment(idList)
        
    def getAllComments(self):
        return self.service.getComments()

    def __str__(self):
        return f'Post({self.id},{self.title},{self.content}'




    