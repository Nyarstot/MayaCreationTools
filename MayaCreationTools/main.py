import maya.cmds as cmds


class MainWindow(object):
    # Window constructor
    def __init__(self):
        self.window = "MainWindow"
        self.title = "Maya Creation"
        self.size = (300, 100)
    
    def createUI(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)
        
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size, sizeable=True)
        cmds.formLayout(parent=self.window)
        
        cmds.rowLayout(adjustableColumn=2, numberOfColumns=2, columnWidth2=(100, 80))
        
        cmds.iconTextButton(style="iconAndTextHorizontal", image="MeasurementTools/VertexRuler.png",
                            h=30, w=100, bgc=[0.35, 0.35, 0.35], label="Vertex Ruler")
        cmds.iconTextButton(style="iconAndTextHorizontal", image="MeasurementTools/MeshRuler.png",
                            h=30, w=100, bgc=[0.35, 0.35, 0.35], label="Mesh Ruler")
        
        cmds.setParent('..')
        cmds.dockControl(area="right", content=self.window, allowedArea=["left", "right"])
        
        return self.window


if __name__ == "__main__":
    PlugWindow = MainWindow().createUI()
    cmds.showWindow()

