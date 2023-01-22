import pandas as pd
import re

Sheet1_df = pd.read_excel('Assignment v2 - Data Engineer.xlsx', sheet_name='Sales Data')
Sheet2_df = pd.read_excel('Assignment v2 - Data Engineer.xlsx', sheet_name='Customer Details')

Sheet1_df = Sheet1_df.assign(Final_Name=None, Years=None)
Sheet2_df = Sheet2_df.assign(Final_Name=None, Gender=None)

def sheeetGetLoc(sheet_name, column_name):
    index_column = sheet_name.columns.get_loc(column_name)
    return index_column

def sheet2_Refactor():
    for row in range(0, len(Sheet2_df)):
        sheet = Sheet2_df
        Name_Pattern = re.compile(r'[A-z]+\.\s')
        Name = re.sub(Name_Pattern, '', sheet.iat[row, sheeetGetLoc(sheet, 'Full Name')])
        sheet.iat[row, sheeetGetLoc(sheet, 'Final_Name')] = Name
        if 'Ms. ' in sheet.iat[row, sheeetGetLoc(sheet, 'Full Name')]:
            sheet.iat[row, sheeetGetLoc(sheet, 'Gender')] = 'Female'
        else:
            sheet.iat[row, sheeetGetLoc(sheet, 'Gender')] = 'Male'
    return Sheet2_df

def sheet1_Refactor():
    for row in range(0, len(Sheet1_df)):
        sheet = Sheet1_df
        NameList = (sheet.iat[row, sheeetGetLoc(sheet, 'Name')]).split()
        NameList[0], NameList[-1] = NameList[-1], NameList[0]
        NameListToStr = ' '.join([str(elem) for elem in NameList])
        sheet.iat[row, sheeetGetLoc(sheet, 'Final_Name')] = NameListToStr

        Date_Pattern = r'([0-9]{4})'
        ExtractYear = re.search(Date_Pattern, str(sheet.iat[row, sheeetGetLoc(sheet, 'Order Date')])).group()
        sheet.iat[row, sheeetGetLoc(sheet, 'Years')] = ExtractYear
    return Sheet1_df

def mergeXlsxSheet():
    MergeXlsx_df = sheet1_Refactor()[["Final_Name", "Item", "Units", "Unit Cost", "Years"]].merge(
        sheet2_Refactor()[["Final_Name", "AGE", "Gender"]], on="Final_Name", how="left")
    return MergeXlsx_df

def deriveSheetByGroup(xlsx_sheet, coulm_groupby, column_sum):
    xlsx_sheet = xlsx_sheet.sort_values(coulm_groupby)
    derive = (xlsx_sheet[coulm_groupby] != xlsx_sheet[coulm_groupby].shift()).cumsum()
    GroupByYears = xlsx_sheet.groupby([coulm_groupby, derive], as_index=False, sort=False)[column_sum].sum()
    return GroupByYears

def addAgeGroup(xlsx_sheet):
    ageGroupSheet=xlsx_sheet
    bins = [20, 35, 50, 110]
    labels = ['Young', 'Adult', 'Old']
    ageGroupSheet['AgeGroup'] = pd.cut(xlsx_sheet['AGE'], bins=bins, labels=labels, right=False)
    return ageGroupSheet
