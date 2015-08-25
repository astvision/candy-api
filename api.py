# -*- coding: utf-8 -

import xml.etree.ElementTree as xml_et

from utils import api_request, logging


def get_balance(isdn):
    result = None

    try:
        xml = '<request><customer>%(isdn)s</customer><customer.system>ISDN</customer.system></request>' % {
            'isdn': isdn,
        }

        result = api_request('customer', xml)

        if result and not result.has_error:
            result.balance = None
            root = xml_et.fromstring(result.body)
            result.balance =  int(float(root.find('balance').text))
    except Exception as ex:
        logging.error('[candy api] [get balance] error: %s' % ex)

    return result


def sell(branch, isdn, amount):
    result = None

    try:
        xml = '<request><branch>%(branch)s</branch><customer system="ISDN">%(isdn)s</customer><point>%(point)s</point><smsPrefix>my.ubedn.mn</smsPrefix><smsSuffix>UBEDN</smsSuffix><product>tsaxilgaanii tulbur</product><productType></productType><description>tsaxilgaanii tulbur tulugdsun.</description></request>' % {
            'branch': branch,
            'isdn': isdn,
            'point': amount,
        }

        result = api_request('sell', xml)
    except Exception as ex:
        logging.error('[candy api] [sell] error: %s' % ex)

    return result


def sell_confirm(branch, isdn, tan):
    result = None

    try:
        xml = '<request><branch>%(branch)s</branch><customer system="ISDN">%(isdn)s</customer><tancode>%(tan)s</tancode></request>' % {
            'branch': branch,
            'isdn': isdn,
            'tan': tan,
        }

        result = api_request('sell/confirm', xml)

        if result and not result.has_error:
            result.trans_id = None
            root = xml_et.fromstring(result.body)
            result.trans_id =  root.find('transactionId').text
    except Exception as ex:
        logging.error('[candy api] [sell confirm] error: %s' % ex)

    return result
