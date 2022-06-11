import maya.cmds as cmds
import math


class MeasureTool:
    def __init__(self):
        self.__SelectionList = []
        self.__MayaUnits = ""
        self.__LengthAxis = "x"
    
    # Private methods
    
    def __update_tool_info(self):
        self.__SelectionList.clear()
        self.__SelectionList = cmds.ls(sl=True)
        self.__MayaUnits = cmds.currentUnit(query=True, linear=True)
    
    # Public methods
    
    def vertex_distance(self):
        self.__update_tool_info()
        if len(self.__SelectionList) > 2 or len(self.__SelectionList) == 0:
            cmds.error("You must select exactly two vertices!")
        else:
            vtx_pos = cmds.xform(self.__SelectionList, q=True, ws=True, t=True)
            distance = math.sqrt((vtx_pos[3] - vtx_pos[0]) ** 2 +
                                 (vtx_pos[4] - vtx_pos[1]) ** 2 +
                                 (vtx_pos[5] - vtx_pos[2]) ** 2)
            distance = round(distance, 6)
            cmds.confirmDialog(title="Measure Result", message=str(distance) + ' ' + self.__MayaUnits,
                               button=["Confirm"], defaultButton="Confirm")
            
    def mesh_length(self, axis: str):
        self.__update_tool_info()
        

MTool = MeasureTool()
MTool.vertex_distance()
