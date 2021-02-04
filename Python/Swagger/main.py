import get_badge as gb
import send_to_excel as excel
# GUI Library
import PySimpleGUI as sg


EXCEL_FILE = 'swag_list.xlsx'
IMAGES = 'images/'
BADGE_IMAGE = IMAGES + 'badge_id.png'
BARCODE_ID = IMAGES + 'barcode_id'
NULL_BADGE = IMAGES + 'null_badge.png'
NULL_BARCODE = IMAGES + 'null_id.png'
SIZES = ['XS', 'S', 'M', 'L', 'XL', '2XL', '3Xl']
menu_def = [['File', ['Open', 'Save', 'About']]]
badge_color = 'lightskyblue'


def name_correction(name):
    if "," in name:
        name = name.split(",")
        name.reverse()
    elif " " in name:
        name = name.split(" ")
    return f'{name[0]} {name[1]}'


def check_radios():
    selected = ""
    for size in SIZES:
        if values[size] is True:
            selected = size
    return selected


def update_images(name, login, barcode_number):
    gb.set_image(login, BADGE_IMAGE)
    gb.set_barcode(barcode_number, BARCODE_ID)
    full_name = name_correction(name)
    window['image_badge'](filename=BADGE_IMAGE)
    window['image_badge'].set_tooltip(tooltip_text=f'{full_name}')
    window['text_login'](f'{login}')
    window['text_name'](f'{full_name}')
    window['image_barcode'](filename=BARCODE_ID + '.png', size=(150, 30))
    window['image_barcode'].set_tooltip(tooltip_text=f'{barcode_number}')


def set_employee_info(shift, site, employee_id):
    window['input_shift'](shift)
    site = site.split(" ")
    window['input_site'](site[0])
    window['input_employee_id'](employee_id)


def update_badge_info(value):
    try:
        if value.isdigit():
            numerical = gb.get_partial(value)[0]['employeeLogin']
            associate_info = gb.get_full(numerical)
        else:
            associate_info = gb.get_full(value)

        login = associate_info['azuid']
        site = associate_info['locName']
        employee_id = associate_info['employeeId']
        name = associate_info['name']
        barcode_number = associate_info['employeeBarcode']

        set_employee_info(0, site, employee_id)
        update_images(name, login, barcode_number)
        status_update(f'{name}: {login} info found!')
    except Exception as e:
        status_update(f'Grab Badge: {e}')


def employee_info_frame():
    text_shift = sg.Text('Shift:')
    input_shift = sg.InputText('', key='input_shift', size=(10, 1), disabled=True)
    text_site = sg.Text('Building:')
    input_site = sg.InputText('', key='input_site', size=(10, 1), disabled=True)
    text_employee_id = sg.Text('Employee ID:')
    input_employee_id = sg.InputText('', key='input_employee_id', size=(10, 1), disabled=True)
    layout_info = [[text_shift, input_shift], [text_site, input_site], [text_employee_id, input_employee_id]]
    frame_info = sg.Frame('', layout=layout_info, key='frame_info', element_justification='right')
    return frame_info


def badge_frame():
    image_badge = sg.Image(filename=NULL_BADGE, key='image_badge')
    image_barcode = sg.Image(filename=NULL_BARCODE, key='image_barcode', size=(150, 30))
    text_login = sg.Text("Login", font=('Any', 16), size=(8, 1), justification='center', text_color='black',
                         background_color=badge_color, key='text_login')
    text_name = sg.Text("Name", font=('Any', 16), size=(8, 2), justification='center', text_color='black',
                        background_color=badge_color, key='text_name')
    column_badge_layout_1 = [[text_login], [image_badge], [text_name], [image_barcode]]
    column_badge = sg.Column(column_badge_layout_1, background_color=badge_color,
                         element_justification='center', key='column_badge')
    frame_badge = sg.Frame('', [[column_badge]], key='frame_badge', background_color=badge_color)
    return frame_badge


def badge_input_frame():
    text_input_login = sg.Text("Login")
    input_badge = sg.InputText('', key='input_badge', focus=True, do_not_clear=False, size=(30, 1))
    submit_badge = sg.Button('Get Badge', key='submit_badge', bind_return_key=True)
    frame_layout_badge_input = [[text_input_login, input_badge, submit_badge]]
    frame_badge_input = sg.Frame('', frame_layout_badge_input, element_justification='center')
    return frame_badge_input


def selection_frame():
    confirm_selection = sg.Button('Confirm')
    column_sizes = sg.Column(all_sizes, justification='center')
    frame_layout_selection = [[column_sizes, confirm_selection]]
    frame_selection = sg.Frame('', frame_layout_selection, element_justification='center')
    return frame_selection


def radio_sizes(text, group_id):
    return sg.Radio(text, group_id=group_id, key=text, font=("default", 20))


all_sizes = [[radio_sizes(size, 'Sizes')] for size in SIZES]
menu_1 = sg.Menu(menu_def)
status_update = sg.StatusBar('', size=(45, 1), key='status_update', relief='flat', text_color='black')

layout = [[menu_1],
          [employee_info_frame()],
          [badge_frame(), selection_frame()],
          [badge_input_frame()],
          [status_update]]

window = sg.Window('Swag Keeper', layout, use_default_focus=True)

data_sheet = excel.Book(EXCEL_FILE)
data_sheet.get_values()

if __name__ == '__main__':
    while True:  # Event Loop
        event, values = window.Read()
        print(values['input_badge'])
        if event == 'submit_badge':
            update_badge_info(values['input_badge'])

        if event == 'Confirm':
            radio_selection = check_radios()
            if not data_sheet.check_value(window["text_login"].DisplayText):
                data_sheet.add_row([window["text_login"].DisplayText, window["text_name"].DisplayText,
                                   values['input_employee_id'], radio_selection])
            else:
                status_update(f'{window["text_login"].DisplayText} is already on list!')
                new_selection = sg.PopupYesNo("Would you like to change selection?")
                print(new_selection)
                if new_selection == 'Yes':
                    data_sheet.change_selection(window["text_login"].DisplayText, radio_selection)
            data_sheet.get_values()
        if event == 'About':
            sg.Popup("Program designed by Sean Duncan")
        if event in ('Exit', None):
            break

window.Close()
