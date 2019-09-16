def break_words(stuff):  # 拆分成word集合
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):    # 对word集合进行排序
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): # 打印第一个word
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):   #打印最后一个word
    """Prints the last word after poping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):   #对句子排序
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence): #打印句子中的第一和最后的word
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):   #打印排序后句子中的第一和最后的word
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
