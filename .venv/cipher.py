sentence = str(input("Please enter a sentence. "))
ciphered = ''
deciphered = ''
for char in range(len(sentence)):
    new_value = ord(sentence[char]) + 1
    ciphered += chr(new_value)

print(ciphered)

for char in range(len(ciphered)):
    new_value2 = ord(ciphered[char]) - 1
    deciphered += chr(new_value2)

print(deciphered)