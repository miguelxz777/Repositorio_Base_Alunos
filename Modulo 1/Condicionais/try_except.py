def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("por favor,nao ultilize zeros!")
    except:
        print("\033[91m algo deu errado...]")
    else:
        print(f"seu resultado é:{result}")
    finally:
        print("\033[92m Vamos de novo?")
divide(13,0)
divide("x","y")
divide(-3,-4,)