# -*- coding: utf-8 -*-

from Translator import Translator

T = Translator()

while True:
    word = input("Enter a word: ")
    if word == "-1":
        break
    word = T.TranslateSentense(word)
    print(word)
