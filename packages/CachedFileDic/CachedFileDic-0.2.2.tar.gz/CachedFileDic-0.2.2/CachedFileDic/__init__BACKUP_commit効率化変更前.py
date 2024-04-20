
# 高速辞書DB [CachedFileDic]

import os
import sys
import fies
import atexit
import pickle
import slim_id
from sout import sout

# プログラム終了時にcommitを実行する
commit_target_ls = []	# コミット対象
def cleanup():
	for db in commit_target_ls: db.commit()
# プログラム終了時に呼び出す関数を登録
atexit.register(cleanup)

# 初期化済みではない場合に初期化
def init_db(db_dir_name, fmt):
	# 初期化済みかどうかを判断
	index_filename = os.path.join(db_dir_name, f"index.{fmt}")
	if os.path.exists(index_filename) is True: return None
	# 初期化
	if os.path.exists(db_dir_name) is False:
		os.makedirs(db_dir_name)
	fies[db_dir_name][f"index.{fmt}"] = {
		"latest_cont": "cont_eden",	# 書き込み対象コンテナ
		"latest_cont_size": 0,	# 書き込み対象コンテナの容量
		"cont_idx": {}	# データは0件
	}
	fies[db_dir_name][f"cont_eden.{fmt}"] = {}

# 高速辞書DB [CachedFileDic]
class DB:
	# 初期化処理
	def __init__(self,
		dir_name,	# データベースディレクトリ
		fmt = "fpkl",	# バックエンドのファイル形式 (fpkl: fast-pickle(default), pickle: pickle)
		cont_size_th = 100 * 1024 ** 2,	# コンテナサイズ目安
		cache_n = 3	# 最大loadコンテナ数
	):
		self.fmt = fmt
		self.dir_name = dir_name
		self.cont_size_th = cont_size_th	# コンテナサイズ目安
		init_db(self.dir_name, self.fmt)	# 初期化済みではない場合に初期化
		self.index = fies[self.dir_name][f"index.{self.fmt}"]
		self.loaded_cont_dic = {}	# 現在メモリにloadされているコンテナの一覧
		self.priority_idx_dic = {}	# 現在メモリにloadされているコンテナの優先順位インデックス辞書
		self.cache_n = cache_n	# 最大loadコンテナ数
		commit_target_ls.append(self)	# 終了時に強制コミットするオブジェクトの一覧に登録
	# データ読み出し [CachedFileDic]
	def __getitem__(self, key):
		# コンテナ名の特定
		cont_name = self.index["cont_idx"][key]
		# コンテナの読み込み (cache付き)
		cont = self.get_container(cont_name)
		# データを返す
		raw_data = cont[key]
		return pickle.loads(raw_data)
	# データ書き込み [CachedFileDic]
	def __setitem__(self, key, value):
		# すでに存在するkeyの場合
		if key in self: raise Exception("[error] Updateは未実装です。")
		# コンテナの読み込み
		cont_name = self.index["latest_cont"]	# 書き込み対象コンテナ
		cont = self.get_container(cont_name)	# コンテナの読み込み (cache付き)
		# データ追記 (データの保存は次に別のコンテナが読み込まれたときに自動的に実施される)
		data = pickle.dumps(value)
		cont[key] = data
		self.index["cont_idx"][key] = cont_name
		self.index["latest_cont_size"] += len(data)
		# spill処理 (データが規定容量を超えたら、latest_contとして新しいコンテナを設定)
		self.spill()
	# key存在確認 [CachedFileDic]
	def __contains__(self, key): return (key in self.index["cont_idx"])
	# for文での利用
	def __iter__(self): return iter(self.index["cont_idx"])
	# 要素数取得
	def __len__(self): return len(self.index["cont_idx"])
	# 強制保存 (コミット) [CachedFileDic]
	def commit(self):
		# インデックスを保存
		fies[self.dir_name][f"index.{self.fmt}"] = self.index
		# すべてのload済みコンテナを保存
		for cont_name in self.loaded_cont_dic:
			self.save_container(cont_name)	# コンテナ保存 (手元にあるコンテナを補助記憶装置 (HDD等) に保存する)
	# コンテナ保存 (指定されたコンテナを補助記憶装置 (HDD等) に保存する)
	def save_container(self, cont_name):
		fies[self.dir_name][f"{cont_name}.{self.fmt}"] = self.loaded_cont_dic[cont_name]
	# コンテナの読み込み (cache付き)
	def get_container(self, cont_name):
		# コンテナが未loadの場合
		if cont_name not in self.loaded_cont_dic:
			# コンテナを空ける (cache_nの上限ギリギリの場合は優先されないコンテナを保存して削除)
			self._reduce_container()
			# コンテナをloadする (注意: 優先度は次の行で書き込まれる)
			self.loaded_cont_dic[cont_name] = fies[self.dir_name][f"{cont_name}.{self.fmt}"]
		# cont_nameで指定されたものがもっとも最近使われたものとして、優先度を上昇させる
		self.priority_idx_dic[cont_name] = self._max_priority() + 1	# 最優先idxの取得
		# cacheから返す
		return self.loaded_cont_dic[cont_name]
	# spill処理 (データが規定容量を超えたら、latest_contとして新しいコンテナを設定)
	def spill(self):
		# 溢れていない場合は何もしない
		if self.index["latest_cont_size"] <= self.cont_size_th: return None
		# 新しいコンテナを作成
		def exists(new_id): return os.path.exists(os.path.join(self.dir_name, f"cont_{new_id}.{self.fmt}"))
		new_cont_name = "cont_" + slim_id.gen(exists, length = 1)
		self.index["latest_cont"] = new_cont_name	# 書き込み対象コンテナの更新
		self.index["latest_cont_size"] = 0	# 新コンテナの容量
		fies[self.dir_name][f"{new_cont_name}.{self.fmt}"] = {}
	# 最優先idxの取得
	def _max_priority(self):
		if len(self.priority_idx_dic) == 0: return 0
		return max([self.priority_idx_dic[k] for k in self.priority_idx_dic])
	# コンテナを空ける (cache_nの上限ギリギリの場合は優先されないコンテナを保存して削除)
	def _reduce_container(self):
		# load数にまだ余裕があるときは何もしない
		if len(self.loaded_cont_dic) < self.cache_n: return None
		# 最も優先されないコンテナを見つける
		target_cont_name = min(self.priority_idx_dic,
			key = lambda cont_name: self.priority_idx_dic[cont_name])
		# コンテナ保存 (指定されたコンテナを補助記憶装置 (HDD等) に保存する)
		self.save_container(target_cont_name)
		# メモリ上から削除
		del self.loaded_cont_dic[target_cont_name]
		del self.priority_idx_dic[target_cont_name]

# 対象ディレクトリに接続 [CachedFileDic]
def conn(dir_name,
	fmt = "fpkl",	# バックエンドのファイル形式 (fpkl: fast-pickle(default), pickle: pickle)
	cont_size_th = 100 * 1024 ** 2,	# コンテナサイズ目安
	cache_n = 3	# 最大loadコンテナ数
):
	db = DB(dir_name,
		fmt = fmt,
		cont_size_th = cont_size_th, cache_n = cache_n
	)
	return db
