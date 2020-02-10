''' Given a string and a set of characters, find the length of the smallest
substring that contains all those characters
'''

s = "twcpblmabccabasdcbasaasbacccbajkhca"
targets = ['a', 'b', 'c']


head = 0
tail = 0
n = len(s)

counts = {}
for c in targets:
  counts[c] = 0

print(n)



while head < n:

  if s[head] in targets:
    counts[s[head]] += 1

  head += 1

  if min(counts.values()) > 0:

    while min(counts.values()) > 0:
      if s[tail] in targets:
        counts[s[tail]] -= 1
      tail += 1

    print(s[tail - 1: head])

# moving_head = True


# while True:
#   print("h: {}, t:{}".format(head, tail))

#   # add the head character
#   if head < n:
#     if s[head] in targets:
#       counts[s[head]] += 1

#   print(" --" + str(counts))
#   # not there yet
#   if min(counts.values()) < 1 and head < n:
#     print("incrementing head")
#     head += 1
#   else:
#     print("entering tail")
#     while True:
#       print(" h: {}, t:{}".format(head, tail))
#       # print ("  " + s[tail])
#       # print("--" + str(counts))
#       tail += 1
#       if s[tail - 1] in targets:
#         counts[s[tail - 1]] -= 1

#       print("   --" + str(counts))


#       if min(counts.values()) < 1:
#         # print(" breaking at {}, {}".format(s[head], s[tail]))
#         print("breaking: {}, {}".format(head, tail))
#         head += 1
#         print("********len: {},  {}".format(head, tail, s[tail - 1: head + 1]))

#         break

#     # if min(counts.values()) > 0:

#     if tail >= n:
#       break
