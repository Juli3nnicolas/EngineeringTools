import sys

if len(sys.argv) != 2:
    print("Error, you must provide a size")
    sys.exit(1)

input_size = sys.argv[1]

try:
    input_size = int(input_size)
except ValueError:
    print("Invalid input size - it must a number")
    sys.exit(2)

output_str = 'a' * input_size
print(output_str)
