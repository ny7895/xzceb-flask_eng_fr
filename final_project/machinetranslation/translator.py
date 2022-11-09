"""
This will import json and IBM Watson library
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('M86xNg7TNZeLOfzgp_WjxDu8IL3fFFhWCKgV06tM5di4')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url = ("https://api.us-south.language-translator.watson.cloud.ibm.com/instances/d170e854-586c-4865-875f-4eb5350e0bbc")

def english_to_french(english_text):

        french_text = language_translator.translate(
        text=english_text, 
        model_id="en-fr").get_result()
    return french_text['translations'][0]['translation'] 

def french_to_english(french_text):  #This function wil translate from French to English
#write the code here
        english_text = language_translator.translate(
        text=french_text, 
        model_id="fr-en").get_result()
    return english_text['translations'][0]['translation'] 

