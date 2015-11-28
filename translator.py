__author__ = 'hesham'
from textblob import TextBlob
class Translator:
    @staticmethod
    def translate(english_word):
        english_blob = TextBlob(english_word)
        english_blob = english_blob.correct()
        return unicode(english_blob.translate('en', 'ar'))
