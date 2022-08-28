
from operator import le


first_name = "عمره_مفرده"
second_name = "عمره_‌مفرده"

print(f"len first: {len(first_name)} , len second: {len(second_name)}")
half_space = second_name[5]
print(len(half_space))
file = open("resources\\SpecialCharacters.txt", 'w', encoding="utf8")
file.write(half_space)
file.close()
for i in range(len(first_name)):
    print(i + 1, "first:", first_name[i], "second:", second_name[i])
    if first_name[i] != second_name[i]:
        #print(i + 1, "first:", first_name[i], "second:", second_name[i])
        pass
    
file = open("resources\\SpecialCharacters.txt", 'r', encoding="utf8")
half_space = file.read()
if len(half_space) == 2:
    half_space = half_space[:1]
    print("ff")
    
print(len(half_space))
print(half_space)  
file.close()