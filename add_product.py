import PySimpleGUI as sg
import layouts
import lists


def add_product_window():
    categories = ['Laptop', 'Tablet', 'Smartphone']
    sg.theme('DarkAmber')
    layout = [
        [
            sg.Frame('Add Product',
                     [[sg.Text('Select Category'), sg.Combo(categories, enable_events=True, default_value=categories[0],
                                                            key='-categories-'), sg.Button('Continue')]
                      ])
        ],
        [sg.Column(layouts.layout_for_laptop, key='Laptop', visible=False),
         sg.Column(layouts.layout_for_tablet, key='Tablet', visible=False),
         sg.Column(layouts.layout_for_smartphone, key='Smartphone', visible=False)]
    ]

    window = sg.Window('Add product', layout, size=(600, 600))
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
            correct = True
            # assigns all values
            name, brand, model, processor, ram, display_size, display_quality, ssd, storage, graphics, description, price, currency = values['-laptop_name-'], values['-laptop_brand-'], values['-laptop_model-'], values['-laptop_processor-'], values['-laptop_ram-'], values['-laptop_size-'], values['-laptop_quality-'], values['-storage_type-'], values['-laptop_storage-'], values['graphics'], values['-laptop_description-'], values['-laptop_price-'], values['-laptop_currency-']
            # checks inputs
            if brand not in lists.laptop_brands:
                correct = False
                sg.PopupError('Invalid value for Brand')
            if processor not in lists.laptop_processors:
                correct = False
                sg.PopupError('Invalid value for Processor')
            if ram not in lists.laptop_ram:
                correct = False
                sg.PopupError('Invalid value for RAM')
            if display_size not in lists.laptop_display_size:
                correct = False
                sg.PopupError('Invalid value for Display Size')
            if display_quality not in lists.display_quality:
                correct = False
                sg.PopupError('Invalid value for Display Quality')
            if storage not in lists.laptop_storage_size:
                correct = False
                sg.PopupError('Invalid value for Storage Size')
            if graphics:
                vram = values['-vram-']
                if vram not in lists.vram:
                    correct = False
                    sg.PopupError('Invalid value for VRAM')
            else:
                vram = None
            if not price.isdigit():
                correct = False
                sg.PopupError('Invalid format for price!\nNUMBERS ONLY')
            else:
                price = int(price)
            if correct:  # assigns all to database
                print(f'name:{name} brand:{brand} model:{model} pro:{processor} ram:{ram} ds:{display_size} dq:{display_quality} ssd:{ssd} str:{storage} gr:{graphics} vrm:{vram} dsc:{description} p:{price} cu:{currency}')
                sg.PopupOK('Successfully Posted')
                window.close()
        elif event == 'Add Tablet':
            correct = True
            # assign values
            name, brand, model, processor, ram, battery, storage, display_size, display_quality, network, description, price, currency = values['-tablet_name-'], values['-tablet_brand-'], values['-tablet_model-'], values['-tablet_processor-'], values['-tablet_ram-'], values['-tablet_battery-'], values['-tablet_storage-'], values['-tablet_size-'], values['-tablet_quality-'], values['net'], values['-tablet_description-'], values['-tablet_price-'], values['-tablet_currency-']
            # check values
            if brand not in lists.tablet_brands:
                correct = False
                sg.PopupError('Invalid value for Brand')
            if processor not in lists.smartphone_processor:
                correct = False
                sg.PopupError('Invalid value for Processor')
            if ram not in lists.smartphone_ram:
                correct = False
                sg.PopupError('Invalid value for RAM')
            if not battery.isdigit():
                correct = False
                sg.PopupError('Invalid format for Battery!\nNUMBERS ONLY')
            else:
                battery = int(battery)
            if storage not in lists.smartphone_storage:
                correct = False
                sg.PopupError('Invalid value for Storage Size')
            try:
                display_size = float(display_size)
                if not(display_size >= 10 and display_size < 15):
                    correct = False
                    sg.PopupError('Invalid value for Display Size')
            except ValueError:
                correct = False
                sg.PopupError('Invalid format for Display Size!\nNUMBERS ONLY')
            if display_quality not in lists.display_quality:
                correct = False
                sg.PopupError('Invalid value for Display Quality')
            if not price.isdigit():
                correct = False
                sg.PopupError('Invalid format for Battery!\nNUMBERS ONLY')
            else:
                price = int(price)
            if currency not in lists.currency:
                correct = False
                sg.PopupError('Invalid value for Currency')
            if correct:  # if everything fine, inserts in database
                sg.PopupOK('Successfully Posted')
                print(f'name:{name} brand:{brand} model:{model} processor:{processor} ram:{ram} display_size:{display_size} quality:{display_quality} battery:{battery} storage:{storage} net:{network} desc:{description} p:{price} cu:{currency}')
                window.close()
        elif event == 'Add Smartphone':
            correct = True
            # assign values
            name, brand, model, processor, ram, battery, storage, connector, display_size, display_quality, double_sim, description, price, currency = values['-phone_name-'], values['-phone_brand-'], values['-phone_model-'], values['-phone_processor-'], values['-phone_ram-'], values['-phone_battery-'], values['-phone_storage-'], values['-phone_storage-'], values['-phone_size-'], values['-phone_quality-'], values['sim'], values['-phone_description-'], values['-phone_price-'], values['-phone_currency-']
            # checks values
            if brand not in lists.smartphone_brands:
                correct = False
                sg.PopupError('Invalid value for Brand')
            if processor not in lists.smartphone_processor:
                correct = False
                sg.PopupError('Invalid value for Processor')
            if ram not in lists.smartphone_ram:
                correct = False
                sg.PopupError('Invalid value for RAM')
            if not battery.isdigit():
                correct = False
                sg.PopupError('Invalid format for Battery!\nNUMBERS ONLY')
            else:
                battery = int(battery)
            if storage not in lists.smartphone_storage:
                correct = False
                sg.PopupError('Invalid value for Storage Size')
            try:
                display_size = float(display_size)
                if not (display_size >= 4.7 and display_size < 8):
                    correct = False
                    sg.PopupError('Invalid value for Display Size')
            except ValueError:
                correct = False
                sg.PopupError('Invalid format for Display Size!\nNUMBERS ONLY')
            if display_quality not in lists.display_quality:
                correct = False
                sg.PopupError('Invalid value for Display Quality')
            if not price.isdigit():
                correct = False
                sg.PopupError('Invalid format for Battery!\nNUMBERS ONLY')
            else:
                price = int(price)
            if currency not in lists.currency:
                correct = False
                sg.PopupError('Invalid value for Currency')
            if correct:  # inserts in database
                sg.PopupOK('Successfully Posted')
                print(
                    f'name:{name} brand:{brand} model:{model} processor:{processor} ram:{ram} display_size:{display_size} quality:{display_quality} battery:{battery} storage:{storage} sim:{double_sim} desc:{description} p:{price} cu:{currency}')
                window.close()


add_product_window()
