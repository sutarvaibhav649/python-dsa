## creating the node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
## Create the list
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    ## function to insert data from beginning
    def insert_at_beginning(self,data):
        newNode = Node(data=data)
        newNode.next = self.head
        self.head = newNode
    
    ## function to add the data at specific position
    def insert_at_position(self,data,position):
        if position < 1:
            print("Invalid Position")
            return
        
        if position == 1:
            self.insert_at_beginning(data=data)
            return
        
        ## create the temp node to traverse to the position pointing to the head
        temp = self.head
        count = 1
        while temp is not None and count < position-1:
            temp = temp.next
            count += 1
        
        if temp is None:
            print("Position Out of Bound")
            return
        
        newNode = Node(data=data)
        newNode.next = temp.next
        temp.next = newNode
        
    ## function to add data at the end
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_beginning(data=data)
            return
        
        ## create the temp node to traverse to the end of the list
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        newNode = Node(data=data)
        temp.next = newNode
        
    ## function to delete node from the beginning
    def delete_from_beginning(self):
        ## handle edge cases
        if self.head is None:
            print("List is Empty")
            return
        
        self.head = self.head.next
        
    ## function to delete node from position
    def delete_from_position(self,position):
        ## handling edge cases
        if position < 1:
            print("Invalid Position")
            return
        
        if position == 1:
            self.delete_from_beginning()
            return
        
        ## create temp node to traverse upto position
        temp = self.head
        count = 1
        while temp is not None and count < position-1:
            temp = temp.next
            count += 1
        
        if temp is None or temp.next is None:
            print("Position out of Bound")
            return
        
        temp.next = temp.next.next
        
    ## function to delete node from end
    def delete_from_end(self):
        ## handle edge cases
        if self.head is None:
            print("List is Empty")
            return
        
        ## create the temp node to traverse upto end of the list
        temp = self.head
        
        while temp.next.next is not None:
            temp = temp.next
        
        temp.next = None
        
    ## function to display the list
    def display_list(self):
        ## handle edge cases
        if self.head is None:
            print("List is Empty")
            return
        
        temp = self.head
        while temp is not None:
            print(f"{temp.data} -->",end="")
            temp = temp.next
        print("NULL")
        
    ## function to search the element from the list
    def search_element(self,target):
        ## handle edge cases
        if self.head is None:
            print("List is Empty")
            return
        
        temp = self.head
        count = 1
        while temp is not None:
            if temp.data == target:
                return f"{target} found at {count} position"
            
            temp = temp.next 
            count += 1
            return f"No such element in the list"
    
if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    while True:
        print("----------------------------------------------")
        print("1.Insert data at Beginning")
        print("2.Insert data at Position")
        print("3.Insert data at End")
        print("4.Delete from Beginning")
        print("5.Delete from Position")
        print("6.Delete from End")
        print("7.Display list")
        print("8.Search element")
        print("9.Exit program")
        print("----------------------------------------------")
        choice = int(input("Enter you choice: "))
        
        if choice == 1:
            data = int(input("Enter the data: "))
            singly_linked_list.insert_at_beginning(data=data)
        elif choice == 2:
            data = int(input("Enter the data: "))
            position = int(input("Enter the position: "))
            singly_linked_list.insert_at_position(data=data,position=position)
        elif choice == 3:
            data = int(input("Enter the data: "))
            singly_linked_list.insert_at_end(data=data)
        elif choice == 4:
            singly_linked_list.delete_from_beginning()
        elif choice == 5:
            position = int(input("Enter the position: "))
            singly_linked_list.delete_from_position(position=position)
        elif choice == 6:
            singly_linked_list.delete_from_end()
        elif choice == 7:
            print("======================== Displaying the list Element ========================")
            singly_linked_list.display_list()
            print("======================== Displaying the list Element ========================")
        elif choice == 8:
            target = int(input("Enter the element to search: "))
            found = singly_linked_list.search_element(target=target)
            print(found)
        elif choice == 9:
            print("Exiting program.................")
            print("😊 Good bye 😊")
            exit()
        else:
            print("❌ select valid option ❌")