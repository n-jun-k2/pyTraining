# -*- conding: utf-8 -*-

"""
 手動でフォワードパスとバックワードパスを実装するサンプル

pyTorchの行列を使用する。

"""

import torch

dtype = torch.float
device = torch.device("cuda:0")

N, D_in, H, D_out = 64, 1000, 100, 10

#入力情報を乱数で作成
x = torch.randn(N, D_in, device=device, dtype=dtype)
y = torch.randn(N, D_out, device=device, dtype=dtype)

#モデル情報　重み情報を乱数で作成
w1 = torch.randn(D_in, H, device=device, dtype=dtype)
w2 = torch.randn(H, D_out, device=device, dtype=dtype)

learning_rate = 1e-6
for t in range(500):
    #入力情報を計算.
    h = x.mm(w1)
    h_relu = h.clamp(min=0)
    y_pred = h_relu.mm(w2)

    #誤差を出力
    loss = (y_pred - y).pow(2).sum().item()
    if t % 100 == 99:
        print(t,loss)
    
    # w1, w2の勾配を計算。
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.t().mm(grad_y_pred)
    grad_h_relu = grad_y_pred.mm(w2.t())
    grad_h = grad_h_relu.clone()
    grad_h[h < 0] = 0
    grad_w1 = x.t().mm(grad_h)

    #勾配をもとに更新
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2