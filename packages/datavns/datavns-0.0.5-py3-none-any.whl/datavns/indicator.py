from .data_function import *



class data_for_backtest:
    @classmethod
    def take(cls) -> list:
        try:
            with open('file_path.txt', 'r') as file:
                file_path = file.read()
            with open(file_path + r'\data_price.pkl', 'rb') as file:
                df_raw = pickle.load(file)

            with open(file_path + r'\cps.pkl', 'rb') as file:
                cls.cps = pickle.load(file)

            cls.data = df_raw
            print("Dữ liệu phục vụ backtest được lưu tại dict: .data")
        except:
            print('Chưa có dữ liệu phục vụ backtest. Vui lòng cập nhật dữ liệu')


def element(el ='priceClose',stocks = None) -> pd.DataFrame:
    '''
    In ra ma trận về thông tin giao dịch của các cổ phiếu niêm yết trên sàn chứng khoán tại Việt Nam
    -----

        Parameter:
        -----
        `el (str)`: Khoản mục trong dữ liệu liên quan đến thông tin giao dịch cần lầy
        `stocks (list)`: Danh sách cổ phiếu chỉ định
            stocks = None: Lấy thông tin dựa trên toàn bộ cổ phiếu
            stocks = list: Lấy thông tin bao gồm cổ phiếu được chỉ định trong list

        Return:
        -----
        pd.Dataframe chứa thông tin về cổ phiếu bao gồm:
        Danh sách mã chứng khoán tương ứng là columns của DataFrame
        Danh sách ngày được ghi nhận tương ứng là index của DataFrame
        
        Lưu ý:
        ------
        Nếu dữ liệu chưa được cập nhật sẽ không lấy được data, vui lòng cập nhật dữ liệu
    '''
    try:
        data = [x[el].rename(y) for x,y in zip(data_for_backtest.data,data_for_backtest.cps)]
        df = pd.DataFrame(data).transpose().sort_index(ascending=True).fillna(0)
        if stocks == None:
            return df
        else:
            return df.loc[:,stocks]
    except:
        print('Vui lòng cập nhật data phục vụ backtest')



class indicatior:
    def Moving_Average(method = 'priceClose', period = 20) -> pd.DataFrame:

        return element(method).rolling(window=period).mean()
    
    def Relative_Streng_Index(method, period )-> pd.DataFrame:
        return