def div_check():
    name_of_class = __name__
    module_name = __module__
    list = [0,1,2,3,4,5,6,7,8,9,10]
    output = filter(lambda x:x % 2 == 0, list)
    print(output)
    print(name_of_class)
    #print(module_name)
    
div_check()
