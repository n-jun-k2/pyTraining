# -*- coding: utf-8 -*-


"""
PyTorch:nnパッケージを利用しニューラルネットワークを構築する
計算する複数のレイヤー、最適化パラメータはグラフ上により高いレベルの抽象化を提供する。
今回は,nnパッケージで2層のネットワークを実装する。
"""

import torch


#バッチサイズ、入力次元数、中間層の次元数、出力次元数
N, D_in, H, D_out = 64, 1000, 100, 10

#入力値の乱数を生成
x = torch.randn(N,D_in) #サンプル値 * バッチ数
y = torch.randn(N,D_out)#正解値 * バッチ数

#nnパッケージを利用しネットワークモデルを作成。
model = torch.nn.Sequential(
    torch.nn.Linear(D_in, H),
    torch.nn.ReLU(),
    torch.nn.Linear(H,D_out),
)


#nnパッケージにある一般的な損失関数を定義
#平均二乗誤差
loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-4
for t in range(500):
    #予測値を出力
    y_pred = model(x)
    #予測値から誤差を算出し勾配グラフを構築
    loss = loss_fn(y_pred, y) #y_pred：予測値, y:正解値
    if t % 100 == 99:
        print(t, loss.item())
    
    #ネットワークモデルの勾配グラフを初期化
    model.zero_grad()
    #学習可能なすべての要素に関する損失の勾配グラフを計算。
    loss.backward()
    #勾配降下を使用しモデルの重みを更新。
    with torch.no_grad():
        for param in model.parameters():
            param -= learning_rate * param.grad
