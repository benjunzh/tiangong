from time import ctime
from testDataRead import forecastResult

import struct

resultValue = forecastResult("testData.csv", "人身、财产侵权责任.csv")
print(resultValue)