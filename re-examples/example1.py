# -*- coding: utf-8 -*-
import re
#パターンの文字列前のr表記は[raw string]のrです。これは特殊記号などの文字[\]、[\n]などがただの文字列に変換されます。
serchPattern = r'猫'
testString = '吾輩は猫である。名前はまだ無い。'
#seach関数では、正規表現のパターンにヒットした場合にはMatchオブジェクトが返る。
match = re.search(serchPattern, testString)
#ヒットした部分や文字列の位置などが格納されている。
print(match)