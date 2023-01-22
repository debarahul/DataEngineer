from tabulate import tabulate
from prettytable import PrettyTable

def createTable_tab(dataframe_df,head):
    table = tabulate(dataframe_df, headers=head, tablefmt="grid")
    return table

def createTablePretty_tab(head,row_added):
    prettyTable = PrettyTable(head)
    prettyTable.add_row(row_added)
    return prettyTable