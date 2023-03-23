from translate import Translator


class TranslateCommon:

    @classmethod
    def chinese_translate(cls, string):
        if string:
            string = string.replace("'", ' ') or string.replace('"', ' ')
        translate_or = Translator(to_lang='chinese')
        translation = translate_or.translate(string)
        return translation
