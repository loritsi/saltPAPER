class Position():
    def __init__(
            self,
            layer:int=0,
            x:int=0,
            y:int=0,
            height:int=0,
            width:int=0
    ):
        self.layer = layer
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    @property
    def position(self):
        return (self.x, self.y)

    def set_layer(self, layer):
        self.layer = layer

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def is_point_inside(self, point):
        x, y  = point