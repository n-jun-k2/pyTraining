from unittest import mock

#モック呼び出されたら１００を返す
mock_obj = mock.Mock(return_value=100)
print(mock_obj())

#変数を登録
mock_obj.name = 'Foo'
print(mock_obj.name)

#greet()のHello, Worldを返す。
mock_obj.greet.return_value = 'Hello, World!'
print(mock_obj.greet())


#複雑な処理を記述する場合にはside_effectに関数を登録。

mappings = {
    'a':1,
    'b':2, 
    'c':3
    }

def side_effect(arg):
    return mappings.get(arg)

#sample()がよばれたときの処理を登録
mock_obj.sample.side_effect = side_effect
print(mock_obj.sample('a'))

#未知の呼び出しには新たなモックを呼ぶ
print(mock_obj.unknown_call())

#モックでmethod()を呼び出す。
mock_obj.method(1,2,3,'Hello')

mock_obj.method.assert_called_with(1,2,3,'Hello')#想定通りの呼び出しかを確認

mock_obj.method.assert_called_with(1,2,3,'Bye')#想定と異なる呼ばれ方だった場合例外。