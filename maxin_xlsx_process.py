# -*- coding: utf-8 -*-
import xlrd
import xlwt
import csv

classRoomFile="./data/教室统计.xlsx"



classRoomData = xlrd.open_workbook(classRoomFile)
classRoomSheet = classRoomData.sheets()[0]

# print(classRoomSheet.nrows)

# for i in range(classRoomSheet.nrows):
#     print(classRoomSheet.row_values(i))

head=["序号","房间号","容量（人）","备注"]


for i in range(1,19):
    for j in range(1,8):
        for k in range(1,12):
            head.append("周次：%d,星期：%d,课程：%d," %(i,j,k))

print(head)
columnNumber=len(head)
print(columnNumber)

#
# workbook = xlwt.Workbook(encoding = 'ascii')
# worksheet = workbook.add_sheet('My Worksheet')


with open("./mycsv.csv","w",encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerows(head)
    f.close()




#
#
#
# for i in range(257):
#     worksheet.write(0, i, label=head[i])
#


