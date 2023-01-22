from createTable import createTable_tab, createTablePretty_tab
from xlsxSheet_refactor import mergeXlsxSheet, deriveSheetByGroup, addAgeGroup
from plotTable import plotGraph


MergeXlsx_df = mergeXlsxSheet()

print("--------1.1. Total sales per year-----------")
GroupByYears = deriveSheetByGroup(MergeXlsx_df, 'Years', 'Units')
head = ["Sr.No", "Year", "Units"]
print(createTable_tab(GroupByYears,head))
plotGraph(GroupByYears, 'Years', 'Units', 'Sales Per Year','red')
print("")

print("--------1.2. Total sales by gender-----------")
GroupByGender = deriveSheetByGroup(MergeXlsx_df, 'Gender', 'Units')
head = ["Sr.No", "Gender", "Units"]
print(createTable_tab(GroupByGender,head))
plotGraph(GroupByGender, 'Gender', 'Units', 'Sales By Gender','violet')
print("")

print("--------1.3. Total sales by customer-----------")
GroupByName = deriveSheetByGroup(MergeXlsx_df, 'Final_Name', 'Units')
head = ["Sr.No", "Name", "Units"]
print(createTable_tab(GroupByName,head))
plotGraph(GroupByName, 'Final_Name', 'Units', 'Sales By Customer','yellow')
print("")

print("--------1.4. Most bought item by customer - if multiple, consider any one item only-----------")
MostBroughtItem = MergeXlsx_df.value_counts('Item')
MaxNum = MostBroughtItem.max()
extract_index=MostBroughtItem.index.tolist()[0]
head = ["Items", "Sale Count"]
row_added = [extract_index,MaxNum]
print(createTablePretty_tab(head,row_added))
print("")

print("--------1.5. Create age bins/groups of your choice and calculate the total sales per bin/group-----------")
bins= [20,35,50,110]
print("For this question used bins is --> ", bins)
ageGroup_df=addAgeGroup(MergeXlsx_df)
GroupByAgeGroup = deriveSheetByGroup(ageGroup_df, 'AgeGroup', 'Units')
GroupByTable = GroupByAgeGroup[(GroupByAgeGroup[['Units']] != 0).all(axis=1)]
head = ["Sr.No", "Age Group", "Units"]
print(createTable_tab(GroupByTable,head))
plotGraph(GroupByTable, 'AgeGroup', 'Units', 'Sales By Age Group','blue')
print("")

print("--------1.7. Top 2 customers per each item if available-----------")
unique_item_list=[]
sort_Item_Unit_df=MergeXlsx_df.sort_values(by=['Item','Units'],ascending=[True, False])
for row in range(0, len(sort_Item_Unit_df)):
    item_list = sort_Item_Unit_df['Item'].iloc[row]
    if item_list not in unique_item_list:
        unique_item_list.append(item_list)
for items in unique_item_list:
    print("Top 2 customber for -> ", items)
    topUsersByitem_table=(sort_Item_Unit_df[sort_Item_Unit_df.Item == items]).head(2)
    head = ["Sr.No","Name", "Item", "Units", "Unit Cost", "Years", "Age", "Gender","AgeGroup"]
    print(createTable_tab(topUsersByitem_table,head))
    print(" ")

