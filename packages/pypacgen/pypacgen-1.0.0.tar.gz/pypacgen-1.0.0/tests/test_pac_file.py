import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from pypacgen import *

from py_mini_racer import MiniRacer
from urllib.parse import urlparse

pac_function_definitions = '''
function dnsDomainIs(host, domain) {
    return (host.length >= domain.length && host.substring(host.length - domain.length) == domain);
}

function dnsDomainLevels(host) {
    return host.split('.').length-1;
}

function convert_addr(ipchars) {
    var bytes = ipchars.split('.');
    return ((bytes[0] & 0xff) << 24) | ((bytes[1] & 0xff) << 16) | ((bytes[2] & 0xff) <<  8) | (bytes[3] & 0xff);
}

function isInNet(ipaddr, pattern, maskstr) {
    var test = /^(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})$/.exec(ipaddr);
    if (test == null) {
        ipaddr = dnsResolve(ipaddr);
        if (ipaddr == null)
            return false;
    } else if (test[1] > 255 || test[2] > 255 ||
               test[3] > 255 || test[4] > 255) {
        return false;
    }
    var host = convert_addr(ipaddr);
    var pat  = convert_addr(pattern);
    var mask = convert_addr(maskstr);
    return ((host & mask) == (pat & mask));
}

function isResolvable(host) {
    var ip = dnsResolve(host);
    return (ip != null);
}

function localHostOrDomainIs(host, hostdom) {
    return (host == hostdom) ||
           (hostdom.lastIndexOf(host + '.', 0) == 0);
}

function shExpMatch(url, pattern) {
   pattern = pattern.replace(/\\./g, '\\\\.');
   pattern = pattern.replace(/\\*/g, '.*');
   pattern = pattern.replace(/\\?/g, '.');
   var newRe = new RegExp('^'+pattern+'$');
   return newRe.test(url);
}

var wdays = {SUN: 0, MON: 1, TUE: 2, WED: 3, THU: 4, FRI: 5, SAT: 6};

var months = {JAN: 0, FEB: 1, MAR: 2, APR: 3, MAY: 4, JUN: 5, JUL: 6, AUG: 7, SEP: 8, OCT: 9, NOV: 10, DEC: 11};

function weekdayRange() {
    function getDay(weekday) {
        if (weekday in wdays) {
            return wdays[weekday];
        }
        return -1;
    }
    var date = new Date();
    var argc = arguments.length;
    var wday;
    if (argc < 1)
        return false;
    if (arguments[argc - 1] == 'GMT') {
        argc--;
        wday = date.getUTCDay();
    } else {
        wday = date.getDay();
    }
    var wd1 = getDay(arguments[0]);
    var wd2 = (argc == 2) ? getDay(arguments[1]) : wd1;
    return (wd1 == -1 || wd2 == -1) ? false
                                    : (wd1 <= wday && wday <= wd2);
}

function dateRange() {
    function getMonth(name) {
        if (name in months) {
            return months[name];
        }
        return -1;
    }
    var date = new Date();
    var argc = arguments.length;
    if (argc < 1) {
        return false;
    }
    var isGMT = (arguments[argc - 1] == 'GMT');

    if (isGMT) {
        argc--;
    }
    // function will work even without explict handling of this case
    if (argc == 1) {
        var tmp = parseInt(arguments[0]);
        if (isNaN(tmp)) {
            return ((isGMT ? date.getUTCMonth() : date.getMonth()) == getMonth(arguments[0]));
        } else if (tmp < 32) {
            return ((isGMT ? date.getUTCDate() : date.getDate()) == tmp);
        } else {
            return ((isGMT ? date.getUTCFullYear() : date.getFullYear()) == tmp);
        }
    }
    var year = date.getFullYear();
    var date1, date2;
    date1 = new Date(year,  0,  1,  0,  0,  0);
    date2 = new Date(year, 11, 31, 23, 59, 59);
    var adjustMonth = false;
    for (var i = 0; i < (argc >> 1); i++) {
        var tmp = parseInt(arguments[i]);
        if (isNaN(tmp)) {
            var mon = getMonth(arguments[i]);
            date1.setMonth(mon);
        } else if (tmp < 32) {
            adjustMonth = (argc <= 2);
            date1.setDate(tmp);
        } else {
            date1.setFullYear(tmp);
        }
    }
    for (var i = (argc >> 1); i < argc; i++) {
        var tmp = parseInt(arguments[i]);
        if (isNaN(tmp)) {
            var mon = getMonth(arguments[i]);
            date2.setMonth(mon);
        } else if (tmp < 32) {
            date2.setDate(tmp);
        } else {
            date2.setFullYear(tmp);
        }
    }
    if (adjustMonth) {
        date1.setMonth(date.getMonth());
        date2.setMonth(date.getMonth());
    }
    if (isGMT) {
        var tmp = date;
        tmp.setFullYear(date.getUTCFullYear());
        tmp.setMonth(date.getUTCMonth());
        tmp.setDate(date.getUTCDate());
        tmp.setHours(date.getUTCHours());
        tmp.setMinutes(date.getUTCMinutes());
        tmp.setSeconds(date.getUTCSeconds());
        date = tmp;
    }
    return ((date1 <= date) && (date <= date2));
}

function timeRange() {
    var argc = arguments.length;
    var date = new Date();
    var isGMT= false;

    if (argc < 1) {
        return false;
    }
    if (arguments[argc - 1] == 'GMT') {
        isGMT = true;
        argc--;
    }

    var hour = isGMT ? date.getUTCHours() : date.getHours();
    var date1, date2;
    date1 = new Date();
    date2 = new Date();

    if (argc == 1) {
        return (hour == arguments[0]);
    } else if (argc == 2) {
        return ((arguments[0] <= hour) && (hour <= arguments[1]));
    } else {
        switch (argc) {
        case 6:
            date1.setSeconds(arguments[2]);
            date2.setSeconds(arguments[5]);
        case 4:
            var middle = argc >> 1;
            date1.setHours(arguments[0]);
            date1.setMinutes(arguments[1]);
            date2.setHours(arguments[middle]);
            date2.setMinutes(arguments[middle + 1]);
            if (middle == 2) {
                date2.setSeconds(59);
            }
            break;
        default:
          throw 'timeRange: bad number of arguments'
        }
    }

    if (isGMT) {
        date.setFullYear(date.getUTCFullYear());
        date.setMonth(date.getUTCMonth());
        date.setDate(date.getUTCDate());
        date.setHours(date.getUTCHours());
        date.setMinutes(date.getUTCMinutes());
        date.setSeconds(date.getUTCSeconds());
    }
    return ((date1 <= date) && (date <= date2));
}

function dnsResolve( hostname ) {
    var test = /^(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})$/.exec(hostname);
    if (test != null) {
        return hostname;
    }
    if (shExpMatch(hostname, 'www.test.com')) {
        return '52.6.51.18';
    }
    if (shExpMatch(hostname, 'sample.com')) {
        return '52.20.84.62';
    }
    return '9.1.2.3';
}   
'''


class TestPACFile(unittest.TestCase):
    def test_default_only_pac_file(self):
        f = PACFile("default_only.pac", "1.0")
        f.set_default_return(PACReturn("DIRECT"))
        v8 = MiniRacer()
        v8.eval(pac_function_definitions)
        v8.eval(f"var pac = { f.render() }")
        actual = v8.call("pac", ("FindProxyForURL", "test.com"))
        expected = "DIRECT"
        self.assertEqual(
            actual,
            expected,
            f"The test returned \"{ actual }\", it should actually return \"{ expected }\"!"
        )

    def test_dns_domain_is_pac(self):
        f = PACFile("dns_domain_is.pac", "1.0")
        f.set_default_return(PACReturn("DIRECT"))
        f.add_block(
            PACBlock(
                PACReturn("PROXY", "socks.proxy.com", 8090),
                [
                    DnsDomainIs(host="test.com"),
                    DnsDomainIs(host="org.net")
                ]
            )
        )
        v8 = MiniRacer()
        v8.eval(pac_function_definitions)
        v8.eval(f"{ f.render() }")
        # Define a dictionary of test cases.
        tests = {
            'https://www.test.com/about.php': 'PROXY socks.proxy.com:8090',
            'https://www.notmyorg.com/welcome.html': 'DIRECT',
            'https://note.nkmk.me/en/python-dict-keys-values-items/': 'DIRECT',
            'https://mail.org.com/information-architecture-devops-heroku/S': 'DIRECT',
            'http://wrench.sample.org/cherry/leg.php': 'DIRECT',
            'http://org.net/reaction?lock=lake': 'PROXY socks.proxy.com:8090',
            'https://www.sample.com/?wheel=desire&baby=society': 'DIRECT',
            'http://account.test.org/?girl=vegetable&river=spy#powe': 'DIRECT',
            'https://www.crow.sample.edu/creator/throne?point=mark#dirt': 'DIRECT',
            'http://me.org.sample.info/lace/scarecrow.html': 'DIRECT',
            'http://www.sample.com/?corn=button&land=string': 'DIRECT'
        }
        for url, outcome in tests.items():
            host = urlparse(url).netloc
            actual = v8.eval(f'FindProxyForURL("{ url }", "{ host }")')
            self.assertEqual(
                actual,
                outcome,
                f"The test returned \"{ actual }\", it should actually return \"{ outcome }\"!"
            )

    def test_sh_exp_match_host_pac(self):
        f = PACFile("sh_exp_match_host.pac", "1.0")
        f.set_default_return(PACReturn("DIRECT"))
        f.add_block(
            PACBlock(
                PACReturn("PROXY", "socks.proxy.com", 8090),
                [
                    ShExpMatchHost(host="*.test.com"),
                    ShExpMatchHost(host="*.org.*"),
                    ShExpMatchHost(host="org.*")
                ]
            )
        )
        v8 = MiniRacer()
        v8.eval(pac_function_definitions)
        v8.eval(f"{f.render()}")
        # Define a dictionary of test cases.
        tests = {
            'https://www.test.com/about.php': 'PROXY socks.proxy.com:8090',
            'https://www.notmyorg.com/welcome.html': 'DIRECT',
            'https://note.nkmk.me/en/python-dict-keys-values-items/': 'DIRECT',
            'https://mail.org.com/information-architecture-devops-heroku/S': 'PROXY socks.proxy.com:8090',
            'http://wrench.sample.org/cherry/leg.php': 'DIRECT',
            'http://org.net/reaction?lock=lake': 'PROXY socks.proxy.com:8090',
            'https://www.sample.com/?wheel=desire&baby=society': 'DIRECT',
            'http://account.test.org/?girl=vegetable&river=spy#powe': 'DIRECT',
            'https://www.crow.sample.edu/creator/throne?point=mark#dirt': 'DIRECT',
            'http://me.org.sample.info/lace/scarecrow.html': 'PROXY socks.proxy.com:8090',
            'http://www.sample.com/?corn=button&land=string': 'DIRECT'
        }
        for url, outcome in tests.items():
            host = urlparse(url).netloc
            actual = v8.eval(f'FindProxyForURL("{url}", "{host}")')
            self.assertEqual(
                actual,
                outcome,
                f"The test \"{ url }\" returned \"{actual}\", it should actually return \"{outcome}\"!"
            )

    def test_sh_exp_match_url_pac(self):
        f = PACFile("sh_exp_match_url.pac", "1.0")
        f.set_default_return(PACReturn("DIRECT"))
        f.add_block(
            PACBlock(
                PACReturn("PROXY", "socks.proxy.com", 8090),
                [
                    ShExpMatchUrl(url="*.test.com/*"),
                    ShExpMatchUrl(url="*.org.*"),
                    ShExpMatchUrl(url="org.*")
                ]
            )
        )
        v8 = MiniRacer()
        v8.eval(pac_function_definitions)
        v8.eval(f"{f.render()}")
        # Define a dictionary of test cases.
        tests = {
            'https://www.test.com/about.php': 'PROXY socks.proxy.com:8090',
            'https://www.notmyorg.com/welcome.html': 'DIRECT',
            'https://note.nkmk.me/en/python-dict-keys-values-items/': 'DIRECT',
            'https://mail.org.com/information-architecture-devops-heroku/S': 'PROXY socks.proxy.com:8090',
            'http://wrench.sample.org/cherry/leg.php': 'DIRECT',
            'http://org.net/reaction?lock=lake': 'DIRECT',
            'https://www.sample.com/?wheel=desire&baby=society': 'DIRECT',
            'http://account.test.org/?girl=vegetable&river=spy#powe': 'DIRECT',
            'https://www.crow.sample.edu/creator/throne?point=mark#dirt': 'DIRECT',
            'http://me.org.sample.info/lace/scarecrow.html': 'PROXY socks.proxy.com:8090',
            'http://www.sample.com/?corn=button&land=string': 'DIRECT'
        }
        for url, outcome in tests.items():
            host = urlparse(url).netloc
            actual = v8.eval(f'FindProxyForURL("{url}", "{host}")')
            self.assertEqual(
                actual,
                outcome,
                f"The test \"{ url }\" returned \"{ actual }\", it should actually return \"{ outcome }\"!"
            )

    def test_is_in_net_pac(self):
        f = PACFile("is_in_net.pac", "1.0")
        f.set_default_return(PACReturn("DIRECT"))
        f.add_block(
            PACBlock(
                PACReturn("PROXY", "socks.proxy.com", 8090),
                [
                    IsInNet(net='52.6.51.0', mask='255.255.255.0'),
                    IsInNet(net='52.20.84.0', mask='255.255.255.0'),
                    IsInNet(net='1.2.0.0', mask='255.255.0.0')
                ]
            )
        )
        v8 = MiniRacer()
        v8.eval(pac_function_definitions)
        v8.eval(f"{f.render()}")
        # Define a dictionary of test cases.
        tests = {
            'https://www.test.com/about.php': 'PROXY socks.proxy.com:8090',
            'https://www.notmyorg.com/welcome.html': 'DIRECT',
            'https://note.nkmk.me/en/python-dict-keys-values-items/': 'DIRECT',
            'https://mail.org.com/information-architecture-devops-heroku/S': 'DIRECT',
            'http://wrench.sample.org/cherry/leg.php': 'DIRECT',
            'http://org.net/reaction?lock=lake': 'DIRECT',
            'https://www.sample.com/?wheel=desire&baby=society': 'DIRECT',
            'http://account.test.org/?girl=vegetable&river=spy#powe': 'DIRECT',
            'https://www.crow.sample.edu/creator/throne?point=mark#dirt': 'DIRECT',
            'http://me.org.sample.info/lace/scarecrow.html': 'DIRECT',
            'http://sample.com/?corn=button&land=string': 'PROXY socks.proxy.com:8090'
        }
        for url, outcome in tests.items():
            host = urlparse(url).netloc
            actual = v8.eval(f'FindProxyForURL("{url}", "{host}")')
            self.assertEqual(
                actual,
                outcome,
                f"The test \"{ url }\" returned \"{ actual }\", it should actually return \"{ outcome }\"!"
            )

    def test_complex_pac(self):
        f = PACFile("complex.pac", "1.0")
        f.set_default_return(PACReturn("PROXY", "10.110.3.1", 8090))
        f.add_block(
            PACBlock(
                PACReturn("PROXY", "socks5.proxy.org.com", 8080),
                [
                    DnsDomainIs(host='sample.com'),
                    ShExpMatchHost(host='*.google.com'),
                    ShExpMatchHost(host='google.com')
                ]
            )
        )
        f.add_block(
            PACBlock(
                PACReturn("DIRECT"),
                [
                    IsInNet(net='10.0.0.0', mask='255.0.0.0'),
                    IsInNet(net='192.168.0.0', mask='255.255.0.0'),
                    IsInNet(net='172.16.0.0', mask='255.240.0.0'),
                ]
            )
        )
        v8 = MiniRacer()
        v8.eval(pac_function_definitions)
        v8.eval(f"{f.render()}")
        # Define a dictionary of test cases.
        tests = {
            'https://192.168.1.1/setup.php': 'DIRECT',
            'https://www.notmyorg.com/welcome.html': 'PROXY 10.110.3.1:8090',
            'https://note.nkmk.me/en/python-dict-keys-values-items/': 'PROXY 10.110.3.1:8090',
            'https://mail.org.com/information-architecture-devops-heroku/S': 'PROXY 10.110.3.1:8090',
            'http://wrench.sample.org/cherry/leg.php': 'PROXY 10.110.3.1:8090',
            'http://org.net/reaction?lock=lake': 'PROXY 10.110.3.1:8090',
            'https://www.sample.com/?wheel=desire&baby=society': 'PROXY socks5.proxy.org.com:8080',
            'http://account.test.org/?girl=vegetable&river=spy#powe': 'PROXY 10.110.3.1:8090',
            'https://www.crow.sample.edu/creator/throne?point=mark#dirt': 'PROXY 10.110.3.1:8090',
            'http://me.org.sample.info/lace/scarecrow.html': 'PROXY 10.110.3.1:8090',
            'http://sample.com/?corn=button&land=string': 'PROXY socks5.proxy.org.com:8080'
        }
        for url, outcome in tests.items():
            host = urlparse(url).netloc
            actual = v8.eval(f'FindProxyForURL("{url}", "{host}")')
            self.assertEqual(
                actual,
                outcome,
                f"The test \"{ url }\" returned \"{ actual }\", it should actually return \"{ outcome }\"!"
            )


if __name__ == '__main__':
    unittest.main(verbosity=3)
