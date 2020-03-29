# -*- coding: utf-8 -*-
import re

"""
 スペースや改行、タブなどを一括して扱う。
 \s,\Sというパターン表現を使用するとスペース,改行,タブ,空白などを一括して扱う。
"""

testPattern = r'吾輩は\s猫である。'

#半角スペース
match = re.search(testPattern,'吾輩は 猫である。名前はまだ無い。')
print(match)
#全角スペース
match = re.search(testPattern,'吾輩は　猫である。名前はまだ無い。')
print(match)
#改行
match = re.search(testPattern,'吾輩は\n猫である。名前はまだ無い。')
print(match)
#タブ
match = re.search(testPattern,'吾輩は\t猫である。名前はまだ無い。')
print(match)