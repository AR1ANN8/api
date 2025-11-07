from googletrans import Translator
translator = Translator()
result = translator.translate("Hello world", src = "fa", dest = "en")
print(result.text)