#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print(sys.argv)
    num_arg = len(sys.argv) -1
if num_arg == 0:
    print(f"Number of arguments {num_arg}")
elif num_arg == 1:
    print(f"Number of arguments {num_arg}")
else:
    print(f"Number of arguments {num_arg}")

for i in range(1, len(sys.argv)):
    print(f"{i}: {sys.argv[i]}")

