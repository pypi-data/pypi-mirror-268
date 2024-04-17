# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  qlvClient
# FileName:     converter.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/17
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from decimal import Decimal
from utils import iso_to_standard_datestr


class QlvRequestParamsConverter(object):

    @classmethod
    def covert_flight_info(cls, order_id: int, flights: dict) -> dict:
        flight_info = dict(
            pre_order_id=order_id,
            departure_time=iso_to_standard_datestr(datestr=flights.get("DatDep"), time_zone_step=8),
            departure_city=flights.get("CodeDep"),
            departure_city_name=flights.get("CityDep"),
            arrive_time=iso_to_standard_datestr(datestr=flights.get("DatArr"), time_zone_step=8),
            arrive_city=flights.get("CodeArr"),
            arrive_city_name=flights.get("CityArr"),
            flight=flights.get("FlightNo"),
            pre_sale_amount=str(Decimal(flights.get("PriceStd")))
        )
        return flight_info
