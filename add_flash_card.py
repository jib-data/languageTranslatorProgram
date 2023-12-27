from googletrans import Translator
import os
import ast

translator = Translator()
mainCards = []

spanishFlashFile = 'esWordCards.txt'
frenchFlashFile = 'frWordCards.txt'

def langaugeDestination():
    """
    This function asks the user to input language and returns a string of the language
    the user wants to translate
    :return: str es/fr
    """
    print('Hello, welcome to the language translation App...')
    lan_destination = input('In what language do you want to translate your words? es/fr')
    return lan_destination


def retrieve_existing_cards(lan_destination):
    """
    This function takes the language into which the user wants to translate the word
    and retrieves already translated words in that language in the users previous session
    :param lan_destination:
    :return: returns a list
    """
    cards = []
    if lan_destination == 'es':
        if os.path.exists(spanishFlashFile):
            with open(spanishFlashFile, 'r') as file:
                cards.append(ast.literal_eval(file.read()))

        else:
            print('No cards exist')
    elif lan_destination == 'fr':
        if os.path.exists(frenchFlashFile):
            with open(frenchFlashFile, 'r') as file:
                cards.append(ast.literal_eval(file.read()))

        else:
            print('No cards exist')
    return cards
def display_existing_cards(cards):
    """
    This function takes a list of cards as input and displays it to the user
    :param cards:
    :return:
    """
    if len(cards) == 1:
        print('There is currently ' + str(len(cards)) + ' card in the flash cards')
        for i, card in enumerate(cards[0]):
            print(i+1, 'eng:' + card[0], 'esp:' + card[1])

    elif len(cards) > 1:
        print('There are currently ' + str(len(cards)) + ' cards in the flash cards')
        for i, card in enumerate(cards[0]):
            print(i+1, 'eng:' + card[0], 'esp:' + card[1])

def transSpanish(enWord):
    """
    This function takes an english word from the user and translates it into Spanish
    :param enWord:
    :return: (enWord, spanishWord)
    """
    global mainCards
    spanishWord = translator.translate(enWord, dest = 'es').text
    print('{}, translates as {} in the Spanish Language'.format(enWord, spanishWord))
    # ask if user wants to add translated word to translated card list
    addCard = input(' Do you want to save translated word? yes/no')
    if addCard == 'yes':
        mainCards.append((enWord, spanishWord))
    else:
        print('card was not added')


def transFrench(enWord):
    """
        This function takes an english word from the user and translates it into French
        :param enWord:
        :return: (enWord, French)
        """
    global mainCards
    frenchWord = translator.translate(enWord, dest = 'fr').text
    print('{}, translates as {} in the French Language'.format(enWord, frenchWord))
    # Ask if they want to save word to translated word cards
    addCard = input(' Do you want to save translated word? yes/no')
    if addCard == 'yes':
        mainCards.append((enWord, frenchWord))
    else:
        print('card was not added')

def saveCardtoFile(lan_destination):
    """
    This function takes the language destination as an argument and then saves the generated flash cards
    to the file of that language
    :param lan_destination:
    :return: None
    """
    if lan_destination == 'es':
        with open(spanishFlashFile, 'a') as file:
            file.write(str(mainCards))
    elif lan_destination == 'fr':
        with open(frenchFlashFile, 'a') as file:
            file.write(str(mainCards))

lan_destination = langaugeDestination()
# retrieve existing flash card
mainCards = retrieve_existing_cards(lan_destination)
# display existing flash cards
display_existing_cards(mainCards)

if lan_destination == 'es':
    # ask which word user wants to translate
    while True:
        enWord = input('Which word do you want to translate? ')
        transSpanish(enWord)
        continue_translation = input('Do you want to translate another word? yes/no')
        if continue_translation == 'no':
            break
    # ask if user wants to write the translated languages to file for later use?
    toFile = input('Do you want to save translated words to file? yes/no ')
    if toFile == 'yes':
        saveCardtoFile(lan_destination)
    else:
        print('Word card not saved to file')
elif lan_destination == 'fr':
    while True:
        enWord = input('Which word do you want to translate? ')
        transFrench(enWord)
        continue_translation = input('Do you want to translate another word? yes/no ')
        if continue_translation == 'no':
            break
    toFile = input('Do you want to save tranlated words to file? yes/no ')
    if toFile == 'yes':
        saveCardtoFile(lan_destination)
    else:
        print('Word card was not saved to file')
else:
    print('Sorry, App cannot translate to this language')

exit()

