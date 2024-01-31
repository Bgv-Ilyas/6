#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    def count_same_characters(sequence):
        first_char = sequence[0]
        count = sum(1 for char in sequence if char == first_char)
        return count
    sequence = input("Введите последовательность символов: ")
    count = count_same_characters(sequence)
    if count == len(sequence):
        print(f"Все символы последовательности одинаковы. Количество: {count}")
    else:
        print(f"Количество одинаковых символов в начале последовательности: {count}")

