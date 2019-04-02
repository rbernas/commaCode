def commaCode(inputList):

    output = ''

    for i in range(len(inputList) - 1):
        output += inputList[i] + ', '

    output += 'and ' + str(inputList[-1])

    print(output)
    print(type(output))
    
    
spam = ['apples', 'bananas', 'tofu', 'cats']

commaCode(spam)
