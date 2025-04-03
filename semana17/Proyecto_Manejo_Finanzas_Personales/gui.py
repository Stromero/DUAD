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

        if event == sg.WINDOW_CLOSED:
            break
        if event == '-ADDCATEGORY-':
            window.hide()
            new_window = category_window()
        if event == '-EXPENSE-':
             window.hide()
             new_window = expense_window()
        # if event == '-INCOME-':
        #     window.hide()
        #     new_window = add_income()

        while True:
            new_event , new_values = new_window.read()

            if new_event in (sg.WIN_CLOSED, 'Back'):
                new_window.close()
                window.un_hide()
                break
            if new_event == '-CANCELCATEGORY-':
                new_window['-INCATEGORY-'].update('')
                new_window['-TYPECATEGORY-'].update('')
            if new_event == '-ADDCATEGORY-':
                check_category_name = data.check_input_is_valid_string(new_values['-INCATEGORY-'])
                check_category_type = data.check_input_is_valid_string(new_values['-TYPECATEGORY-'])
                if check_category_name == 'Empty' or check_category_type == 'Empty':
                    sg.popup('Category or type are in blank')
                else:
                    name_of_category = new_values['-INCATEGORY-']
                    type_of_category = new_values['-TYPECATEGORY-']
                    category = models.Category(name_of_category,type_of_category)
                    data.save_category(category)
                    table_values_category.append([category.nombre, category.tipo])
                    new_window['-INCATEGORY-'].update('')
                    new_window['-TYPECATEGORY-'].update('')
                    new_window['-CATEGORYTABLE-'].update(values=table_values_category)   
            if new_event == '-CANCELEXPENSE-':
                new_window['-COMBOBOXCATEGORY-'].update('')
                new_window['-INDETAIL-'].update('')
                new_window['-AMOUNTDETAIL-'].update('')
            if new_event == '-ADDEXPENSE-':
                check_category_info = data.check_input_is_valid_string(new_values['-COMBOBOXCATEGORY-'])
                print(f'Category information: {check_category_info}')
                if check_category_info == 'Empty':
                    sg.popup('Choose a category')
                else:
                    list_of_category_values = new_values['-COMBOBOXCATEGORY-']
                    category_information = list_of_category_values[0]
                    type_information = list_of_category_values[1]
                    print(f'category: {category_information}, type: {type_information}')


                #category_information = new_values['-COMBOBOXCATEGORY-']
                #convert_to_string = ' '.join(category_information)
                #new_category_value = convert_to_string        
                #res = check_if_category_exist(new_category_value,table_values_category)   
                #print(res)
                #if res == 'does not exist':
                #    sg.popup('Category does not exist, add the category to continue')
                #    new_window.close()
                #    window.un_hide()
                #    break
                #print(f'new category info: {new_category_value}')
                #detail_information = new_values['-INDETAIL-']
                #amount_information = new_values['-AMOUNTDETAIL-']
                #print(f'the category selected is: {new_category_value}, detail information is: {detail_information}, amount of this expense is: {amount_information}')
                #register(detail_information,new_category_value,'Expense',amount_information)
                #new_window['-INDETAIL-'].update('')
                #new_window['-AMOUNTDETAIL-'].update('')
                #new_window['-COMBOBOXCATEGORY-'].update(values=table_values_category)

    window.close()

if __name__ == '__main__':
    main_window()