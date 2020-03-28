# -*- coding: utf-8 -*-
import re

"""
OR条件(文字単体の場合)
文字列の一部で、いずれかにヒットするOR条件パターンを使用するには”[]”の括弧を利用します。
例として、特定の文字部分が猫もしくは犬のどちらかにヒットするといった条件のパターンは以下のようになります。
"""

searchPattern = r'吾輩は[猫犬]である。' #[]内にある文字のいずれかに該当する場合ヒットする。(文字単体の場合)
testCatString = '吾輩は猫である。名前はまだない。'
testDogString = '吾輩は犬である。名前はまだない。'

match = re.search(searchPattern,testCatString)

print(match)

match = re.search(searchPattern,testDogString)

print(match)