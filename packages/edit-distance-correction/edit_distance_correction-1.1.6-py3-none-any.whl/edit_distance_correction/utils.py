import Levenshtein
import pypinyin
from pypinyin import pinyin
import itertools
import re

#常用替换拼音
def replace_char(char_list, di, max_k=6):
    res = set()
    for j in range(len(char_list)):
        for i in range(max_k):
            if j + i > len(char_list):
                break
            if char_list[j : j + i] in di:
                for rv in di[char_list[j : j + i]]:
                    res.add(char_list[:j] + rv + char_list[j + i:])
    return res


#处理多音字字典的每一行
def process_heteronym_line(line, dict):
    res = re.split("\s+", line)
    hanzi = res[0].strip()
    if re.match('^[\u4e00-\u9fa5]+$', hanzi) is not None:
        if hanzi not in dict:
            dict[hanzi] = set()
        for elem in res[1:]:
            elem = elem.strip().lower()
            if re.match('^[a-z]+$', elem):
                dict[hanzi].add(elem)


#通用拓展近音
def transform_char(char_list):
    res = set()
    # #去掉一个字母
    # for i in range(len(char_list) - 1):
    #     res.add(char_list[:i] + char_list[i + 1:])
    # #相邻拼音换位
    # for i in range(len(char_list) - 2):
    #     res.add(char_list[:i] + char_list[i + 1] + char_list[i] + char_list[i + 2:])
    #相连重复字母保留一个
    for i in range(len(char_list) - 1):
        if char_list[i] == char_list[i + 1]:
            res.add(char_list[:i] + char_list[i + 1:])
    return res


def read_files(filename, use_list=False):
    res = [] if use_list else set()
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if use_list: res.append(line)
            else: res.add(line)
    return res


#最大后向匹配
def max_backward_match(word_list, vocab, max_k=10):
    res = []
    end = len(word_list)
    while end > 0:
        break_flag = False
        for i in range(max_k):
            start = end - max_k + i
            if start < 0: continue
            temp = "".join(word_list[start:end])
            if temp in vocab:
                res.append([temp, start, end])
                end = start
                break_flag = True
                break
        if not break_flag:
            end -= 1
    res.reverse()
    return res


#arr:[[word, start, end], ...]
def combine_same_position(arr):
    di = dict()
    for elem in arr:
        if elem[1] not in di:
            di[elem[1]] = []
        di[elem[1]].append(elem)
    res = [(elem[0][1], elem[0][2], [e[0] for e in elem]) for elem in di.values()]
    return res


#所有的组合先生成再计算和判断
def get_all_combinations(query_pinyin_list, max_k=5):
    for i in range(len(query_pinyin_list)):
        end = max_k + 1 if max_k + 1 < len(query_pinyin_list) else len(query_pinyin_list)
        for j in range(1, end):
            res = get_all(query_pinyin_list[i : i + j])
    return res


def get_all(arr):
    i = 1
    temp_res = list(arr[0])
    while i < len(arr):
        res = []
        for elem1 in temp_res:
            for elem2 in arr[i]:
                res.append(elem1 + elem2)
        temp_res = res.copy()
        i += 1
    return temp_res


def get_all_list(arr):
    i = 1
    temp_res = [[elem] for elem in arr[0]]
    while i < len(arr):
        res = []
        for elem1 in temp_res:
            for elem2 in arr[i]:
                elem1_copy = elem1.copy()
                elem1_copy.append(elem2)
                res.append(elem1_copy)
        temp_res = res.copy()
        i += 1
    return temp_res


#每个位置上多种可能（汉字、拼音）的编辑距离之和
def min_distance(original_arr, arr):
    dis = 0
    for elem1, elems in zip(original_arr, arr):
        dis += min([Levenshtein.distance(elem1, elem2) for elem2 in elems])
    return dis


#判断是否冲突，冲突时保留insider部分，去掉outsider冲突的部分
#insider: [[i, j, ..]]  outsider[[i, j, ..]]
def check_conflict(insider, outsider):
    res = insider
    for o in outsider:
        flag = True
        for ins in res:
            if not (o[0] >= ins[1] or o[1] <= ins[0]):
                flag = False
                break
        if flag: res.append(o)
    return res


#候选改正词和分词结果还原得到最终改正结果
def get_correct(candidates, cuts):
    res = []
    cands = sorted(candidates, key=lambda x: x[0])
    for i, cand in enumerate(cands):
        before_start = cands[i-1][1] if i != 0 else 0
        before_end = cand[0]
        if before_start != before_end:
            res.append(["".join(cuts[before_start: before_end])])
        res.append(cand[2])
    if len(cands) == 0:
        res.append(["".join(cuts)])
    else:
        if cands[-1][1] != len(cuts):
            res.append(["".join(cuts[cands[-1][1]:])])
    res = get_all(res)
    return res




    # res = ""
    # candidates_dict = {cand[2]:{"end": cand[3], "word": cand[0]} for cand in candidates}
    # i = 0
    # while i < len(cuts):
    #     if i in candidates_dict:
    #         res += candidates_dict[i]["word"]
    #         i = candidates_dict[i]["end"]
    #     else:
    #         res += cuts[i]
    #         i += 1
    # return res


#用自己的多音字字典拓展多音字拼音
def _heteronym_pinyin(s, heteronym_dict):
    li = []
    for ch in s:
        if re.match('[\u4e00-\u9fa5]+', ch) is not None:
            original = pinyin(ch, style=pypinyin.NORMAL)[0]
            temp = set(original).union(heteronym_dict.get(ch, set()))
            li.append(list(temp).copy())
        else:
            li.append([ch])
    return li


def get_pinyin(word, mode="all", heteronym=False, heteronym_dict=None):
    if heteronym:
        if heteronym_dict is None:
            li = list(itertools.product(*pinyin(word.lower(), heteronym=heteronym, style=pypinyin.NORMAL)))
        else:
            li = list(itertools.product(*_heteronym_pinyin(word.lower(), heteronym_dict)))
        heteronym_res = []
        for one in li:
            if mode == "pinyin_list":
                heteronym_res.append([elem for elem in one])
            elif mode == "pinyin":
                heteronym_res.append("".join([elem for elem in one]))
            elif mode == "start":
                heteronym_res.append("".join([elem[0] for elem in one]))
            else:
                res = dict()
                res["pinyin_list"] = [elem for elem in one]
                res["pinyin"] = "".join(res["pinyin_list"])
                res["start"] = "".join([elem[0] for elem in one])
                heteronym_res.append(res.copy())
        return heteronym_res
    word_pinyin = pypinyin.pinyin(word.lower(), style=pypinyin.NORMAL)
    if mode == "pinyin_list":
        return [elem[0] for elem in word_pinyin]
    elif mode == "pinyin":
        return "".join([elem[0] for elem in word_pinyin])
    elif mode == "start":
        return "".join([elem[0][0] for elem in word_pinyin])
    res = dict()
    res["pinyin_list"] = [elem[0] for elem in word_pinyin]
    res["pinyin"] = "".join(res["pinyin_list"])
    res["start"] = "".join([elem[0][0] for elem in word_pinyin])
    return res


#长串拼音分割，多种路径
def pinyin_split(pinyin, valid_pinyin):
    res = []
    def split_helper(pinyin, pos, before_res):
        if pos >= len(pinyin):
            res.append(before_res)
        for i in range(pos, len(pinyin)+1):
            if pinyin[pos:i] in valid_pinyin:
                before_res_copy = before_res.copy()
                before_res_copy.append(pinyin[pos:i])
                split_helper(pinyin, i, before_res_copy)
    split_helper(pinyin, 0, [])
    #暂时取最小粒度切分结果，最长的一个
    if len(res) == 0: return None
    return sorted(res, key=lambda x: len(x), reverse=True)[0]


#形近字替换结果
def get_stroke_replace(query, gram, stroke_dict, head):
    last_valid = list(filter(lambda x: x is not None, [None if elem not in head and elem != query[0] else elem for elem in stroke_dict.get(query[0], [query[0]])]))
    res = [last_valid.copy()]
    for i in range(1, len(query)):
        last_valid_copy = last_valid.copy()
        last_valid = set()
        for first in last_valid_copy:
            for second in stroke_dict.get(query[i], [query[i]]):
                if second in gram.get(first, []) or second in head or second == query[i]:
                    last_valid.add(second)
        res.append(list(last_valid).copy())
    return res


#拼音合一起，其他单独一个字符
def cut(query):
    res = []
    last_char = False
    for char in query:
        if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            if last_char:
                res[-1] = res[-1] + char
            else:
                res.append(char)
            last_char = True
        else:
            res.append(char)
            last_char = False
    return res



