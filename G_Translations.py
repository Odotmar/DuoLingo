from googletrans import Translator
from tabulate import tabulate


def language_translator(list):
    en_el_dict = {}
    translator = Translator()

    for words in list:
        words = words.strip()
        translated_words = translator.translate(text=words, src='el',dest='en')
        en_el_dict[words] = translated_words.text

    return en_el_dict


