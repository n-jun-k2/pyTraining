# -*- coding: utf-8 -*-
import re

"""
 数量詞：文字のオプション指定
 ０以上の場合の条件パターンは?の記号を利用する。
"""

testPattern = r'猫犬兔?'

match = re.search(testPattern,'猫犬兔')
print(match)

match = re.search(testPattern,'猫犬')
print(match)

match = re.search(testPattern,'猫')
print(match)