class Stack():
    def __init__(self):
        self.item = []
    def empty(self):
        return len(self.item) == 0
    def push(self,item):
        self.item.append(item)
    def pop(self):
        if not self.empty():
            return self.item.pop()
        else:
            print("Cannot Pop from empty Stack")
    def peek(self):
        if not self.empty():
            return self.item[-1]
        else:
            print("Cannot Peek in empty stack")
    def display(self):
        print("Stack:",self.item)
def main():
    s = Stack()
    print("\n Menu")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    while True:
        choice = int(input("Enter the choice:"))
        if choice == 1:
            item = int(input("Enter the item to push:"))
            s.push(item)
            s.display()
        elif choice == 2:
            pop_i = s.pop()
            if pop_i is not None:
                print("Popped Item:",pop_i)
                s.display()
            else:
                print("Stack is Empty")
        elif choice == 3:
            pp = s.peek()
            if pp is not None:
                print("Peek Element:",pp)
            else:
                print("Not peek an empty stack")
        elif choice ==4:
            s.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice")
if __name__== "__main__":
    main()
