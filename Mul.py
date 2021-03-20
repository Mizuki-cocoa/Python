class MulLayer:
    def __init__(self):
        #初期化
        self.x=None
        self.y=None

    def forward(self,x,y):
        self.x=x
        self.y=y

        out=x*y
        return out

    def backward(self,dout):
        dx=dout*self.y
        dy=dout*self.x

        return dx,dy
        
class AddLayer:
    def __init__(self):
        pass
    #passは、何もしない

    def forward(self,x,y):
        out=x+y

        return out

    def backward(self,dout):
        dx=dout*1
        dy=dout*1

        return dx,dy


class Relu:
        def __init__(self):
        #初期化
        self.x=None
        self.y=None

    def forward(self,x):
        self.x=x

        out=x*y
        return out

    def backward(self,dout):



