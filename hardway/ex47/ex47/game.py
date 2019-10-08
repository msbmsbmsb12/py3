class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        
    def go(self, direction):
        return self.paths.get(direction, None)
        # dict.get(key, default=None)
        # key字典中查找的键 ，default 如果指定的值不存在，返回默认值none 

    def add_paths(self, paths):
        self.paths.update(paths)
        # dict.update(dict2),dict更新或补充dict2的值