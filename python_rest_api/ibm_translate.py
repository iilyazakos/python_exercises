import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

with open('C:\\fortranslate.txt', encoding = 'utf-8') as f:
    authenticator = IAMAuthenticator('*ibm_token*')
    language_translator = LanguageTranslatorV3(
    version = '2021-06-09',
    authenticator = authenticator)

    language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')

    translation = language_translator.translate(
    text = f.readline(),
    model_id = 'ru-en').get_result()

    print(str(translation['translations'][0]['translation']))
