#-------------------------------EXCEPTION-------------------------------------
#try something that might throw an EXCEPTION
#except (exception name) and what you;ll do instead
#else:
#finally:

#Common exception errors:
#IndexError

try:
    int(input("Enter an integer"))
except SyntaxError:
        print("it is a syntax error!")
except ValueError:
    print("it's a value error!")

    
