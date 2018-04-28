import xlrd
import os
from datetime import datetime



DATE_ROW=7
DAY_ROW=6
TIME_COL=0
DIFF=9
GlobalRecord=None
PATH= "F:\study history\cornell semester two\intro cloud\dataset"

class Record:
    gymName=""
    date=None
    time=None
    cardioCount=-1
    day = None
    weightCount=-1

    def __init__(self, gymName, dateTime, day, cardioCount, weightCount):
        self.gymName=gymName
        self.dateTime = dateTime
        self.day = day
        self.cardioCount = cardioCount
        self.weightCount = weightCount

    def __getitem__(self):
        print(self.cardioCount)

    def serialize(self,option):
        if option==0:
            return {
                'gymName':self.gymName,
                'dateTime' : self.dateTime,
                'day':self.day,
                'cardioCount':self.cardioCount,
                'weightCount':self.weightCount
            }
        #elif option==1:


def dataExtraction(path):
    dirList = os.listdir(path)
    filePathList = []
    for filename in dirList:
        filePath=path+"\\" + filename
        filePathList.append(filePath)
    record = dict()

    for pathFile in filePathList:
        workbook = xlrd.open_workbook(pathFile)
        worksheet = workbook.sheet_by_index(0)
        for dateIndex in range(1, 8):
            dateObject = worksheet.cell(DATE_ROW, dateIndex)
            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(dateObject.value, workbook.datemode)
            dayString = worksheet.cell(DAY_ROW, dateIndex).value
            for timeIndex in range(8, 44):
                timeString = worksheet.cell(timeIndex, TIME_COL).value
                timeOnly = datetime.strptime(timeString, '%I:%M%p')
                fullTime = timeOnly.replace(year=year,month=month,day=day)
                cardioCountInt = worksheet.cell(timeIndex, dateIndex)
                if cardioCountInt.value == "":
                    cardioCountInt = 0
                else:
                    cardioCountInt = int(cardioCountInt.value)
                weightCountInt = worksheet.cell(timeIndex, dateIndex + DIFF)
                if weightCountInt.value == "":
                    weightCountInt = 0
                else:
                    weightCountInt = int(weightCountInt.value)

                record[fullTime]=(Record("Helen Newman Fitness Center",fullTime, dayString,cardioCountInt, weightCountInt))
    return record


'''

def main():
    path = "F:\study history\cornell semester two\intro cloud\dataset"
    GlobalRecord = dataExtraction(path)
    app.run()

if __name__== "__main__":
    main()
'''




