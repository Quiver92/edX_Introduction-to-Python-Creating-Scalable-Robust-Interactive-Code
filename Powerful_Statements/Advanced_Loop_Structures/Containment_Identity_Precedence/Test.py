sentence = "This is a test sentence"
word1 = "test"
word2 = "something"

# testing if word1 is a substring of sentence
if (word1 in sentence):
    print(word1, "is contained in:", sentence)
else:
    print(word1, "is not contained in:", sentence)
