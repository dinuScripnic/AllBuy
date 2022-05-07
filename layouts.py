import PySimpleGUI as sg
import lists

sg.theme('NeutralBlue')
layout_for_laptop = [
        [sg.Text('Name', font=('Bookman Old Style', 14)), sg.Input(key='-laptop_name-', font=('Bookman Old Style', 11))],
        [
            sg.Frame('Main Information', [
                [sg.Text('Brand', size=(10, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.laptop_brands, enable_events=True, key='-laptop_brand-', size=(20,1), font=('Bookman Old Style', 11))],
                [sg.Text('Model', size=(10, 1), font=('Bookman Old Style', 11)), sg.Input(key='-laptop_model-', size=(21, 1), font=('Bookman Old Style', 11))],
                [sg.Text('Processor', size=(10, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.laptop_processors, enable_events=True, key='-laptop_processor-', size=(20, 1), font=('Bookman Old Style', 11))],
                [sg.Text('Ram', size=(10, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.laptop_ram, default_value=8, enable_events=True, key='-laptop_ram-', size=(3, 1), font=('Bookman Old Style', 11)), sg.Text('GB', font=('Bookman Old Style', 11))]
            ], font=('Bookman Old Style', 14),  size=(500, 150))
        ],
        [
            sg.Frame('Display', [
                [sg.Text('Size', size=(6,1), font=('Bookman Old Style', 11)), sg.Combo(lists.laptop_display_size, enable_events=True, key='-laptop_size-', size=(8, 1), font=('Bookman Old Style', 11)), sg.Text('Inch', size=(5,1), font=('Bookman Old Style', 11))],
                [sg.Text('Quality', size=(6, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.display_quality, enable_events=True, key='-laptop_quality-', size=(8, 1), font=('Bookman Old Style', 11))]
            ], font=('Bookman Old Style', 14), size=(250, 90))
        ],
        [
            sg.Frame('Storage', [
                [sg.Radio('SSD', "storage", key='-storage_type-', size=(5, 1), font=('Bookman Old Style', 11)), sg.Radio('HDD', "storage", key='-storage_type-', size=(5, 1), font=('Bookman Old Style', 11))],
                [sg.Text('Size', size=(6, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.laptop_storage_size, enable_events=True, key='-laptop_storage-', size=(5, 1), font=('Bookman Old Style', 11)), sg.Text('GB', size=(5,1), font=('Bookman Old Style', 11))]
            ], font=('Bookman Old Style', 14), size=(200, 90))
            ,
            sg.Frame('Graphics', [
                [sg.Radio('Dedicated', "gc", key='graphics', size=(10,1), font=('Bookman Old Style', 11)), sg.Radio('Integrated', "gc", key='graphics', size=(10, 1), font=('Bookman Old Style', 11))],
                [sg.Text('VRAM', size=(5, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.vram, enable_events=True, key='-vram-', size=(3,1), font=('Bookman Old Style', 11))]
            ], font=('Bookman Old Style', 14), size=(250,90), element_justification='c')
        ],
        [sg.Text('Description', font=('Bookman Old Style', 11)), sg.Multiline(key='-laptop_description-', size=(30, 7), font=('Bookman Old Style', 10))],
        [sg.Text('Price', size=(6, 1), font=('Bookman Old Style', 11)), sg.Input(key='-laptop_price-', size=(18, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.currency, default_value='$', enable_events=True, key='-laptop_currency-', size=(3, 1), font=('Bookman Old Style', 11))],
        [sg.Button('Add Laptop', size=(10,2), font=('Bookman Old Style', 11))]
    ]

layout_for_tablet = [
        [sg.Text('Name', font=('Bookman Old Style', 14)), sg.Input(key='-tablet_name-', font=('Bookman Old Style', 11))],
        [
            sg.Frame('Main Information', [
                [sg.Text('Brand', size=(14, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.tablet_brands, enable_events=True, key='-tablet_brand-', size=(20,1), font=('Bookman Old Style', 11))],
                [sg.Text('Model', size=(14, 1), font=('Bookman Old Style', 11)), sg.Input(key='-tablet_model-', size=(21, 1), font=('Bookman Old Style', 11))],
                [sg.Text('Processor', size=(14, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.smartphone_processor, enable_events=True, key='-tablet_processor-', size=(20, 1), font=('Bookman Old Style', 11))],
                [sg.Text('Ram', size=(14, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.smartphone_ram, default_value=4, enable_events=True, key='-tablet_ram-', size=(4, 1), font=('Bookman Old Style', 11)), sg.Text('GB')],
                [sg.Text('Battery Capacity', size=(14, 1), font=('Bookman Old Style', 11)), sg.Input(key='-tablet_battery-', size=(21, 1), font=('Bookman Old Style', 11)), sg.Text('mAh', size=(10, 1), font=('Bookman Old Style', 11))],
                [sg.Text('Storage Size', size=(14, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.smartphone_storage, enable_events=True, key='-tablet_storage-', size=(4, 1), font=('Bookman Old Style', 11)), sg.Text('GB', size=(10, 1), font=('Bookman Old Style', 11))]
                ], font=('Bookman Old Style', 14),  size=(500, 200))
        ],
        [
            sg.Frame('Display', [
                [sg.Text('Size', size=(6, 1), font=('Bookman Old Style', 11)), sg.Input(key='-tablet_size-', size=(21, 1), font=('Bookman Old Style', 11)), sg.Text('Inch', size=(10, 1), font=('Bookman Old Style', 11))],
                [sg.Text('Quality', size=(6, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.display_quality, enable_events=True, key='-tablet_quality-', size=(8, 1), font=('Bookman Old Style', 11))]
            ], font=('Bookman Old Style', 14),  size=(500, 100))
        ],
        [sg.Radio('LTE', "net", key='net', size=(10,1), font=('Bookman Old Style', 11)), sg.Radio('Wifi', "net", key='net', size=(10,1), font=('Bookman Old Style', 11))],
        [sg.Text('Description', font=('Bookman Old Style', 11)), sg.Multiline(key='-tablet_description-', size=(30, 7), font=('Bookman Old Style', 10))],
        [sg.Text('Price', size=(6, 1), font=('Bookman Old Style', 11)), sg.Input(key='-tablet_price-', size=(18, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.currency, default_value='$', enable_events=True, key='-tablet_currency-', size=(3, 1), font=('Bookman Old Style', 11))],
        [sg.Button('Add Tablet', size=(10, 2), font=('Bookman Old Style', 11))]
    ]

layout_for_smartphone = [
        [sg.Text('Name', font=('Bookman Old Style', 14)), sg.Input(key='-phone_name-', font=('Bookman Old Style', 11))],
        [
            sg.Frame('Main Information', [
                [sg.Text('Brand', size=(14, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.smartphone_brands, enable_events=True, key='-phone_brand-', size=(20,1), font=('Bookman Old Style', 11))],
                [sg.Text('Model', size=(14, 1), font=('Bookman Old Style', 11)), sg.Input(key='-phone_model-', size=(21, 1), font=('Bookman Old Style', 11))],
                [sg.Text('Processor', size=(14, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.smartphone_processor, enable_events=True, key='-phone_processor-', size=(20, 1), font=('Bookman Old Style', 11))],
                [sg.Text('Ram', size=(14, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.smartphone_ram, default_value=4, enable_events=True, key='-phone_ram-', size=(4, 1), font=('Bookman Old Style', 11)), sg.Text('GB', size=(10, 1), font=('Bookman Old Style', 11))],
                [sg.Text('Battery Capacity', size=(14, 1), font=('Bookman Old Style', 11)), sg.Input(key='-phone_battery-', size=(21, 1), font=('Bookman Old Style', 11)), sg.Text('mAh', size=(10, 1), font=('Bookman Old Style', 11))],
                [sg.Text('Storage Size', size=(14, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.smartphone_storage, enable_events=True, key='-phone_storage-', size=(4, 1), font=('Bookman Old Style', 11)), sg.Text('GB')],
                [sg.Text('Connector', size=(14, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.connectors, enable_events=True, key='-connector-', size=(10,1), font=('Bookman Old Style', 11))]
            ], font=('Bookman Old Style', 14),  size=(500, 200))
        ],
        [
            sg.Frame('Display', [
                [sg.Text('Size', size=(6,1), font=('Bookman Old Style', 11)), sg.Input(key='-phone_size-', size=(21, 1), font=('Bookman Old Style', 11)), sg.Text('Inch', size=(10, 1), font=('Bookman Old Style', 11))],
                [sg.Text('Quality', size=(6, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.display_quality, enable_events=True, key='-phone_quality-', size=(8, 1), font=('Bookman Old Style', 11))]
            ], font=('Bookman Old Style', 14),  size=(500, 100))
        ],
        [sg.Radio('Double SIM', "sim", key='sim', size=(10,1), font=('Bookman Old Style', 11)), sg.Radio('Single SIM', "sim", key='sim', size=(10,1), font=('Bookman Old Style', 11))],
        [sg.Text('Description', font=('Bookman Old Style', 11)), sg.Multiline(key='-phone_description-', size=(30, 7), font=('Bookman Old Style', 10))],
        [sg.Text('Price', size=(6, 1), font=('Bookman Old Style', 11)), sg.Input(key='-phone_price-', size=(18, 1), font=('Bookman Old Style', 11)), sg.Combo(lists.currency, default_value='$', enable_events=True, key='-phone_currency-', size=(3, 1), font=('Bookman Old Style', 11))],
        [sg.Button('Add Smartphone', size=(14, 2), font=('Bookman Old Style', 11))]
    ]
