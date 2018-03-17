#################
# Honors Project 3 - STACK
#################

class Stack:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self, capacity=2, homepage = None):
        """
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack.
        """
        self._capacity = capacity
        self._data = [0] * self._capacity
        self._size = 0
        self._homepage = homepage
        if homepage is not None:
            self._data[0] = homepage
            self._size += 1

    def __str__(self):
        """
        Prints the elements in the stack from bottom of the stack to top,
        followed by the capacity.
        :return: string
        """
        if self._size == 0:
            return "Empty Stack"

        output = ""
        for website in range(self._size):
            website = self._data[website]
            if type(website) is str:
                output += website + " -> "
        output = output[:-4]

        return "{} \nCapacity: {}".format(output, str(self._capacity))

    ###### COMPLETE THE FUNCTIONS BELOW ######

    # --------------------Accessor Functions---------------------------------
    def get_size(self):
        """
        Checks and returns the size of the stack
        :return: size of the stack
        """
        return self._size

    def is_empty(self):
        """
        Checks if the stack is empty
        :return: Boolean
        """
        if self._size == 0:  # True if size is 0
            return True
        else:
            return False

    def top(self):
        """
        Gets the value at the top of the stack
        :return: Value at the last index of the stack
        """
        if self._size == 0:
            return None
        else:
            return self._data[self._size-1] # Return the top value

    # ---------------------------Mutator Functions------------------------------

    def push(self, addition):
        """
        Adds a value to the stack, grows the stack if necessary
        :param addition: Value to be added to the stack
        :return: Nothing
        """
        # If the capacity has been filled the stack must grow
        if self._size == self._capacity:
            self.grow()
        self._data[self._size] = addition  # Add value to the stack
        self._size += 1  # Increase the size
        return

    def pop(self):
        """
        Removes an element from the top of the stack, min size of 1 if there is a homepage
        :return: Value from the top of the stack
        """
        #  If the stack is empty the item can not be popped
        if self._size == 0:
            return None
        if self._homepage is not None and self._size == 1:
            print("Sup shawty")
            return None

        temp = self._data[self._size - 1]  # saves the last item in stack
        self._data[self._size - 1] = 0  # reassigns popped value index to 0
        self._size -= 1  # decrement the size
        #  If the new size is less than half the capacity, stack is shrunk
        if self._size <= self._capacity//2 and self._capacity > 2:
            self.shrink()
        return temp


    def grow(self):
        """
        Increases the capacity of the stack by a factor of 2
        :return: Nothing
        """
        # Doubles the capacity of the stack
        self._data = self._data + [0] * self._capacity
        self._capacity = self._capacity*2
        return

    def shrink(self):
        """
        Decreases the capacity of the stack by a factor of 2
        :return: Nothing
        """
        # Halves the capacity of the stack
        self._data = self._data[:self._capacity//2]
        self._capacity = self._capacity // 2
        return
    
    def clear_stack(self):
        """
        Pops everything in the stack
        """
        self._data = [0] * 2
        self._capacity = 2
        self._size = 0


    def find(self, element):
        """
        Searches the stack for a particular element
        :param element: the element being looked for
        :return: True if the element is in the stack, false otherwise
        """
        for i in self._data:
            if i == element:
                return True
        return False


def browse_web(back_stack, forward_stack, site_name):
    if back_stack.find(site_name):
        while site_name != back_stack.top():
            backward(back_stack, forward_stack)
        return back_stack
    elif forward_stack.find(site_name):
        while site_name != forward_stack.top():
            forward(back_stack, forward_stack)
        forward(back_stack, forward_stack)
        return forward_stack
    return None


def backward(back_stack, forward_stack):
    if back_stack.is_empty():
        return None
    forward_stack.push(back_stack.pop())

def forward(back_stack, forward_stack):
    if forward_stack.is_empty():
        return None
    back_stack.push(forward_stack.pop())

def visit(back_stack, forward_stack, site):
    if not forward_stack.is_empty():
        forward_stack.clear_stack()
    if type(site) != str:
        print( "Type Error, not a valid website" )
        return
    back_stack.push(site)
