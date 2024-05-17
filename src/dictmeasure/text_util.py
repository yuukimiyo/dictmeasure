# coding: utf-8

def get_text_chars(t=''):
    # テキストの文字数を返す
    # 絵文字や合字（リガチャ）は複数文字としてカウントするため、表示上の文字数とは結果が異なる
    return len(t)

def get_number_chars(n=None):
    # 数値を文字列とみなして、文字数を返す
    if n is None:
        return 0
    else:
        return len(str(n))

def get_text_bytes(t=''):
    # テキストのバイト数を返す
    # 絵文字や合字（リガチャ）が含まれる場合は容量が大きくなる
    return len(t.encode('utf-8'))

def get_number_bytes(n=None):
    # 数値を文字列とみなして、バイト数を返す
    if n is None:
        return 0
    else:
        t = str(n)
        return len(t.encode('utf-8'))