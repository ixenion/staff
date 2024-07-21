import traceback


def main():

    try:
        1/0
    except:
        tb = traceback.format_exc()
        print(tb)

main()
