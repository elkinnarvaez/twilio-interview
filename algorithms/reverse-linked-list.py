class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end = " ")
            temp = temp.next
        print()
    
    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
    
    def reverse(self):
        prevNode = None
        currentNode = self.head
        while(currentNode != None):
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        self.head = prevNode

def main():
    linkedList = LinkedList()
    linkedList.push(1)
    linkedList.push(2)
    linkedList.push(3)
    linkedList.push(4)
    linkedList.push(5)
    linkedList.print()
    linkedList.reverse()
    linkedList.print()

main()