class Queue():
    
    def __init__(self):
        self.items = []
        self.length = 0

    def print(self):
        print(self.items)

    def enqueue(self, item):
        self.items.append(item)
        self.length += 1
    
    def dequeue(self):
        if self.length < 1:
            print('No items in queue to remove')
            return None
        else:
            item_to_remove = self.items[0]
            if self.length == 1:
                self.items = []
            else:
                self.items = self.items[1:]
            self.length -= 1
            return item_to_remove
    
    def get_front(self):
        if self.length < 1:
            return None
        else:
            return self.items[0]
    
    def get_back(self):
        if self.length < 1:
            return None
        else:
            return self.items[-1]
    
    def is_empty(self):
        return self.length == 0

def create_test_queue():
    test_queue = Queue()
    test_queue.enqueue(1)
    test_queue.enqueue(2)
    test_queue.enqueue(3)
    return test_queue

def main():
    test_queue = create_test_queue()
    test_queue.print()
    print(test_queue.length)
    test_queue.enqueue(4)
    test_queue.print()
    print(test_queue.length)

if __name__ == '__main__':
    main()