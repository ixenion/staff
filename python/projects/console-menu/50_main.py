# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from consolemenu.menu_component import Dimension

def action(name):
    print("\nHello from action {}!!!\n".format(name))
    Screen().input('Press [Enter] to continue')
def input_handler():
    pu = PromptUtils(Screen())
    # PromptUtils.input() returns an InputResult
    result = pu.input("Enter an input")
    pu.println("\nYou entered:", result.input_string, "\n")
    pu.enter_to_continue()


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


# Create a second submenu, but this time use a standard ConsoleMenu instance
submenu_1 = ConsoleMenu("Another Submenu Title", "Submenu subtitle.")
function_item_1 = FunctionItem("Fun item", input_handler)
item1 = MenuItem("Another Item")
submenu_1.append_item(function_item_1)
submenu_1.append_item(item1)
submenu_item_1 = SubmenuItem("Another submenu", submenu=submenu_1)
submenu_item_1.set_menu(menu)


menu.append_item(FunctionItem("Add UE", input_handler, args=['one']))
menu.append_item(submenu_item_1)


menu.show()
menu.join()
