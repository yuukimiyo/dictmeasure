# coding: utf-8

def yield_leaf_nodes(obj):
    # 辞書を再帰的に探索し、末端の値ノードをyieldする

    if isinstance(obj, dict):
        # 入力の1次元目が辞書の場合
        if obj == {}:
            yield {}
        else:
            for value in obj.values():
                if isinstance(value, (dict, list, tuple)): # valueが配列か辞書の場合、再帰
                    yield from yield_leaf_nodes(value)
                else: # 通常の変数（ツリーの末端）の場合
                    yield value
    elif isinstance(obj, (list, tuple)):
        # 入力の1次元目がリストの場合
        if obj == []:
            yield []
        else:
            for value in obj:
                if isinstance(value, (dict, list, tuple)): # valueが配列か辞書の場合、再帰
                    yield from yield_leaf_nodes(value)
                else: # 通常の変数（ツリーの末端）の場合
                    yield value
    else:
        # 入力の1次元目が通常の変数の場合
        yield obj
    
def yield_leaf_nodes_with_path(obj, path=[], sep='.', withListIndex=False):
    # 辞書を再帰的に探索し、末端の値ノードとそのパスのタプル(paht, value)をyieldする

    if isinstance(obj, dict):
        # 入力の1次元目が辞書の場合
        if obj == {}:
            yield (sep.join(path), {})
        else:
            for key, value in obj.items():
                new_path = path + [key]
                if isinstance(value, (dict, list, tuple)): # valueが配列か辞書の場合、再帰
                    yield from yield_leaf_nodes_with_path(value, path=new_path, sep=sep, withListIndex=withListIndex)
                else: # 通常の変数（ツリーの末端）の場合
                    yield (sep.join(new_path), value)
    elif isinstance(obj, (list, tuple)):
        # 入力の1次元目がリストの場合
        if obj == []:
            yield (sep.join(path), [])
        else:
            for i, value in enumerate(obj):
                new_path = path + ["[{}]".format(str(i))] if withListIndex else path

                if isinstance(value, (dict, list, tuple)): # valueが配列か辞書の場合、再帰
                    yield from yield_leaf_nodes_with_path(value, path=new_path, sep=sep, withListIndex=withListIndex)
                else: # 通常の変数（ツリーの末端）の場合
                    yield (sep.join(new_path), value)
    else:
        # 入力の1次元目が通常の変数の場合
        yield (sep.join(path), obj)