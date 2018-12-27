#reverse morse code program
#converts morse code into letters and numbers

#imports
#import morsecodeConverter


def getMorse():
    print("---Reverse morse code converter---")

    #get morse input
    morse = input("Enter your morse code: ")
    #loop through characters in morse word
    for chars in morse:
        #ensure characters are not letters or numbers
        if chars.isalpha() or chars.isnumeric():
            #pass down to next if
            pass
            #ensure characters are either . or - or |
            if chars != "." or "-" or "|":
                morse = input("That's not morse. Enter morse: ")
        else:
            #correct input. Break the loop.
            break

    return morse


def convertMorse(morse):
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

    #reverse alphabet keys and values
    invertAlphabet = {value:key for key, value in alphabet.items()}

    return invertAlphabet
    

def loopMorse(morse):
    symbol = ""
    #loop through morse word
    for char in morse:
        if char == " ":
        return symbol
            if char == "  ":
                break
            else:
                continue
        else:
        #assign character to variable
        symbol += char
        ################# problem: this may return all characters in morse
    #return all characters as 1 word
    return char


def loopAlphabet(char,invertAlphabet):
    for key in invertAlphabet:
        #if characters are identical to a key
            if char == key:
                #####problem is that it cannot read individual morse letters seperately. a b because they may be in groups.
                #so you can seperate them with a space/tell program to look for a space
                morseWord = invertAlphabet[key]
                print(morseLetters,end="")
                continue
            elif char != key:
                #add letters together and loop back to start of for
                #####problem: it's adding the same char together
                char += char
                continue
        else:
            break


        loopMorse(morse)
        if char in invertAlphabet:
            
            



   

#MAIN AS FUNCTION
def main():
    morse = getMorse()
    invertAlphabet = convertMorse(morse)
    char = loopMorse(morse)
    loopAlphabet(char,invertAlphabet)
    #allows a newline before the title pops up whilst keeping it at top first run
    print("\n")
    main()

#MAIN FUNCTION RUN
main()



