class SpaceAsset:
    def __init__(self, name, battery_capacity, battery_level):
        self.name = name
        self.battery_capacity = battery_capacity
        self.battery_level = battery_level
        self.modules = []