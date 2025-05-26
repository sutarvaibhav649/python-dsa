## program to create the stack using list in python

## create the class called Stack
class Stack:
    def __init__(self):
        self.stack = []
    
    ## function to push the data is the stack
    def push(self,data):
        self.stack.append(data)
    
    ## function to pop the element from the stack   
    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return
        
        self.stack.pop()
    
    ## function to see the top element in the stack
    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
            return
        
        print(f'Top element from the stack {self.stack[-1]}')
        
    ## function to display the stack element
    def display_stack(self):
        if self.is_empty():
            print("Stack is Empty")
            return
        
        for items in self.stack:
            print(f"{items}-->",end="")
    
    ## function to see the stack is empty or not
    def is_empty(self)->bool:
        return (len(self.stack)==0)
    
if __name__ == "__main__":
    stack = Stack()
    while True:
        print("\n-------------------- Menu --------------------")
        print("1.push elemet")
        print("2.pop elemet")
        print("3.show top element")
        print("4.display stack")
        print("5.Exit")
        print("-------------------- Menu --------------------")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter the data: "))
            stack.push(data=data)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.peek()
        elif choice == 4:
            stack.display_stack()
        elif choice == 5:
            print("Exiting program................")
            print("😊😊 Good bye 😊😊")
            exit()
        else:
            print("❌ Enter valid choice ❌")
