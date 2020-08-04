#-*-coding: utf-8-*-
import re

BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

JONGSUNG_LIST = ['#', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def convert(keyword: str):
    split_keyword_list = list(keyword)
    result = list()
    result_tmp = list()
    for keyword in split_keyword_list:
        result_tmp = []
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
            char_code = ord(keyword) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            result_tmp.append(CHOSUNG_LIST[char1])
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            result_tmp.append(JUNGSUNG_LIST[char2])
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            result_tmp.append(JONGSUNG_LIST[char3])
            result.append(result_tmp)
        else:
            result.append(keyword)
    return result

def the_rule_of_the_last_syllable(keyword_list):
    for i in range(len(keyword_list)):
        if keyword_list[i] == ' ':
            continue
        GIEOK_LIST = ['ㄱ', 'ㅋ', 'ㄲ', 'ㄺ', 'ㄳ']
        NIEUN_LIST = ['ㄴ', 'ㄵ']
        DIGEUT_LIST = ['ㄷ', 'ㅌ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅎ']
        RIEUL_LIST = ['ㄹ', 'ㄼ', 'ㄽ', 'ㄽ', 'ㄾ']
        MIEUM_LIST = ['ㅁ', 'ㄻ']
        BIEUP_LIST = ['ㅂ', 'ㅍ', 'ㅄ', 'ㄿ']
        IEUNG_LIST = ['ㅇ'] 
        if keyword_list[i][2] in GIEOK_LIST:
            keyword_list[i][2] = GIEOK_LIST[0]
        if keyword_list[i][2] in NIEUN_LIST:
            keyword_list[i][2] = NIEUN_LIST[0]
        if keyword_list[i][2] in DIGEUT_LIST:
            keyword_list[i][2] = DIGEUT_LIST[0]
        if keyword_list[i][2] in RIEUL_LIST:
            keyword_list[i][2] = RIEUL_LIST[0]
        if keyword_list[i][2] in MIEUM_LIST:
            keyword_list[i][2] = MIEUM_LIST[0]
        if keyword_list[i][2] in BIEUP_LIST:
            keyword_list[i][2] = BIEUP_LIST[0]
        if keyword_list[i][2] in IEUNG_LIST:
            keyword_list[i][2] = IEUNG_LIST[0]
    
    return keyword_list

def combine(keyword_list):
    combined_word = str()
    for i in range(len(keyword_list)):
        if keyword_list[i] == ' ':
            combined_word += ' '
            continue
        tmp = '\\u' + hex(CHOSUNG_LIST.index(keyword_list[i][0]) * CHOSUNG + JUNGSUNG_LIST.index(keyword_list[i][1]) * JUNGSUNG + JONGSUNG_LIST.index(keyword_list[i][2]) + BASE_CODE)[2:]
        # print(tmp)
        tmp = tmp.encode('utf-8')
        combined_word += tmp.decode('unicode_escape')
    # print(combined_word)
    return combined_word

if __name__ == '__main__':

    test_keyword = input('input your text: ')
    print(convert(test_keyword))
    print(the_rule_of_the_last_syllable(convert(test_keyword)))
    print(combine(the_rule_of_the_last_syllable(convert(test_keyword))))