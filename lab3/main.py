from singly_linked_list import SinglyLinkedList
from queue import Queue
from stack import Stack
from currency_calculator import Currency



def main():
    print("Welcome to the ADT Demonstration Program!")
    print("Developed by: Monobina Saha & Haoyun Luo\n")
    print("This program will demonstrate SinglyLinkedList, Stack, and Queue functionalities.\n")

    # ------------------- Create 20 Currency Objects ------------------- #
    dollar_values = [
        57.12, 23.44, 87.43, 68.99, 111.22,
        44.55, 77.77, 18.36, 543.21, 20.21,
        345.67, 36.18, 48.48, 101.00, 11.00,
        21.00, 51.00, 1.00, 251.00, 151.00
    ]
    currencies = [Currency("USD", value) for value in dollar_values]

    # ------------------- SinglyLinkedList Demonstration ------------------- #
    print("\nDemonstrating SinglyLinkedList...")
    linked_list = SinglyLinkedList()

    print("Adding first 7 objects in reverse order to the linked list.")
    SinglyLinkedList.print_list(linked_list)

    for i in range(6, -1, -1):
        linked_list.add_currency(currencies[i], 0)  # Insert at index 0 to reverse the order

    print("\nSearching for $87.43 and $44.56:")
    print("Search result for $87.43:", linked_list.find_currency(Currency("USD", 87.43)))
    print("Search result for $44.56:", linked_list.find_currency(Currency("USD", 44.56)))

    print("\nRemoving node containing $111.22 and node at index 2.")
    linked_list.remove_currency(Currency("USD", 111.22))
    linked_list.remove_currency_by_index(2)

    print("\nCurrent List:")
    print(linked_list)

    print("\nAdding next 4 objects (#9 to #12) to the list at calculated indexes.")
    for i in range(8, 12):
        index = i % 5
        linked_list.add_currency(currencies[i], index)

    print("\nRemoving objects at indexes (countCurrency % 6) and (countCurrency / 7).")
    linked_list.remove_currency_by_index(linked_list.get_count() % 6)
    linked_list.remove_currency_by_index(linked_list.get_count() // 7)

    print("\nCurrent List:")
    print(linked_list)

    # ------------------- Stack Demonstration ------------------- #
    print("\n\nDemonstrating Stack...")
    stack = Stack()

    print("Pushing 7 objects starting from index 13 onto the stack.")
    for i in range(13, 20):
        stack.push(currencies[i])

    print("\nPeeking at the top of the stack:")
    print(stack.peek())

    print("\nPerforming 3 pops in succession.")
    for _ in range(3):
        print(f"Popped: {stack.pop()}")

    print("\nCurrent Stack:")
    print(stack.print_stack())

    print("\nPushing 5 objects from the start of the array onto the stack.")
    for i in range(5):
        stack.push(currencies[i])

    print("\nPopping twice in succession.")
    for _ in range(2):
        print(f"Popped: {stack.pop()}")

    print("\nCurrent Stack:")
    print(stack.print_stack())

    # ------------------- Queue Demonstration ------------------- #
    print("\n\nDemonstrating Queue...")
    queue = Queue()

    print("Enqueuing 7 objects at odd indexes starting from index 5.")
    for i in range(5, 20, 2):
        queue.enqueue(currencies[i])

    print("\nPeeking at the front and rear of the queue:")
    print("Front:", queue.peek_front())
    print("Rear:", queue.peek_rear())

    print("\nPerforming 2 dequeues in succession.")
    for _ in range(2):
        print(f"Dequeued: {queue.dequeue()}")

    print("\nCurrent Queue:")
    print(queue.print_queue())

    print("\nEnqueuing 5 more objects starting from index 10.")
    for i in range(10, 15):
        queue.enqueue(currencies[i])

    print("\nDequeuing 3 times in succession.")
    for _ in range(3):
        print(f"Dequeued: {queue.dequeue()}")

    print("\nCurrent Queue:")
    print(queue.print_queue())

    print("\n\nThank you for using this ADT demonstration! Goodbye!")


if __name__ == "__main__":
    main()