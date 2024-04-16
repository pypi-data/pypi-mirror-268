from pyqqq.utils.logger import get_logger
import datetime as dtm
import pandas as pd
import pyqqq
import pyqqq.config as c
import pytz
import requests

logger = get_logger("realtime")


def get_all_last_trades():
    """
    모든 종목의 최근 체결 정보를 반환합니다.

    Returns:
        list:
        - dict:
            - chetime (str): 체결시간
            - sign (str): 전일대비구분
            - change (int): 전일대비가격
            - drate (float): 전일대비등락율
            - price (int): 체결가
            - opentime (str): 시가시간
            - open (int): 시가
            - hightime (str): 고가시간
            - high (int): 고가
            - lowtime (str): 저가시간
            - low (int): 저가
            - cgubun (str): 체결구분
            - cvolume (int): 체결량
            - value (int): 누적거래대금
            - mdvolume (int): 매도체결수량
            - mdchecnt (int): 매도체결건수
            - msvolume (int): 매수체결수량
            - mschecnt (int): 매수체결건수
            - cpower (float): 체결강도
            - offerho (int): 매도호가
            - bidho (int): 매수호가
            - status (str): 장정보
            - jnilvolume (int): 전일거래량
            - shcode (str): 종목코드

    """

    r = requests.get(f"{c.PYQQQ_API_URL}/domestic-stock/trades")
    r.raise_for_status()

    data = r.json()
    result = [data[k] for k in data.keys()]

    return result


