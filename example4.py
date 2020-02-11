# -*- conding: utf-8 -*-

"""
PyTorchで autograd.functionのサブクラスを定義。
バックワード、フォワードを実装。
ReLU非線形性を実現するため独自カスタムのautograd関数を実装。
"""

import torch

class myReLU(torch.autograd.Function):
    """
    autograd
    サブクラス化し独自カスタムのforward,backwaordを実装。
    """

    @staticmethod
    def forward(ctx, input):
        """
        ctx:コンテキストオブジェクト
        input:入力テンソル
        """
        ctx.save_for_backward(input)
        return input.clamp(min=0)

    @staticmethod
    def backward(ctx, grad_output):
        """
        ctx:コンテキストオブジェクト
        grad_output:損失勾配テンソル
        """
        input, = ctx.saved_tensors
        grad_input = grad_output.clone()
        grad_input[input < 0] = 0
        return grad_input



dtype = torch.float
device = torch.device("cuda:0")

N, D_in, H, D_out = 64,  1000, 100, 10

x = torch.randn(N, D_in, device=device,dtype=dtype)
y = torch.randn(N, D_out, device=device,dtype=dtype)


w1 = torch.randn(D_in, H, device=device,dtype=dtype, requires_grad=True)
w2 = torch.randn(H, D_out, device=device,dtype=dtype, requires_grad=True)

learning_rate=1e-6
for t in range(500):
    #Functionを利用するためにFunction.applyを呼び出す為[relu]というエイリアスにする。
    relu=myReLU.apply

    y_pred=relu(x.mm(w1)).mm(w2)

    #誤差を算出
    loss = (y_pred - y).pow(2).sum()
    if t % 100 == 99:
        print(t, loss.item())
    
    #勾配算出
    loss.backward()

    #重みの更新
    with torch.no_grad():
        w1 -= learning_rate * w1.grad
        w2 -= learning_rate * w2.grad

        w1.grad.zero_()
        w2.grad.zero_()