# -*- coding: utf-8 -*-

"""
PyTorchによる最適化モジュールを使用する。
高度なオプティマイザーを使用しニューラルネットワークをトレーニングする。
"""

import torch

#バッチサイズ、入力次元数、中間次元数、出力次元数
N, D_in, H, D_out = 64, 1000, 100, 10

#入力値、正解値を作成。
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)

#ネットワークモデルの作成
model = torch.nn.Sequential(
    torch.nn.Linear(D_in,H),
    torch.nn.ReLU(),
    torch.nn.Linear(H,D_out),
)
loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-4
#最適化モジュールを作成（モデルの計算グラフ、学習率）
optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)
for t in range(500):
    #予測値:y_predの算出
    y_pred = model(x)
    #誤差グラフを算出
    loss = loss_fn(y_pred,y)
    if t % 100 == 99:
        print(t, loss.item())
    #最適化の重みを初期化
    optimizer.zero_grad()
    #勾配グラフを計算
    loss.backward()
    #最適化処理を呼び出す。
    optimizer.step()
