from Language import Language

"""
Notes:
I have made a few assumptions here to simplify the code.
I assume that a multi-line comment will only be the first thing that happens
in a line of code that starts/ends a multi-line block. A way to get around this
is to do what I have done in the JavaScriptLanguage, using regex to remove strings
and then just checking if /* is in the string.

"""

class JavaLanguage(Language):
    def __init__(self):
        pass
    
    def check_multi_start(self, text):
        if len(text) >= 2 and text[0] == '/' and text[1] == '*':
            return True

        return False
    
    def check_multi_end(self, text):
        if len(text) >= 2 and text[0] == '*' and text[1] == '/':
            return True
        
        return False
    
    def check_single_comment(self, text):
        in_single_quote = False
        in_double_quote = False
        last_char = None

        for char in text:
            if char == '"':
                in_double_quote = not in_double_quote
            elif char == "'":
                in_single_quote = not in_single_quote
            elif not in_single_quote and not in_double_quote and last_char and last_char == '/' and char == '/':
                return True
            
            last_char = char

        return False
