import duolingo
import getpass
from dotenv import load_dotenv

class get_info_duo():
    
def get_words():
    credentials = duolingo.Duolingo(username="omar467236",password="E6H5BYkv3DVf")
    known_words = credentials.get_known_words(lang='el')
    return known_words

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


