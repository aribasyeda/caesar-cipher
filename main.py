from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(cipher_direction, start_text, shift_amount):

    end_text = []
    for char in start_text:

      if char in alphabet:
        index = alphabet.index(char)
          
        if direction == "encode": 
          new_index = (index + shift_amount) % len(alphabet)
        elif direction == "decode":
          new_index = (index - shift_amount) % len(alphabet)
        
        end_text.append(alphabet[new_index])

        end_text.append(char) 

    print(f"\n✨  Here's the {cipher_direction}d result: {''.join(end_text)} ✨\n")


# Usage
should_continue = True

while should_continue:
  
  direction = input("👉 Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("👉 Type your message:\n").lower()
  shift = int(input("👉 Type the shift number:\n"))

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  user_choice = input("🎩 Type 'yes' if you want to go again. Otherwies type 'no': \n").lower()
    
  if user_choice == "no":
    should_continue = False
    print("\n Goodbye 👋 ")
