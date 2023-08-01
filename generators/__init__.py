from generators.user.name import Name
from generators.store.storetype import StoreType

def loadFiles(filename, target):
    try :
        f = open(filename, 'r', encoding='UTF8')
        for line in f.readlines() :
            target.append(line.strip())  
        f.close
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

loadFiles('src/firstname.txt', Name.firstnames)
loadFiles('src/lastname.txt', Name.lastnames)
loadFiles('src/storetypes.txt', StoreType.types)
print("Loaded 3 files")