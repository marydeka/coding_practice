str1 = "P@#yn26at^&i5ve"

char_count = 0
digit_count = 0
symbols = 0

for char in str1:
    if 'A' <= char >= 'Z' or 'a' <= char <= 'z':
        char_count += 1
print(char_count)
