# tutorial
# https://www.youtube.com/watch?v=3QiPPX-KeSc&ab_channel=TechWithTim
# to transfer objects use pickle (the way to serialize it)

import select
import socket 
import threading
import time

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        
def start():
    global dead
    server.listen()
    read_list = [server]
    #print(f"[LISTENING] Server is listening on {SERVER}")
    while not dead:
        #try:
        readable, writable, errored = select.select(read_list, [], [], 1)
        #except ValueError:
        #    pass
        #print(read_list)
        for s in readable:
            if s is server:
                conn, addr = server.accept()
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()
                #read_list.append(conn)
        #print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

threads = []
def start_server():
    global dead, thread
    dead = False
    print(f"[INFO] SERVER Listening on {SERVER}")
    thread = threading.Thread(target=start)
    threads.append(thread)
    thread.start()
    Screen().input('\nPress [Enter] to continue.')

def stop_server():
    global dead, thread
    dead = True
    server.close()
    while thread.is_alive():
        time.sleep(0.2)
    print(f"[INFO] SERVER Down.")
    Screen().input('\nPress [Enter] to continue.')
    #thread.exit()


###################################################3

# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from consolemenu.menu_component import Dimension

def clients_list():
    #print("\nHello from action {}!!!\n".format(name))
    #print("\n{}\n".format(name))
    print(f"[INFO] SERVER Active connections: {threading.activeCount() - 3}")
    #for i in msisdn_list:
    #    print(i)
    Screen().input('\nPress [Enter] to continue.')

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

menu_format.set_title_align('center')
menu_format.set_prologue_text_align('center')
menu_format.show_prologue_bottom_border(True)

# Create the root menu
menu = ConsoleMenu("Server menu.",
                   prologue_text=("This is a demo of client-server app."))
menu.formatter = menu_format

list_cl = FunctionItem("Clients connected", clients_list, args=None)
start_s = FunctionItem("SERVER Start",start_server,args=None)
stop_s = FunctionItem("SERVER Stop",stop_server,args=None)

add_ue = FunctionItem("Add UE", input_handler, args=['add'])
remove_ue = FunctionItem("Remove UE", input_handler, args=['remove'])
get_location = MenuItem("Get location")




#list_ue = FunctionItem("List available UE", action, args=['UE list:'])
#add_ue = FunctionItem("Add UE", input_handler, args=['add'])
#remove_ue = FunctionItem("Remove UE", input_handler, args=['remove'])
#get_location = MenuItem("Get location")

menu.append_item(list_cl)
menu.append_item(start_s)
menu.append_item(stop_s)
#menu.append_item(remove_ue)
#menu.append_item(get_location)


menu.show()
menu.join()

