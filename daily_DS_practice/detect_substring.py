#TEST CASE 1    should return 2
# txt = "cacat"
# subStr = "cat"

#TEST CASE 2     should return 6
# txt = "thepigflewwow"
# subStr = "flew"

#TEST CASE 3    should return 0
# txt = "twocanplay"
# subStr = "two"

#TEST CASE 3    should return -1
txt = "wherearemyshorts"
subStr = "pork"



def detectSubstring(txt, subStr):
  str_ptr = 0
  substr_ptr = 0
  index = -1
  
  while str_ptr < len(txt):
    # print("entered outside for loop")
    if txt[str_ptr] == subStr[substr_ptr]:
      # print(substr_ptr)
      index = str_ptr
      # print(index)
      while substr_ptr < len(subStr):
        # print(f"str ptr: {str_ptr}")
        # print(f"substr ptr: {substr_ptr}")
        str_ptr += 1
        substr_ptr += 1
        if txt[str_ptr] != subStr[substr_ptr]:
          substr_ptr = 0
          index = -1
          break
        elif txt[str_ptr] == subStr[substr_ptr] and substr_ptr == (len(subStr) - 1):
          return index
    else:
      str_ptr += 1
  
  return index

print(detectSubstring(txt, subStr))