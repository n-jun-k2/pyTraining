# -*- coding: utf-8 -*-

"""
 テストを行う対象モジュール。

  FizzBuzz
   ・関数はint型の引数を受け取ってstr型の値を返す。
   ・渡された引数が「3」で割り切れるときに「Fizz」を返す。
   ・渡された引数が「5」で割り切れるときは「Buzz」を返す。
   ・「3」「5」の両方で割り切れるときは「FizzBuzz」を返す。
   ・「3」「5」のいずれかで割り切れないときは数値を文字列にして返す。
"""


def fizzbuzz(n):
   if n % 3 == 0 and n % 5 == 0:
      return 'FizzBuzz'
   
   if n % 3 == 0:
      return 'Fizz'
   
   if n % 5 == 0:
      return 'Buzz'
   
   return str(n)