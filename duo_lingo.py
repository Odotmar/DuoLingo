import duolingo
import getpass
from dotenv import load_dotenv

class get_info_duo():
    
def get_words():
    credentials = duolingo.Duolingo(username="omar467236",password="E6H5BYkv3DVf")
    known_words = credentials.get_known_words(lang='el')
    return known_words

