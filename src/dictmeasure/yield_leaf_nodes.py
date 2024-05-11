# coding: utf-8

def yield_leaf_nodes(obj):
    # 与えられたオブジェクトの各要素について、要素パスオブジェクト(※)をyieldする
    # ※要素パスオブジェクト：(key, value, type)のタプルのリスト

    if isinstance(obj, dict):
        # 入力の1次元目が辞書の場合
        if obj == {}:
            yield {}
        else:
            for key, value in obj.items():
                if isinstance(value, dict):
                    # 小要素ツリーを作成し元の辞書に追加
                    yield from yield_leaf_nodes(value)
                elif isinstance(value, (list, tuple)):
                    # 小要素ツリーを作成し元の辞書に追加
                    yield from yield_leaf_nodes(value)
                else:
                    # 通常の変数（ツリーの末端）の場合
                    yield value
    elif isinstance(obj, (list, tuple)):
        # 入力の1次元目がリストの場合
        if obj == []:
            yield []
        else:
            for i, value in enumerate(obj):
                if isinstance(value, dict):
                    # 辞書か配列の、小要素ツリーを作成し元のリストに追加
                    yield from yield_leaf_nodes(value)
                elif isinstance(value, (list, tuple)):
                    # 辞書か配列の、小要素ツリーを作成し元のリストに追加
                    yield from yield_leaf_nodes(value)
                else:
                    # 通常の変数（ツリーの末端）の場合
                    yield value
    else:
        # 入力の1次元目が通常の変数の場合
        yield obj