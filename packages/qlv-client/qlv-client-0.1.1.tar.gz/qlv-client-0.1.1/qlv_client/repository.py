# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  qlvClient
# FileName:     repository.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/17
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from qlv_client.config import qvl_map


class QlvConfigRepository(object):

    @classmethod
    def get_request_base_params(cls, inter_name: str) -> dict:
        return {
            "path": qvl_map.get("interfaces").get(inter_name).get("path"),
            "method": qvl_map.get("interfaces").get(inter_name).get("method"),
            "user_key": qvl_map.get("user_key"),
            "user_id": qvl_map.get("user_id")
        }

    @classmethod
    def get_host_params(cls) -> dict:
        return dict(domain=qvl_map.get("domain"), protocol=qvl_map.get("protocol"))

    @classmethod
    def get_unlock_order_params(cls, **kwargs) -> dict:
        return {
            "order_id": kwargs.get("order_id"),
            "oper": kwargs.get("oper"),
            "order_state": kwargs.get("order_state"),
            "order_lose_type": kwargs.get("order_lose_type"),
            "remark": kwargs.get("remark")
        }

    @classmethod
    def get_unlock_reason_params(cls, flag: bool, order_id: int, oper: str, remark: str) -> dict:
        """flag 为 true时，出票成功，反之出票失败"""
        return dict(
            order_id=order_id,
            oper=oper,
            order_state="1" if flag is True else "0",
            order_lose_type="解锁订单",
            remark=remark
        )

    @classmethod
    def get_order_pay_info(cls, **kwargs) -> dict:
        return {
            "order_id": kwargs.get("pre_order_id"),
            "payment_time": kwargs.get("payment_time"),
            "out_pf": kwargs.get("out_pf"),
            "out_ticket_account": kwargs.get("out_ticket_account"),
            "pay_account_type": kwargs.get("pay_account_type"),
            "pay_account": kwargs.get("pay_account"),
            "money": kwargs.get("payment_amount"),
            "serial_number": kwargs.get("ctrip_order_id"),
            "air_co_order_id": kwargs.get("ctrip_order_id"),
            "pnames": kwargs.get("passenger"),
            "oper": kwargs.get("oper"),
            "remark": "{}-{}".format(kwargs.get("ctrip_username"), kwargs.get("user_pass")),
            "d_type": 1
        }

    @classmethod
    def get_order_itinerary_info(cls, **kwargs) -> dict:
        card_id = kwargs.get("card_id")
        passenger = kwargs.get("passenger")
        arrive_city = kwargs.get("arrive_city")
        itinerary_id = kwargs.get("itinerary_id")
        departure_city = kwargs.get("departure_city")
        return {
            "order_id": kwargs.get("pre_order_id"),
            "oper": kwargs.get("oper"),
            "ticket_infos": "#".join([passenger, card_id, itinerary_id, departure_city, arrive_city])
        }
