'''English French Translations'''
import os
import json
from unittest import result
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(url)

def english_to_french(english_text):
    '''translate english to french'''
    french_text = lt.translate(text= str(english_text), model_id='en-fr').get_result()
    translated = french_text['translations']

    return translated[0]['translation']

def french_to_english(french_text):
    '''translate french to english'''
    english_text = lt.translate(text= str(french_text), model_id='fr-en').get_result()
    translated = english_text['translations']

    return translated[0]['translation']


print(french_to_english('Bonjour'))
print(english_to_french("Hello"))
