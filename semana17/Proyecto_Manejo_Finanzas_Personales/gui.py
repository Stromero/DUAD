import FreeSimpleGUI as sg
import data
import models
# Declare the elements

table_header_main_window = ['Detail','Category','Type','Amount']
table_header_category = ['Category','type']

data_values_movemets = data.load_main_window_movements_table()
if data_values_movemets is None:
    table_values_movements = list()   
else:
    table_values_movements = data_values_movemets.copy()

data_values_category = data.load_category_window_table()
if data_values_category is None:
    table_values_category = list()   
else:
    table_values_category = data_values_category.copy()


def category_window():

    layout = [
        [sg.Text('Add the new category:')],
        [sg.Text('Write the name of the category')],
        [sg.InputText(key='-INCATEGORY-')],
        [sg.Text('Write the type of this category (Income or expense)')],
        [sg.InputText(key='-TYPECATEGORY-')],
        [sg.Table(values=table_values_category, headings=table_header_category ,key='-CATEGORYTABLE-',
                auto_size_columns=False,justification='left',enable_events=True,num_rows=10)],
        [sg.Button('Add',key='-ADDCATEGORY-'),sg.Button('Cancel',key='-CANCELCATEGORY-'),sg.Button('Back')]
    ]

    return sg.Window('Cateogry',layout)

def expense_window():
    
    layout = [
        [sg.Text('Add the new expense')],
        [sg.Text('Category: '), sg.Combo(values=table_values_category,key='-COMBOBOXCATEGORY-')],
        [sg.Text('Detail: '),sg.InputText(key='-INDETAIL-')],
        [sg.Text('Amount: '),sg.InputText(key='-AMOUNTDETAIL-')],
        [sg.Button('Add',key='-ADDEXPENSE-'),sg.Button('Cancel', key='-CANCELEXPENSE-'),sg.Button('Back')]
    ]

    return sg.Window('Expense',layout)

def income_window():
        
    layout = [
        [sg.Text('Add the income')],
        [sg.Text('Category: '),sg.Combo(values=table_values_category,key='-COMBOCATEGORY-')],
        [sg.Text('Detail: '),sg.InputText(key='-INDETAIL-')],
        [sg.Text('Amount: '),sg.InputText(key='-INAMOUNT-')],
        [sg.Button('Add',key='-ADDINCOME-'),sg.Button('Cancel',key='-CANCELINCOME-'),sg.Button('Back')]
    ]

    return sg.Window('Income',layout)

def main_window():

    layout = [
        [sg.Text('Personal financial management')],
        [sg.Text('My movements')],
        [sg.Table(values=table_values_movements,headings=table_header_main_window,key='-MAINTABLE-')],
        [sg.Button('Add category', key='-ADDCATEGORY-'), sg.Button('Register expense', key='-EXPENSE-'), sg.Button('Register income', key='-INCOME-')],
        [sg.Button('Exit')]
    ]


    window = sg.Window('PFM System',layout)

    while True:
        event , values =  window.read()

        if event in (sg.WINDOW_CLOSED,'Exit'):
            break
        if event == '-ADDCATEGORY-':
            window.hide()
            new_window = category_window()
        if event == '-EXPENSE-':
            window.hide()
            new_window = expense_window()
        if event == '-INCOME-':
            window.hide()
            new_window = income_window()

        while True:
            new_event , new_values = new_window.read()

            if new_event in (sg.WIN_CLOSED, 'Back'):
                new_window.close()
                window.un_hide()
                break

            if new_event == '-CANCELCATEGORY-':
                new_window['-INCATEGORY-'].update('')
                new_window['-TYPECATEGORY-'].update('')

            if new_event == '-CANCELEXPENSE-':
                new_window['-COMBOBOXCATEGORY-'].update('')
                new_window['-INDETAIL-'].update('')
                new_window['-AMOUNTDETAIL-'].update('')

            if new_event == '-CANCELINCOME-':
                new_window['-COMBOCATEGORY-'].update('')
                new_window['-INDETAIL-'].update('')
                new_window['-INAMOUNT-'].update('')    

            if new_event == '-ADDCATEGORY-':
                check_category_name = models.check_input_is_valid_string(new_values['-INCATEGORY-'])
                check_category_name_has_spaces = models.check_if_user_entry_has_spaces(new_values['-INCATEGORY-'])
                check_category_type = models.check_input_is_valid_string(new_values['-TYPECATEGORY-'])
                check_category_type_has_spaces = models.check_if_user_entry_has_spaces(new_values['-TYPECATEGORY-'])
                if check_category_name == 'Empty' or check_category_type == 'Empty' or check_category_name_has_spaces == 'has spaces' or check_category_type_has_spaces == 'has spaces':
                    sg.popup('Category or type are in blank')
                else:
                    name_of_category = new_values['-INCATEGORY-']
                    type_of_category = new_values['-TYPECATEGORY-']
                    category = models.Category(name_of_category,type_of_category)
                    models.Category.save_category(category)
                    table_values_category.append([category.nombre, category.tipo])
                    new_window['-INCATEGORY-'].update('')
                    new_window['-TYPECATEGORY-'].update('')
                    new_window['-CATEGORYTABLE-'].update(values=table_values_category)

            if new_event == '-ADDEXPENSE-':
                check_category_info = models.check_input_is_valid_string(new_values['-COMBOBOXCATEGORY-'])
                check_detail_info = models.check_input_is_valid_string(new_values['-INDETAIL-'])
                check_detail_has_spaces = models.check_if_user_entry_has_spaces(new_values['-INDETAIL-'])
                check_amount_info = models.check_input_is_valid_string(new_values['-AMOUNTDETAIL-'])

                if check_category_info == 'Not empty':
                    check_if_category_already_exist = models.Category.check_if_category_already_exist(new_values['-COMBOBOXCATEGORY-'],table_values_category)
                else:
                    check_if_category_already_exist = None

                if check_if_category_already_exist == 'does not exist':
                    sg.popup('Category does not exist, please add to continue with the process')

                if check_amount_info == 'Not empty':
                    check_is_valid_number = models.Transaction.check_valid_input_number(new_values['-AMOUNTDETAIL-'])
                    if check_is_valid_number == 'is numeric':
                        amount_information = new_values['-AMOUNTDETAIL-']
                    else:
                        sg.popup('Amount value should be bigger than 0')
                else:
                    check_is_valid_number = 'Not numeric'
                
                if check_category_info == 'Empty':
                    sg.popup('Missing or Invalid Category, choose a category from dropdown list')

                if check_detail_info == 'Empty':
                    sg.popup('Missing or invalid detail, add a detail')
                
                if check_detail_has_spaces == 'has spaces':
                    sg.popup('Missing or invalid detail, add a detail')

                if check_amount_info == 'Empty':
                    sg.popup('Missing or Invalid amount, add an amount')

                if check_category_info != 'Empty' and check_detail_info != 'Empty' and check_detail_has_spaces == 'No spaces' and check_is_valid_number == 'is numeric' and check_if_category_already_exist == 'exist':
                    list_of_category_values = new_values['-COMBOBOXCATEGORY-']
                    category_information = list_of_category_values[0]
                    type_information = list_of_category_values[1]
                    detail_information = new_values['-INDETAIL-']
                    print(f'category: {category_information}, type: {type_information}, detail is: {detail_information}, amount information is: {amount_information}')
                    transaction = models.Transaction(detail_information,category_information,type_information,amount_information)
                    models.Transaction.save_transaction(transaction)
                    new_window['-INDETAIL-'].update('')
                    new_window['-AMOUNTDETAIL-'].update('')
                    new_window['-COMBOBOXCATEGORY-'].update(values=table_values_category)

            if new_event == '-ADDINCOME-':
                check_category_info = models.check_input_is_valid_string(new_values['-COMBOCATEGORY-'])
                check_detail_info = models.check_input_is_valid_string(new_values['-INDETAIL-'])
                check_detail_has_spaces = models.check_if_user_entry_has_spaces (new_values['-INDETAIL-'])
                check_amount_info = models.check_input_is_valid_string(new_values['-INAMOUNT-'])

                if check_category_info == 'Not empty':
                    check_if_category_already_exist = models.Category.check_if_category_already_exist(new_values['-COMBOCATEGORY-'],table_values_category)
                else:
                    check_if_category_already_exist = None

                if check_if_category_already_exist == 'does not exist':
                    sg.popup('Category does not exist, please add to continue with the process')
                

                if check_amount_info == 'Not empty':
                    check_is_valid_number = models.Transaction.check_valid_input_number(new_values['-INAMOUNT-'])
                    if check_is_valid_number == 'is numeric':
                        amount_information = new_values['-INAMOUNT-']
                    else:
                        sg.popup('Amount value should be bigger than 0')
                else:
                    check_is_valid_number = 'Not numeric'

                if check_category_info == 'Empty':
                    sg.popup('Missing or Invalid Category, choose a category from dropdown list')

                if check_detail_info == 'Empty':
                    sg.popup('Missing or invalid detail, add a detail')
                
                if check_detail_has_spaces == 'has spaces':
                    sg.popup('Missing or invalid detail, add a detail')

                if check_amount_info == 'Empty':
                    sg.popup('Missing or Invalid amount, add an amount')

                if check_category_info != 'Empty' and check_detail_info != 'Empty' and check_is_valid_number == 'is numeric' and check_if_category_already_exist == 'exist' and check_detail_has_spaces == 'No spaces':
                    list_of_category_values = new_values['-COMBOCATEGORY-']
                    category_information = list_of_category_values[0]
                    type_information = list_of_category_values[1]
                    detail_information = new_values['-INDETAIL-']
                    print(f'category: {category_information}, type: {type_information}, detail is: {detail_information}, amount information is: {amount_information}')
                    transaction = models.Transaction(detail_information,category_information,type_information,amount_information)
                    models.Transaction.save_transaction(transaction)
                    new_window['-INDETAIL-'].update('')
                    new_window['-INAMOUNT-'].update('')
                    new_window['-COMBOCATEGORY-'].update(values=table_values_category)

        table_values_test = data.load_main_window_movements_table()
        window['-MAINTABLE-'].update(values=table_values_test)


    window.close()

if __name__ == '__main__':
    main_window()