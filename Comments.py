import Comment

class Comments:
    def __init__(self):
        self.count = 0
        self.headComment = None
        self.commentMap = {}


    # Addition of comments happen at head to show the latest comments first
    def addComment(self, text, author):
        comment = Comment.Comment(text, author)
        if(self.headComment == None):
            self.headComment = comment
        else:
            comment.setNextComment(self.headComment)
            self.headComment.setPrevComment(comment)
            self.headComment = comment
        self.count = self.count + 1
        self.commentMap[comment.getId()] = comment
        return True

    # Return all the siblings
    def getComments(self):
        commentList = []
        tempComment = self.headComment
        while(tempComment != None):
            commentList.append(tempComment)
            tempComment = tempComment.getNextComment()
        return commentList

    # Get the siblings count
    def getCommentsCount(self):
        return self.count

    # Search for comment by id
    def searchCommentById(self, id):
        comment = None
        if id in self.commentMap.keys():
            comment = self.commentMap[id]
        return comment

    # Edit the comment by id
    def editComment(self, id, text):
        if id in self.commentMap.keys():
            comment = self.searchCommentById(id)
            if(comment != None):
                comment.setText(text)
            else:
                raise Exception("Comment not found in comment list")
        else:
            raise Exception("Comment not found in comment list")

    # Delete comment by id
    def deleteComment(self, id):
        if id in self.commentMap.keys():
            self.count = self.count - 1
            if(self.headComment.getId() == id):
                if(self.headComment.getNextComment() == None):
                    self.headComment = None
                else:
                    self.headComment = self.headComment.getNextComment()
                    self.headComment.setPrevComment(None)
            else:
                comment = self.searchCommentById(id)
                if(comment.getNextComment() != None):
                    comment.getNextComment().setPrevComment(comment.getPrevComment())
                comment.getPrevComment().setNextComment(comment.getNextComment())
            del self.commentMap[id]
        else:
            raise Exception("Comment cannot be deleted as it is not found in the comment list")
