# -*- coding: utf-8 -*-
import re

"""
OR条件(文字列の場合)
条件の範囲を()で囲み、文字列間にｌを挟みます。

"""

searchPattern = r'吾輩は(猫である|犬だよ)' #[]内にある文字のいずれかに該当する場合ヒットする。(文字単体の場合)
testCatString = '吾輩は猫である。名前はまだない。'
testDogString = '吾輩は犬だよ。名前はまだない。'

match = re.search(searchPattern,testCatString)

print(match)

match = re.search(searchPattern,testDogString)

print(match)