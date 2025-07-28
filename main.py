from security_tasks import check_password_strength
from gpt_helper import ask_gpt
from base64_tool import encode_string, decode_string

def print_menu():
    print("\n🛡️  AI Security Assistant")
    print("1. Check password strength")
    print("2. Explain a security concept with GPT")
    print("3. Base64 Encode/Decode a string")
    print("4. Exit")

def main():
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            password = input("Enter a password to check: ")
            result = check_password_strength(password)
            print(f"\n[RESULT] {result}")

        elif choice == "2":
            topic = input("What security concept do you want explained? ")
            print("\n[GPT EXPLAINS]:")
            print(ask_gpt(topic))

        elif choice == "3":
            action = input("Type 'e' to encode or 'd' to decode: ").strip().lower()
            data = input("Enter your string: ")
            if action == 'e':
                result = encode_string(data)
                print(f"\n[ENCODED]: {result}")
            elif action == 'd':
                result = decode_string(data)
                print(f"\n[DECODED]: {result}")
            else:
                print("Invalid action. Please try again.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

