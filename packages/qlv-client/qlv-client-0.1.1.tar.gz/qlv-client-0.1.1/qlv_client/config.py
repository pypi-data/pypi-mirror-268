# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  qlvClient
# FileName:     config.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/17
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""

qvl_map = {
    "user_id": 186,
    "user_key": "9a68295ec90b1fc10ab94331c882bab9",
    "domain": "outsideapi.qlv88.com",
    "protocol": "http",
    "interfaces": {
        "lock_order": {
            "path": "/LockOrder.ashx",
            "method": "post"
        },
        "unlock_order": {
            "path": "/OrderUnlock.ashx",
            "method": "post"
        },
        "write_order_log_new": {
            "path": "/OrderLogWriteNew.ashx",
            "method": "post"},
        "save_order_pay_info": {
            "path": "/OrderPayInfoSave.ashx",
            "method": "post"},
        "fill_order_itinerary_info": {
            "path": "/BackfillTicketNumberNew.ashx",
            "method": "post"
        }
    }
}
