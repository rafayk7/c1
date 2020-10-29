from LanguageFactory import LanguageFactory

"""
This class is the main class that does the counting
and calls on the requisite functions to collect the data on each line.
"""

class AbstractCodeChecker:
    def __init__(self):
        self.num_lines = 0

    def check_file(self, file_path):
        self.num_lines = 0
        lang = LanguageFactory().generate(file_path)

        multi_lines = 0
        multi_blocks = 0
        comment_lines = 0
        single_comments = 0
        todo = 0

        with open(file_path, 'r') as f:
            multi = False

            for line in f.readlines():
                # Update total no. of lines
                self.num_lines += 1

                text = line.strip()
                data = lang.perform_checks(text)

                # Start of a new block of comments
                if data["multi_start"]:
                    multi = True
                    multi_blocks += 1
                
                # End of a block of comments
                # Note use of if vs elif here,
                # in case both are on same line
                if data["multi_end"]:
                    multi = False
                # New single comment
                elif data["single_comment"]:
                    single_comments += 1
                
                # New todo
                if data["todo"]:
                    todo += 1
                
                if multi:
                    multi_lines += 1
                
        comment_lines = multi_lines + single_comments
        
        print("Total # of lines {}".format(self.num_lines))
        print("Total # of block line comments: {}".format(multi_blocks))
        print("Total # of comment lines within block comments: {}".format(multi_lines))
        print("Total # of single line comments: {}".format(single_comments))
        print("Total # of TODO’s: {}".format(todo))
        print("Total # of comment lines: {}".format(comment_lines))
    
        return 1