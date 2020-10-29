from Language import Language
import re

"""
Notes:
I have made a few assumptions but have tried to make this as general as possible.
The regex string below removes any strings (defined as any text between "" or '')

This way, if a user is writing /* or */ or ''' in a string, it won't be counted as a
comment.

I could use a decorator function here to pre-remove the strings, however
I am running into a challenge where I am not sure how data from a child function should be passed up
to the decorator, modified, and then sent back to the function. Nor am I sure if this is recommended.

I have also included a non-regex method for finding a single-line comment below. This is if you are
interested in seeing some more algorithmic work, as compared to just seeing regex!

"""
class JavaScriptLanguage(Language):
    def __init__(self):
        pass
    
    def check_multi_start(self, text):
        no_string = re.sub("[\'\"].*[\'\"]", '', text)
        if len(text) >= 2 and '/*' in no_string:
            return True

        return False
    
    def check_multi_end(self, text):
        no_string = re.sub("[\'\"].*[\'\"]", '', text)
        if len(text) >= 2 and '*/' in no_string:
            return True
        
        return False
    
    def check_single_comment(self, text):
        no_string = re.sub("[\'\"].*[\'\"]", '', text)
        if '//' in no_string:
            return True
        
        return False
        # in_single_quote = False
        # in_double_quote = False
        # last_char = None

        # for char in text:
        #     if char == '"':
        #         in_double_quote = not in_double_quote
        #     elif char == "'":
        #         in_single_quote = not in_single_quote
        #     elif not in_single_quote and not in_double_quote and last_char and last_char == '/' and char == '/':
        #         return True
            
        #     last_char = char

        # return False
