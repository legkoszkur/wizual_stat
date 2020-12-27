def data_preparation(input_var):
    result = input_var.split(" ")
    result = [x for x in result if x]
    result[-1] = result[-1].strip()
    if result[-1] == '':
        result = result[:-1]
    return result
