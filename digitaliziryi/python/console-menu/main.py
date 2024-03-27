# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from consolemenu.menu_component import Dimension

def action(name):
    #print("\nHello from action {}!!!\n".format(name))
    print("\n{}\n".format(name))
    for i in msisdn_list:
        print(i)
    Screen().input('\nPress [Enter] to continue')

def input_handler(action):
    pu = PromptUtils(Screen())
    # PromptUtils.input() returns an InputResult
    result = pu.input("Enter an MSISDN: ")
    pu.println("\nYou entered: ", result.input_string, "\n")
    if action == 'add':
        msisdn_list.append(result.input_string)
    if action == 'remove':
        msisdn_list.remove(result.input_string)
    pu.enter_to_continue()

msisdn_list = []

# Menu Format
thin = Dimension(width=80, height=40)  # Use a Dimension to limit the "screen width" to 40 characters

menu_format = MenuFormatBuilder(max_dimension=thin)

# Set the border style to use heavy outer borders and light inner borders
menu_format.set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_OUTER_LIGHT_INNER_BORDER)

menu_format.set_title_align('center')                   # Center the menu title (by default it's left-aligned)
menu_format.set_prologue_text_align('center')           # Center the prologue text (by default it's left-aligned)
menu_format.show_prologue_bottom_border(True)           # Show a border under the prologue

# Create the root menu
menu = ConsoleMenu("QGIS Console",
                   prologue_text=("This is a demo of qgis console app."))
menu.formatter = menu_format

list_ue = FunctionItem("List available UE", action, args=['UE list:'])
add_ue = FunctionItem("Add UE", input_handler, args=['add'])
remove_ue = FunctionItem("Remove UE", input_handler, args=['remove'])

get_location = MenuItem("Get location")

menu.append_item(list_ue)
menu.append_item(add_ue)
menu.append_item(remove_ue)
menu.append_item(get_location)


menu.show()
menu.join()
