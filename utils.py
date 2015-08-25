# -*- coding: utf-8 -

import logging
import httplib, ssl, socket

import config as c

logging.basicConfig(filename=c.PATH_LOG, level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] %(message)s')


class Object(object):
    pass


def api_request(action, xml, request_id=None):
    con = None
    result = None

    try:
        xml = u'<?xml version="1.0" encoding="UTF-8"?>%s' % (xml)
        logging.info('[candy sdk] request xml: %s' % xml)

        con = httplib.HTTPSConnection(c.CANDY_API_HOST, c.CANDY_API_PORT, key_file=c.CANDY_API_KEYFILE, cert_file=c.CANDY_API_CERTFILE)
        sock = socket.create_connection((con.host, con.port), con.timeout, con.source_address)

        con.sock = ssl.wrap_socket(sock, con.key_file, con.cert_file, ssl_version=ssl.PROTOCOL_TLSv1)

        headers = {
            'Content-type': 'application/xml;',
            'Username': c.CANDY_API_USERNAME,
            'Password' : c.CANDY_API_PASSWORD
        }

        if request_id:
            headers['x-request-id'] = request_id

        con.request('POST', '/mxstgw/loyalty/%s' % action, xml, headers)
        response = con.getresponse()

        result = Object()

        result.status = response.status
        result.headers = response.getheaders()
        result.error = response.getheader('x-error-code', None)
        result.id = response.getheader('x-request-id', None)
        result.body = response.read()

        result.has_error = result.status != 200 or result.error or not result.id

        result.is_not_found = result.error == '7'
        result.is_invalid_tan = result.error == '6'

        logging.info(u'[candy sdk] response status: %s' % result.status)
        logging.info(u'[candy sdk] response headers: %s' % result.headers)
        logging.info(u'[candy sdk] response body: %s' % result.body)
    except Exception as ex:
        logging.error('[candy sdk] error: %s' % ex)
        return None
    finally:
        if con:
            con.close()

    return result
