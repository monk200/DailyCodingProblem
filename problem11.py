"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries
"""


def preprocess(dictionary):
    d = {}
    for word in dictionary:
        for index in range(len(word)):
            print(index)
            prefix = word[0, index+1]
            if prefix in d:
                curr = d.get(prefix)
                curr.append(word)
                d[prefix] - curr
            else:
                d[prefix] = [word]
    return d


def autocomplete(s, d):
    return d[s].values


d = preprocess(["dog", "dear", "deal"])
print(autocomplete("de", d))

