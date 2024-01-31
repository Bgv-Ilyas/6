#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    def find_two_identical_letters(word):
        seen_letters = set()
        duplicate_letters = set()

        for letter in word:
            if letter in seen_letters:
                duplicate_letters.add(letter)
            else:
                seen_letters.add(letter)

        return list(duplicate_letters)

    word = input("Введите слово: ")
    result = find_two_identical_letters(word)

    if result:
        print(f"В слове '{word}' есть две одинаковые буквы: {result}")
    else:
        print(f"В слове '{word}' нет двух одинаковых букв.")


