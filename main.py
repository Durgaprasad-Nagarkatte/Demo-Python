from ThreadNode import Thread
from Threads import Threads
from Post import Post

def test():
    # Creating a Post
    post = Post("DataStructure", "Use of Trees")
    print(post)

    # Adding comments to the post
    post.addComment([], "Wonderful article")
    post.addComment([], "Great insight to the working of tree data-structure")

    # Reading all the comments 
    li = post.getAllComments()
    print(li)

    # Addding threads to the post
    post.addComment([li[0].id], "Wonderful article, but have a questions")
    post.addComment([li[0].id], "Insightful post")
    thread = post.comments.getAllThreads()[0]
    childComments = thread.childThread.getAllThreads()
    print("Comments : ", childComments, childComments[0].id)

    # Editing threads of the post
    post.editComment([li[0].id, childComments[0].id], "Wonderful article, my question is resolved now")
    print("Comments : ", childComments)
    
    # Deleting threads of the post
    # post.deleteComment([li[0].id, childComments[0].id])
    # print("After deletions : ", childComments.getAllThreads())


if __name__ == "__main__":
    test()




