# -*- coding utf-8 -*-

"""
ネットワークモデルの重みの共有と動的グラフのサンプル。
中間層の計算時にフォワードパスで１から４の間の乱数を選択し中間層を繰り替す。
同じ重みを共有する。
"""

import random
import torch

class DynamicNet(torch.nn.Module):
    def __init__(self,D_in,H,D_out):
        super(DynamicNet,self).__init__()
        self.L1 = torch.nn.Linear(D_in,H)
        self.L2 = torch.nn.Linear(H,H)
        self.L3 = torch.nn.Linear(H, D_out)
    
    def forward(self,x):
        """
        中間層の計算で、0から3までのいずれかをランダムで選択します。
        選択された回数分、中間層の計算を行います。

        通常のループ、条件ステートメントなどで動的な計算グラフが作成されます。        
        """
        h_relu=self.L1(x).clamp(min=0)
        for _ in range(random.randint(0,3)):
            h_relu = self.L2(h_relu).clamp(min=0)
        y_pred = self.L3(h_relu)
        return y_pred

N, D_in, H, D_out = 64, 1000, 100, 10

x = torch.randn(N,D_in)
y = torch.randn(N,D_out)

#動的ネットワークモデルの構築
model = DynamicNet(D_in, H, D_out)
#誤差関数を構築
criterion = torch.nn.MSELoss(reduction='sum')
#最適化モデルを構築
optimizer = torch.optim.SGD(model.parameters(),lr=1e-4,momentum=0.9)

for t in range(500):
    #予測値 Y を算出
    y_pred = model(x)
    #誤差を算出、勾配グラフを構築
    loss = criterion(y_pred, y)
    if t % 100 == 99:
        print(t, loss.item())
    
    #勾配グラフの初期化
    optimizer.zero_grad()
    #勾配を算出s
    loss.backward()
    #更新
    optimizer.step()
