import Comments
class Service:
    def __init__(self):
        self.rootComments = None

    # Searching for comment in a tree structrure
    def searchForComment(self, idList):
        tempComment = self.rootComments
        comment = None
        for id in idList:
            comment = tempComment.searchCommentById(id)
            if(comment == None):
                raise Exception("comment not available with id : ", id)
            tempComment = tempComment.getComments()
        print("List :", idList)
        print("Comment :", comment)
        return comment

    # Adding comment in a tree structure
    def addComment(self, idList, text, author):
        if(len(idList) == 0):
            if(self.rootComments == None):
                self.rootComments = Comments.Comments()
            self.rootComments.addComment(text, author)
        else:
            comment = self.searchForComment(idList)
            comment.getComments().addComment(text, author)
        
    # Editing a comment in a tree structure
    def editComment(self, idList, text):
        if(self.rootComments == None):
            raise Exception("Operation cannot be performed")
        if(len(idList) == 1):
            self.rootComments.editComment(idList[0], text)
        else:
            comment = self.searchForComment(idList[0:len(idList)-1])
            if(comment != None):
                comment.getComments().editComment(idList[-1], text)
        
    # Delete a comment from the tree structure
    def deleteComment(self, idList):
        if(self.rootComments == None):
            raise Exception("Operation cannot be performed")

        tempComment = self.rootComments
        for i in range(len(idList) - 1):
            tempComment = tempComment.searchCommentById(idList[i])
        tempComment.getComments().deleteComment(idList[-1])

    # Retrieving all the comments by id from the tree structure
    def getComments(self, idList):
        if(len(idList) == 0):
            if(self.rootComments == None):
                return []
            else:
                return self.rootComments.getComments()
        else:
            comment = self.searchForComment(idList)
            return comment.getComments().getComments()

    def addLikeToComment(self):
        ""

    def removeLikeFromComment(self):
        ""
