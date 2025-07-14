class Node:
    def _init_(self, value):
        self.value = value
        self.next = None

class Queue:
    def _init_(self):
        self.front = None
        self.rear = None
        self.size = 0

    def _len_(self):
        return self.size

    def _repr_(self):
        items = []
        current_item = self.front

        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next

        return ', '.join(items)

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is Empty")

        dequeue_value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        return dequeue_value

    def peek(self):
        if self.front is None:
            raise IndexError('Queue is Empty')

        return self.front.value

    def is_Empty(self):
        return self.front is None

if _name_ == '_main_':
    q = Queue()
    q.enqueue(11)
    q.enqueue(22)
    q.enqueue(33)
    q.enqueue(44)
    q.enqueue(55)
    q.enqueue(66)

    print(q)
    print(len(q))

    print(q.dequeue())
    print(q.dequeue())
    print(q)
    print(len(q))