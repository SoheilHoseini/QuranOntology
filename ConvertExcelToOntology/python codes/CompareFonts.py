
from operator import le


first_name = ""
second_name = ""

print(f"len first: {len(first_name)} , len second: {len(second_name)}")

# file = open("resources\\SpecialCharacters.txt", 'w', encoding="utf8")
# file.write(half_space)
# file.close()

if len(first_name) < len(second_name):
    word_length = len(first_name)
else:
    word_length = len(second_name)
    
for i in range(word_length):
    print(i + 1, "first:", first_name[i], "second:", second_name[i])
    if first_name[i] != second_name[i]:
        #print(i + 1, "first:", first_name[i], "second:", second_name[i])
        print(f"Not equality at {i}")
        pass
    
# file = open("resources\\SpecialCharacters.txt", 'r', encoding="utf8")
# half_space = file.read()
# if len(half_space) == 2:
#     half_space = half_space[:1]
#     print("ff")
    
# print(len(half_space))
# print(half_space)  
# file.close()