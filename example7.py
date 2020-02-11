# -*- coding: utf-8 -*-

"""
 既存のネットワークモデルより更に複雑なモデルを作成するサンプル
 2層ネットワークをカスタムモジュールサブクラスを実装。
"""

import torch

class TwoLayerNet(torch.nn.Module):
    def __init__(self, D_in, H, D_out):
        """
        ２つのLinearモジュールをインスタンス化しメンバー変数に格納する。
        """
        super(TwoLayerNet,self).__init__()
        self.L1 = torch.nn.Linear(D_in,H)
        self.L2 = torch.nn.Linear(H,D_out)
        
    def forward(self, x):
        """
        フォワード関数：入力データのテンソルを受け入れ返す。
        """
        h_relu = self.L1(x).clamp(min=0)
        y_pred = self.L2(h_relu)
        return y_pred
#GPU device
device = torch.device('cuda:0')

N, D_in, H, D_out = 64, 1000, 100, 10

#サンプル値の作成
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)

#ネットワークモデルの構築
model = TwoLayerNet(D_in, H, D_out)

#誤差関数を作成
criterion = torch.nn.MSELoss(reduction='sum')
#最適化モジュール
optimizer = torch.optim.SGD(model.parameters(),lr=1e-4)

for t in range(500):
    y_pred = model(x)
    loss = criterion(y_pred, y)
    if t % 100 == 99:
        print(t, loss.item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()



