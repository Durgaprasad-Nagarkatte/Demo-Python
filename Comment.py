import uuid
import Comments

class Comment:
    def __init__(self, text, author):
        self.id = str(uuid.uuid4())
        self.text = text
        self.author = author
        self.timeStamp = None
        self.likes = 0
        self.prevComment = None
        self.nextComment = None
        self.comments = Comments.Comments()

    def getId(self):
        return self.id

    def getText(self):
        return self.text

    def setText(self, text):
        self.text = text
        return True

    def getAuthor(self):
        return self.author

    def setAuthor(self, author):
        self.author = author
        return True

    def getTimeStamp(self):
        return self.timeStamp

    def incrementLike(self):
        self.likes = self.likes + 1
        return True

    def decrementLike(self):
        if(self.likes > 0):
            self.likes = self.likes - 1
            return True
        return False

    def getComments(self):
        return self.comments

    def setComments(self, comments):
        self.comments = comments
        return True

    def getPrevComment(self):
        return self.prevComment

    def getNextComment(self):
        return self.nextComment

    def setPrevComment(self, comment):
        self.prevComment = comment
        return True

    def setNextComment(self, comment):
        self.nextComment = comment
        return True

    def __repr__(self):
        # TODO: Overwrite this method
        return f'Comment({self.id},{self.text},{self.author})'