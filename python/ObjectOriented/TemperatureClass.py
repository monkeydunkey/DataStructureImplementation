class temperatureClass(object):
    def __init__(self):
        self.maxVal = 0
        self.minVal = 1111
        self.maxFreq = (0,0)
        self.numRecords = 0
        self.records = {x:0 for x in range(111)}
        self.sumVal = 0

    def insert(self, value):
        self.maxVal = max(value, self.maxVal)
        self.minVal = min(value, self.minVal)
        self.numRecords += 1
        self.records[value] += 1
        self.sumVal += value
        if self.records[value] > maxFreq[1]:
            maxFreq = (value, self.records[value])
    
    def getMin(self):
        return self.minVal

    def getMax(self):
        return self.maxVal

    def getMean(self):
        return float(self.sum) / self.numRecords

    def getMode(self):
        return self.maxFreq(0)


