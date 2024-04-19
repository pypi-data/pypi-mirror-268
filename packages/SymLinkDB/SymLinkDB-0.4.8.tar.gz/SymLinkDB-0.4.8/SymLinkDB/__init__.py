
# 双方向グラフDB [SymLinkDB]

import os
import sys
import fies
import json
import atexit
import pickle
import slim_id
from sout import sout, souts

# 十分な長さの64進idの発行 (uuidの桁数を参考に決定)
def gen_unique_id(): return slim_id.gen(lambda e: False, length = 22)

# プログラム終了時にcommitを実行する
commit_target_dbs = []	# コミット対象
def cleanup():
	for sldb in commit_target_dbs:
		sldb.commit()	# 強制コミット [SymLinkDB]
# プログラム終了時に呼び出す関数を登録
atexit.register(cleanup)

# メモリバックエンドの初期化 [SymLinkDB]
def memory_backend(backend_dir):
	# 単純メモリbackend (SLDB-backend) [memory_backend]
	from .parts import memory_backend as m_back_module
	# メモリバックエンドへの接続 [memory_backend]
	return m_back_module.conn(backend_dir)

# CachedFileDicバックエンドの初期化 [SymLinkDB]
def cfd_backend(backend_dir,
	fmt = "fpkl",	# バックエンドのファイル形式 (fpkl: fast-pickle(default), pickle: pickle)
	cont_size_th = 100 * 1024 ** 2,	# コンテナサイズ目安
	cache_n = 3	# 最大loadコンテナ数
):
	# CachedFileDic-backend (SLDB-backend) [cfd_backend]
	from .parts import cfd_backend as cfd_back_module
	# CachedFileDicバックエンドへの接続 [cfd_backend]
	return cfd_back_module.conn(
		backend_dir,
		fmt = fmt,	# バックエンドのファイル形式 (fpkl: fast-pickle(default), pickle: pickle)
		cont_size_th = cont_size_th,	# コンテナサイズ目安
		cache_n = cache_n	# 最大loadコンテナ数
	)

# SLDB-backendとして初期化
def init_sldb_backend(backend):
	# このバックエンドを一意に特定するID
	backend[("meta", "backend_id")] = gen_unique_id()	# 十分な長さの64進idの発行 (uuidの桁数を参考に決定)
	# このバックエンドに格納されているデータの一覧
	backend[("meta", "backend_contain_data")] = []

# このバックエンドがSLDB-sysとして初期化されているかを判定
def judge_sys_initialized(backend):
	bcd = backend[("meta", "backend_contain_data")]
	# backend_contain_data 内に定義されたsysの数を数える
	sys_n = len([e for e in bcd
		if e["entity_type"] == "SLDB-system"])
	# 数に応じて分岐
	if sys_n == 0: return False
	if sys_n == 1: return True
	raise Exception("[SymLinkDB error] Inconsistency in database structure. (Despite the fact that this version of SymLinkDB can only have one system per backend, multiple systems are defined.)")

# 辞書-likeオブジェクトの所定のkeyのvalue(list)にデータを追加
def back_ls_push(
	target_dic_like,	# 追記対象の辞書-likeオブジェクト
	key,	# 編集対象のkey
	value	# 追記するデータ
):
	target_ls = target_dic_like[key]
	target_ls.append(value)
	target_dic_like[key] = target_ls

# このバックエンドをSLDB-sysとして初期化
def init_sldb_sys(backend):
	# systemの情報を記入
	backend[("meta", "system_contain_data")] = []
	# backend_contain_dataにsysを登録
	back_ls_push(	# 辞書-likeオブジェクトの所定のkeyのvalue(list)にデータを追加
		backend, ("meta", "backend_contain_data"),
		{"entity_type": "SLDB-system"})

# metaのcontain_dataを条件でフィルタリングする
def entity_filter(
	entity_ls,	# entityがたくさん入ったlist (metaのxx_contain_dataなど)
	cond,	# フィルタリング条件
	unique = False	# 検索結果が唯一でないといけないか (True指定の場合は戻り値がentityのリストではなくentityになる)
):
	class VOID: pass	# 他のどの値にも一致しない値 (等価性演算子に対して)
	def check_one(entity):
		for k in cond:
			if entity.get(k, VOID) != cond[k]: return False
		return True
	ret_ls = [e for e in entity_ls
		if check_one(e) is True]
	# uniqueかどうかで返し方を変える
	if unique is True:
		if len(ret_ls) != 1: raise Exception("[SymLinkDB error] The search results of entity_filter() violate the unique constraint.")
		return ret_ls[0]
	else:
		return ret_ls

# あるエンティティについて、バックエンドが整合しているかを確かめる (NGの場合は例外を送出する)
def check_entity_backend(
	filter_condition,	# エンティティのフィルタリング条件 (uniqueになるようなもの)
	sys_backend,	# DB全体情報 (system) が保管されているバックエンド
	table_data_backend,	# テーブルのデータが保管されているバックエンド
):
	# データが格納されているbackend-idが同じかを見る (system側とdata側の記載の整合性)
	sys_entity = entity_filter(sys_backend[("meta", "system_contain_data")],	# metaのcontain_dataを条件でフィルタリングする
		filter_condition, unique = True)
	b_id_A = sys_entity["data_backend_id"]
	b_id_B = (table_data_backend[("meta", "backend_id")]
		if (("meta", "backend_id") in table_data_backend) else None)	# backendが未初期化の場合も想定
	if b_id_A == b_id_B: return True
	raise Exception(f"[SymLinkDB error] The entityfilter_condition is already initialized, but there is no data in the specified backend. Please specify the correct backend. (Correct backend ID = {b_id_A})")

# search_keysの整合性を確認
def check_search_keys(
	search_keys,	# チェック対象のsearch_keys
	table_name,	# テーブル名
	system_contain_data,	# 該当sysの内容物一覧
):
	# 該当テーブルの情報を取得
	tbl_entity = entity_filter(system_contain_data,	# metaのcontain_dataを条件でフィルタリングする
		{"entity_type": "SLDB-table", "table_name": table_name}, unique = True)
	# 整合性違反の場合は例外を送出する
	ls_2_set = lambda e: (set(e) if type(e) == type([]) else e)
	a = ls_2_set(search_keys)
	b = ls_2_set(tbl_entity["search_keys"])
	if a != b: raise Exception("[SymLinkDB error] It differs from the search_keys defined initially.")

# テーブル新規作成処理
def create_table(
	table_name,	# テーブル名
	search_keys,	# 検索用に使いたい列名
	sys_backend,	# DB全体情報 (system) を保管するバックエンド
	table_data_backend,	# テーブルのデータを保管するバックエンド
):
	# table初期化不整合チェック
	filtered_entities = entity_filter(table_data_backend[("meta", "backend_contain_data")],
		{"table_name": table_name, "sys_backend_id": sys_backend[("meta", "backend_id")]})
	if len(filtered_entities) > 0: raise Exception("[SymLinkDB error] Inconsistency in the stored table information. According to the information on the DB-system side, the table that is currently being created is uninitialized, but within the backend that stores the table, it is already initialized. Degradation in material management is suspected.")
	# search_keysの形式チェック
	if search_keys is not None:
		if type(search_keys) != type([]): raise Exception("[SymLinkDB error] Please specify search_key in the form of a list of strings.")
		for e in search_keys:
			if type(e) != type(""): raise Exception("[SymLinkDB error] Please specify search_key in the form of a list of strings.")
	# table情報
	table_data = {
		"entity_type": "SLDB-table",
		"table_id": gen_unique_id(),	# 十分な長さの64進idの発行 (uuidの桁数を参考に決定)
		"sys_backend_id": sys_backend[("meta", "backend_id")],
		"data_backend_id": table_data_backend[("meta", "backend_id")],
		"table_name": table_name,
		"search_keys": search_keys,
	}
	# systemにtable情報を書き込む
	back_ls_push(	# 辞書-likeオブジェクトの所定のkeyのvalue(list)にデータを追加
		sys_backend, ("meta", "system_contain_data"),
		table_data)
	# backendにtable情報を書き込む
	back_ls_push(	# 辞書-likeオブジェクトの所定のkeyのvalue(list)にデータを追加
		table_data_backend, ("meta", "backend_contain_data"),
		table_data)
	# レコード数・レコード一覧を書き込む
	table_data_backend[("table_info", "all_rec_ids", table_data["table_id"])] = {}	# レコード数0
	table_data_backend[("table_info", "rec_n", table_data["table_id"])] = 0	# レコード数0

# 辞書-likeオブジェクトの所定keyのvalueを編集
def dic_like_edit(
	dic_like_obj, key,
	edit_func	# 値を編集する関数 (今の値を受け取って更新後の値を返す)
):
	dic_like_obj[key] = edit_func(dic_like_obj[key])

# レコード一覧を表した要約文字列の生成
def gen_recs_str(table):
	for rec in table: break	# table内のrec_idの一例を取り出す処理
	if len(table) == 0:
		inner = ""
	elif len(table) == 1:
		inner = f'"{rec.id}": <Rec {souts(rec.data)}>'
	else:
		inner = f'"{rec.id}": <Rec {souts(rec.data)}>, ... (n = {len(table)})'
	return "{"+ inner +"}"

# role指定からlink_table_nameを特定 (role指定が曖昧な場合は例外を投げる)
def role_to_link_name(
	obj_role,	# 相手のrole
	subj_table_id,	# 自分のtable_id
	sys_backend	# システムバックエンド
):
	# link_tableのentityのみに絞り込み
	lt_entities = entity_filter(sys_backend[("meta", "system_contain_data")],
		{"entity_type": "SLDB-link-table"})
	# roleとtable_idで絞り込み (両側見る)
	filtered_tn_ls = []
	for entity in lt_entities:
		role_0, role_1 = entity["rel_table_info"]
		for subj_dic, obj_dic in [(role_0, role_1), (role_1, role_0)]:
			# 一致しないものは除外
			if subj_dic["table_id"] != subj_table_id: continue
			if obj_dic["role"] != obj_role: continue
			# 候補の格納
			filtered_tn_ls.append(entity["link_table_name"])
	# 候補が唯一かどうかを確認して返す
	if len(filtered_tn_ls) > 1: raise Exception("[SymLinkDB error] Ambiguous link identification information is specified, and the link cannot be uniquely determined. If you have not specified the name of the link table, please consider specifying it.")
	if len(filtered_tn_ls) == 0: raise Exception("[SymLinkDB error] The role specification is invalid. There is no corresponding link.")
	link_table_name = filtered_tn_ls[0]
	return link_table_name

# role, link_table_name からlink特定情報を取得する
def get_link_info_core(link_table_name, role, table_id, sys_backend):
	# link_table_nameで絞り込み
	entity = entity_filter(sys_backend[("meta", "system_contain_data")],
		{"entity_type": "SLDB-link-table", "sys_backend_id": sys_backend[("meta", "backend_id")], "link_table_name": link_table_name},
		unique = True)
	# 対象tableがどちら側かを検索 (両側同一tableである可能性があることに注意)
	role_0, role_1 = entity["rel_table_info"]
	suspect_role = None	# 書き間違い疑いのrole名
	for subj_role, obj_role in [(role_0, role_1), (role_1, role_0)]:
		# 一致を確認
		if subj_role["table_id"] != table_id: continue
		if obj_role["role"] != role:
			suspect_role = obj_role["role"]
			continue
		# 情報を返す
		return {
			"link_table_id": entity["link_table_id"],
			"link_table_name": entity["link_table_name"],
			"subj_role_info": subj_role, "obj_role_info": obj_role,
		}
	# 不整合エラー
	if suspect_role is not None:
		raise Exception(f'[SymLinkDB error] The specified role name does not match. ("{suspect_role}" is suspected to be the correct role name)')
	raise Exception("[SymLinkDB error] The specified link_table_name does not have a relationship with the specified table.")

# role名あるいはrole名とlink table名からlink情報を取得
def get_link_info(query, table_id, system_backend):
	# roleのみで指定している場合 -> 完全な指定に変換
	if type(query) == type(""):
		role = query
		link_table_name = role_to_link_name(obj_role = role, subj_table_id = table_id, sys_backend = system_backend)	# role指定からlink_table_nameを特定 (role指定が曖昧な場合は例外を投げる)
		query = (link_table_name, role)	# 完全な指定に変換
	# 「完全な指定」の形式をチェック
	if type(query) != type(tuple()) or len(query) != 2: raise Exception("[SymLinkDB error] invalid type")
	# 「完全な指定」によるlink特定情報の取得
	link_table_name, role = query
	return get_link_info_core(link_table_name, role, table_id, system_backend)	# role, link_table_name からlink特定情報を取得する

# 1-Nチェック (片側; 制約違反の場合は例外を投げる)
def check_1N(
	subj,	# 「自分側」の情報 (rec_idとrole_info3つ)
	obj,	# 「相手側」の情報 (rec_idとrole_info3つ)
	link_table_backend,	# link tableの入っているバックエンド
	link_table_id	# link table ID
):
	# Nの場合はどんな場合もOK
	if obj["1-N"] == "N": return True
	# 1Nルール指定が不正な場合
	if obj["1-N"] != "1": raise Exception('[SymLinkDB error] Incorrect rule notation: Please specify either "1" or "N"')
	# 1の場合のチェック
	key = ("link_rec", link_table_id, subj["role"], obj["role"], subj["table_id"], subj["rec_id"])
	now_n = (len(link_table_backend[key]) if key in link_table_backend else 0)
	if now_n + 1 > 1: raise Exception("[SymLinkDB error] Violation of 1-N constraint")

# 片側のリンク追加
def add_link(
	subj,	# 「自分側」の情報 (rec_idとrole_info3つ)
	obj,	# 「相手側」の情報 (rec_idとrole_info3つ)
	link_table_backend,	# link tableの入っているバックエンド
	link_table_id,	# link table ID
):
	key = ("link_rec", link_table_id, subj["role"], obj["role"], subj["table_id"], subj["rec_id"])
	# keyがまだ存在しない場合は空のレコードを追加
	if key not in link_table_backend: link_table_backend[key] = []
	# 辞書-likeオブジェクトの所定のkeyのvalue(list)にデータを追加
	back_ls_push(link_table_backend, key, (obj["table_id"], obj["rec_id"]))

# 双方向にリンクを追加
def add_sym_link(
	subj,	# 「自分側」の情報 (rec_idとrole_info3つ)
	obj,	# 「相手側」の情報 (rec_idとrole_info3つ)
	link_table_backend,	# link tableの入っているバックエンド
	link_table_id,	# link table ID
):
	# 1-Nチェック (片側; 制約違反の場合は例外を投げる)
	check_1N(subj, obj, link_table_backend, link_table_id)
	check_1N(obj, subj, link_table_backend, link_table_id)	# 1-Nチェック (片側; 制約違反の場合は例外を投げる)
	# 両側のリンクを追加
	add_link(subj, obj, link_table_backend, link_table_id)	# 片側のリンク追加
	add_link(obj, subj, link_table_backend, link_table_id)	# 片側のリンク追加

# rec指定をrec_id指定に統一化 (どちらでもないtypeは例外を投げる)
def to_rec_id(original_query):
	# rec_id指定の場合
	if type(original_query) == type(""): return original_query
	# レコード型の場合
	if original_query.__class__ == Record: return original_query.id
	# 想定外の型の場合
	raise Exception("[SymLinkDB error] invalid type.")

# 自分側のリンクから相手への参照を削除
def delete_link(subj, obj, link_table_backend, link_table_id):
	backend_key = ("link_rec", link_table_id,
		subj["role"], obj["role"],
		subj["table_id"], subj["rec_id"])
	# 元々のレコード一覧を取得 (tableID, recIDの組のリスト)
	org_link_ls = link_table_backend[backend_key]
	# 削除対象のレコード以外を書き戻す
	new_link_ls = []
	for table_id, rec_id in org_link_ls:
		if (table_id == obj["table_id"]) and (rec_id == obj["rec_id"]): continue
		new_link_ls.append((table_id, rec_id))
	link_table_backend[backend_key] = new_link_ls
	# 削除できていない場合に例外を出す
	if len(new_link_ls) == len(org_link_ls):
		raise Exception("[SymLinkDB error] Unable to delete the link. There may be internal data inconsistency.")
	# 空のlink_recになったら、link_recそのものを削除 (注意：linkが関係するレコード自身が削除されたときにゴミが残ること等を避けるため)
	if len(new_link_ls) == 0: del link_table_backend[backend_key]

# 双方向にリンクを削除
def delete_sym_link(
	subj,	# 「自分側」の情報 (rec_idとrole_info3つ)
	obj,	# 「相手側」の情報 (rec_idとrole_info3つ)
	link_table_backend,	# link tableの入っているバックエンド
	link_table_id,	# link table ID
):
	# 自分側のリンクから相手への参照を削除
	delete_link(subj, obj,
		link_table_backend = link_table_backend,
		link_table_id = link_table_id)
	# 相手側のリンクから自分への参照を削除
	delete_link(obj, subj,
		link_table_backend = link_table_backend,
		link_table_id = link_table_id)

# LinkSetクラス [SymLinkDB]
class LinkSet:
	# 初期化処理
	def __init__(self,
		link_table_id,	# link table ID
		link_table_name,	# link table名
		subj_role_info,	# 自roleの情報
		obj_role_info,	# 相手側roleの情報
		rec	# recオブジェクト
	):
		# リンクを特定する情報の登録
		self.link_table_id = link_table_id
		self.link_table_name = link_table_name
		self.subj_role_info = subj_role_info
		self.obj_role_info = obj_role_info
		# 所属するrecやsldbに関する情報の登録
		self.rec = rec
		self.sldb = self.rec.table.sldb
		# link tableの入っているバックエンドの参照を登録
		if self.link_table_name not in self.sldb.loaded_link_tables_dic: raise Exception(f"[SymLinkDB error] specified link table not loaded (link table name = {self.link_table_name})")
		self.link_table_backend = self.sldb.loaded_link_tables_dic[self.link_table_name]
		self.backend_key = ("link_rec", self.link_table_id,
			self.subj_role_info["role"], self.obj_role_info["role"],
			self.subj_role_info["table_id"], self.rec.id)
	# linkの追加 [SymLinkDB]
	def push(self, obj_rec_id):
		if type(obj_rec_id) in [type([]), tuple]:
			for one_id in obj_rec_id: self.push(one_id)
			return None
		# 単一要素をpushする場合
		obj_rec_id = to_rec_id(obj_rec_id)	# rec指定をrec_id指定に統一化 (どちらでもないtypeは例外を投げる)
		obj_table = self.sldb.get_table_by_id(self.obj_role_info["table_id"])	# table_idからTableオブジェクトを引き当て
		if obj_rec_id not in obj_table: raise Exception("[SymLinkDB error] specified record ID does not exist in the table")	# 指定されたrec idが正しくobj tableに存在するかを確認
		if obj_rec_id in self: raise Exception("[SymLinkDB error] This is a link that has already been added")
		# 双方向にリンクを追加
		add_sym_link(
			subj = {"rec_id": self.rec.id, **self.subj_role_info},	# 「自分側」の情報 (rec_idとrole_info3つ)
			obj = {"rec_id": obj_rec_id, **self.obj_role_info},	# 「相手側」の情報 (rec_idとrole_info3つ)
			link_table_backend = self.link_table_backend,	# link tableの入っているバックエンド
			link_table_id = self.link_table_id,	# link table ID
		)
	# linkの存在確認 [SymLinkDB]
	def __contains__(self, obj_rec_id):
		value = (self.obj_role_info["table_id"], to_rec_id(obj_rec_id))	# rec指定をrec_id指定に統一化 (どちらでもないtypeは例外を投げる)
		return (value in self.__get_links())
	# linkの削除 [SymLinkDB]
	def __delitem__(self, obj_rec_id):
		if type(obj_rec_id) in [type([]), tuple]:
			for one_id in obj_rec_id: del self[one_id]
			return None
		# 単一要素をdeleteする場合
		obj_rec_id = to_rec_id(obj_rec_id)	# rec指定をrec_id指定に統一化 (どちらでもないtypeは例外を投げる)
		if obj_rec_id not in self:	# 現在対象としているレコード (subj_rec) が対象としているlink_tableのリンクをそもそも持っていない場合
			raise Exception("[SymLinkDB error] You cannot delete a link that does not exist")
		# 双方向にリンクを削除
		delete_sym_link(
			subj = {"rec_id": self.rec.id, **self.subj_role_info},	# 「自分側」の情報 (rec_idとrole_info3つ)
			obj = {"rec_id": obj_rec_id, **self.obj_role_info},	# 「相手側」の情報 (rec_idとrole_info3つ)
			link_table_backend = self.link_table_backend,	# link tableの入っているバックエンド
			link_table_id = self.link_table_id,	# link table ID
		)
	# link_set内の要素をイテレート [SymLinkDB]
	def __iter__(self):
		obj_table = None
		for table_id, rec_id in self.__get_links():	# 対象のrecが持っているリンク一覧の取得
			if obj_table is None:
				obj_table = self.sldb.get_table_by_id(table_id)	# table_idからTableオブジェクトを引き当て
			yield obj_table[rec_id]
	# link_set内の要素数を取得 [SymLinkDB]
	def __len__(self): return len(self.__get_links())	# 対象のrecが持っているリンク一覧の取得
	# 対象のrecが持っているリンク一覧の取得
	def __get_links(self):
		if self.backend_key not in self.link_table_backend: return []
		return self.link_table_backend[self.backend_key]
	# 文字列化 (その1, その2)
	def __str__(self):
		subj_t_name = self.sldb.get_table_by_id(self.subj_role_info['table_id']).table_name	# table_idからTableオブジェクトを引き当て
		obj_t_name = self.sldb.get_table_by_id(self.obj_role_info['table_id']).table_name	# table_idからTableオブジェクトを引き当て
		return (
			f"<LinkSet {self.link_table_name}: " +
			f"{subj_t_name}({self.subj_role_info['role']};{self.subj_role_info['1-N']}) -> " +
			f"{obj_t_name}({self.obj_role_info['role']};{self.obj_role_info['1-N']};n={len(self)})>"
		)
	def __repr__(self): return str(self)

# レコードクラス [SymLinkDB]
class Record:
	# 初期化処理
	def __init__(self, rec_id, table):
		# レコードに関する情報の登録
		self.id = rec_id
		# 所属するtableに関する情報の登録
		self.table = table
		self.table_name = table.table_name
		self.table_id = table.table_id
	# dataのgetter
	@property
	def data(self):
		self.is_deleted(raise_err = True)	# 自身が削除済みかどうかを判定
		return self.table.backend[("rec", self.table_id, self.id)]["data"]
	# dataのsetter
	@data.setter
	def data(self, new_data):
		self.is_deleted(raise_err = True)	# 自身が削除済みかどうかを判定
		# dataが正しく検索キーを持っているか確認する
		if self.table.search_keys is not None: check_data_format(new_data, self.table.search_keys)
		# バックエンドへの書き込み
		old_data = self.table.backend[("rec", self.table_id, self.id)]["data"]
		def add_data(v):
			v["data"] = new_data
			return v
		dic_like_edit(	# 辞書-likeオブジェクトの所定keyのvalueを編集
			self.table.backend, key = ("rec", self.table_id, self.id),
			edit_func = add_data)
		# 検索インデックス関連
		if self.table.search_keys is not None:
			# 検索インデックスの削除
			del_search_idx(old_data, self.table.search_keys, self.table_id, self.id, self.table.backend)
			# 検索インデックスの追加
			add_search_idx(new_data, self.table.search_keys, self.table_id, self.id, self.table.backend)
	# link_setの取得 [SymLinkDB]
	def __getitem__(self, query):
		self.is_deleted(raise_err = True)	# 自身が削除済みかどうかを判定
		# 注意: 「必要な情報はメモリではなくbackendから都度請求する」という設計思想に基づき、キャッシュ化を使わない
		# # クエリからlink情報取得 (キャッシュ化バージョン; クエリは「role名」または「関係名, role名」)
		# link_info = self.table.cached_link_info_getter(query)
		# クエリからlink情報取得 (クエリは「role名」または「関係名, role名」)
		link_info = get_link_info(query, self.table_id, self.table.sldb.backend)	# role名あるいはrole名とlink table名からlink情報を取得
		# LinkSetオブジェクトを作成して返す
		return LinkSet(	# LinkSetクラス [SymLinkDB]
			link_info["link_table_id"],	# link table ID
			link_info["link_table_name"],	# link table名
			subj_role_info = link_info["subj_role_info"],	# 自roleの情報
			obj_role_info = link_info["obj_role_info"],	# 相手側roleの情報
			rec = self)	# linkオブジェクト
	# 文字列化 (その1, その2)
	def __str__(self):
		if self.is_deleted() is True: return "<SymLinkRecord (deleted)>"	# 自身が削除済みかどうかを判定
		links = souts(list(self), None)
		return f"<SymLinkRecord {self.table_name}.{self.id} data = {souts(self.data)} links = {links}>"
	def __repr__(self): return str(self)
	# link一覧をイテレートして取得 [SymLinkDB]
	def __iter__(self):
		self.is_deleted(raise_err = True)	# 自身が削除済みかどうかを判定
		# link_tableのentityのみに絞り込み
		sys_backend = self.table.sldb.backend
		lt_entities = entity_filter(self.table.sldb.backend[("meta", "system_contain_data")],
			{"entity_type": "SLDB-link-table", "sys_backend_id": sys_backend[("meta", "backend_id")]})
		# 全linkを確認し、自recに関係するものをiterする (両側確認)
		for entity in lt_entities:
			link_table_name = entity["link_table_name"]
			for role_dic in entity["rel_table_info"]:
				key = (link_table_name, role_dic["role"])
				if key in self: yield key
	# 指定されたlinkの存在確認 [SymLinkDB]
	def __contains__(self, query):
		self.is_deleted(raise_err = True)	# 自身が削除済みかどうかを判定
		try:
			self[query]
			return True
		except:
			return False
	# 自身が削除済みかどうかを判定
	def is_deleted(self, raise_err = False):
		deleted = (self.id not in self.table)
		if deleted is True and raise_err is True: raise Exception("[SymLinkDB error] This record is already deleted.")
		return deleted

# dataが正しく検索キーを持っているか確認する
def check_data_format(data, search_keys):
	# 辞書形式でない場合はエラー
	if type(data) != type({}):
		raise Exception("[SymLinkDB error] Insert data in dictionary format into the table where the search_key is set.")
	# search_keyを1つでも持たない場合はエラー
	for key in search_keys:
		if key not in data: 
			raise Exception("[SymLinkDB error] Specified search_key is not included.")
	return True

# 検索対象データをjson文字列にする
def to_json_str(arg_data):
	try:
		return json.dumps(arg_data, sort_keys=True)
	except TypeError as e:
		raise Exception(f"[SymLinkDB error] Value of the search_key must be JSON-able\n{e}")

# 検索インデックスの追加
def add_search_idx(data, search_keys, table_id, rec_id, backend):
	for key in search_keys:
		# 該当keyの値をjson文字列にする
		val_str = to_json_str(data[key])	# 検索対象データをjson文字列にする
		# 値が既にインデックスとして初期化されていない場合は初期化
		idx_key = ("search_idx", table_id, key, val_str)
		if idx_key not in backend: backend[idx_key] = {}
		# バックエンドへの追加
		def add_key(v):
			v[rec_id] = True
			return v
		dic_like_edit(	# 辞書-likeオブジェクトの所定keyのvalueを編集
			backend, key = idx_key,
			edit_func = add_key)

# 検索インデックスの削除
def del_search_idx(data, search_keys, table_id, rec_id, backend):
	for key in search_keys:
		# 該当keyの値をjson文字列にする
		val_str = to_json_str(data[key])	# 検索対象データをjson文字列にする
		# バックエンドからの削除
		def del_key(v):
			del v[rec_id]
			return v
		dic_like_edit(	# 辞書-likeオブジェクトの所定keyのvalueを編集
			backend, key = ("search_idx", table_id, key, val_str),
			edit_func = del_key)

# リストの共通要素を見つける
def find_common_elements(id_dic_ls):
	if len(id_dic_ls) == 0: raise Exceprion("[SymLinkDB error] Unexpected error in the program.")
	# 最初の辞書を共通要素の候補とする
	common_elements = set(id_dic_ls[0])
	# 残りのリストに対して共通要素を探す
	for id_dic in id_dic_ls[1:]:
	    common_elements.intersection_update(id_dic)
	# 共通要素をリストとして返す
	return list(common_elements)

# Tableクラス
class Table:
	# 初期化処理 (table自体を作る処理はすでに実行されている想定)
	def __init__(self,
		table_name,	# table名
		table_id,	# table-ID
		search_keys, # 検索用に使える列名
		backend,	# tableのデータが存在するbackend
		sldb	# 所属するsldbオブジェクト
	):
		self.table_name = table_name
		self.table_id = table_id
		self.search_keys = search_keys
		self.backend = backend
		self.sldb = sldb
		# link_infoのcache (rec[role]等のlink_set取得が重いため、高速化するためのキャッシュ)
		self.link_info_cache = {}
	# レコードの新規作成 [SymLinkDB]
	def create(self, data, links = None):
		# dataが正しく検索キーを持っているか確認する
		if self.search_keys is not None: check_data_format(data, self.search_keys)
		# linksが省略された場合
		if links is None: links = {}
		# rec_idの発行
		rec_id = slim_id.gen(lambda arg_id: (arg_id in self))
		# レコードデータをbackendに書き込み
		self.backend[("rec", self.table_id, rec_id)] = {"data": data}
		# id一覧に書き込み
		def add_key(v):
			v[rec_id] = True
			return v
		dic_like_edit(	# 辞書-likeオブジェクトの所定keyのvalueを編集
			self.backend, key = ("table_info", "all_rec_ids", self.table_id),
			edit_func = add_key)
		# レコード数の更新
		dic_like_edit(	# 辞書-likeオブジェクトの所定keyのvalueを編集
			self.backend, key = ("table_info", "rec_n", self.table_id),
			edit_func = lambda v: v + 1)
		# 検索インデックスの追加
		if self.search_keys is not None:
			add_search_idx(data, self.search_keys, self.table_id, rec_id, self.backend)
		# link情報の書き込み
		new_rec = self[rec_id]	# 新しく生成したレコード
		for query in links:
			if links[query] is None: continue
			new_rec[query].push(links[query])
		# 新規生成したrec_idを返す
		return self[rec_id]
	# レコードの取得 [SymLinkDB]
	def __getitem__(self, rec_id):
		# 検索条件での指定
		if type(rec_id) == type({}):
			rec_ls = self.search_rec(search_cond_dic = rec_id)	# 検索条件でレコードIDを取得
			return rec_ls
		# 単一要素を処理する場合
		rec_id = to_rec_id(rec_id)	# rec指定をrec_id指定に統一化 (どちらでもないtypeは例外を投げる)
		return Record(rec_id, table = self)	# レコードクラス [SymLinkDB]
	# レコードの存在確認 [SymLinkDB]
	def __contains__(self, rec_id):
		rec_id = to_rec_id(rec_id)	# rec指定をrec_id指定に統一化 (どちらでもないtypeは例外を投げる)
		return (("rec", self.table_id, rec_id) in self.backend)
	# レコード数取得 [SymLinkDB]
	def __len__(self): return self.backend[("table_info", "rec_n", self.table_id)]
	# tableのイテレート [SymLinkDB]
	def __iter__(self):
		for rec_id in self.backend[("table_info", "all_rec_ids", self.table_id)]:
			yield self[rec_id]
	# レコードの削除 [SymLinkDB]
	def __delitem__(self, rec_id):
		rec_id = to_rec_id(rec_id)	# rec指定をrec_id指定に統一化 (どちらでもないtypeは例外を投げる)
		if rec_id not in self: raise Exception("[SymLinkDB error] You cannot delete a record that does not exist")
		# 削除対象が関係するリンクの削除
		rec = self[rec_id]
		for link_query in rec:
			link_set = rec[link_query]
			for obs_rec in link_set: del link_set[obs_rec]
		# 検索インデックスの削除
		if self.search_keys is not None:
			del_search_idx(rec.data, self.search_keys, self.table_id, rec_id, self.backend)
		# レコード記録本体の削除
		del self.backend[("rec", self.table_id, rec_id)]
		# id一覧から削除
		def del_key(v):
			del v[rec_id]
			return v
		dic_like_edit(	# 辞書-likeオブジェクトの所定keyのvalueを編集
			self.backend, key = ("table_info", "all_rec_ids", self.table_id),
			edit_func = del_key)
		# レコード数の更新 (デクリメント)
		dic_like_edit(	# 辞書-likeオブジェクトの所定keyのvalueを編集
			self.backend, key = ("table_info", "rec_n", self.table_id),
			edit_func = lambda v: v - 1)
	# 検索条件でレコードIDを取得
	def search_rec(self, search_cond_dic):
		if len(search_cond_dic) == 0: raise Exception("[SymLinkDB error] Please specify one or more keys for the search condition.")
		cand_ls = []
		for search_key in search_cond_dic:
			if search_key not in self.search_keys: raise Exception("[SymLinkDB error] You cannot search by a key that is not specified as the search_key during load_table.")
			# 該当keyの値をjson文字列にする
			search_val_str = to_json_str(search_cond_dic[search_key])	# 検索対象データをjson文字列にする
			# rec_id候補を取得する
			idx_key = ("search_idx", self.table_id, search_key, search_val_str)
			if idx_key not in self.backend: return []	# 値がそもそもインデックスとして初期化されていない場合
			cand_ls.append(self.backend[idx_key])
		# すべての検索条件に合致するrec_idに絞り込む
		rec_id_ls = find_common_elements(cand_ls)	# リストの共通要素を見つける
		# recを取得して返す
		return [self[rec_id] for rec_id in rec_id_ls]	# レコードの取得 [SymLinkDB]
	# 文字列化 (その1, その2)
	def __str__(self):
		recs_str = gen_recs_str(self)	# レコード一覧を表した要約文字列の生成
		return f"<SymLinkTable {self.table_name} recs = {recs_str} search_keys = {souts(self.search_keys, 3)} >"
	def __repr__(self): return str(self)
	# クエリからlink情報取得 (キャッシュ化バージョン; クエリは「role名」または「関係名, role名」)
	def cached_link_info_getter(self, query):
		if query not in self.link_info_cache:
			# role名あるいはrole名とlink table名からlink情報を取得
			self.link_info_cache[query] = get_link_info(query, self.table_id, self.sldb.backend)
		return self.link_info_cache[query]

# versionの書き換え
def rewrite_data_version(backend, target_key, filter_condition, new_ver_str):
	old_value = backend[target_key]
	def rewriter(entity):
		entity["data_version"] = new_ver_str
		return entity
	def judge_func(entity):
		for k in filter_condition:
			if k not in entity: return False
			if entity[k] != filter_condition[k]: return False
		return True
	new_value = [
		(rewriter(e) if judge_func(e) else e)
		for e in old_value]
	backend[target_key] = new_value

# keyが旧形式の場合にデータを修正する (同一table内リンクにおいてリンクが両方向に増殖するバグに関連)
def link_dup_bug_fix(
	filter_condition,	# エンティティのフィルタリング条件 (uniqueになるようなもの)
	sys_backend,	# DB全体情報 (system) を保管するバックエンド
	table_data_backend,	# テーブルのデータを保管するバックエンド
):
	# バージョンを確認 (修正要否を判断)
	entity = entity_filter(sys_backend[("meta", "system_contain_data")],	# link_tableのentityのみに絞り込み
		filter_condition, unique = True)
	data_version = entity.get("data_version", "with_same_table_link_duplication_bug_ver")
	if data_version != "with_same_table_link_duplication_bug_ver": return "no_fix_needed"
	# 修正
	keys = list(table_data_backend)
	for key in keys:
		# 対象の絞り込み (link_table_idが一致するlink_rec)
		if type(key) != tuple: continue
		if key[:2] != ("link_rec", entity["link_table_id"]): continue
		# データ形式が想定外の場合
		if len(key) != 4: raise Exception("unknown error has occurred.")
		# 新形式のkeyに書き換え
		value = table_data_backend[key]
		del table_data_backend[key]
		info_A, info_B = entity["rel_table_info"]
		for subj, obj in [(info_A, info_B), (info_B, info_A)]:
			if key[2] != subj["table_id"]: continue
			new_key = key[:2] + (subj["role"], obj["role"]) + key[2:]
			table_data_backend[new_key] = value
	# versionの書き換え
	rewrite_data_version(sys_backend, ("meta", "system_contain_data"), filter_condition, "same_table_link_duplication_bug_fix_ver")
	rewrite_data_version(table_data_backend, ("meta", "backend_contain_data"), filter_condition, "same_table_link_duplication_bug_fix_ver")	# versionの書き換え
	# コミット
	sys_backend.commit()
	table_data_backend.commit()
	return "fixed"

# linkテーブル新規作成処理
def create_link_table(
	rel_info0,	# 関係性情報0 (table名, role, 1 or N)
	rel_info1,	# 関係性情報1 (table名, role, 1 or N)
	link_table_name,	# テーブル名
	sys_backend,	# DB全体情報 (system) が保管されているバックエンド
	link_table_data_backend,	# linkテーブルのデータが保管されているバックエンド
	sldb	# sldbオブジェクト
):
	# role名規則チェック
	if rel_info0[1] == rel_info1[1]: raise Exception("[SymLinkDB error] The role names at both ends of the link must be different.")
	# link table初期化不整合チェック
	filtered_entities = [
		e for e in link_table_data_backend[("meta", "backend_contain_data")]
		if (
			e.get("link_table_name") == link_table_name and
			e.get("sys_backend_id") == sys_backend[("meta", "backend_id")]
		)
	]
	if len(filtered_entities) > 0: raise Exception("[SymLinkDB error] Inconsistency in the stored link table information. According to the information on the DB-system side, the link table that is currently being created is uninitialized, but within the backend that stores the link table, it is already initialized. Degradation in material management is suspected.")
	# link table情報
	link_table_data = {
		"entity_type": "SLDB-link-table",
		"data_version": "same_table_link_duplication_bug_fix_ver",	# データ形式
		"link_table_id": gen_unique_id(),	# 十分な長さの64進idの発行 (uuidの桁数を参考に決定)
		"sys_backend_id": sys_backend[("meta", "backend_id")],
		"data_backend_id": link_table_data_backend[("meta", "backend_id")],
		"link_table_name": link_table_name,
		"rel_table_info": [
			{"table_id": sldb[rel_info0[0]].table_id, "role": rel_info0[1], "1-N": rel_info0[2]},
			{"table_id": sldb[rel_info1[0]].table_id, "role": rel_info1[1], "1-N": rel_info1[2]},
		]
	}
	# systemにtable情報を書き込む
	back_ls_push(	# 辞書-likeオブジェクトの所定のkeyのvalue(list)にデータを追加
		sys_backend, ("meta", "system_contain_data"),
		link_table_data)
	# backendにtable情報を書き込む
	back_ls_push(	# 辞書-likeオブジェクトの所定のkeyのvalue(list)にデータを追加
		link_table_data_backend, ("meta", "backend_contain_data"),
		link_table_data)

# SLDBクラスのオブジェクトを返す
class SLDB:
	# 初期化処理
	def __init__(self, backend):
		self.backend = backend
		# SLDB-backendとして初期化 (必要な場合)
		if ("meta", "backend_id") not in self.backend:
			init_sldb_backend(self.backend)		# SLDB-backendとして初期化
		# さらにDB-systemとして初期化 (必要な場合)
		if judge_sys_initialized(self.backend) is not True:	# このバックエンドがSLDB-sysとして初期化されているかを判定
			init_sldb_sys(self.backend)	# このバックエンドをSLDB-sysとして初期化
		# loadが完了しているtable一覧 (valueはTableクラス)
		self.loaded_tables_dic = {}
		# loadが完了しているlink table一覧 (valueはbackend)
		self.loaded_link_tables_dic = {}
	# table数取得 [SymLinkDB]
	def __len__(self):
		sc_data = self.backend[("meta", "system_contain_data")]
		return len([e for e in sc_data
			if e["entity_type"] == "SLDB-table"])
	# tableの存在確認 [SymLinkDB]
	def __contains__(self, table_name):
		for t_name in self:
			if t_name == table_name: return True
		return False
	# tableのイテレート [SymLinkDB]
	def __iter__(self):
		sc_data = self.backend[("meta", "system_contain_data")]
		for e in sc_data:
			if e["entity_type"] != "SLDB-table": continue
			if e["sys_backend_id"] != self.backend[("meta", "backend_id")]: continue
			yield e["table_name"]
	# tableの読み込み (存在しない場合は空で初期化される) [SymLinkDB]
	def load_table(self, table_name, search_keys = None, backend = None):
		sys_backend = self.backend
		if backend is None: backend = sys_backend
		table_filter = {"sys_backend_id": sys_backend[("meta", "backend_id")], "table_name": table_name}	# 対象テーブルを一意に特定する条件 (DBをまたぐとtable_nameが衝突する可能性があることに留意すべし)
		if table_name in self:	# tableの存在確認 [SymLinkDB]
			# テーブルがすでにある場合
			check_entity_backend(	# あるエンティティについて、バックエンドが整合しているかを確かめる (NGの場合は例外を送出する)
				filter_condition = table_filter,	# エンティティのフィルタリング条件 (uniqueになるようなもの)
				sys_backend = sys_backend,	# DB全体情報 (system) を保管するバックエンド
				table_data_backend = backend,	# テーブルのデータを保管するバックエンド
			)
			# search_keysの整合性を確認
			check_search_keys(
				search_keys,	# チェック対象のsearch_keys
				table_name,	# テーブル名
				sys_backend[("meta", "system_contain_data")],	# 該当sysの内容物一覧
			)
		else:
			# テーブルがない場合
			if ("meta", "backend_id") not in backend:	# SLDB-backendとして初期化 (必要な場合)
				init_sldb_backend(backend)		# SLDB-backendとして初期化
			create_table(	# テーブル新規作成処理
				table_name = table_name,	# テーブル名
				search_keys = search_keys,	# 検索用に使いたい列名
				sys_backend = sys_backend,	# DB全体情報 (system) が保管されているバックエンド
				table_data_backend = backend,	# テーブルのデータが保管されているバックエンド
			)
		# load済み一覧に追加
		table_id = entity_filter(sys_backend[("meta", "system_contain_data")], table_filter, unique = True)["table_id"]	# metaのcontain_dataを条件でフィルタリングする
		self.loaded_tables_dic[table_name] = Table(table_name, table_id, search_keys, backend, self)	# Tableクラス
	# Tableの取得
	def __getitem__(self, table_name):
		if table_name in self.loaded_tables_dic:
			return self.loaded_tables_dic[table_name]
		# 2種類の非存在エラー
		if table_name in self: raise Exception("[SymLinkDB error] The specified table exists, but has not been loaded. Please load it using the load_table() function.")
		raise Exception("[SymLinkDB error] The specified table does not exist.")
	# linkの読み込み (存在しない場合は空で初期化される) [SymLinkDB]
	def load_link(self,
		link_table_name,	# テーブル名
		rel_info0,	# 関係性情報0 (table名, role, 1 or N)
		rel_info1,	# 関係性情報1 (table名, role, 1 or N)
		backend = None	# バックエンド (None指定でsystemのデフォルトバックエンド)
	):
		if backend is None: backend = self.backend
		if self.__contain_link(link_table_name) is True:	# linkの存在確認 [SymLinkDB]
			# linkテーブルがすでにある場合
			filter_condition = {"sys_backend_id": self.backend[("meta", "backend_id")],	# link_tableを一意に特定する条件
				"link_table_name": link_table_name}
			check_entity_backend(	# あるエンティティについて、バックエンドが整合しているかを確かめる (NGの場合は例外を送出する)
				filter_condition = filter_condition,	# エンティティのフィルタリング条件 (uniqueになるようなもの)
				sys_backend = self.backend,	# DB全体情報 (system) を保管するバックエンド
				table_data_backend = backend,	# テーブルのデータを保管するバックエンド
			)
			link_dup_bug_fix(	# keyが旧形式の場合にデータを修正する (同一table内リンクにおいてリンクが両方向に増殖するバグに関連)
				filter_condition = filter_condition,	# エンティティのフィルタリング条件 (uniqueになるようなもの)
				sys_backend = self.backend,	# DB全体情報 (system) を保管するバックエンド
				table_data_backend = backend,	# テーブルのデータを保管するバックエンド
			)
		else:
			# linkテーブルがない場合
			if ("meta", "backend_id") not in backend:	# SLDB-backendとして初期化 (必要な場合)
				init_sldb_backend(backend)		# SLDB-backendとして初期化
			create_link_table(	# linkテーブル新規作成処理
				rel_info0,	# 関係性情報0 (table名, role, 1 or N)
				rel_info1,	# 関係性情報1 (table名, role, 1 or N)
				link_table_name = link_table_name,	# テーブル名
				sys_backend = self.backend,	# DB全体情報 (system) が保管されているバックエンド
				link_table_data_backend = backend,	# linkテーブルのデータが保管されているバックエンド
				sldb = self	# sldbオブジェクト
			)
		# load済み一覧に追加
		self.loaded_link_tables_dic[link_table_name] = backend
	# linkの存在確認 [SymLinkDB]
	def __contain_link(self, link_table_name):
		sc_data = self.backend[("meta", "system_contain_data")]
		for e in sc_data:
			if e["entity_type"] != "SLDB-link-table": continue
			if e["sys_backend_id"] != self.backend[("meta", "backend_id")]: continue
			if e["link_table_name"] == link_table_name: return True
		return False
	# 強制コミット [SymLinkDB]
	def commit(self):
		# 関係するbackendを列挙
		backend_dic = {self.backend[("meta", "backend_id")]: self.backend}	# systemのbackend
		for table_name in self:	# 所属している全tableのbackendを列挙
			backend = self[table_name].backend
			backend_dic[backend[("meta", "backend_id")]] = backend
		# 列挙したbackendをcommit
		for backend_id in backend_dic:
			backend_dic[backend_id].commit()
	# 強制コミット [SymLinkDB]
	def commit(self):
		# backendを一時登録
		backend_dic = {}
		def reg(backend): backend_dic[backend[("meta", "backend_id")]] = backend
		# 関係するbackendを列挙
		reg(self.backend)	# system
		for name in self.loaded_tables_dic: reg(self.loaded_tables_dic[name].backend)	# tables
		for name in self.loaded_link_tables_dic: reg(self.loaded_link_tables_dic[name])	# link-tables
		# 列挙したbackendをcommit
		for backend_id in backend_dic:
			backend_dic[backend_id].commit()
	# 文字列化 (その1, その2)
	def __str__(self):
		table_name_ls = list(self)	# table名一覧を取得
		return f"<SymLinkDB tables = {souts(table_name_ls, 3)}>"
	def __repr__(self): return str(self)
	# table_idからTableオブジェクトを引き当て
	def get_table_by_id(self, table_id):
		entity = entity_filter(	# metaのcontain_dataを条件でフィルタリングする
			self.backend[("meta", "system_contain_data")],
			{"table_id": table_id}, unique = True)
		return self[entity["table_name"]]

# SLDB初期化 [SymLinkDB]
def conn(backend):
	# SLDBクラスのオブジェクトを返す
	sldb = SLDB(backend)
	# sldbをプログラム終了時自動commit対象に追加
	commit_target_dbs.append(sldb)
	return sldb
