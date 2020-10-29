from AbstractCodeChecker import AbstractCodeChecker

if __name__ == '__main__':
    files = [
        'testfiles/test.js',
        'testfiles/test.java'
    ]

    a = AbstractCodeChecker()

    for file in files:
        print("Checking {}".format(file))
        a.check_file(file)
