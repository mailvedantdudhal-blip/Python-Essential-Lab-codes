coded_message = input("Enter the main coded sentence: ")
secret_message = input("Enter the secret message to find: ")

if secret_message.lower() in coded_message.lower():
    pos = coded_message.lower().find(secret_message.lower())
    print(f"\nResult: Secret message FOUND at index position {pos}!")
    snippet = coded_message[pos:pos + len(secret_message) + 5]
    print(f"Extracted Snippet: '{snippet}'")
else:
    print("\nResult: Secret message NOT FOUND in the coded sentence.")
