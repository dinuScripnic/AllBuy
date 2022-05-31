import PySimpleGUI as sg
import lists


def validation(category, brand, processor, ram, storage, display_size, display_quality, price, currency, *args):
    """
    Check the validity of the input before sends data to database
    Works for all categories in one go
    If something is not valid, sends an error
    """
    if category == "Laptop":
        if brand not in lists.laptop_brands:  # check validity of brand
            sg.PopupError('Invalid value for Brand')
            return False
        if processor not in lists.laptop_processors:  # check validity of processor
            sg.PopupError('Invalid value for Processor')
            return False
        if ram not in lists.laptop_ram:  # check validity of ram
            sg.PopupError('Invalid value for RAM')
            return False
        if display_size not in lists.laptop_display_size:  # check validity of display size
            sg.PopupError('Invalid value for Display Size')
        if storage not in lists.laptop_storage_size:  # check validity of storage size
            sg.PopupError('Invalid value for Storage Size')
            return False
    if category in ['Tablet', 'Smartphone']:
        if category == 'Tablet':
            if brand not in lists.tablet_brands:
                sg.PopupError('Invalid value for Brand')
                return False
            try:
                display_size = float(display_size)
                if not(display_size >= 10 and display_size < 15):  # made like this because i need to check for float
                    # if use range checks just for int
                    sg.PopupError('Invalid value for Display Size')
            except ValueError:
                sg.PopupError('Invalid format for Display Size!\nNUMBERS ONLY')
                return False
        if category == 'Smartphone':
            try:
                display_size = float(display_size)
                if not (display_size >= 4.7 and display_size < 8):
                    sg.PopupError('Invalid value for Display Size')
                    return False
            except ValueError:
                sg.PopupError('Invalid format for Display Size!\nNUMBERS ONLY')
                return False
        if processor not in lists.smartphone_processor:
            sg.PopupError('Invalid value for Processor')
            return False
        if ram not in lists.smartphone_ram:
            sg.PopupError('Invalid value for RAM')
            return False
        if storage not in lists.smartphone_storage:
            sg.PopupError('Invalid value for Storage Size')
            return False
        if not args[0].isdigit():
            sg.PopupError('Invalid format for Battery!\nNUMBERS ONLY')
            return False
    if display_quality not in lists.display_quality:
        sg.PopupError('Invalid value for Display Quality')
        return False
    if not price.isdigit():
        sg.PopupError('Invalid format for Price!\nNUMBERS ONLY')
        return False
    if currency not in lists.currency:
        sg.PopupError('Invalid value for Currency')
        return False
    return True
