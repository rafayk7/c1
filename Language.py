import re

"""
This is a general language class that each language can inherit from.
"""

class Language:
    def __init__(self):
        pass

    # Checks if the line is the start of a multiline comment
    def check_multi_start(self, text):
        raise NotImplementedError
    
    # Checks if the line is the end of a multiline comment
    def check_multi_end(self, text):
        raise NotImplementedError

    # Checks if the line has a comment
    def check_single_comment(self, text):
        raise NotImplementedError

    # Checks if the line has a todo
    def check_todo(self, text):
        no_string = re.sub("[\'\"].*[\'\"]", '', text)
        if "TODO" in no_string:
            return True
        
        return False
    
    # Performs all checks and returns dictionary with results
    def perform_checks(self, text):
        multi_start = self.check_multi_start(text)
        multi_end = self.check_multi_end(text)
        single_comment = self.check_single_comment(text)
        todo = self.check_todo(text)

        return {
            "multi_start": multi_start,
            "multi_end": multi_end,
            "single_comment": single_comment,
            "todo": todo
        }

