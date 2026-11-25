filename = input("Enter the filename to read (e.g., sample.txt): ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\n--- File Content ---")
        print(content)
        print("--------------------")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError as e:
    print(f"IO Error: {e}")
