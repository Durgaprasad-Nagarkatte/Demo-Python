import uuid
import datetime
import Threads

class Post:
    def __init__(self, title, content):
        self.id = str(uuid.uuid4)
        self.title = title
        self.content = content 
        self.timeStamp = datetime.datetime.now()
        self.comments = Threads.Threads()

    # Adding comments to the post
    def addComment(self, idList, content):
        if(len(idList) == 0):
            self.comments.addThread(content)
            return

        thread = None
        currentThread = self.comments
        for i in range(len(idList)):
            thread = currentThread.getThread(idList[i])
            thread = thread.getChildThread()
        thread.addThread(content)
        
    # Editing comment
    def editComment(self, idList, content):
        if(len(idList) == 0):
            raise Exception("Operation not suppored")

        thread = None
        currentThread = self.comments
        for i in range(len(idList)):
            thread = currentThread.getThread(idList[i])
            currentThread = thread.getChildThread()
        thread.setContent(content)

    def deleteComment(self, idList):
        if(len(idList) == 0):
            raise Exception("operation not suppported")

        thread = None
        currentThread = self.comments
        for i in range(len(idList)-1):
            thread = currentThread.getThread(idList[i])
            currentThread = thread.getChildThread()
        print(thread.childThread.deleteThread(idList[-1]))
        
    def getAllComments(self):
        return self.comments.getAllThreads();

    def __str__(self):
        return f'Post({self.id},{self.title},{self.content},{self.comments})'




    