import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook

excel_file = 'PFS.xlsx'
sheet_name_expense_income = 'Expense and incomes'
sheet_name_category = 'category'


def load_main_window_movements_table():

    if os.path.exists(excel_file):
        try:
                data = pd.read_excel(excel_file,sheet_name_expense_income)
                return data.values.tolist()
        except Exception as e:
                print(f"Error when try to upload file: {e}")
        return None
    else:
        print('No existe')
        wb = Workbook()
        wb.save(excel_file)

def load_category_window_table():

    try:
        data = pd.read_excel(excel_file,sheet_name_category)
        return data.values.tolist()
    except Exception as e:
        print(f"Error when try to upload file: {e}")
        return None






