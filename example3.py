# -*- coding: utf-8 -*-

"""
pyTorchのautogradを利用するサンプル

自動勾配を使用する場合はネットワークモデルの計算グラフ(computational graph)を構築する。

"""

import torch

dtype = torch.float
device = torch.device("cuda:0")

N,D_in,H,D_out = 64,1000,100,10

#入力情報を作成
x = torch.randn(N,D_in,device=device,dtype=dtype)
y = torch.randn(N,D_out,device=device,dtype=dtype)

#モデルの重み情報を作成 自動勾配を行う場合 requires_grad=True を行う。
w1 = torch.randn(D_in, H, device=device,dtype=dtype,requires_grad=True)
w2 = torch.randn(H, D_out, device=device, dtype=dtype, requires_grad=True)

learning_rate = 1e-6
for t in range(500):
    # forward pass : 予測のyを計算。
    y_pred = x.mm(w1).clamp(min=0).mm(w2)
    # 誤差の計算
    loss = (y_pred - y).pow(2).sum()
    if t % 100 == 99:
        print(t, loss.item())

    # requires_grad=True の勾配を求める
    loss.backward()
    
    #重みの更新
    with torch.no_grad():
        w1 -= learning_rate * w1.grad
        w2 -= learning_rate * w2.grad
        #重みを更新した際は手動で勾配をゼロにする。
        w1.grad.zero_()
        w2.grad.zero_()