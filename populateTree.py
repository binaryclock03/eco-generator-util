import DataHandler.json_handler as jh

handler = jh.JsonHandler("./IN/WorldGenerator.eco")
handler.dumpTree("./OUT/tree.txt")