class QueueList:
    def __init__(self):
        self.queue = []
        
    ## function to append the data
    def enqueue(self,data):
        self.queue.append(data)
        
    ## function to dequeue 
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        
        self.queue.pop()
    
    ## function to see the first element of the queue
    def front(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        
        print(f"Front element of Queue is: {self.queue[0]}")
    
    ## function to see the size of the queue
    def size(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        
        print(f"Size of the queue is: {len(self.queue)}")        
    
    ## function to see the empty queue
    def is_empty(self)->bool:
        return len(self.queue)==0
    
    ## function to display the queue
    def display_queue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        print("Queue:",list(self.queue))
        
if __name__ == "__main__":
    queue = QueueList()
    while(True):
        print("------------------------ Menu starts ------------------------")
        print("1.Add to queue")
        print("2.remove from queue")
        print("3.front of queue")
        print("4.display queue")
        print("5.size of queue")
        print("6.exit")
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
            queue.size()
        elif choice == 6:
            print("Exiting the program.............")
            print("😊😊 Good bye 😊😊")
            exit()
        else:
            print("❌ Invalid option try again❌")
        