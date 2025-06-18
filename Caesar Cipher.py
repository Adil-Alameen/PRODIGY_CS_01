import string

# Define characters to encrypt: letters, digits, and optional symbols
CHARACTER_SET = string.ascii_letters + string.digits + string.punctuation + ' '

def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char in CHARACTER_SET:
            index = CHARACTER_SET.index(char)
            new_index = (index + shift) % len(CHARACTER_SET)
            result += CHARACTER_SET[new_index]
        else:
            result += char  # Keep unknown characters unchanged
    return result

def brute_force_decrypt(text):
    print("\n🔍 Brute Force Results:")
    for shift in range(len(CHARACTER_SET)):
        decrypted = caesar_cipher(text, shift, mode='decrypt')
        print(f"Shift {shift}: {decrypted}")

def main():
    print("=== Caesar Cipher Advanced ===")
    choice = input("Choose mode (e=encrypt, d=decrypt, b=brute): ").lower()

    if choice == 'b':
        message = input("Enter the encrypted message: ")
        brute_force_decrypt(message)
    else:
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value (integer): "))
        except ValueError:
            print("❌ Invalid shift. Please enter an integer.")
            return

        if choice == 'e':
            encrypted = caesar_cipher(message, shift)
            print("✅ Encrypted message:", encrypted)
        elif choice == 'd':
            decrypted = caesar_cipher(message, shift, mode='decrypt')
            print("🔓 Decrypted message:", decrypted)
        else:
            print("❌ Invalid mode selected.")

if __name__ == "__main__":
    main()
