string = "The dog is the best"
string1 = "'Happy thanksgiving, I am so full"

def find_duplicates(s):
    #split string into list of words and make all lowercase
    words = s.split(" ")
    words = [word.lower() for word in words]
    word_dict = {}
    repeated_words = []

    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    # print(word_dict)

    for word in word_dict.keys():
        if word_dict[word] > 1:
            repeated_words.append(word)
    return repeated_words

#TEST 1     should print ['the']
print(find_duplicates(string))

#TEST 2     should print []
print(find_duplicates(string1))