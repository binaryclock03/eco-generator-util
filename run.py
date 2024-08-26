import json
import os
import DataHandler.json_handler as jh
import DataHandler.Module as md
import DataHandler.SubModule as sb

handler = jh.JsonHandler("./IN/WorldGenerator.eco")

for files in os.listdir("./IN"):
    if files.endswith(".txt"):
        with open("./IN/" + files, 'r') as file:
            file = json.loads(file.read())
            for ore in file:
                biome = ore[0]
                moduleIndex = ore[1]
                id = ore[2]
                generatorType = ore[3]
                params = ore[4]

                deposit = sb.SubModule()
                deposit.create(id, generatorType, params)
                handler.addOre(biome, moduleIndex, deposit)

handler.dumpJson("./OUT/WorldGenerator.eco")

print("Done!")