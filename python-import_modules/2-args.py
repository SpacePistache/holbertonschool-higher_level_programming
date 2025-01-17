#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print(sys.argv)
    num_arg = len(sys.argv) -1
if num_arg == 0:
    print(f"Number of argument(s) {num_arg} arguments:")
elif num_arg == 1:
    print(f"Number of argument(s) {num_arg} arguments:")
else:
    print(f"Number of argument(s): {num_arg} arguments:")

for i in range(1, len(sys.argv)):
    print(f"{i}: {sys.argv[i]}")

