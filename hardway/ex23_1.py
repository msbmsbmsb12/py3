from sys import argv
script, encoding, error = argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

    
def print_line(line, encoding, errors):
    next_lang = line.strip()
    cooked_string = next_lang.encode()
    print(">>>>>>>>>>>>>>>>>>>,COOKED_STRING= ", repr(cooked_string))
    raw_bytes = cooked_string.decode(encoding, errors = errors)
    print(cooked_string,"<===>",raw_bytes)



languages = open("languages_encode.txt", encoding = "utf-8")

main(languages, encoding, error)