# Напишите функцию, которая находит самое длинное слово в строке.

# Пример 1:
# sentence1 = "The quick brown fox jumped over the lazy dog"
# print(longest_word(sentence1))  # "jumped"

# Пример 2:
# sentence2 = "Python programming is fun"
# print(longest_word(sentence2))  # "programming"


sentence = "Какой чудесный день, какой чудесный пень!"

def long_word(sentence):
    words = sentence.split()
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(long_word(sentence))