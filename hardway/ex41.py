import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "Class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a funcation *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first    如果输入python3 ex41.py english ，启用读写模式
if len(sys.argv) == 2 and sys.argv[1] =="english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8")) # .strip() 用于移除字符串首尾字符，默认为空格


def convert(snippet, phrase):   # snippet 片段  phrase 词组
    class_names = [w.capitalize() for w in     # #captitalize()将第一个首字母大写，其余全部小写  count()统计snippt中出现字符串%%%的个数
                   random.sample(WORDS, snippet.count("%%%"))] # random.sample()可以从指定的序列中，随机的截取指定长度的片断，不作原地修改。
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)  # random.randint(a, b) 返回随机整数 N 满足 a <= N <= b。相当于 randrange(a, b+1)。random.randint()随机生一个整数int类型，可以指定这个整数的范围，同样有上限和下限值
        param_names.append(', '.join(random.sample(WORDS, param_count)))  #.join()将序列中的元素以指定的字符连接生成一个新的字符串

    for sentence in snippet, phrase:
        result = sentence[:]              # python中复制列表的方法

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1) # replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())  #Python 字典(Dictionary) keys() 函数以列表返回一个字典所有的键
        random.shuffle(snippets)         #random.shuffle()如果你想将一个序列中的元素，随机打乱的话可以用这个函数方法。

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER:  {answer}\n\n")
except EOFError:
    print("\nBye")