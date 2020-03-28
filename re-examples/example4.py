# -*- coding: utf-8 -*-
import re

"""
    特定の文字範囲のルールによるOR条件
    数値ならなんでも良いといった条件を設定する際に範囲の間にハイフンの記号設定することで対応可能。
    例として3~5の範囲なら何でも良いとしたい場合を以下に記載する。
"""

testHalfPattern = r'[3-5]匹の猫'
testFullPattern = r'[３-５]匹の猫'
testPattern = r'[3-5３-５]匹の猫'

#半角の場合
match = re.search(testHalfPattern,'帰り道に3匹の猫を見かけた。')
print(match)

match = re.search(testHalfPattern,'帰り道に5匹の猫を見かけた。')
print(match)


#全角の場合
match = re.search(testHalfPattern,'帰り道に３匹の猫を見かけた。')
print(match)

match = re.search(testHalfPattern,'帰り道に５匹の猫を見かけた。')
print(match)

match = re.search(testFullPattern,'帰り道に３匹の猫を見かけた。')
print(match)

match = re.search(testFullPattern,'帰り道に５匹の猫を見かけた。')
print(match)


#半角の場合
match = re.search(testPattern,'帰り道に3匹の猫を見かけた。')
print(match)

match = re.search(testPattern,'帰り道に5匹の猫を見かけた。')
print(match)

#全角の場合
match = re.search(testPattern,'帰り道に３匹の猫を見かけた。')
print(match)

match = re.search(testPattern,'帰り道に５匹の猫を見かけた。')
print(match)