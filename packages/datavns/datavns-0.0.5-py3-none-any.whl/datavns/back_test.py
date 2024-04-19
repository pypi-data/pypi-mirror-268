from .data_function import *
from .optimize import *
from .indicator import *
##########

class back_test: 
    @classmethod
    def buy_conditions(cls, conds = None) -> pd.DataFrame:
        matrix = 1
        for i in conds:
            i = i.replace(' and ', '*').replace(' or ', '+')
            matrix *= eval(i)
        cls.buy_matrix  = matrix
    
    @classmethod
    def sub_conditions(cls,els = [['totalValue',False,50]]) -> pd.DataFrame:
        sub_matrix = 1
        try:
            for el in els:
                df = element(el[0])
                sub_matrix *= df
        except:
            pass
        cls.total = (sub_matrix * cls.buy_matrix).apply(lambda x: sub_conditions_optimize(row=x,nums=el[2]),axis = 1, result_type='expand')

    @classmethod
    def sell_conditions(cls, conds = None) -> pd.DataFrame:
        matrix = 1
        for i in conds:
            i = i.replace(' and ', '*').replace(' or ', '+')
            matrix *= eval(i)
        cls.sell_matrix = matrix
        cls.order_matrix = cls.total.mask(cls.sell_matrix == 1,-1).apply(order_matrix_optimize,axis = 0)


    