# -*- coding: utf-8 -*-
import numpy as np

# N : バッチサイズ D_in : 入力次元数 H : 中間層の数 D_out : 出力次元数
N, D_in, H, D_out = 64, 1000, 100, 10

#ランダムの入出力データを作成
x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)

#重みを乱数で初期化　（ネットワークモデル情報)
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

learning_rate = 1e-6
for t in range(500):
    #forward pass ：　モデル情報をもとに結果を出力。
    h = x.dot(w1)
    h_relu = np.maximum(h, 0)
    y_pred = h_relu.dot(w2)

    #正解値との誤差を出力
    loss = np.square(y_pred -y).sum()
    print(t, loss)

    #Backprop : w1,w2の勾配を計算。
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)

    #Update: 重み情報を更新
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
