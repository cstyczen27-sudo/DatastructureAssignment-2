# Create a Node class to represent each customer in the waitlist
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''

# Create a LinkedList class to manage the waitlist
class LinkedList:
    def __init__(self, head):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self,name):
        current = self.head
        prev = None
        while current:
            if current.name == name:
                if prev is None:
                    self.head = self.head.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
        print("Name not found in list")

    def print_list(self):
        current = self.head
        if not current:
            print("Current waitlist is empty")
        else:
            while current:
                print(current.name)
                current = current.next

    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''

def waitlist_generator():
    # Create a new linked list instance
    mylist = LinkedList(None)

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            mylist.add_front(name)
        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            mylist.add_end(name)
        elif choice == "3":
            name = input("Enter customer name to remove: ")
            mylist.remove(name)
        elif choice == "4":
            mylist.print_list()
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")


waitlist_generator()
# Call the waitlist_generator function to start the program


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''
