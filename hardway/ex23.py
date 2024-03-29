import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()  # 只是把每行结尾的\n删掉

    print(">>>>>>>nextlang= ",repr(next_lang) )
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>",cooked_string)
    #print(raw_bytes)


languages = open ("languages.txt", encoding = "utf-8")

main(languages, encoding, error)