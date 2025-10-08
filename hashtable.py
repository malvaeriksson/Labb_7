import csv

fileName = "kdrama.csv"

class HashNode:
    """Noder till klassen Hashtable"""

    def __init__(self, key="", data=None):
        """
        key är nyckeln som används vid hashningen
        data är det objekt som ska hashas in
        """
        self.key = key
        self.data = data


class Hashtable:
    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def store(self, key, data):
        """
        key är nyckeln
        data är objektet som ska lagras
        Stoppar in "data" med nyckeln "key" i tabellen.
        """
        index = self.hashfunction(key)
        bucket = self.table[index]
        for node in bucket:
            if node.key == key:
                node.data = data
                return
        bucket.append(HashNode(key, data))

    def search(self, key):
        """
        key är nyckeln
        Hämtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska det bli KeyError
        """
        index = self.hashfunction(key)
        bucket = self.table[index]
        for node in bucket:
            if node.key == key:
                return node.data
        raise KeyError

    def hashfunction(self, key):
        """
        key är nyckeln
        Beräknar hashfunktionen för key
        """
        sumOfChars = 0
        for char in key:
            sumOfChars = sumOfChars + ord(char)

        return sumOfChars % self.size

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False


def readFile(file):
    dict = Hashtable(2000000)

    with open(file, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict.store(row['Drama Name'], row['Rating(Out of 10)'] +
                       row['Actors'] +
                       row['Viewship Rate'] +
                       row['Genre'] +
                       row['Director'] +
                       row['Writer'] +
                       row['Year'] +
                       row['No of Episodes'] +
                       row['Network'])

    return dict


def testReadFile():
    dictionary = readFile(fileName)

    print(dictionary.search("Suspicious Partner"))
    print(dictionary["I am not a robot"])
    if "start down" in dictionary:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    testReadFile()
