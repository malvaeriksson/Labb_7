from Labb_6.sokning_och_sortering import fileName
import csv
fileName = kdrama.csv
class DictHash:
    def __init__(self):
        self.dict = {}

    def store(self, nyckel, data):
       return self.dict.update({nyckel:data})

    def search(self, nyckel):
        return self.dict.get(nyckel)

    def __getitem__(self, nyckel):
        return self.dict.get(nyckel)

    def __contains__(self, nyckel):
        if self.dict.get(nyckel) is not None:
            return True
        else:
            return False
            



def testDictHash():
    dict = DictHash()
    dict.store("hej","hejdå")
    x = dict["hej"]
    y = dict.search("hej")
    z = "hej" in dict
    a = "bla" in dict
    print(x)
    print(y)
    print(z)   #true
    print(a)   #false


def readFile(fileName):

    with open(fileName, encoding='uft-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pass


if __name__ == "__main__":
    testDictHash()

