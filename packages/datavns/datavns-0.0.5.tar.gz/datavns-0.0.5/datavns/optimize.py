


def order_matrix_optimize(columns):
    '''
    Function dùng optimize cho order matrix
    '''
    result = []
    order = 0
    gap = 2
    for value in columns:
        gap += 1
        if gap > 2:
            if order == 0 and value == 1:
                result.append(value)
                order = 1
                gap = 0
            elif order == 1 and value == -1 :
                result.append(value)
                order = 0
                gap = 0
            else:
                result.append(0)
        else:
            result.append(0)
            
    return result


def sub_conditions_optimize(row,nums = 5):
    '''
    Function dùng để optimize điều kiện phụ cho danh mục đầu tư
    '''
    result = row.rank(ascending=False,method='max',na_option='bottom')
    result = result.apply(lambda x: 1 if x < nums + 1 else 0)
    return result