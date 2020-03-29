# -*- coding: utf-8 -*-
import re

"""
 文字や数字、アンダースコア範囲の代替
 \w,\W
"""

testPattern = r'紙には「\w」'

match = re.search(testPattern,'紙には「3」と書かれていた。')
print(match)

match = re.search(testPattern,'紙には「P」と書かれていた。')
print(match)