# -*- coding: utf-8 -*-
import re

"""
 任意文字
 .記号をパターン内に使用すると、任意の１文字にヒットします。
 改行コードはヒットしない。要設定。
"""

testPattern = r'吾輩は.である。'
testPattern2 = r'吾輩は...である。'

match = re.search(testPattern,'吾輩は猫である。名前はまだ無い。')
print(match)

match = re.search(testPattern2,'吾輩は猫である。名前はまだ無い。')
print(match)

#.記号の数で任意の文字数でヒットする。

match = re.search(testPattern,'吾輩は野良猫である。名前はまだ無い。')
print(match)

match = re.search(testPattern2,'吾輩は野良猫である。名前はまだ無い。')
print(match)

