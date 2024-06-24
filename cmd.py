import sys

if len(sys.argv) < 2:
    print("This is the name.")
else:
    name = sys.argv[1]
    print(f"This is the {name}")