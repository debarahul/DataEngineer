import pandas as pd
import re
import matplotlib.pyplot as plt
from tabulate import tabulate

Sheet1_df = pd.read_excel('Assignment v2 - Data Engineer.xlsx', sheet_name='Sales Data')
Sheet2_df = pd.read_excel('Assignment v2 - Data Engineer.xlsx', sheet_name='Customer Details')

Sheet2_df['Final_Name'] = None
Sheet2_df['Gender'] = None
Sheet1_df['Final_Name'] = None
Sheet1_df['Years'] = None

index_FullName = Sheet2_df.columns.get_loc('Full Name')
index_FinalName = Sheet2_df.columns.get_loc('Final_Name')
index_Gender = Sheet2_df.columns.get_loc('Gender')
index_Name = Sheet1_df.columns.get_loc('Name')
index_FinalName_sh1 = Sheet1_df.columns.get_loc('Final_Name')
index_OrderDate = Sheet1_df.columns.get_loc('Order Date')
index_Years = Sheet1_df.columns.get_loc('Years')

for row in range(0, len(Sheet2_df)):
    Name_Pattern = re.compile(r'[A-z]+\.\s')
    Name = re.sub(Name_Pattern, '', Sheet2_df.iat[row, index_FullName])
    Sheet2_df.iat[row, index_FinalName] = Name
    if 'Ms. ' in Sheet2_df.iat[row, index_FullName]:
        Sheet2_df.iat[row, index_Gender] = 'Female'
    else:
        Sheet2_df.iat[row, index_Gender] = 'Male'

#print(Sheet2_df.sort_values('Gender'))

sort_df=Sheet1_df.sort_values('Order Date')
for row in range(0, len(sort_df)):
    NameList=(sort_df.iat[row, index_Name]).split()
    #print(NameList)
    NameList[0], NameList[-1] = NameList[-1], NameList[0]
    NameListToStr = ' '.join([str(elem) for elem in NameList])
    #print(NameListToStr)
    sort_df.iat[row, index_FinalName_sh1] = NameListToStr

    Date_Pattern = r'([0-9]{4})'
    ExtractYear = re.search(Date_Pattern, str(sort_df.iat[row, index_OrderDate])).group()
    sort_df.iat[row, index_Years] = ExtractYear

#print(Sheet1_df)
MergeXlsx_df = sort_df[["Final_Name", "Item", "Units","Unit Cost","Years"]].merge(Sheet2_df[["Final_Name", "AGE","Gender"]], on = "Final_Name", how = "left")
#print(MergeXlsx_df)

print("--------1.1. Total sales per year-----------")
derive = (MergeXlsx_df.Years != MergeXlsx_df.Years.shift()).cumsum()
GroupByYears = MergeXlsx_df.groupby(['Years',derive], as_index=False, sort=False)['Units'].sum()
#print(GroupByYears)
head = ["Year", "Units"]
print(tabulate(GroupByYears, headers=head, tablefmt="grid"))
print("")

print("--------1.2. Total sales by gender-----------")
sort_Gender_df=MergeXlsx_df.sort_values('Gender')
#print(sort_Gender_df)
derive_gender = (sort_Gender_df.Gender != sort_Gender_df.Gender.shift()).cumsum()
GroupByGender = sort_Gender_df.groupby(['Gender',derive_gender], as_index=False, sort=False)['Units'].sum()
head = ["Gender", "Units"]
print(tabulate(GroupByGender, headers=head, tablefmt="grid"))
print("")

print("--------1.3. Total sales by customer-----------")
sort_Name_df=MergeXlsx_df.sort_values('Final_Name')
#print(sort_Name_df)
derive_name = (sort_Name_df.Final_Name != sort_Name_df.Final_Name.shift()).cumsum()
GroupByName = sort_Name_df.groupby(['Final_Name',derive_name], as_index=False, sort=False)['Units'].sum()
head = ["Name", "Units"]
print(tabulate(GroupByName, headers=head, tablefmt="grid"))
print("")

""""
order_date = GroupByYears['Years'].tolist()
order_units = GroupByYears['Units'].tolist()

plt.title('Units by year')
plt.plot(order_date, order_units, label = 'YearWise Unit purches')
plt.xlabel('Year Basis')
plt.ylabel('Units Purches')
plt.xticks(order_date)
plt.yticks([1000,1100,1200,1300])
plt.show()"""