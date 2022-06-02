from typing import Dict, Any

from G_Translations import language_translator
from duo_lingo import get_words
import tabulate

learned_words = get_words()
translated_words = language_translator(learned_words)

print(translated_words)

