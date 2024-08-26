import DataHandler.SubModule as sm

class Module:
    def create(self, id, noiseFrequency, min, max, blockType, submodules):
        '''init a whole new module from params'''
        self.id = id
        self.noiseFrequency = noiseFrequency
        self.min = min
        self.max = max
        self.blockType = blockType
        self.submodules = submodules

    def load(self, moduleLoc):
        '''init from a module location in the json'''
        self.id = moduleLoc["$id"]
        self.noiseFrequency = moduleLoc["NoiseFrequency"]
        self.min = moduleLoc["Min"]
        self.max = moduleLoc["Max"]
        self.blockType = moduleLoc["BlockType"]

        self.submodules = []
        for index in range(0,len(moduleLoc["SubModules"])):
            submodule = sm.SubModule()
            submodule.load(moduleLoc["SubModules"][index])
            self.submodules.append(submodule)

    def package(self):
        '''package class into a form that can be shoved back into the json'''
        submodulelist = []
        for submodule in self.submodules:
            submodulelist.append(submodule.package())
        return {"$id": self.id, "NoiseFrequency":self.noiseFrequency, "Min":self.min, "Max":self.max, "BlockType":self.blockType, "SubModules":submodulelist}

    def addSubmodule(self, submodule):
        '''add a new submodule into the submodule list in this module'''
        self.submodules.append(submodule)

    def getBlockName(self, handler):
        '''returns the blockname of the block in the module'''
        try:
            return self.blockType["Type"].split('.')[-2].split(',')[0]
        except:
            return handler.getBlockFromRef(self.blockType["$ref"]).split('.')[-2].split(',')[0]
            