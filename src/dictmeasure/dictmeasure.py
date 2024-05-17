# coding: utf-8

from .yield_leaf_nodes import yield_leaf_nodes, yield_leaf_nodes_with_path
from .text_util import get_text_chars, get_number_chars, get_text_bytes, get_number_bytes

def count_leaf_nodes(dict={}):
    node_count = 0
    for _ in yield_leaf_nodes(dict):
        node_count += 1
    return node_count

def get_leaf_chars(dict={}):
    # 全ての葉ノードの合計文字数を返す

    total = 0
    for leaf_node in yield_leaf_nodes(dict):
        if isinstance(leaf_node, str):
            total += get_text_chars(leaf_node)
        elif isinstance(leaf_node, (int, float)):
            total += get_number_chars(leaf_node)
        else:
            total += get_text_chars(str(leaf_node))
    
    return total

def get_leaf_bytes(dict={}):
    # 全ての葉ノードの合計バイト数を返す

    total = 0
    for leaf_node in yield_leaf_nodes(dict):
        if isinstance(leaf_node, str):
            total += get_text_bytes(leaf_node)
        elif isinstance(leaf_node, (int, float)):
            total += get_number_bytes(leaf_node)
        else:
            total += get_text_bytes(str(leaf_node))
    
    return total