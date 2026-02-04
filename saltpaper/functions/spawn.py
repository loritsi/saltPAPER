from saltpaper.worldsystem.entity import Entity
from saltpaper.worldsystem.components import Position, Sprite

def make_display_entity(world, layer, position, asset_id) -> Entity:
    
    ent = Entity(world)
    position = Position(layer, position)
    sprite = Sprite(asset_id)
    ent.add_many(position, sprite)

    return ent