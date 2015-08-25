#!/usr/bin/env python
# -*- coding: utf-8 -

from utils import logging
from api import get_balance, sell, sell_confirm

TEST_ISDN = '99xxxxxx'
TEST_BRANCH = 'BRANCH1'


def test_balance():
    result = get_balance(TEST_ISDN)

    if result is None or result.has_error or result.balance is None:
        if result.is_not_found:
            logging.info(u'Хүсэлт амжилтгүй боллоо, таны CANDY данс идэвхгүй байна.')
        else:
            logging.info(u'Хүсэлт амжилтгүй боллоо.')

    else:
        logging.info(u'Таны CANDY үлдэгдэл %s байна.' % result.balance)


def test_sell(amount):
    result = sell(TEST_BRANCH, TEST_ISDN, amount)

    if result is None or result.has_error:
        logging.info(u'Хүсэлт амжилтгүй боллоо.')
    else:
        logging.info(u'TAN код илгээгдсэн.')


def test_sell_confirm(tancode):
    result = sell_confirm(TEST_BRANCH, TEST_ISDN, tancode)

    if result is None or result.has_error or not result.trans_id:
        if result.is_invalid_tan:
            logging.info('Гүйлгээ амжилтгүй боллоо, таны TAN код буруу байна.')
        else:
            logging.info(u'Гүйлгээ амжилтгүй боллоо.')

    else:
        logging.info(u'Гүйлгээ амжилттай хийгдлээ, гүйлгээний дугаар %s.' % result.trans_id)


def main():
    test_balance()
    test_sell(100)
    test_sell_confirm('TAN CODE')


if __name__ == '__main__':
    main()
