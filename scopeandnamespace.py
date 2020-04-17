
#namespace is like container in which names and the values are mapped
#scope is the region where a variable is acessible
name="bhanu"
def home():
    #name="bannu"#this variable is different from the name which is present in global scope
    #if we want to use the name in the home function then we need to use global keyword
    global name
    name='baanu'
    print(name)
    #say we need to access a variable a which is in local scope also which
    #is outside the scope from where we need to access then we need to use nonlocal
    name2='bhanu prathap'
    
    def sister():
        nonlocal name2
        print(name2)
        name2='annaya'
        print(name2)
    sister()
    
    
home()
print(name)
