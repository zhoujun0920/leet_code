def zigzag_conversion(s, numRows):
    turn_num = 2 * numRows - 2
    temp = ''
    converted_str_dict = {}
    column = 0
    column_count = 0
    batch_count = 0
    for n, ltr in enumerate(s):
        if column_count < numRows:
            row = (n - batch_count * turn_num) % numRows
            column_count = column_count + 1
            converted_str_dict[(row, column)] = ltr
            if column_count >= turn_num:
                column_count = 0
                column = column + 1
                batch_count = batch_count + 1
        else:
            row = numRows - (n - batch_count * turn_num) % numRows - 2
            column = column + 1
            column_count = column_count + 1
            converted_str_dict[(row, column)] = ltr
            if column_count >= turn_num:
                column_count = 0
                column = column + 1
                batch_count = batch_count + 1
    for k in (sorted(converted_str_dict.keys(), key=lambda tup: (tup[0], tup[1]))):
        temp = temp + converted_str_dict[k]
    return temp

e1 = 'PAYPALISHIRING'  #PAHNAPLSIIGYIR
e2 = 'ABCDEFGHIJKLMNOP' #
e3 = 'AB'
print(zigzag_conversion(e1, 3))
print(zigzag_conversion(e2, 4))
print(zigzag_conversion(e3, 1))