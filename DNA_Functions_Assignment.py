# DNA_Functions_Assignment.py

# Task 1: A simple function
def print_name_and_major():
    print("Your Name: Ayeh Khorshidian")
    print("Your Major: Individualized Genomics and Health")

# Task 2: Argument receiving function
def gc_content(dna_sequence):
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    total_length = len(dna_sequence)
    if total_length == 0:
        gc_content_value = 0
    else:
        gc_content_value = ((g_count + c_count) / total_length) * 100
    print(f"GC Content: {gc_content_value:.2f}%")

# Task 3: Functions that return a value
def timesTen(number):
    return number * 10

# Task 4: Multiple arguments
def average_of_three(num1, num2, num3):
    return (num1 + num2 + num3) / 3

def main():
    # Task 1
    print_name_and_major()

    # Task 2
    dna_seq = "GATTACA"
    gc_content(dna_seq)

    # Task 3
    result = timesTen(5)
    print(f"Result of timesTen(5): {result}")

    # Task 4
    avg = average_of_three(3, 7, 10)
    print(f"Average of 3, 7, and 10: {avg}")

if __name__ == "__main__":
    main()

