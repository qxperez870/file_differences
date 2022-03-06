'''
Programa para identificar la primera diferencia entre dos archivos
'''

def is_short_line1(line_1, line_2):
    '''
    Inputs:
    

    Output:
    
    '''
    len_line_1 = len(line_1)
    len_line_2 = len(line_2)
    if (len_line_1 <  len_line_2):
        return True
    elif (len_line_2 < len_line_1):
        return False

#print(is_short_line1("abcd", "abc"))


def is_equal_len(l_1, l_2):
    '''
    Inputs:
    

    Output:
    
    '''
    if (len(l_1) == len(l_2)):
        return True
    else:
        return False



def singleline_diff(string1, string2):
    '''
    Inputs:
    

    Output:
    
    '''
    idx_change = 0
    cont = 0
    for char1, char2 in zip(string1, string2):
        if char1 == char2:
            cont += 1
                
        else: 
            idx_change = cont
            break
    
    identical = idx_change != cont
    ident = -1
    if (not identical and is_equal_len(string1, string2)) and ((string1 != '') and (string2 !='')):
        return idx_change
    elif identical and not is_equal_len(string1, string2):
        if is_short_line1(string1, string2):
            
            return len(string1)
        else:
            
            return len(string2)
    elif (identical and is_equal_len(string1, string2)) or ((string1 == '') and (string2 == '')):
        return ident
    else:
        return idx_change


#print(singleline_diff("abcd", "abc"))
#print(singleline_diff('a', 'b'))
#print(singleline_diff('abc', 'abc'))
#print(singleline_diff('abc', 'abcd'))
#print(singleline_diff('', ''))



def singleline_diff_format(line1, line2, idx):
    '''
    Inputs:
    line1 --> first single line string
    line2 --> second single line string

    Output:
    Return the index where the first difference between
    line1 and line2 occurs.
    '''
    
    shorter = is_short_line1(line1, line2)

    
    if (shorter and (0 <= idx <= len(line1))) or (not shorter and ( 0 <= idx <= len(line2))):
        mult = idx
        separator_line = (mult*"=") + '^'

        line1_print = line1 + '\n'
        return line1_print + separator_line + '\n' + line2 +'\n'



    else:
        return ""


def multiline_diff(lines1, lines2):
    '''
    Inputs:
    lines1 --> list of single line strings
    lines2 --> list of single line strings

    Output:
    Return a tuple containing the line number (starting from 0) and 
    index in that line where the first difference between lines1 and
    lines2 occurs

    Returns (IDENTICAL, IDENTICAL) if the 2 lists are the same.
    '''
    cont = 0
    indice = 0

    if ((lines1 == []) and (lines2 == [])):
        return (-1, -1)

    elif (len(lines1) == len(lines2)):
        for string1, string2 in zip(lines1, lines2):
            equal_string = (string1 == string2) 
            
            if equal_string:
                cont = cont + 1

                if cont == len(lines1):
                    return (-1, -1)

            if not equal_string:
                indice = singleline_diff(string1, string2)
        
                return (cont, indice)
               

    else:
        len_lines1 = len(lines1) 
        len_lines2 = len(lines2)

        shorter_lines = len_lines1
        if len_lines2 < len_lines1:
            shorter_lines = len_lines2

        for string1, string2 in zip(lines1[:shorter_lines], lines2[:shorter_lines]):
            equal_string = (string1 == string2) 
            
            if equal_string:
                cont = cont + 1

            elif not equal_string:
                indice = singleline_diff(string1, string2)
        
                return (cont, indice)

                


        return (cont, indice)

        
def get_file_lines(filename):
    '''
    Inputs
    Filename: name to file to read
    Output
    Return a list of lines from the file named filename. Each line will be a single line
    string with no newline ('\n') or return ('\r') characters. If the file does
    not exist or is not readable, then the behavior of this function is undefined
    '''
    with open(filename, "rt") as openfile:
    
    
        lines = []
        for line in openfile:
            lines1 = line.strip()
            lines.append(lines1)
        

    return lines



def file_diff_format(filename1, filename2):
    '''
    Inputs
    filename1 - name of first file
    filename2 - name of second file
    Output
    Return 4 lines string showing the location of the first difference
    between the two files named by the inputs
    If the files are identical, the function instead returns the string
    "No diferences\n"
    If either file does not exist or is not readable, the the behavior of
    this function is undefined
    '''

    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)

    if (len(lines1) >= 0 and len(lines2) >= 0):

        if (lines1 == lines2):
            return "No differences\n"

        elif (lines1 != lines2):
            cont, index = multiline_diff(lines1, lines2)
            for_return = "Line " + str(cont) + ":" + '\n'
            return for_return + singleline_diff_format(lines1[cont], lines2[cont], index)


        

#print(multiline_diff(["aeiou", "pepito"], ["aeiou", "pepiito"]))
#print(multiline_diff(['line1', 'line2'], ['line1', 'line2']))
#print(multiline_diff(['line1', 'line2'], ['line1', 'line2', 'line3']))
print(multiline_diff([], []))

#print(get_file_lines("esto_es.txt"))
#print(file_diff_format("ensayos1.txt", "ensayos.txt"))