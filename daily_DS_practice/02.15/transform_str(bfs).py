from collections import deque
import pprint




s = "cat"
t = "dog"
words = ["bat", "cot", "dog", "dag", "dot", "cat"]

def are_neighbors(word1, word2):
    num_diff = 0
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            num_diff += 1
    return num_diff == 1

print(are_neighbors("cat", "cot"))  #T
print(are_neighbors("cat", "cop"))  #F
print(are_neighbors("cat", "dog"))  #F



# Step 1: make a graph of all the words (find all neighbors of each word)
graph = {}
for word in words:
    graph[word] = []

for word1 in words:
    for word2 in words:
        if are_neighbors(word1, word2):
            graph[word1].append(word2)

pp = pprint.PrettyPrinter(indent = 4)
pp.pprint(graph)


# graph = {
#     "bat": ["cat"],
#     "cot": ["dot", "cat"],
#     "dog": ["dag", "dot"],
#     "dag": ["dog"],
#     "dot": ["dog"],
#     "cat": ["cot"]
# }


# Step 2: BFS search for target word, starting from s
def transform_str(s, t, graph):

    q = deque()
    distance = 0

    q.append(["cat", distance])

    while q:
        current = q.popleft()
        cur_word = current[0]
        cur_dist = current[1]
        # print(f"")
        if cur_word == t:
            return cur_dist
        else:
            distance += 1
            neighbors = graph[cur_word]
            for neighbor in neighbors:
                print(f"neighbor: {neighbor}, dist: {distance}")
                q.append([neighbor, distance])

    return -1

print(transform_str(s,t, graph))


