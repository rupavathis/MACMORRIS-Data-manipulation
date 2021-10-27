# from tqdm.auto import tqdm


def read_file(filename):
    with open(filename, 'r') as readFile:
        lines = readFile.readlines()
    return lines
    

def strip_elements(lines):
    lines_stripped = []
    for i in lines:
        i = i.split(',')
        stripWords = [e.strip(' ') for e in i]
        lines_stripped.append(stripWords)
    return lines_stripped

def write_file(lines, filename):
    with open(filename, 'w') as write_File:
        for i in lines:      
            i_str = ','.join(i)         
            print(i_str.rstrip(), file=write_File)


def change_names_to_ids(lines, language_list):
    linesList = []
 
    for i in lines:
        splitLines = i.split(',')
        linesList.append(splitLines)

    print(set(language_list))
    print(linesList)
    a = set(linesList[1])
    print(a)
    # return changedIds       
   
                   
     

lines = read_file('test.csv')
lines = strip_elements(lines)
write_file(lines, 'test_out.csv')
# out_lines = read_file('people_output.csv')
# language_list = read_file('Language_List.csv')
# print(language_list)
# ids = change_names_to_ids(out_lines, language_list)

# print(ids)
