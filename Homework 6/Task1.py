# Задание 1.
# Напишите функцию, которая принимает на вход строку (предложение), а возвращает самое длинное слово из строки.
def longest_word(sentence):
    words = sentence.split()
    new_dict = {}
    for word in words:
        new_dict[len(word)] = [word]
    max_length = max(new_dict.keys())
    return new_dict[max_length]
sentence = input()
print(longest_word(sentence))