class Queue:
    def __init__(self):
        self.items =[]
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self,item):
        if len(self.items) == size:
            print("Queue is Full")
        else:
            self.items.append(item)
            print("Item",item,"enqueued to Queue")
    def is_full(self):
        if len(self.items) == size:
            print("Queue is full")
        else:
            print("Queue is not full")
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None
    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Queue is empty")
            return None
    def size(self):
        return len(self.items)
    def display(self):
        if not self.is_empty():
            print("Queue :",self.items)
        else:
            print("Queue is empty")

print("\n\t Basic operations of Queue")
print("\t********************************\n")
size = int(input("Enter the size of Queue:"))
def main():
    q = Queue()
    while True:
        print("\n1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Rear")
        print("5. IsEmpty")
        print("6. IsNull")
        print("7. Size")
        print("8. Display")
        print("9. Exit\n")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            item = input("Enter the item to Enqueue:")
            q.enqueue(item)
        elif choice == 2:
            item = q.dequeue()
            if item is not None:
                print("Dequeue Item:",item)
        elif choice == 3:
            item = q.front()
            if item is not None:
                print("Front element of Queue:",item)
        elif choice == 4:
            item = q.rear()
            if item is not None:
                print("Last Element of Queue:",item)
        elif choice == 5:
            if q.is_empty():
                print("Queue is Empty")
            else:
                print("Queue is Not Empty")
        elif choice == 6:
            if q.is_full():
                print("Queue is Full")
        elif choice == 7:
            print("Size of Queue:",q.size())
        elif choice == 8:
            q.display()
        elif choice == 9:
            print("Exiting the program")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
            
        
