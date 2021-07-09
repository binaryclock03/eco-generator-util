import json
import DataHandler.modules as md

class JsonHandler:
    def __init__(self, fileloc):
        file = open(fileloc, "r").read()
        self.jsonFile = json.loads(file)

        self.biomedict = {"Grassland":0,"RainForest":1,"WarmForest":2,"ColdForest":3,"Taiga":4,"Tundra":5,"Ice":6,"Desert":7,"Ocean":8,"DeepOcean":9,"ColdCoast":10,"WarmCoast":11,"Wetland":12}
        self.stonetypesdict = {"Eco.World.Blocks.DirtBlock, Eco.World":"DirtBlock","Eco.Mods.TechTree.LimestoneBlock, Eco.Mods":"LimestoneBlock","Eco.Mods.TechTree.SandstoneBlock, Eco.Mods":"SandstoneBlock","Eco.Mods.TechTree.GraniteBlock, Eco.Mods":"GraniteBlock","Eco.Mods.TechTree.GneissBlock, Eco.Mods":"GneissBlock","Eco.Mods.TechTree.GneissBlock, Eco.Mods":"BasaltBlock"}

    def getBiomeLoc(self, biomeName):
        return self.jsonFile["TerrainModule"]["Modules"][self.biomedict[biomeName]]

    def getStoneLoc(self, biomeLoc, stoneName):
        groundtypedict = dict()
        for index in range(0,len(biomeLoc)):
            try:
                groundtypedict[self.stonetypesdict[(biomeLoc["Module"]["BlockDepthRanges"][index]["BlockType"]["Type"])]] = index
            except:
                pass
        return biomeLoc["Module"]["BlockDepthRanges"][groundtypedict[stoneName]]

    def dumpJson(self, path):
        with open(path, 'w') as file:
            file.write(json.dumps(self.jsonFile, indent = 2))

    def listStoneInBiome(self, biomeName):
        biomeLoc = self.getBiomeLoc(biomeName)
        groundtypedict = dict()
        for index in range(0,len(biomeLoc)):
            try:
                groundtypedict[self.stonetypesdict[(biomeLoc["Module"]["BlockDepthRanges"][index]["BlockType"]["Type"])]] = index
            except:
                pass
        return groundtypedict

    def addOre(self, biomeName, moduleNumb, subModule):
        module = md.Module()
        module.load(self.getBiomeLoc(biomeName)["Module"]["BlockDepthRanges"][moduleNumb])
        module.addSubmodule(subModule)
        self.getBiomeLoc(biomeName)["Module"]["BlockDepthRanges"][moduleNumb] = module.package()
