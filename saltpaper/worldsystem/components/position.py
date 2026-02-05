class Position():
    def __init__(
            self,
            layer:int=0,
            position:tuple[int,int]=(0,0),
            width:int=0,
            height:int=0,
    ):
        self.layer = layer
        self.position = position
        self.width = width
        self.height = height

    @property
    def x(self):
        return self.position[0]
    
    @property
    def y(self):
        return self.position[1]

    def set_layer(self, layer):
        self.layer = layer

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def is_point_inside(self, point):
        x, y  = point