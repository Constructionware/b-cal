import uuid
from time import time, ctime


class Door:
    dlog:list = []
    door_areas :list = []
    door_wall_log:list = []
    wall_tags:set = set ()
    
    def __init__(self, doortype:str=None, width:float=None, height:float=None, thickness:float = None, tag:str=None, walltag:str=None):
        self._id = uuid.uuid4().hex
        self.dtag = tag
        self.dtype = doortype
        self.dwidth = width
        self.dheight = height
        self.dthickness = thickness
        self.dlog.append({"id": self._id, "tag": self.dtag, "logged": self.currentime()})
        self.door_areas.append(self.doorarea())
        if walltag:
            data = self.__dict__
            data['walltag'] = walltag
            self.door_wall_log.append(data)
            self.wall_tags.add(walltag)

    
    def doorarea(self):
        if self.dwidth and self.dheight and self.dwidth > 300:
            self.dunit = 'm2'
            self.drarea = round((self.dwidth / 1000) * (self.dheight / 1000),2)
            return round(self.drarea,2), self.dunit
        else:
            return None
        return 'You need to supply a width and a length in metric units'

    def __repr__(self):
        return f"{self.dtype} Door, {self.dtag} Width: {self.dwidth} Height: {self.dheight}"

    @property
    def total_door_areas(self):
        self.total_doorareas = sum([a[0] for a in self.door_areas])
        return  round(self.total_doorareas,2)

    @property
    def door_areas_list(self):
        self.door_areaslist = [a[0] for a in self.door_areas]
        return  self.door_areaslist 
        
    @staticmethod
    def timestamp():
        ''' Time Time Stamp '''
        return int(time() * 1000 )

    @staticmethod
    def currentime():
        ''' Now '''
        return ctime()

    @classmethod
    def externalDoor(cls, doortype:str="External HardWood Door", width:float=950, height:float=2100, thickness:float = 50, tag:str='Dh1', walltag:str=None):
        door = Door(doortype=doortype, width=width, height=height, thickness=thickness, tag=tag,  walltag=walltag)
        return door
        

    
        

#d = Door.externalDoor()
#d1=Door(doortype='Internal Hollow', width=900, height=2100, thickness = 42, tag='D2')
#d2=Door(doortype='External Solid', width=925, height=2100, thickness = 50, tag ='D1')
