def somma_valori(input_file):
    values=[]
    my_file = open(str(input_file) ,'r')
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            dates = elements[0] 
            value = elements[1]
            values.append(float(value))
    
    return sum(values)

