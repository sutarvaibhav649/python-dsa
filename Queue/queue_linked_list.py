class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
    
    ## function to enqueue
    def enqueue(self,data):
        new_node = Node(data=data)
        if self.rear_node is None:
            self.front_node = self.rear_node = new_node
            return
        
        self.rear_node.next = new_node
        self.rear_node = new_node
    
    ## function to dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        result = self.front_node.data
        self.front_node = self.front_node.next
        
        if self.front_node is None:
            self.rear_node = None
        
    ## function to see the first element
    def front(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        
        print("First element is: ",self.front_node.data)
    
    ## function to see the queue is empty
    def is_empty(self):
        if self.front_node == None and self.rear_node == None:
            return True
        
        return False
    
    ## function to display the queue
    def display_queue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        
        current = self.front_node
        while current:
            print(f"{current.data} --> ",end="")
            current = current.next
        print("NULL")
        
if __name__ == "__main__":
    queue = QueueLinkedList()
    while(True):
        print("------------------------ Menu starts ------------------------")
        print("1.Add to queue")
        print("2.remove from queue")
        print("3.front of queue")
        print("4.display queue")
        print("5.exit")
        print("------------------------ Menu ends ------------------------")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter the data: "))
            queue.enqueue(data=data)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.front()
        elif choice == 4:
            queue.display_queue()
        elif choice == 5:
           print("Exiting the program.............")
           print("😊😊 Good bye 😊😊")
           exit()
        else:
            print("❌ Invalid option try again❌")
    
    