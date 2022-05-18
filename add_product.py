import PySimpleGUI as sg
import layouts
import lists
import adding_validation
from categories import *
import database_func as df


def add_product_window():
    sg.theme('NeutralBlue')
    layout = [
        [
            sg.Frame('Add Product',
                     [[sg.Text('Select Category', font=('Bookman Old Style', 11)), sg.Combo(lists.categories, enable_events=True, default_value=lists.categories[0], key='-categories-', size=(15, 1), font=('Bookman Old Style', 11)), sg.Button('Continue', size=(12, 1), font=('Bookman Old Style', 10))]
                      ], font=('Bookman Old Style', 14), size=(500, 60), element_justification='c')
        ],
        [sg.Column(layouts.layout_for_laptop, key='Laptop', visible=False, element_justification='c'),
         sg.Column(layouts.layout_for_tablet, key='Tablet', visible=False, element_justification='c'),
         sg.Column(layouts.layout_for_smartphone, key='Smartphone', visible=False, element_justification='c')]
    ]

    window = sg.Window('Add product', layout, size=(500, 700), element_justification='c')
    layout = 'Laptop'
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Continue':  # if press on continue then layouts change according to category
            category = values['-categories-']
            window[f'{layout}'].update(visible=False)
            layout = category
            window[f'{layout}'].update(visible=True)
        elif event == 'Add Laptop':
            # assigns all values
            name, brand, model, processor, ram, display_size, display_quality, ssd, storage, graphics, description, price, currency = values['-laptop_name-'], values['-laptop_brand-'], values['-laptop_model-'], values['-laptop_processor-'], values['-laptop_ram-'], values['-laptop_size-'], values['-laptop_quality-'], values['-storage_type-'], values['-laptop_storage-'], values['graphics'], values['-laptop_description-'], values['-laptop_price-'], values['-laptop_currency-']
            if adding_validation.validation(category, brand, processor, ram, storage, display_size, display_quality, price, currency):  # assigns all to database
                vram = None
                if graphics:
                    vram = values['-vram-']
                    product = Laptop(name, brand, model, processor, ram, display_size, display_quality, ssd, storage, graphics, vram, description, price, currency)
                    if vram not in lists.vram:
                        sg.PopupError('Invalid value for VRAM')
                else:
                    product = Laptop(name, brand, model, processor, ram, display_size, display_quality, ssd, storage, graphics, vram, description, price, currency)
                df.add_laptop(product)
                sg.PopupOK('Successfully Posted')
                window.close()
        elif event == 'Add Tablet':
            # assign values
            name, brand, model, processor, ram, battery, storage, display_size, display_quality, network, description, price, currency = values['-tablet_name-'], values['-tablet_brand-'], values['-tablet_model-'], values['-tablet_processor-'], values['-tablet_ram-'], values['-tablet_battery-'], values['-tablet_storage-'], values['-tablet_size-'], values['-tablet_quality-'], values['net'], values['-tablet_description-'], values['-tablet_price-'], values['-tablet_currency-']
            # checks values
            if adding_validation.validation(category, brand, processor, ram, storage, display_size, display_quality, price, currency, battery):
                product = Tablet(name, brand, model, processor, ram, battery, storage,  display_size, display_quality, network, description, price, currency)
                # inserts in database
                df.add_tablet(product)
                sg.PopupOK('Successfully Posted')
                window.close()
        elif event == 'Add Smartphone':
            # assign values
            name, brand, model, processor, ram, battery, storage, connector, display_size, display_quality, double_sim, description, price, currency = values['-phone_name-'], values['-phone_brand-'], values['-phone_model-'], values['-phone_processor-'], values['-phone_ram-'], values['-phone_battery-'], values['-phone_storage-'], values['-phone_storage-'], values['-phone_size-'], values['-phone_quality-'], values['sim'], values['-phone_description-'], values['-phone_price-'], values['-phone_currency-']
            # check values
            if adding_validation.validation(category, brand, processor, ram, storage, display_size, display_quality, price, currency, battery):
                # inserts in database
                product = Smartphone(name, brand, model, processor, ram, battery, storage, display_size, display_quality, double_sim, description, price, currency)
                print(product)
                df.add_smartphone(product)
                sg.PopupOK('Successfully Posted')
                window.close()
