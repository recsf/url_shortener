from __future__ import with_statement
import contextlib

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

try:
    from urllib.request import urlopen
except ImportError:
    print("Libreria no existe")


def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


print(make_tiny("https://www.digitalife.com.mx/productos/horno-microondas-panasonic-13-pies-cubicos-negro"))
