def readResults(file_address):  # used to read a result file (wtop40,wtop50...)

    with open(file_address) as f:
        lines = f.readlines()  # list of lines
        lines.pop(-1)  # we remove the last element as it is empty (only '\n')
        lines = [s.strip('\n ') for s in lines]  # we remove spaces and line breaks

    return lines


def readData(file_address):  # used to read data about problems
    # returns a list of 125 problems with n jobs, each one of them with its parameters
    if file_address == "data/wt40.txt":
        size = 40
    elif file_address == "data/wt50.txt":
        size = 50
    elif file_address == "data/wt100.txt":
        size = 100
    else:
        raise ValueError('File address not expected')

    with open(file_address) as f:
        lines = f.readlines()  # list of lines
        lines.pop(-1)  # we remove the last element as it is empty (only '\n')
        lines = [s.strip('\n ').split() for s in lines]  # we remove spaces and line breaks
        lines = [[int(element) for element in s] for s in lines]  # str->int for every value
        flatten_lines = sum(lines, [])  # we flatten the list to go through it more easily

        problems = dict()
        problems['processing_time'] = list()
        problems['due_date'] = list()
        problems['weight'] = list()

        n = size * 3

        for i in range(0, len(flatten_lines)-1, n):  # start,stop,step
#he cambiado due_date por weight TODO:##########################
            problems['processing_time'].append(flatten_lines[i:i + size])
            problems['weight'].append(flatten_lines[i + size:i + size*2])
            problems['due_date'].append(flatten_lines[i + size*2:i + size*3])

            #problems.append([flatten_lines[i:i + size * 3]])

    return problems



