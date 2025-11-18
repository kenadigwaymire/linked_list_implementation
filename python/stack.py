class Stack():

    def __init__(self):
        self.list = []
        self.length = 0

    def push(self, item):
        self.list = [item] + self.list
        self.length += 1
    
    def pop(self):
        if self.length < 1:
            print('No items to pop')
            return None
        else:
            item_to_pop = self.list[0]
            if self.length < 2:
                self.list = []
            else:
                self.list = self.list[1:]
            self.length -= 1
            return item_to_pop

    def top(self):
        if self.length > 0:
            return self.list[0]
        else:
            print('No item at top of list')
            return None
    
    def is_empty(self):
        return self.length == 0
    
    def print(self):
        print(self.list)
    
def create_test_stack():
    test_stack = Stack()
    test_stack.push(3)
    test_stack.push(2)
    test_stack.push(1)
    return test_stack

def main():
    test_stack = create_test_stack()
    test_stack.print()
    test_stack.pop()
    test_stack.print()


if __name__ == '__main__':
    main()

