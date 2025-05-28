from collections import deque

class QueueDeque:
    def __init__(self):
        self.queue = deque()
    
    ## function to enqueue
    def enqueue(self,data):
        self.queue.append(data)
    
    ## funtion to dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        self.queue.popleft()
    
    ## function to see the first element
    def front(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        
        print(f"Font element of the queue is: {self.queue[0]}")
        
    ## function to see the size of the queue
    def size(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        print(f"size of the queue is: {len(self.queue)}")    
    
    ## function to see the queue is empty
    def is_empty(self)->bool:
        return len(self.queue) == 0
    
    ## function to display the queue
    def display_queue(self):
        if self.is_empty():
            print("Queue is Empty")
            return

        print("Queue: ",list(self.queue))
    
if __name__ == "__main__":
    queue = QueueDeque()
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
    
        
    