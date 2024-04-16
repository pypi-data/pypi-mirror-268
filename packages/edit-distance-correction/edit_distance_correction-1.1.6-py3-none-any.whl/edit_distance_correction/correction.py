import Levenshtein
import edit_distance_correction.utils as utils
import pandas as pd
import re
from itertools import chain
import os
import time
#import kenlm

_get_module_path = lambda path: os.path.normpath(os.path.join(os.getcwd(),
                                                 os.path.dirname(__file__), path))
class Corrector:
    def __init__(self):
        self.max_k = 0
        #pinyin:set(word)
        self.pinyin_di = dict()
        self.target_word = dict()
        #start:set(pinyin)
        # self.start_pinyin_di = dict()
        self.start_word_di = dict()
        self.correction_dict = dict()
        self.original_dict = dict()
        self.same_stroke_dict = dict()
        self.same_stroke_head = set()
        self.heteronym_dict = dict()
        self.gram = dict()
        self.lm = None
        self.valid_pinyin = set()
        self._load_correction()
        self._load_same_stroke()
        self._load_valid_pinyin()
        self._load_heteronym_dict()
        #self._load_language_model()


    # def _load_language_model(self):
    #     self.lm = kenlm.Model(self.language_model_path)

    def _load_valid_pinyin(self):
        self.valid_pinyin = utils.read_files(_get_module_path("valid_pinyin"))


    def _load_correction(self):
        correction = pd.read_csv(_get_module_path("correction.csv"), na_values=[''], keep_default_na=False)
        for original, corr in zip(correction["original"], correction["correction"]):
            if original not in self.correction_dict:
                self.correction_dict[original] = set()
            self.correction_dict[original].add(corr)


    def _load_same_stroke(self):
        with open(_get_module_path("same_stroke.txt")) as f:
            for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                arr = re.split("\s+", line)
                if len(arr) > 1:
                    for i, elem1 in enumerate(arr):
                        for j, elem2 in enumerate(arr):
                            if elem1 not in self.same_stroke_dict:
                                self.same_stroke_dict[elem1] = set()
                            self.same_stroke_dict[elem1].add(elem2)


    def load_target_words(self, target_words):
        for word in target_words:
            #word = word.lower()
            if len(word) > self.max_k:
                self.max_k = len(word)
            all_res = utils.get_pinyin(word, "all", True, self.heteronym_dict)
            for res in all_res:
                if res["pinyin"] not in self.pinyin_di:
                    self.pinyin_di[res["pinyin"]] = set()
                self.pinyin_di[res["pinyin"]].add(word)
                # if re.match('^[\u4e00-\u9fa5]+$', word) is not None:
                #     if res["start"] not in self.start_pinyin_di:
                #         self.start_pinyin_di[res["start"]] = set()
                #     self.start_pinyin_di[res["start"]].add(res["pinyin"])
                if re.match('^[\u4e00-\u9fa5]+$', word) is not None:
                    if res["start"] not in self.start_word_di:
                        self.start_word_di[res["start"]] = set()
                    self.start_word_di[res["start"]].add(word)
                if word not in self.target_word:
                    self.target_word[word] = set()
                self.target_word[word].add(res["pinyin"])
            if len(word) > 0:
                self.same_stroke_head.add(word[0])

            for i in range(len(word)):
                if word[i] not in self.gram:
                    self.gram[word[i]] = set()
                if i == len(word) - 1:
                    self.gram[word[i]].add("")
                else:
                    self.gram[word[i]].add(word[i+1])


    def _load_heteronym_dict(self):
        lines = utils.read_files(_get_module_path("heteronym.txt"))
        for line in lines:
            utils.process_heteronym_line(line, self.heteronym_dict)


    def _transform_pinyin(self, pinyin, include_self=False):
        res = utils.replace_char(pinyin, self.correction_dict, max_k=6)
        res = res.union(utils.transform_char(pinyin))
        if include_self:
            res.add(pinyin)
        return res


    def max_backward_match_transform(self, word_list, vocab, max_k=10):
        res = []
        second_res = []
        end = len(word_list)
        while end > 0:
            break_flag = False
            for i in range(max_k):
                start = end - max_k + i
                if start < 0: continue
                temp = "".join(word_list[start:end])
                temp_res = self._transform_pinyin(temp)
                #直接匹配是最好的
                if temp in vocab:
                    res.append([temp, start, end])
                    end = start
                    break_flag = True
                    break
                #其次是有转换的匹配
                else:
                    for second_temp in temp_res:
                        if second_temp in vocab:
                            second_res.append([second_temp, start, end, temp])
            if not break_flag:
                end -= 1
        res.reverse()
        return res, second_res


    def max_backward_match_list(self, cuts, word_list, vocab, max_k=10):
        res = []
        end = len(word_list)
        while end > 0:
            break_flag = False
            for i in range(max_k):
                start = end - max_k + i
                if start < 0: continue
                # temp = "".join(word_list[start:end])
                temps = utils.get_all_list(word_list[start:end])
                for temp in temps:
                    temp = "".join(temp)
                    if temp in vocab:
                        res.append([temp, start, end])
                        break_flag = True
                if break_flag:
                    end = start
            if not break_flag:
                end -= 1
        res.reverse()
        return res


    def recall_word(self, query):
        #temp_cuts = jieba.lcut(query)
        temp_cuts = utils.cut(query)
        cuts = []
        for cut in temp_cuts:
            if re.search("^[a-zA-Z]+$", cut) is not None:
                res = utils.pinyin_split(cut, self.valid_pinyin)
                if res is None:
                    cuts.append(cut)
                else:
                    cuts.extend(res)
            else:
                cuts.append(cut)
        cuts_stroke = utils.get_stroke_replace(cuts, self.gram, self.same_stroke_dict, self.same_stroke_head)
        #cuts_stroke = utils.get_all_list(cuts_stroke)
        #print(len(cuts_stroke))

        query_pinyin, query_start_pinyin, query_pinyin_list = "", "", []
        for cut in cuts:
            qp = utils.get_pinyin(cut, mode="pinyin")
            query_pinyin_list.append(qp)
        res, second_res = self.max_backward_match_transform(query_pinyin_list, self.pinyin_di, max_k=self.max_k * 5)
        jianpin_res = utils.max_backward_match(cuts, self.start_word_di, max_k=1)
        #stroke_res = [utils.max_backward_match(elem, self.target_word, max_k=10) for elem in cuts_stroke]
        #stroke_res = list(chain(*stroke_res))
        #todo:这里找到一个直接返回，实际上最好收集所有可能再比较最好的
        stroke_res = self.max_backward_match_list(cuts, cuts_stroke, self.target_word, max_k=self.max_k)
        stroke_res = utils.combine_same_position(stroke_res)
        first_pinyin_r = []
        second_pinyin_r = []
        for elem in res:
            original = "".join(cuts[elem[1]:elem[2]])
            pinyin = "".join(query_pinyin_list[elem[1]:elem[2]])
            candidates = []
            for word in self.pinyin_di.get(pinyin, []):
                transform_words = utils.get_all([[char, utils.get_pinyin(char, "pinyin")] for char in word])
                candidates.append([word, min([Levenshtein.distance(w, original) for w in transform_words]), elem[1], elem[2]])
            candidates = list(filter(lambda x: x[0] != "".join(cuts[x[2]: x[3]]), candidates))
            candidates = sorted(candidates, key=lambda x: x[1])
            i = len(candidates)
            if len(candidates) > 1:
                for ii in range(1, len(candidates)):
                    if candidates[ii][1] > candidates[0][1]:
                        i = ii
                        break
            candidates = candidates[:i]
            if len(candidates) > 0:
                first_pinyin_r.append([elem[1], elem[2], [word[0] for word in candidates]])
        for elem in second_res:
            original = "".join(cuts[elem[1]:elem[2]])
            pinyin = elem[0]
            candidates = []
            for word in self.pinyin_di.get(pinyin, []):
                transform_words = utils.get_all([[char, utils.get_pinyin(char, "pinyin")] for char in word])
                candidates.append(
                    [word, min([Levenshtein.distance(w, original) for w in transform_words]), elem[1], elem[2]])
            candidates = list(filter(lambda x: x[0] != "".join(cuts[x[2]: x[3]]), candidates))
            candidates = sorted(candidates, key=lambda x: x[1])
            i = len(candidates)
            if len(candidates) > 1:
                for ii in range(1, len(candidates)):
                    if candidates[ii][1] > candidates[0][1]:
                        i = ii
                        break
            candidates = candidates[:i]
            if len(candidates) > 0:
                second_pinyin_r.append([elem[1], elem[2], [word[0] for word in candidates]])
        jianpin_r = []
        for elem in jianpin_res:
            jianpin_r.append([elem[1], elem[2], self.start_word_di[elem[0]]])
            # for e in self.start_word_di[elem[0]]:
            #     jianpin_r.append([e, 0, elem[1], elem[2]])

        stroke_r = []
        for elem in stroke_res:
            start, end = elem[0], elem[1]
            original = query[start : end]
            candidates = []
            for correct in elem[2]:
                #correct_pinyin = self.target_word[correct]
                correct_pinyins = self.target_word[correct]
                original_pinyin = utils.get_pinyin(original, mode="pinyin")
                candidates.append([correct, Levenshtein.distance(correct, original) + min(
                    [Levenshtein.distance(correct_pinyin, original_pinyin) for correct_pinyin in correct_pinyins])])
                # stroke_r.append([correct, Levenshtein.distance(correct, original) + min(
                #     [Levenshtein.distance(correct_pinyin, original_pinyin) for correct_pinyin in correct_pinyins]),
                #                  elem[1],
                #                  elem[2]])
            candidates = list(filter(lambda x: x[0] != original, candidates))
            candidates = sorted(candidates, key=lambda x: x[1])
            i = len(candidates)
            if len(candidates) > 1:
                for ii in range(1, len(candidates)):
                    if candidates[ii][1] > candidates[0][1]:
                        i = ii
                        break
            candidates = candidates[:i]
            if len(candidates) > 0:
                stroke_r.append([start, end, [word[0] for word in candidates]])

        all_candidates = utils.check_conflict(first_pinyin_r, second_pinyin_r)
        all_candidates = utils.check_conflict(all_candidates, jianpin_r)
        all_candidates = utils.check_conflict(all_candidates, stroke_r)

        #all_candidates = list(filter(lambda x: x[0] != "".join(cuts[x[2]: x[3]]), all_candidates))
        res = utils.get_correct(all_candidates, cuts)
        #暂时取第一个，实际可以算分比较
        res = res[0]
        return res

































