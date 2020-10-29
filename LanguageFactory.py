from JavaLanguage import JavaLanguage
from JavaScriptLanguage import JavaScriptLanguage


# A factory class that generates the required Language Class
class LanguageFactory:
    def generate(self, path):
        extension = path.split('.')[1]

        # Add Python Language here
        if extension == 'py':
            print("python")

        elif extension == 'java':
            jl = JavaLanguage()
            return jl

        elif extension == 'js':
            jsl = JavaScriptLanguage()
            return jsl
