import json
import time
import utils
from correction import Corrector

c = Corrector()
target_words = utils.read_files("target_words")
test_words = utils.read_files("test_file", True)


with open("temp.txt") as f:
    json_str = f.read()
    di = json.loads(json_str)
    for elem in di["body"]:
        target_words.add(elem["r"].split("|")[1])
c.load_target_words(target_words)
start = time.time()
for w in test_words:
    print(w)
    res = c.recall_word(w)
    print(res)
    print(time.time() - start)
    start = time.time()
    print("\n")