from .data_function import *
import os
##########

def update_data():
    today = datetime.now()
    if os.path.exists('file_path.txt'):
        with open('file_path.txt','r') as file:
            file_path = file.read()
    else:
        file_path = set_backtest_filepath()
        with open('file_path.txt','w') as file:
            file.write(file_path)

    cps = list_cp().Symbol.to_list()
    cpu = multiprocessing.cpu_count()
    if os.path.exists(file_path + r'\time.txt'):
        with open(file_path + r'\time.txt','r') as file:
            day = file.read()

        if today.strftime(format= '%Y-%m-%d') == day and today.hour < 15:
            print('Cập nhật dữ liệu, xin vui lòng đợi. Do phiên giao dịch chưa kết thúc nên sẽ sử dụng dữ liệu ngày hôm qua cho backtest')

            end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')

            with multiprocessing.Pool(cpu) as pool:
                results = pool.starmap(price,[(cp,'2000-01-01', end_date) for cp in cps])

        else:
            print('Đang cập nhật dữ liệu cuối phiên')
            end_date = today.strftime(format= '%Y-%m-%d')

            with multiprocessing.Pool(cpu) as pool:
                results = pool.starmap(price,[(cp,'2000-01-01', end_date) for cp in cps])

    else:
        print('Cập nhật dữ liệu lần đầu, xin vui lòng đợi')
        end_date = today
        # if __name__ == "__main__":
        with multiprocessing.Pool(cpu) as pool:
            results = pool.starmap(price,[(cp,'2000-01-01', end_date) for cp in cps])


    #Lưu dữ liệu backtest
    with open(file_path + r'\data_price.pkl', 'wb') as file:
        pickle.dump(results, file, protocol=pickle.HIGHEST_PROTOCOL)

    #Lưu dữ liệu cps
    with open(file_path + r'\cps.pkl', 'wb') as file:
        pickle.dump(cps, file, protocol=pickle.HIGHEST_PROTOCOL)

    #Lưu lại thông tin về ngày giao dịchi
    with open(file_path + r'\time.txt','w') as file:
        file.write(today.strftime(format= '%Y-%m-%d'))
    print('Đã cập nhật dữ liệu')