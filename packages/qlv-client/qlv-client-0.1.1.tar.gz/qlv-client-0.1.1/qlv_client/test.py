# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  qlvClient
# FileName:     test.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/17
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from qlv_client.proxy import QlvService


def test_lock_order():
    xc = {
        "policy_name": "XCAPP出票",
        "oper": "robot-XCAPP",
        "air_cos": "",
        "order_pk": "",
        "order_src_cat": "国内"
    }
    QlvService.get_lock_order(xc)


def test_unlock_order():
    QlvService.set_unlock_order(
        order_id=1234567890, oper="robot-XC", order_state="0", order_lose_type="政策", remark="价格不符"
    )


def test_save_pay_info():
    kwargs = {
        "pre_order_id": 1232132131231231,
        "payment_time": "2024-04-10 19:46:00",
        "out_pf": "XCAPP",
        "out_ticket_account": "K王总信用卡",
        "pay_account_type": "K王总信用卡",
        "pay_account": "浦发7397",
        "payment_amount": 1000,
        "ctrip_order_id": "2342342342342342",
        "passenger": "徐婷婷,顾欣桐",
        "oper": "robot-XC",
        "ctrip_username": "18600440822",
        "user_pass": "ca161022",
    }
    QlvService.save_pay_info(**kwargs)


def test_fill_order_itinerary_info():
    kwargs = {
        "pre_order_id": 1232132131231231,
        "oper": "robot-XC",
        "card_id": "12312312312",
        "passenger": "牛婷婷",
        "arrive_city": "CSH",
        "itinerary_id": "831-111212121",
        "departure_city": "SZG"
    }
    QlvService.save_itinerary_info(**kwargs)


if __name__ == "__main__":
    import logging
    from qlv_client.utils import logger

    logger.setLevel(level=logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    logger.info("开始打印....")
    test_lock_order()
    test_unlock_order()
    test_save_pay_info()
    test_fill_order_itinerary_info()
    # test_fill_order_itinerary_info()
