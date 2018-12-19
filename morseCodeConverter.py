#morse code program
#convert words to morse code
#need to be able to have multiple words separated with |

def getWord():
    print("---Morse code converter---")

    #get word input
    word = input("Enter a word to convert: ")
    #convert to lowercase
    word.lower()
    #loop through the characters in the word
    for chars in word:
        #check that each character is a letter or number
        if chars.isalpha() or chars.isnumeric():
            break
        else:
            #if it's invalid characters then get them to enter again before relooping to check that input
            print("Enter a word without special symbols.")
            word = input("Enter a word to convert: ")
            word.lower()
            #jump back to start of loop
            continue

    return word

def convertWord(word):
    #a dictionary that contains the morse values to convert to. The keys correspond to characters in word.
    alphabet = {
        "a":".-",
        "b":"-...",
        "c":"-.-.",
        "d":"-..",
        "e":".",
        "f":"..-.",
        "g":"--.",
        "h":"....",
        "i":"..",
        "j":".---",
        "k":"-.-",
        "l":".-..",
        "m":"..",
        "n":"-.",
        "o":"---",
        "p":".--.",
        "q":"--.-",
        "r":".-.",
        "s":"...",
        "t":"-",
        "u":"..-",
        "v":"...-",
        "w":".--",
        "x":"-..-",
        "y":"-.--",
        "z":"--..",
        "1":".----",
        "2":"..---",
        "3":"...--",
        "4":"....-",
        "5":".....",
        "6":"-....",
        "7":"--...",
        "8":"---..",
        "9":"----.",
        "0":"-----"
        }

    #loop through letters in word
    for letter in word:
        #check that alphabet contains the letter
        if letter in alphabet:
            #loop through keys in alphabet
            for key in alphabet:
                #if the letter matches a key in alphabet
                if letter == key:
                    #assign that key:value to a variable
                    morseLetter = alphabet[key]
                    #print it
                    print(morseLetter,end=" ")
        #if there is a space in the word it becomes |. So that seperate words are seperated.
        elif letter == " ":
            letter = "|"
            print(letter,end=" ")
            continue
        else:
            print("Something went wrong.")
            getWord()
            


#MAIN AS FUNCTION
def main():
    word = getWord()
    convertWord(word)
    #allows a newline before the title pops up whilst keeping it at top first run
    print("\n")
    main()

#MAIN FUNCTION RUN
main()




