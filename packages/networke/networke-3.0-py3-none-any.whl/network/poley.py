class Node:
    def __init__(self, coef, exp):
        self.coefficient = coef
        self.exponent = exp
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def insert_term(self, coef, exp):
        new_term = Node(coef, exp)
        if not self.head or exp > self.head.exponent:
            new_term.next = self.head
            self.head = new_term
        else:
            current = self.head
            while current.next and exp < current.next.exponent:
                current = current.next
            new_term.next = current.next
            current.next = new_term

    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.exponent}", end=" ")
            if current.next:
                print("+", end=" ")
            current = current.next
        print()

    def combine_like_terms(self):
        current = self.head
        while current and current.next:
            if current.exponent == current.next.exponent:
                current.coefficient += current.next.coefficient
                current.next = current.next.next
            else:
                current = current.next

def add_polynomials(poly1, poly2):
    result = Polynomial()
    current1, current2 = poly1.head, poly2.head
    while current1 or current2:
        coef1 = current1.coefficient if current1 else 0
        exp1 = current1.exponent if current1 else 0
        coef2 = current2.coefficient if current2 else 0
        exp2 = current2.exponent if current2 else 0
        if exp1 == exp2:
            result.insert_term(coef1 + coef2, exp1)
            current1 = current1.next if current1 else None
            current2 = current2.next if current2 else None
        elif exp1 > exp2:
            result.insert_term(coef1, exp1)
            current1 = current1.next if current1 else None
        else:
            result.insert_term(coef2, exp2)
            current2 = current2.next if current2 else None
    result.combine_like_terms()
    return result

def subtract_polynomials(poly1, poly2):
    result = Polynomial()
    current1, current2 = poly1.head, poly2.head
    while current1 or current2:
        coef1 = current1.coefficient if current1 else 0
        exp1 = current1.exponent if current1 else 0
        coef2 = current2.coefficient if current2 else 0
        exp2 = current2.exponent if current2 else 0
        if exp1 == exp2:
            result.insert_term(coef1 - coef2, exp1)
            current1 = current1.next if current1 else None
            current2 = current2.next if current2 else None
        elif exp1 > exp2:
            result.insert_term(coef1, exp1)
            current1 = current1.next if current1 else None
        else:
            result.insert_term(-coef2, exp2)
            current2 = current2.next if current2 else None
    result.combine_like_terms()
    return result

def multiply_polynomials(poly1, poly2):
    result = Polynomial()
    current1 = poly1.head
    while current1:
        current2 = poly2.head
        while current2:
            result.insert_term(current1.coefficient * current2.coefficient,
                               current1.exponent + current2.exponent)
            current2 = current2.next
        current1 = current1.next
    result.combine_like_terms()
    return result

def divide_polynomials(poly1, poly2):
    result = Polynomial()
    current1 = poly1.head
    while current1:
        current2 = poly2.head
        while current2:
            if current2.coefficient != 0:
                result.insert_term(current1.coefficient / current2.coefficient,
                                   current1.exponent - current2.exponent)
            current2 = current2.next
        current1 = current1.next
    result.combine_like_terms()
    return result

def display_menu():
    print("\nMenu:")
    print("1. Add Polynomials")
    print("2. Subtract Polynomials")
    print("3. Multiply Polynomials")
    print("4. Divide Polynomials")
    print("5. Exit")

def operate_on_polynomials(poly1, poly2, operation):
    print("\nFirst Polynomial:")
    poly1.display()
    print("\nSecond Polynomial:")
    poly2.display()
    if operation == 1:
        result = add_polynomials(poly1, poly2)
        print("\nResult of Addition:")
        result.display()
    elif operation == 2:
        result = subtract_polynomials(poly1, poly2)
        print("\nResult of Subtraction:")
        result.display()
    elif operation == 3:
        result = multiply_polynomials(poly1, poly2)
        print("\nResult of Multiplication:")
        result.display()
    elif operation == 4:
        result = divide_polynomials(poly1, poly2)
        print("\nResult of Division:")
        result.display()
    elif operation == 5:
        print("Exiting the program.")
        exit()
    else:
        print("Invalid operation. Please enter a valid option (1-5).")

def input_polynomial():
    poly = Polynomial()
    n = int(input("Enter the number of terms in the polynomial: "))
    for _ in range(n):
        coef = float(input("Enter the coefficient: "))
        exp = int(input("Enter the exponent: "))
        poly.insert_term(coef, exp)
    return poly

if __name__ == "__main__":
    print("\nEnter the first polynomial:")
    poly1 = input_polynomial()
    print("\nEnter the second polynomial:")
    poly2 = input_polynomial()
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-5): "))
        operate_on_polynomials(poly1, poly2, choice)
