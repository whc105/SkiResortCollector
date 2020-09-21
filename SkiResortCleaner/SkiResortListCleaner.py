import json

def readJSON(fileLoc):
    with open(fileLoc, 'r', encoding='utf8') as file:
        data = json.load(file)
        
    return data

def outputFile(fileLoc, resorts):
    with open(fileLoc, 'w') as outfile:
        json.dump(resorts, outfile)

def parseResortData(resortList):
    for resort in resortList:
        del resort['timezone']
        del resort['weatherWidget']
        del resort['reviewTotals']
        del resort['weatherProvider']
        del resort['pastSnow']
        del resort['primaryRegion']['_id']
        del resort['primaryRegion']['links']
        del resort['resort_id']
        del resort['snowcone']
        
    return resortList




usaResorts = readJSON('./resort-data/resortListUSA.json')['rows']
euResorts = readJSON('./resort-data/resortListEU.json')['rows']
shResorts = readJSON('./resort-data/resortListSH.json')['rows']
canResorts = readJSON('./resort-data/resortListCAN.json')['rows']
resortList = parseResortData(usaResorts) + parseResortData(euResorts) + parseResortData(shResorts) + parseResortData(canResorts)

resortURL = ['https://www.onthesnow.com' + resort['links']['profile'] for resort in resortList]

outputFile('./parsed-resort-data/resort-list.json', resortList)
outputFile('./parsed-resort-data/resort-URLs.json', resortURL)