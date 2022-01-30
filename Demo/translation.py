from modeltranslation.translator import TranslationOptions, translator
from Demo.models import Services

class ServicesTranslationOptions(TranslationOptions):
    fields = ('name','description',)



translator.register(Services, ServicesTranslationOptions)