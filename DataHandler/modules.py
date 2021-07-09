class SubModule:
    def create(self, id, type, params):
        '''init a whole new submodule from params'''
        self.submoduleLoc = None

        self.id = id                        # just make it a big number (over 300) and not one you've already used!!!
        self.type = type  
                          # world generator type
        if self.type == 'Eco.WorldGenerator.StandardTerrainModule, Eco.WorldGenerator':
            self.blockType = params["BlockType"]                              # blocktype {'$id': '23', 'Type': 'Eco.Mods.TechTree.CrushedLimestoneBlock, Eco.Mods'}
            self.heightRange = params["HeightRange"]                          # {'min': -1.0, 'max': 1.0}
            self.depthRange = params["DepthRange"]                            # {'min': 0.0, 'max': 1.0}
            self.percentChance = params["PercentChance"]                      # some int between 0 and 1
            self.noiseFrequency = params["NoiseFrequency"]                    # I think this can be between 0-100? Not sure
            self.noiseType = params["NoiseType"]                              # 'Perlin' is default
            self.noiseDistributionType = params["NoiseDistributionType"]      # 'Bands'
        
        if self.type == 'Eco.WorldGenerator.DepositTerrainModule, Eco.WorldGenerator':
            self.spawnAtLeastOne = params["SpawnAtLeastOne"]
            self.spawnPercentChance = params["SpawnPercentChance"]
            self.depthRange = params["DepthRange"]
            self.depositDepthRange = params["DepositDepthRange"]
            self.blocksCountRange = params["BlocksCountRange"]
            self.blockType = params["BlockType"]
            self.directionWeights = params["DirectionWeights"]
            self.weightVariance = params["WeightVariance"]

    def load(self, submoduleLoc):
        pass
        '''init from a module location in the json'''
        self.submoduleLoc = submoduleLoc

        self.id = submoduleLoc["$id"]
        self.type = submoduleLoc["$type"]

        if self.type == 'Eco.WorldGenerator.StandardTerrainModule, Eco.WorldGenerator':
            self.blockType = submoduleLoc["BlockType"]
            self.heightRange = submoduleLoc["HeightRange"]
            self.depthRange = submoduleLoc["DepthRange"]
            self.percentChance = submoduleLoc["PercentChance"]
            self.noiseFrequency = submoduleLoc["NoiseFrequency"]
            self.noiseType = submoduleLoc["NoiseType"]
            self.noiseDistributionType = submoduleLoc["NoiseDistributionType"]

        if self.type == 'Eco.WorldGenerator.DepositTerrainModule, Eco.WorldGenerator':
            self.spawnAtLeastOne = submoduleLoc["SpawnAtLeastOne"]
            self.spawnPercentChance = submoduleLoc["SpawnPercentChance"]
            self.depthRange = submoduleLoc["DepthRange"]
            self.depositDepthRange = submoduleLoc["DepositDepthRange"]
            self.blocksCountRange = submoduleLoc["BlocksCountRange"]
            self.blockType = submoduleLoc["BlockType"]
            self.directionWeights = submoduleLoc["DirectionWeights"]
            self.weightVariance = submoduleLoc["WeightVariance"]


    def package(self):
        '''package class into a form that can be shoved back into the json'''
        if self.type == 'Eco.WorldGenerator.StandardTerrainModule, Eco.WorldGenerator':
            return {'$id': self.id, '$type': self.type, 'BlockType': self.blockType, 'HeightRange': self.heightRange, 'DepthRange': self.depthRange, 'PercentChance': self.percentChance, 'NoiseFrequency': self.noiseFrequency, 'NoiseType': self.noiseType, 'NoiseDistributionType': self.noiseDistributionType}
        if self.type == 'Eco.WorldGenerator.DepositTerrainModule, Eco.WorldGenerator':
            return {'$id': self.id, '$type': self.type, 'SpawnAtLeastOne': self.spawnAtLeastOne, 'SpawnPercentChance': self.spawnPercentChance, 'DepthRange': self.depthRange, 'DepositDepthRange': self.depositDepthRange, 'BlocksCountRange': self.blocksCountRange, 'BlockType': self.blockType, 'DirectionWeights': self.directionWeights, 'WeightVariance': self.weightVariance}

    def getBlockName(self):
        '''returns the blockname of the block in the module, if the module does not have a block it returns None'''
        try:
            return self.blockType["Type"]
        except:
            return None


class Module:
    def create(self, id, noiseFrequency, min, max, blockType, submodules):
        '''init a whole new module from params'''
        self.moduleLoc = None

        self.id = id
        self.noiseFrequency = noiseFrequency
        self.min = min
        self.max = max
        self.blockType = blockType
        self.submodules = submodules


    def load(self, moduleLoc):
        '''init from a module location in the json'''
        self.moduleLoc = moduleLoc

        self.id = moduleLoc["$id"]
        self.noiseFrequency = moduleLoc["NoiseFrequency"]
        self.min = moduleLoc["Min"]
        self.max = moduleLoc["Max"]
        self.blockType = moduleLoc["BlockType"]

        self.submodules = []
        for index in range(0,len(moduleLoc["SubModules"])):
            submodule = SubModule()
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

    def getBlockName(self):
        '''returns the blockname of the block in the module, if the module does not have a block it returns None'''
        try:
            return self.blockType["Type"]
        except:
            return None