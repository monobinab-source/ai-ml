from MinHeap import MinHeap
from dollar import Dollar

"""
Author: Monobina Saha
CIS 22C Lab 6
"""
def main():
    """
    pre: dollar amounts are inserted in heap in 2 phases
    post: 4 traversals printed in console and in output file
    return:
    """
    # Initialize MinHeap
    heap = MinHeap()

    # Data to insert
    data = [
        57.12, 23.44, 87.43, 68.99, 111.22, 44.55, 77.77, 18.36, 543.21, 20.21,
        345.67, 36.18, 48.48, 101.00, 11.00, 21.00, 51.00, 1.00, 251.00, 151.00
    ]
    dollar_objects = [Dollar(amount) for amount in data]
    output_file = open("output.txt", "w")
    # Insert first 10 Dollar objects
    for i, dollar in enumerate(dollar_objects[:10], start=1):
        heap.insert(dollar)
        if i == 10:
            print(f"Traversals after inserting the 10th Dollar (${dollar.value():.2f}):\n")
            output_file.write(f"Traversals after inserting the 10th Dollar (${dollar.value():.2f}):\n")
            perform_traversals(heap,output_file)

    # Insert remaining Dollar objects
    for i, dollar in enumerate(dollar_objects[10:], start=11):
        heap.insert(dollar)
        if i == 20:
            print(f"\nTraversals after inserting the last Dollar (${dollar.value():.2f}):\n")
            output_file.write(f"\nTraversals after inserting the last Dollar (${dollar.value():.2f}):\n")
            perform_traversals(heap,output_file)


def perform_traversals(heap, output_file):
    """
    Perform all 4 traversals and print the results.
    pre: heap is The MinHeap instance and the output file
    post: 4 traversals are written.
    return:
    """

    print("In-Order Traversal:", heap.in_order())
    output_file.write("In-Order Traversal:")
    output_file.write(str(heap.in_order()))
    output_file.write("\n")

    print("Pre-Order Traversal:", heap.pre_order())
    output_file.write("Pre-Order Traversal:")
    output_file.write(str(heap.pre_order()))
    output_file.write("\n")

    print("Post-Order Traversal:", heap.post_order())
    output_file.write("Post-Order Traversal:")
    output_file.write(str(heap.post_order()))
    output_file.write("\n")

    print("Breadth-First Traversal:", heap.breadth_first())
    output_file.write("Breadth-First Traversal:")
    output_file.write(str(heap.breadth_first()))
    output_file.write("\n")

if __name__ == "__main__":
    main()
