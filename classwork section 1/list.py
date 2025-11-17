# empty = []
# print(empty)
# num = [1, 2, 3 , 4, 5]
# print(num)
# trip =  [1, 2, 3] * 3
# print(trip)
# alist = [100, 200, 300 , 400, 500]
# alist = alist[::-1]
# print(alist)
def match_wor(words):
    ctr = 0
    lst = []
    for word in words:
        print (word[0] , word[-1])
        if len(word) > 1 and word[0] == word[-1]:
            ctr +=1
            lst.append(word)
        print("list of words with first and last  charactar same\n ", lst)
        return ctr
count = match_wor(['aba', 'cdc', 'ntn', 'bob', '606'])
print("the number of word having the first and last charicar bieng the same is ", count)