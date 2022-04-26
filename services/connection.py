import imp
import sys
import http.client as httplib

#check internet connection
def internet_conn(url='www.google.com', timeout=3):
    conn = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn.request('HEAD', '/')
        conn.close()
        return True
    except Exception as e:
        return False

sys.modules[__name__] = internet_conn