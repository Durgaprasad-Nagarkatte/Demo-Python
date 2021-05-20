import ThreadNode

class Threads:
    def __init__(self):
        self.head = None
        self.current = None
        self.length = 0
        self.threadSet = set()

    def getHead(self):
        return self.head

    def getCurrent(self):
        return self.current

    def getThreadSet(self):
        return self.threadSet

    # Adding new Thread
    def addThread(self, content):
        thread = ThreadNode.Thread(content)
        if(self.head == None):
            self.head = thread

        if(self.current != None):
            self.current.setNextNode(thread)
        
        self.threadSet.add(thread.id)
        thread.setPrevNode(self.current)
        self.current = thread
        self.length = self.length + 1

    # Return all the threads
    def getAllThreads(self):
        current = self.head
        threads = []
        while(current != None):
            threads.append(current)
            current = current.nextNode
        return threads

    def getNumberOfThreads(self):
        return self.length

    # Searching a thread and returning the reference
    def searchThread(self, id):
        current = self.head
        while(current != None):
            if(current.getId() == id):
                return current
            current = current.nextNode
        return -1

    # Return the thread for a given id
    def getThread(self, id):
        if(id in self.threadSet):
            result = self.searchThread(id)
            if(result == -1):
                raise Exception("The thread with given id : " + id + " not present")
            return result
        raise Exception("The thread with given id : " + id + " not present")
        

    def delete(self, id):
        if(self.head == None):
            raise Exception("Operation not supported")

        thread = self.searchThread(id)
        if(thread == -1):
            raise Exception("Item not present to delete")
        
        if(thread.prevNode != None):
            thread.prevNode.nextNode = thread.nextNode
            thread.nextNode.prevNode = thread.prevNode 
        
    # Delete the thread for a given id
    def deleteThread(self, id):
        if(id in self.threadSet):
            self.delete(id)