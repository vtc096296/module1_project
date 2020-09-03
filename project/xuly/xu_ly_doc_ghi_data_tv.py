import os
from datetime import datetime
import json

thu_muc_cty = 'project/static/du_lieu/Cong_ty/'
thu_muc_tv = 'project/static/du_lieu/tivi'

def doc_thong_tin_tv(ma_so):
    path = thu_muc_tv + ma_so +'.json'

    if os.path.exists(path):
        f= open(path, 'r', encoding='utf-8')
        tv = json.load(f)
        f.close()

    return tv

def ghi_thong_tin_tv(ma_so, dic):
    path = thu_muc_tv + ma_so +'.json'

    if os.path.exists(path):
        f = open(path, 'w', encoding='utf-8')
        json.dump(dic, f, indent= 4, ensure_ascii=False)
        f.close()

