# Iterative Method
def fibonacci_iterative(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Recursive Method
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Main Program
def main():
    print("Fibonacci Sequence Generator")
    print("1. Iterative Method")
    print("2. Recursive Method")
    choice = input("Choose method (1 or 2): ")

    n = int(input("Enter the number of terms: "))

    if choice == '1':
        result = fibonacci_iterative(n)
        print("Fibonacci Sequence (Iterative):")
        print(result)

    elif choice == '2':
        print("Fibonacci Sequence (Recursive):")
        for i in range(n):
            print(fibonacci_recursive(i), end=" ")
        print()
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the program
if __name__ == "__main__":
    main()