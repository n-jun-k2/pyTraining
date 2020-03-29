# -*- coding: utf-8 -*-
import re

"""
否定条件
文字単体のパターンの場合は、[^]の場合^以降に記載されている単語以外を条件にする。
"""

testPattern = r'吾輩は[^犬兎]である。'

match = re.search(testPattern,'吾輩は猫である。名前はまだ無い。')
print(match)

match = re.search(testPattern,'吾輩は兎である。名前はまだ無い。')
print(match)