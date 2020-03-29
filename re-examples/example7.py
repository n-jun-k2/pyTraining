# -*- coding: utf-8 -*-
import re

"""
数値範囲の代替
[0-9０-９]といった表記の代わりに\d,\Dという表現を使用しパターンを使う。
"""

testPattern = r'\d匹の猫'

match = re.search(testPattern, '3匹の猫が講演で寝ていた。')
print(match)
match = re.search(testPattern, '三匹の猫が講演で寝ていた。')
print(match)