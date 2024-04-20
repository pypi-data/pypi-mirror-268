
# 高速辞書DB [CachedFileDic]
# 【動作確認 / 使用例】

import sys
from sout import sout
from tqdm import tqdm
from ezpip import load_develop
# 高速辞書DB [CachedFileDic]
CachedFileDic = load_develop("CachedFileDic", "../", develop_flag = True)

# 対象ディレクトリに接続 [CachedFileDic]
db = CachedFileDic.conn("./data/")

# 存在確認 [CachedFileDic]
if "key1" not in db:
	# データ書き込み [CachedFileDic]
	db["key1"] = "fuga"
# データ読み出し [CachedFileDic]
print(db["key1"])
# 強制commit [CachedFileDic]
db.commit()
# for文での利用
print({k: db[k] for k in db})
sys.exit()

# 大量書き込み
for idx in tqdm(range(2048)):
	# データ書き込み [CachedFileDic]
	db[idx] = "fuga" * (1024 // 4) * 100
# 強制commit [CachedFileDic]
db.commit()
