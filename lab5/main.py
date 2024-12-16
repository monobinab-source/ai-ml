from dollar import Dollar
from hash_table import HashTable


def main():
    # Initialize seed data
    data = [
        57.12, 23.44, 87.43, 68.99, 111.22, 44.55, 77.77, 18.36, 543.21, 20.21,
        345.67, 36.18, 48.48, 101.00, 11.00, 21.00, 51.00, 1.00, 251.00, 151.00
    ]

    # Create a hash table
    hash_table = HashTable()

    # Insert seed data into the hash table
    for amount in data:
        dollar = Dollar(amount)
        hash_table.insert(dollar)

    # Print hash table status
    print("Hash Table Status After Seed Data:")
    print(hash_table)
    hash_table.print_table()

    # Search functionality
    while True:
        try:
            amount = float(input("\nEnter a Dollar value to search (e.g., 57.12): "))
            dollar = Dollar(amount)
            index = hash_table.search(dollar)
            if index != -1:
                print(f"Found {dollar} at index {index}.")
            else:
                print("Invalid Data.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        cont = input("Do you want to search again? (yes/no): ").strip().lower()
        if cont != "yes":
            break

    print("\nProgram Ended.")


if __name__ == "__main__":
    main()
