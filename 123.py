class node:
    def _init_(self, data):
        self.data = data
        self.nextNode = None

class linkedList:
    def _init_(self):
        self.head = None

    def inserta(self, new_data):
        new_node = node(new_data)
        new_node.nextNode = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")

            temp =temp.nextNode
        print()
    def end(self, new_data):
        new_node = node(new_data)

        if self.head is None:
            self.head = new_node
            return None

        last = self.head


        while last.nextNode:
            last = last.nextNode
        last.nextNode = new_node
if _name_ =='_main_':
    llist = linkedList()
    llist.inserta("Fox")
    llist.inserta("Brown")
    llist.inserta("Quick")
    llist.inserta("The")

    llist.printList()

    llist.end("Jumps")
    llist.end("Over")
    llist.end("The")
    llist.end("Fence")

    llist.printList()