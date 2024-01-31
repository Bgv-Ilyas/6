#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    def remove_chars(sentence, n1, n2):
        if n1 <= n2 and 0 <= n1 < len(sentence) and 0 <= n2 < len(sentence):
            modified_sentence = sentence[:n1] + sentence[n2+1:]
            return modified_sentence
        else:
            return "Ошибка: некорректные значения n1 и n2"

    sentence = input("Введите предложение: ")
    n1 = int(input("Введите значение n1: "))
    n2 = int(input("Введите значение n2: "))

    result = remove_chars(sentence, n1, n2)
    print("Результат:", result)
