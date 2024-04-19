from .lib import *
from .headers import *
##########

def set_backtest_filepath(path = r'D:\Python\datavns\Data') -> str:
    '''
    Chỉ định đường dẫn đến thư mục lưu dữ liệu phục vụ backtest
    -----

        Parameter:
        -----
        `path (str)`: đường dẫn đến thư mục lưu dữ liệu phục vụ backtest

    '''
    path = input('Nhập vào đường dẫn đến thư mục lưu dữ liệu phục vụ backtest:')
    if path == '':
        return r'D:\Python\datavns\Data'
    else:
        return path
    
def list_cp(exchange = 'HSX') -> pd.DataFrame:
    '''
    In ra danh sách cổ phiếu của các sàn giao dịch tại Việt Nam
    -----

        Parameter:
        -----
        `exchange (str)`: Tên của sàn giao dịch

        Return:
        -----
        pd.Dataframe chứa thông tin về cổ phiếu bao gồm:
            Mã giao dịch: Symbol
            Sàn niêm yết: TradeCenterId
            Tên công ty: CompanyName
            Ngành nghề của doanh nghiệp: CategoryName
    '''
    if exchange == 'HOSE' or exchange == 'HSX':
        ex = 1
    elif exchange == 'HNX':
        ex = 2
    elif exchange == 'UpCOM':
        ex = 8
    else:
        ex = 0
    url = 'https://s.cafef.vn/ajax/pagenew/databusiness/congtyniemyet.ashx?centerid={}&skip=0&take=10000&major=0'.format(ex)
    df_raw = rq.get(url,headers=cafef_header).json()['Data']
    df = pd.DataFrame(df_raw)
    df = df[df['Symbol'].apply(lambda x: len(x) == 3)]
    df['TradeCenterId'].replace({1: 'HOSE', 2: 'HNX', 9: 'UpCOM',8: 'OTC'}, inplace=True)
    df = df[['Symbol','TradeCenterId','CompanyName','CategoryName']]
    df.dropna(axis=0,inplace=True)
    df.reset_index(drop=True,inplace=True)
    return df

def bctc(cp,type = 1,year = 2023,quarter = 0) -> pd.DataFrame:
    '''
    In ra dữ liệu về báo cáo tài chính của các doanh nghiệp niêm yết tại Việt Nam
    -----

        Parameter:
        -----
        `cp (str)`: Mã cổ phiếu niêm yết
        `type (int)`: Loại báo cáo trong báo cáo tài chính cần lấy
            type = 1: Bảng cân đối kế toán
            type = 2: Báo cáo kết quả hoạt động kinh doanh
            type = 3: Báo cáo lưu chuyển tiền tệ trực tiếp (Đa số các doanh nghiệp bị trống dữ liệu về báo cáo lưu chuyển tiền tệ trực tiếp, trừ nhóm ngành ngân hàng)
            type = 4: Báo cáo lưu chuyển tiền tệ gián tiếp
        `year (int)`: Năm cuối cùng trong danh sách báo cáo tài chính cần lấy
        `quarter (int)`: Quý của báo cáo tài chính cần lấy
            quarter = 0: Sẽ lấy báo cáo tài chính theo năm của doanh nghiệp
            quarter = 1-4: Sẽ lấy báo cáo tài chính theo quý của năm tương ứng với parameter `year`

        Return:
        -----
        pd.Dataframe chứa thông tin về cổ phiếu bao gồm:
            Các khoản mục của báo cáo tương ứng là columns của DataFrame
                Eg: Để xem các khoản mục có thể thực hiện
                    `bctc('HPG',type=1).columns`
            Năm báo cáo tương ứng là index của DataFrame
    '''
    url_raw = 'https://restv2.fireant.vn/symbols/{}/full-financial-reports?type={}&year={}&quarter={}&limit=999999'.format(cp,type,year,quarter)
    df_raw = rq.get(url_raw,headers=fireant_header).json()
    indexs = [x['name'] for x in df_raw]
    year = [x['year'] for x in df_raw[0]['values']]
    quarter = [x['quarter'] for x in df_raw[0]['values']]
    if quarter != 0:
        col = [str(x) + '-' + str(y) for x, y in zip(year, quarter)]
    ###
    else:
        col = year
    ###
    df = [[z['value']for z in y] for y in [x['values'] for x in df_raw]]
    df = pd.DataFrame(df,index = indexs, columns=col)
    df.loc['Symbol'] = cp
    df = df.fillna(value=0)
    df = df.transpose()
    return df

def price(cp,start_date = '2010-01-01',end_date = '2024-09-20') -> pd.DataFrame:
    '''
    In ra dữ liệu về thông tin giao dịch của các cổ phiếu niêm yết trên sàn chứng khoán tại Việt Nam
    -----

        Parameter:
        -----
            `cp (str)`: Mã cổ phiếu niêm yết
            `start_date (str)`: Ngày bắt đầu trong khoảng thời gian cần lấy thông tin giao dịch
            `end_date (str)`: Ngày kết thúc trong khoảng thời gian cần lấy thông tin giao dịch

        Return:
        -----
        pd.Dataframe chứa thông tin về cổ phiếu bao gồm:
            Các khoản mục của thông tin giao dịch tương ứng là columns của DataFrame
                Eg: Để xem các khoản mục có thể thực hiện
                    `price('HPG').columns`
            Ngày ghi nhận là index của DataFrame
    '''
    url = 'https://restv2.fireant.vn/symbols/{}/historical-quotes?startDate={}&endDate={}&offset=0&limit=999999'.format(cp,start_date,end_date)
    df_raw = rq.get(url,headers=fireant_header).json()
    date_raw = pd.to_datetime([x['date'] for x in df_raw]).strftime(date_format='%Y-%m-%d')
    df = pd.DataFrame(df_raw)
    df.index = date_raw
    df['date'] = date_raw
    df = df.sort_index(ascending=True)
    df['priceOpen'] = df.priceOpen / df.adjRatio
    df['priceClose'] = df.priceClose / df.adjRatio
    df['priceHigh'] = df.priceHigh / df.adjRatio
    df['priceLow'] = df.priceLow / df.adjRatio
    df['priceAverage'] = df.priceAverage / df.adjRatio
    return df

def infor(cp) -> dict:
    '''
    In ra dữ liệu về thông tin của các cổ phiếu niêm yết trên sàn chứng khoán tại Việt Nam
    -----

        Parameter:
        -----
        `cp (str)`: Mã cổ phiếu niêm yết

        Return:
        -----
        pd.Dataframe chứa thông tin về cổ phiếu bao gồm:
            Các khoản mục của thông tin tương ứng là columns của DataFrame
                Eg: Để xem các khoản mục có thể thực hiện
                    `infor('HPG').columns`
    '''
    url = 'https://restv2.fireant.vn/symbols/{}/fundamental'.format(cp)
    df_raw = rq.get(url,headers=fireant_header).json()
    return pd.DataFrame(df_raw,index=[0])

def dividends_historical(cp = 'VCB', num = 50) -> pd.DataFrame:
    '''
    In ra dữ liệu về chi trả cổ tức của các doanh nghiệp
    -----

        Parameter:
        -----
        `cp (str)`: Mã cổ phiếu niêm yết
        `num (int)`: Số năm lấy dữ liệu chi trả cổ tức, tính ngược từ thời điểm hiện tại

        Return:
        -----
        pd.Dataframe chứa thông tin về cổ phiếu bao gồm:
            Năm thực hiện: year
            Cổ tức tiền mặt: cashDividend
            Cổ tức cổ phiếu: stockDividend
            Tổng tài sản doanh nghiệp tại thời điểm chi trả: totalAssets
            Tổng vốn chủ sở hữu tại thời điểm chi trả: stockHolderEquity
    '''
    url = 'https://restv2.fireant.vn/symbols/{}/dividends?count={}'.format(cp,num)
    df_raw = rq.get(url=url,headers=fireant_header).json()
    return pd.DataFrame(df_raw).fillna(0)