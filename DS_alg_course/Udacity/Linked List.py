# Linked List 

# Creating an element for linked list 
"""Make sure you understand this code before moving on! We use __init__ to initialize a new Element. 
An Element has some value associated with it (which could be anything—a number, a string, a character, et cetera), 
and it has a variable that points to the next element in the linked list. 
"""
class Element(object):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
        self.next = None


"""This code is very similar—we're just establishing that a LinkedList is something that has a head Element, 
which is the first element in the list. If we establish a new LinkedList without a head, it will default to None. 
Great! Let's add a method to our LinkedList to make it a little more useful.
This method will add a new Element to the end of our LinkedList.

Again, this part is really important, so don't rush through it. 
Take the code line-by-line and make sure everything makes sense. 
If the LinkedList already has a head, iterate through the next reference in every Element until you reach the end of the list. 

Set next for the end of the list to be the new_element. Alternatively, if there is no head already, 
you should just assign new_element to it and do nothing else.
"""
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


# Now here's the question 

"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        # seting the input as head otherwise None
        self.head = head 
        
    def append(self, new_element):
        current = self.head
        if self.head: # when self.head is not None
            while current.next:
                current = current.next
            current.next = new_element
        else: # when self.head is  None
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1 
        current = self.head
        if position < 1:
            return None
        while counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1 
        current= self.head 
        if position > 1:
            while counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                counter += 1
                current = current.next
        elif position == 1:
            new_element.next = self.head
            self.head = new_element    
    
    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


# Test cases
# Set up some Elements
# To be clear, it's just element their next is None
# so, e1.next = None
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

"""
# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
"""

# Real Answer
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


# Stacks 