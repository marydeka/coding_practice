def make_anagram(str1, str2):


    #make both strings lowercase

    str1_lower = str1.lower()
    str2_lower = str2.lower()

    arr1 = [0] * 26 
    arr2 = [0] * 26

    for char in str1_lower:
        idx = ord(char) - ord('a')
        arr1[idx] += 1

    for char in str2_lower:
        idx = ord(char) - ord('a')
        arr2[idx] += 1

    num_chars_to_drop = 0

    for idx in range(len(arr1)):
        if arr2[idx] > arr1[idx]:
            return -1
        num_chars_to_drop += (arr1[idx] - arr2[idx])
    return num_chars_to_drop



str1 = "abcdeffabbbaz"
str2 = "abcdef"
print(make_anagram(str1, str2))