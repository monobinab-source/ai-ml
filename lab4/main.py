from dollar import Dollar
from bst_node import BSTNode
from binary_search_tree import BinarySearchTree

def write_and_print(message, output_file):
    """Utility function to write a message to the output file and print it."""
    print(message)
    output_file.write(message + "\n")

def print_and_write_traversals(bst, output_file):
    """
    Print traversals to stdout and write them to the output file.
    :param bst: The BinarySearchTree instance.
    :param output_file: The output file object.
    """
    traversals = [
        ("Breadth-First Traversal:", bst.breadth_first()),
        ("In-Order Traversal:", bst.in_order()),
        ("Pre-Order Traversal:", bst.pre_order()),
        ("Post-Order Traversal:", bst.post_order())
    ]
    for title, traversal in traversals:
        write_and_print(title, output_file)
        for value in traversal:
            write_and_print(f"  {value}", output_file)
        write_and_print("", output_file)  # Blank line for separation

def main():
    """
    purpose: this is the driver program. You can input a list of Dollar objects and the program can return 4 types of BST traversals on screen and write in output file.
    You can also delete, insert and search for Dollar objects. The input options will come on the screen when you run main.py.
    E.g. you select your option and can input 2.00 to insert, delete or search
    Program developed by Monobina Saha and Haoyun Luo
    :return:
    """
    # Initialize BST
    bst = BinarySearchTree()
    data = [
        57.12, 23.44, 87.43, 68.99, 111.22, 44.55, 77.77, 18.36, 543.21, 20.21,
        345.67, 36.18, 48.48, 101.00, 11.00, 21.00, 51.00, 1.00, 251.00, 151.00
    ]

    # Insert data into BST
    for amount in data:
        bst.insert(Dollar(amount))

    # Open output file
    with open("output.txt", "w") as output_file:
        write_and_print("Initial Traversals:", output_file)
        print_and_write_traversals(bst, output_file)

        # Interactive menu
        while True:
            print("\nMenu:")
            print("1. Add a Dollar")
            print("2. Search for a Dollar")
            print("3. Delete a Dollar")
            print("4. Print Traversals")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    amount = float(input("Enter Dollar value (e.g., 57.12): "))
                    new_dollar = Dollar(amount)
                    if bst.search(amount):
                        write_and_print(f"Value ${amount} already exists in the tree.", output_file)
                    else:
                        bst.insert(new_dollar)
                        write_and_print(f"Inserted: {new_dollar}", output_file)
                except ValueError:
                    write_and_print("Invalid input. Please enter a valid number.", output_file)

            elif choice == "2":
                try:
                    amount = float(input("Enter Dollar value to search (e.g., 57.12): "))
                    result = bst.search(amount)
                    if result:
                        write_and_print(f"Found: {result.data}", output_file)
                    else:
                        write_and_print(f"${amount} not found in the tree.", output_file)
                except ValueError:
                    write_and_print("Invalid input. Please enter a valid number.", output_file)

            elif choice == "3":
                try:
                    amount = float(input("Enter Dollar value to delete (e.g., 57.12): "))
                    if bst.search(amount):
                        bst.delete(amount)
                        write_and_print(f"Deleted: ${amount}", output_file)
                    else:
                        write_and_print(f"${amount} not found in the tree.", output_file)
                except ValueError:
                    write_and_print("Invalid input. Please enter a valid number.", output_file)

            elif choice == "4":
                write_and_print("Current Traversals:", output_file)
                print_and_write_traversals(bst, output_file)

            elif choice == "5":
                write_and_print("Exiting the program.", output_file)
                break
            else:
                write_and_print("Invalid choice. Please select a valid option.", output_file)

if __name__ == "__main__":
    main()


# def main():
#     # Initialize BST
#     bst = BinarySearchTree()
#     data = [
#         57.12, 23.44, 87.43, 68.99, 111.22, 44.55, 77.77, 18.36, 543.21, 20.21,
#         345.67, 36.18, 48.48, 101.00, 11.00, 21.00, 51.00, 1.00, 251.00, 151.00
#     ]
#
#     # Insert data into BST
#     for amount in data:
#         bst.insert(Dollar(amount))
#
#     # Output file setup
#     output_file = open("output.txt", "w")
#
#     # Perform traversals and write to screen/file
#     traversals = {
#         "Breadth-First": bst.breadth_first(),
#         "In-Order": bst.in_order(),
#         "Pre-Order": bst.pre_order(),
#         "Post-Order": bst.post_order(),
#     }
#
#     for name, result in traversals.items():
#         output = f"{name} Traversal: {result}"
#         print(output)
#         output_file.write(output + "\n")
#
#     # Interactive menu
#     while True:
#         print("\nMenu:")
#         print("1. Add a Dollar")
#         print("2. Search for a Dollar")
#         print("3. Delete a Dollar")
#         print("4. Print Traversals")
#         print("5. Exit")
#         choice = input("Enter your choice: ")
#
#         if choice == "1":
#             try:
#                 amount = float(input("Enter Dollar value (e.g., 57.12): "))
#                 if amount < 0:
#                     raise ValueError("Dollar amount must be non-negative.")
#                 new_dollar = Dollar(amount)
#                 bst.insert(new_dollar)
#                 print(f"Inserted: {new_dollar}")
#             except ValueError as e:
#                 print(f"Invalid input: {e}")
#                 output_file.write(f"Invalid input: {e}\n")
#
#         elif choice == "2":
#             try:
#                 amount = float(input("Enter Dollar value to search (e.g., 57.12): "))
#                 result = bst.search(amount)
#                 if result:
#                     print(f"Found: {result.data}")
#                 else:
#                     print(f"${amount} not found in the tree.")
#             except ValueError:
#                 print("Invalid input")
#                 output_file.write("Invalid input\n")
#
#         elif choice == "3":
#             try:
#                 amount = float(input("Enter Dollar value to delete (e.g., 57.12): "))
#                 bst.delete(amount)
#                 print(f"Deleted: ${amount}")
#             except ValueError:
#                 print("Invalid input")
#                 output_file.write("Invalid input\n")
#
#         elif choice == "4":
#             for name, result in traversals.items():
#                 output = f"{name} Traversal: {result}"
#                 print(output)
#                 output_file.write(output + "\n")
#
#         elif choice == "5":
#             break
#         else:
#             print("Invalid choice")
#             output_file.write("Invalid choice\n")
#
#     output_file.close()
#
# if __name__ == "__main__":
#     main()


# def write_and_print_traversals(bst, output_file):
#     """
#     Print traversals to stdout and write them to the output file.
#
#     :param bst: The BinarySearchTree instance.
#     :param output_file: The output file object.
#     """
#     traversal_messages = [
#         ("Breadth-First Traversal:", bst.breadth_first),
#         ("In-Order Traversal:", bst.in_order),
#         ("Pre-Order Traversal:", bst.pre_order),
#         ("Post-Order Traversal:", bst.post_order),
#     ]
#
#     for title, traversal_method in traversal_messages:
#         print(title)
#         output_file.write(title + "\n")
#         traversal_results = traversal_method()
#         for value in traversal_results:
#             print(value)
#             output_file.write(f"{value}\n")
#         print()
#         output_file.write("\n")
#
# def main():
#     # Create a BinarySearchTree instance
#     bst = BinarySearchTree()
#
#     # Open the output file
#     output_file = open("output.txt", "w")
#
#     # List of Dollar objects to insert
#     dollar_values = [
#         57.12, 23.44, 87.43, 68.99, 111.22, 44.55, 77.77, 18.36, 543.21,
#         20.21, 345.67, 36.18, 48.48, 101.00, 11.00, 21.00, 51.00, 1.00, 251.00, 151.00
#     ]
#
#     # Insert Dollar objects into the BST
#     for value in dollar_values:
#         dollar_obj = Dollar(value)
#         bst.insert(dollar_obj)
#
#     # Write initial traversals to file
#     output_file.write("Initial Traversals:\n")
#     print("Initial Traversals:")
#     write_and_print_traversals(bst, output_file)
#
#     # Interactivity for adding, searching, and deleting nodes
#     while True:
#         print("\nOptions:")
#         print("1. Add a Dollar value")
#         print("2. Search for a Dollar value")
#         print("3. Delete a Dollar value")
#         print("4. Print Traversals")
#         print("5. Exit")
#         choice = input("Enter your choice (1-5): ")
#
#         if choice == "1":
#             try:
#                 value = float(input("Enter a Dollar value to add: "))
#                 if bst.search(value):
#                     message = f"Value ${value} already exists in the tree."
#                 else:
#                     bst.insert(Dollar(value))
#                     message = f"Value ${value} added to the tree."
#                 print(message)
#                 output_file.write(message + "\n")
#             except ValueError:
#                 message = "Invalid input. Please enter a valid number."
#                 print(message)
#                 output_file.write(message + "\n")
#
#         elif choice == "2":
#             try:
#                 value = float(input("Enter a Dollar value to search: "))
#                 node = bst.search(value)
#                 if node:
#                     message = f"Value ${value} found in the tree."
#                 else:
#                     message = f"Value ${value} not found in the tree."
#                 print(message)
#                 output_file.write(message + "\n")
#             except ValueError:
#                 message = "Invalid input. Please enter a valid number."
#                 print(message)
#                 output_file.write(message + "\n")
#
#         elif choice == "3":
#             try:
#                 value = float(input("Enter a Dollar value to delete: "))
#                 if bst.search(value):
#                     bst.delete(value)
#                     message = f"Value ${value} deleted from the tree."
#                 else:
#                     message = f"Value ${value} not found in the tree."
#                 print(message)
#                 output_file.write(message + "\n")
#             except ValueError:
#                 message = "Invalid input. Please enter a valid number."
#                 print(message)
#                 output_file.write(message + "\n")
#
#         elif choice == "4":
#             message = "Current Traversals:"
#             print(message)
#             output_file.write(message + "\n")
#             write_and_print_traversals(bst, output_file)
#
#         elif choice == "5":
#             message = "Exiting the program."
#             print(message)
#             output_file.write(message + "\n")
#             break
#
#         else:
#             message = "Invalid choice. Please select a valid option."
#             print(message)
#             output_file.write(message + "\n")
#
#     # Close the output file
#     output_file.close()
#
#
#
#
#
# if __name__ == "__main__":
#     main()