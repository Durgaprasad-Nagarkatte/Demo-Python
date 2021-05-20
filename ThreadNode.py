import datetime
import Threads
import uuid

class Thread:
    def __init__(self, content):
        self.id = str(uuid.uuid4())
        self.prevNode = None
        self.nextNode = None
        self.likes = 0
        self.content = content
        self.timeStamp = datetime.datetime.now()
        self.isEdited = False
        self.childThread = Threads.Threads()

    def getId(self):
        return self.id

    def setContent(self, content):
        self.content = content
        self.isEdited = True

    def setPrevNode(self, node):
        self.prevNode = node

    def setNextNode(self, node):
        self.nextNode = node

    def getChildThread(self):
        return self.childThread

    def addToChildThread(self, content):
        if(self.childThread == None):
            self.childThread = Threads.Threads()
        print("Child Thread : ", self.childThread)
        self.childThread.addThread(content)

    def getChildThread(self):
        return self.childThread

    def __repr__(self):
        return f'Thread({self.id},{self.content})'