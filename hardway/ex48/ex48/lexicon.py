lexicon = {
    "north": 'direction',
    "south": 'direction',
    "east": 'direction',
    "west": 'direction',
    "go": "verb",
    "kill": "verb",
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'bear': 'noun',
    'princess': 'noun',
    '1234': 'number',
    '3': 'number',
    '91234': 'number',
    'asdfasdf': 'error',
    'ias': 'error',
    'a': 'stop'
}

def scan(sentence):
    results = []
    sentences = sentence.lower() 
    words = sentences.split()
    for word in words:
        word_type = lexicon.get(word)
        results.append((word_type, word))
    return results

# upper()——所有字母大写   
# lower()——所有字母小写
# capitalize()——首字母大写，其他字母小写
# title()——所有单词首字母大写，其他小写