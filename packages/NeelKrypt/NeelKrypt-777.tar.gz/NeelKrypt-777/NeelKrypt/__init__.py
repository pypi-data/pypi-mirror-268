def manna():
    print("DEVELOPED BY NEELANJAN MANNA\n")
    print("JUST OUT OF THE BOX MATHEMATICAL BENGALI THINKING SPEAKING TO THE BARE METAL")
    p_sentence = input("Enter a sentence for public modulus (p): ")
    g_sentence = input("Enter a sentence for public primitive root (g): ")
    x_you_sentence = input("Enter a sentence for your private key: ")
    p = int.from_bytes(p_sentence.encode(), byteorder='big')
    g = int.from_bytes(g_sentence.encode(), byteorder='big')
    x_you = int.from_bytes(x_you_sentence.encode(), byteorder='big')
    y_you = pow(g, x_you, p)
    print(f"Your Public Key (y_you) is: {y_you}")
    y_other = int(input("Enter the other user's public key (y_other): "))
    k_you = pow(y_other, x_you, p)
    print(f"Your Secret Key (k_you) is: {k_you}")
    choice = input("Enter 'e' for encryption or 'd' for decryption: ")
    if choice == 'e':
        text = input("Enter the text to encrypt: ")
        encrypted_text = ""
        for i, char in enumerate(text):
            encrypted_text += chr(ord(char) ^ int(str(k_you)[i % len(str(k_you))]))
        print(f"Encrypted text:\n{encrypted_text}")
    elif choice == 'd':
        encrypted_text = input("Enter the text to decrypt: ")
        decrypted_text = ""
        for i, char in enumerate(encrypted_text):
            decrypted_text += chr(ord(char) ^ int(str(k_you)[i % len(str(k_you))]))
        print(f"Decrypted text:\n{decrypted_text}")
    else:
        print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")
