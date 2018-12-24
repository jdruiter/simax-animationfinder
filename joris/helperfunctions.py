# coding: utf-8
import re



def clear_interpunction(sentence):
    '''
    Removes all interpunction from a sentence
    '''
    replacelist = ['.', ',', '!', '?', ';']
    for r in replacelist:
        sentence = sentence.replace(r, '')
    return sentence


def select_words(sentence):
    '''
    Selects the words from a sentence, ignores the rest
    Only works with English words, not with é, ü and other special language characters
    '''
    word_list = re.findall('\w+', sentence)
    return word_list


def select_words_unicode(sentence):
    '''
    If module regex is installed, this function works with unicode letters (better)
    '''
    # import regex
    # sentence = regex.sub(ur"\p{P}+", "", sentence).split(' ')
    # return [s for s in sentence if s]
    pass


def safe_unicode(obj):
    '''
    Returns the unicode representation of obj;
    '''
    try:
        return unicode(obj)
    except UnicodeDecodeError:
        # obj is byte string
        # 'strict', 'ignore', 'replace', 'xmlcharrefreplace' (htmml equivalent replace)
        try:
            unicode(obj.decode('utf-8', 'replace'))
        except:
            ascii_text = str(obj).encode('string_escape')
            return unicode(ascii_text)
