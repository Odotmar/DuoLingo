import duolingo
from googletrans import Translator


def get_words(user, pwd):
    credentials = duolingo.Duolingo(username=user, password=pwd)
    known_words = credentials.get_known_words(lang='el')
    return known_words


def language_translator(foreign_words):
    en_el_dict = {}
    translator = Translator()

    for words in foreign_words:
        words = words.strip()
        translated_words = translator.translate(text=words, src='el', dest='en')
        en_el_dict[words] = translated_words.text
    return en_el_dict


# greek_words = get_words()
#
# # print(greek_words)
# # print(type(greek_words))
# new_words = language_translator(greek_words)
#
# print(new_words)