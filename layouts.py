import PySimpleGUI as sg
import lists

layout_for_laptop = [
        [sg.Text('Name'), sg.Input(key='-laptop_name-')],
        [
            sg.Frame('Main Information',
                     [[sg.Text('Brand'), sg.Combo(lists.laptop_brands, enable_events=True, key='-laptop_brand-')],
                      [sg.Text('Model'), sg.Input(key='-laptop_model-')],
                      [sg.Text('Processor'), sg.Combo(lists.laptop_processors, enable_events=True, key='-laptop_processor-')],
                      [sg.Text('Ram'), sg.Combo(lists.laptop_ram, default_value=8, enable_events=True, key='-laptop_ram-'), sg.Text('GB')]])
        ],
        [
            sg.Frame('Display', [
                [sg.Text('Size'), sg.Combo(lists.laptop_display_size, enable_events=True, key='-laptop_size-'), sg.Text('Inch')],
                [sg.Text('Quality'), sg.Combo(lists.display_quality, enable_events=True, key='-laptop_quality-')]
            ])
        ],
        [
            sg.Frame('Storage',
                     [[sg.Radio('SSD', "storage", key='-storage_type-'), sg.Radio('HDD', "storage", key='-storage_type-')],
                      [sg.Text('Size'), sg.Combo(lists.laptop_storage_size, enable_events=True, key='-laptop_storage-'), sg.Text('GB')]
                      ])
        ],
        [
            sg.Frame('Graphics',
                     [[sg.Radio('Dedicated', "gc", key='graphics'), sg.Radio('Integrated', "gc", key='graphics')],
                      [sg.Text('VRAM'), sg.Combo(lists.vram, enable_events=True, key='-vram-')]
                      ])
        ],
        [sg.Text('Description'), sg.Multiline(key='-laptop_description-')],
        [sg.Text('Price'), sg.Input(key='-laptop_price-'), sg.Combo(lists.currency, default_value='$', enable_events=True, key='-laptop_currency-')],
        [sg.Button('Add Laptop')]
    ]

layout_for_tablet = [
        [sg.Text('Name'), sg.Input(key='-tablet_name-')],
        [
            sg.Frame('Main Information',
                     [[sg.Text('Brand'), sg.Combo(lists.tablet_brands, enable_events=True, key='-tablet_brand-')],
                      [sg.Text('Model'), sg.Input(key='-tablet_model-')],
                      [sg.Text('Processor'), sg.Combo(lists.smartphone_processor, enable_events=True, key='-tablet_processor-')],
                      [sg.Text('Ram'), sg.Combo(lists.smartphone_ram, default_value=4, enable_events=True, key='-tablet_ram-'), sg.Text('GB')],
                      [sg.Text('Battery Capacity'), sg.Input(key='-tablet_battery-'), sg.Text('mAh')],
                      [sg.Text('Storage Size'), sg.Combo(lists.smartphone_storage, enable_events=True, key='-tablet_storage-'), sg.Text('GB')]
                      ])
        ],
        [
            sg.Frame('Display', [
                [sg.Text('Size'), sg.Input(key='-tablet_size-'), sg.Text('Inch')],
                [sg.Text('Quality'), sg.Combo(lists.display_quality, enable_events=True, key='-tablet_quality-')]
            ])
        ],
        [sg.Radio('LTE', "net", key='net'), sg.Radio('Wifi', "net", key='net')],
        [sg.Text('Description'), sg.Multiline(key='-tablet_description-')],
        [sg.Text('Price'), sg.Input(key='-tablet_price-'), sg.Combo(lists.currency, default_value='$', enable_events=True, key='-tablet_currency-')],
        [sg.Button('Add Tablet')]
    ]

layout_for_smartphone = [
        [sg.Text('Name'), sg.Input(key='-phone_name-')],
        [
            sg.Frame('Main Information',
                     [[sg.Text('Brand'), sg.Combo(lists.smartphone_brands, enable_events=True, key='-phone_brand-')],
                      [sg.Text('Model'), sg.Input(key='-phone_model-')],
                      [sg.Text('Processor'), sg.Combo(lists.smartphone_processor, enable_events=True, key='-phone_processor-')],
                      [sg.Text('Ram'), sg.Combo(lists.smartphone_ram, default_value=4, enable_events=True, key='-phone_ram-'), sg.Text('GB')],
                      [sg.Text('Battery Capacity'), sg.Input(key='-phone_battery-'), sg.Text('mAh')],
                      [sg.Text('Storage Size'), sg.Combo(lists.smartphone_storage, enable_events=True, key='-phone_storage-'), sg.Text('GB')],
                      [sg.Text('Connector'), sg.Combo(lists.connectors, enable_events=True, key='-connector-')]])
        ],
        [
            sg.Frame('Display', [
                [sg.Text('Size'), sg.Input(key='-phone_size-'), sg.Text('Inch')],
                [sg.Text('Quality'), sg.Combo(lists.display_quality, enable_events=True, key='-phone_quality-')]
            ])
        ],
        [sg.Radio('Double SIM', "sim", key='sim'), sg.Radio('Single SIM', "sim", key='sim')],
        [sg.Text('Description'), sg.Multiline(key='-phone_description-')],
        [sg.Text('Price'), sg.Input(key='-phone_price-'), sg.Combo(lists.currency, default_value='$', enable_events=True, key='-phone_currency-')],
        [sg.Button('Add Smartphone')]
    ]
