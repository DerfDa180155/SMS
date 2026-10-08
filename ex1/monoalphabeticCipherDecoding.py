
notFoundChar = "?"

table = {"A": "",
         "B": "",
         "C": "",
         "D": "",
         "E": "",
         "F": "",
         "G": "",
         "H": "",
         "I": "",
         "J": "",
         "K": "",
         "L": "",
         "M": "",
         "N": "",
         "O": "",
         "P": "",
         "Q": "",
         "R": "",
         "S": "",
         "T": "",
         "U": "",
         "V": "",
         "W": "",
         "X": "",
         "Y": "",
         "Z": ""
         }

english_frequency = {
    "A": 8.167,
    "B": 1.492,
    "C": 2.782,
    "D": 4.253,
    "E": 12.702,
    "F": 2.228,
    "G": 2.015,
    "H": 6.094,
    "I": 6.966,
    "J": 0.153,
    "K": 0.772,
    "L": 4.025,
    "M": 2.406,
    "N": 6.749,
    "O": 7.507,
    "P": 1.929,
    "Q": 0.095,
    "R": 5.987,
    "S": 6.327,
    "T": 9.056,
    "U": 2.758,
    "V": 0.978,
    "W": 2.360,
    "X": 0.150,
    "Y": 1.974,
    "Z": 0.074,
}

german_frequency = {
    "A": 6.448,
    "B": 2.113,
    "C": 2.646,
    "D": 4.641,
    "E": 17.220,
    "F": 1.802,
    "G": 3.014,
    "H": 4.180,
    "I": 7.625,
    "J": 0.293,
    "K": 1.512,
    "L": 3.725,
    "M": 2.752,
    "N": 9.502,
    "O": 2.905,
    "P": 1.032,
    "Q": 0.028,
    "R": 7.610,
    "S": 6.575,
    "T": 6.265,
    "U": 4.430,
    "V": 0.904,
    "W": 1.404,
    "X": 0.051,
    "Y": 0.106,
    "Z": 1.217,
}

def main():
    encryptedText = input("enter text to start decrypting: ")
    frequencyTable = frequencyDecryptedChars(encryptedText)

    print("do you have an existing key tabel? (y/n)")
    answer = input().lower()
    if answer == "y":
        inputTable = input("enter key table (A:A, B:B, C:C, ...): ")

        inputTable = inputTable.split(", ")
        for pair in inputTable:
            key, value = pair.split(":")
            table[key] = value
    else:
        printCombinedFrequencyTable(frequencyTable)
        language = input("\ndo you want to use the english frequency table or the german frequency table? (e/g): ").lower()
        amount = int(input("how many Letters starting from the most frequent do you want to use? (1-26): "))
        if language == "e":
            language_frequency = english_frequency
        elif language == "g":
            language_frequency = german_frequency

        encrypted_sorted = sorted(frequencyTable, key=frequencyTable.get, reverse=True)
        language_sorted = sorted(language_frequency, key=language_frequency.get, reverse=True)

        for encrypted_char, decrypted_char in zip(encrypted_sorted[:amount], language_sorted[:amount]):
            table[encrypted_char] = decrypted_char

    while not completeTable():
        print("\nencrypted text: " + encryptedText)
        printDecryptedText(encryptedText)
        printTable()
        
        print("enter a key-value pair to add to the table (A:B):")
        pair = input()
        key, value = pair.split(":")
        table[key] = value

    print("encrypted text: " + encryptedText)
    printDecryptedText(encryptedText)
    printTable()


def completeTable():
    for char in table:
        if table[char] == "":
            table[char] = notFoundChar


def printTable():
    print("key table: ")
    for char in table:
        print(char + " : " + table[char])            


def printDecryptedText(text):
    noneText = [" ", "\n", ",", ".", "!", "?", ";", ":", "'", "\"", "-", "_", "(", ")", "[", "]", "{", "}", "/", "\\", "|", "@", "#", "$", "%", "^", "&", "*", "+", "=", "<", ">"]
    decryptedText = ""
    for char in text:
        if char.upper() in table:
            decryptedText += table[char.upper()]
        elif char in noneText:
            decryptedText += char
        elif char == "\n":
            decryptedText += "\n"
        else:
            decryptedText += notFoundChar
    print("decrypted text: " + decryptedText)

def frequencyDecryptedChars(text):
    frequencyTable = {"A": 0,
                     "B": 0,
                     "C": 0,
                     "D": 0,
                     "E": 0,
                     "F": 0,
                     "G": 0,
                     "H": 0,
                     "I": 0,
                     "J": 0,
                     "K": 0,
                     "L": 0,
                     "M": 0,
                     "N": 0,
                     "O": 0,
                     "P": 0,
                     "Q": 0,
                     "R": 0,
                     "S": 0,
                     "T": 0,
                     "U": 0,
                     "V": 0,
                     "W": 0,
                     "X": 0,
                     "Y": 0,
                     "Z": 0}

    charCount = 0

    for char in text:
        if char.upper() in frequencyTable:
            frequencyTable[char.upper()] += 1
            charCount += 1

    for char in frequencyTable:
        frequencyTable[char] = (frequencyTable[char] / charCount) * 100 if charCount > 0 else 0

    sortedFrequencyTable = dict(sorted(frequencyTable.items(), key=lambda item: item[1], reverse=True))

    return sortedFrequencyTable

def printCombinedFrequencyTable(frequencyTable):
    print("combined frequency table: ")
    print("char\tfrequency\tenglish\t\tgerman")
    for char in frequencyTable:
        print(f"{char}\t{frequencyTable[char]:.2f}%\t\t{english_frequency[char]:.2f}%\t\t{german_frequency[char]:.2f}%")

if __name__ == "__main__":
    main()
