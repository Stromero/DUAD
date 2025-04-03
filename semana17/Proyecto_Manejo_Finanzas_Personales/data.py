import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook

excel_file = 'PFS.xlsx'
sheet_name_expense_income = 'Expense and incomes'
sheet_name_category = 'category'


def load_main_window_movements_table():

    if os.path.exists(excel_file):
        #print('existe')
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
    
def check_input_is_valid_string(parameter):
    
    if len(parameter) == 0:
        res = 'Empty'
    else:
        res = 'Not empty'

    return res

def save_category(parameter):
    
    try:
        workbook = load_workbook(excel_file)
    except FileNotFoundError:
        print('Error')
    if sheet_name_category in workbook.sheetnames:
        sheet = workbook[sheet_name_category]
    else:
        sheet = workbook.create_sheet(sheet_name_category)

    if sheet["A1"].value is None:    
        sheet["A1"] = 'Category'
        
    sheet.append([parameter.nombre, parameter.tipo])  
    
    workbook.save(excel_file)
    workbook.close()

