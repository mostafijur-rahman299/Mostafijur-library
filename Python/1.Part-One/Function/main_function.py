

name=str(input("Enter your name: "))

# Define function to check if name contains a vowel

#
# def has_vowel():
#     for letter in name.lower():
#         if letter=='a' or letter=='e' or letter=='u' or letter=='i' or letter=='o':
#              print("Your name contains vowel")
#              break
#     else:
#         print("Your name not contains vowel")


def has_vowel():
    if set('aeiou').intersection(name.lower()):
        print("Your name contains vowel")
    else:
        print("Your name not contains vowel")


# def has_vowel():
#     if name.find('a') or name.find('e') or name.find('i') or name.find('o') or name.find('u'):
#         print("Your name contains vowel")
#     else:
#         print("Your name not contains vowel")


def print_letters():
    for letter in name:
        print(letter)


def main():
    has_vowel()
    print_letters()

if __name__ == '__main__':
    main()

# if __name__ == "__main__":
#     has_vowel()
#     print_letters()
