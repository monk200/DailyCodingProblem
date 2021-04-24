"""
Daily Coding Problem #11

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries
"""


import time
from pynput import keyboard


# Creates a dictionary where each combo of letters that potentially spells something in the given dictionary has a key that is a list of the possible complete word(s)
def preprocess(dictionary):
    d = {}
    for word in dictionary:
        for index in range(len(word)):
            prefix = word[0: index+1]
            if prefix in d:
                curr = d.get(prefix)
                curr.append(word)
                d[prefix] = curr
            else:
                d[prefix] = [word]
    return d


# Returns a list of potential words given the incomplete input string s, or returns an empty list if word is not found
def autocomplete(s, d):
    if s in d:
        return d[s]
    else:
        return []


text = ""
d = {}
def on_press(key):
    global text
    # Stop listener
    if (key == keyboard.Key.esc) or (key == keyboard.Key.enter):
        return False
    # Allows user to backspace
    if key == keyboard.Key.backspace:
        text = text[:-1]
    else:
        text += key.char

    print("\nINPUT: ", text)
    print("Did you mean", autocomplete(text, d), "?")


# Allows user to type their input in the console and get live updates on their autocomplete query
def realtimeAutocomplete(dic=None):
    # Prompt user to type dictionary if one is not passed to the function
    if dic is None:
        print("Enter given dictionary in the format shown below: ")
        print("dog, dear, deal")
        string = input()
        dic = string.split(", ")

    # Preprocess dictionary
    global d
    startTime = time.time()
    print("Processing given dictionary...")
    d = preprocess(dic)
    totalTime = time.time()-startTime
    time.sleep(0.5)       # Added a delay so that the enter from entering the dictionary doesn't close the program
    print("Dictionary processed in ", totalTime, " seconds")

    # Collect events until released
    print("Type your query now, the program will stop when you press Enter or Esc")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()



# Manual test
#dic = preprocess(["dog", "dear", "deal"])
#print(autocomplete("de", dic))

# Test with realtime input through console
#realtimeAutocomplete(["dog", "dear", "deal"])
realtimeAutocomplete()

