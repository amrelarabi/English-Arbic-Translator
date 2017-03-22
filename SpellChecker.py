import math

class SpellChecker:
    def __init__(self, tree):
        self.wordlist = tree

    @staticmethod
    def __areInRange(num1, num2, Range=1):
        for i in range(Range + 1):
            if math.fabs(num1 - num2) == i:
                return True
        return False

    @staticmethod
    def __LettersInplace(word, Input):
        lettersInplace = 0
        for i in range(len(Input)):
            if (len(word) > i) and (word[i] == Input[i]):
                lettersInplace += 1
        return lettersInplace

    @staticmethod
    def __CommonLetters(word, Input):
        commonLetters = 0

        Inputs = {}
        for i in range(len(Input)):
            if (Inputs.get(Input[i], False)):
                Inputs[Input[i]] += 1
            else:
                Inputs[Input[i]] = 1

        for key, value in Inputs.items():
            if word.count(key) == value:
                commonLetters += 1

        if (Input[len(Input) - 1] == word[len(word) - 1]):
            commonLetters += 1
        if (len(Input) == len(word)):
            commonLetters += 1
        if word[0] == Input[0]:
            commonLetters += 1

        return commonLetters

    @staticmethod
    def __LettersInRange(word, Input):
        lettersInRange = 0
        for i in range(len(Input)):
            if (len(word) > i) and (Input[i] in word) and SpellChecker.__areInRange(i, Input.index(word[i]) if (word[i] in Input) else -1):
                lettersInRange += 1
        return lettersInRange

    def IsValid(self, Input):
        return Input in self.__tree

    def GetSuggestions(self, Input, NumOfSuggestions = 5):
        arr = []
        for word in self.wordlist:
            if SpellChecker.__areInRange(len(word), len(Input), 1):
                arr.append(word)

        dic = {}
        for word in arr:
            NumOfSimilarities = 0
            NumOfSimilarities += SpellChecker.__CommonLetters(str(word), Input)
            NumOfSimilarities += SpellChecker.__LettersInplace(str(word), Input)
            NumOfSimilarities += SpellChecker.__LettersInRange(str(word), Input)
            dic[str(word)] = NumOfSimilarities

        Maxes = []
        for i in range(NumOfSuggestions):
            if len(dic) > 0:
                Max = list(dic.keys())[list(dic.values()).index(max(dic.values()))]
                Maxes.append(Max)
                del dic[str(Max)]

        return Maxes