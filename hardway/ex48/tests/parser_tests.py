from nose.tools import *
from ex48 import parser, lexicon

def test_subject():
    s1 = parser.Sentence(('noun', 'cheese'),
                         ('verb', 'eats'),
                         ('noun','pigeon'))
    assert s1.verb == 'eats'
    assert s1.subject == 'cheese'
    assert s1.object == 'pigeon'

def test_peek():
    word_list = []
    assert None == parser.peek(word_list)

    word_list = lexicon.scan("princess kill bear")
    assert 'noun' == parser.peek(word_list)

def test_match():
    word_list = []
    assert None == parser.match(word_list, 'noun')

    word_list = lexicon.scan("bear eat princess")
    assert_equal(('noun','bear') ,parser.match(word_list, 'noun'))
    assert_equal(None, parser.match(word_list, 'noun'))


def test_skip():
    word_list = lexicon.scan("the bear eat princess")
    parser.skip(word_list, 'stop')
    print(word_list,">>>>ignore here")


def test_parse_verb():
    word_list = lexicon.scan("the eat princess")
    assert_equal(('verb', 'eat'),parser.parse_verb(word_list))

def test_parse_object():
    word_list = lexicon.scan("the north eat princess")
    assert_equal(('direction','north'), parser.parse_object(word_list))
    # assert_equal(('verb','eat'), parser.parse_object(word_list))


def test_parse_subject():
    word_list = lexicon.scan("the bear  eat princess")
    assert_equal(('noun', 'bear'), parser.parse_subject(word_list))
    assert_equal(('noun', 'player'), parser.parse_subject(word_list))
    
def test_parse_sentence():
    word_list = lexicon.scan("the bear a eat a a a princess")
    m = parser.parse_sentence(word_list)

    assert_equal(('bear', 'eat', 'princess'),(m.subject, m.verb, m.object))