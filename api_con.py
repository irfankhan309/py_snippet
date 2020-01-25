def dic():
    dictionary = {}
    while True:
        try:
            key = input('enter key:')
            value = eval(input('enter the value'))
        except Exception as e:
            print('you have not enterd any key and value..')
        else:
            print("no data found")
        finally:
            print(dictionary)
            app = dictionary[key]=value
            print(dictionary)



dic()