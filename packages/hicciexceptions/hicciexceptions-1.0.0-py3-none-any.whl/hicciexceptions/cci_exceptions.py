
class EX_ATTDBG(Exception):
    pass

class HORCM_START(Exception):
    pass

class EW_ENESCR(Exception):
    pass

class EW_ENFILE(Exception):
    pass

class EW_INVOPA(Exception):
    pass

class EW_INVOPT(Exception):
    pass

class EW_LNGARG(Exception):
    pass

class EW_MAXARG(Exception):
    pass

class EW_REQCMD(Exception):
    pass

class EX_CTXCHK(Exception):
    pass

class EX_EACCES(Exception):
    pass

class EX_ENAUTH(Exception):
    pass

class EX_EPPERM(Exception):
    pass

class EX_ENQCLP(Exception):
    pass

class EX_ENOOBJ(Exception):
    pass

class EX_ENOPOL(Exception):
    pass

class EX_ESPERM(Exception):
    pass

class EX_EPRORT(Exception):
    pass

class EX_ESVOLD(Exception):
    pass

class EX_ENOSUP(Exception):
    pass

class EX_ERPERM(Exception):
    pass

class EX_ENQSIZ(Exception):
    pass

class EX_ENPERM(Exception):
    pass

class EX_ENQCTG(Exception):
    pass

class EX_ENXCTG(Exception):
    pass

class EX_EXTCTG(Exception):
    pass

class EX_ENOCTG(Exception):
    pass

class EX_ENQSER(Exception):
    pass

class EX_ENOUNT(Exception):
    pass

class EX_INVMUN(Exception):
    pass

class EX_CMDRJE(Exception):
    pass

class EX_INVVOL(Exception):
    pass

class EX_VOLCRE(Exception):
    pass

class EX_VOLCUE(Exception):
    pass

class EX_VOLCUR(Exception):
    pass

class EX_INVRCD(Exception):
    pass

class EX_ENLDEV(Exception):
    pass

class EX_INVSTP(Exception):
    pass

class EX_INCSTG(Exception):
    pass

class EX_UNWCMD(Exception):
    pass

class EX_ESTMON(Exception):
    pass

class EX_EWSLTO(Exception):
    pass

class EX_EWSTOT(Exception):
    pass

class EX_EWSUSE(Exception):
    pass

class EX_EVOLCE(Exception):
    pass

class EX_ENQVOL(Exception):
    pass

class EX_CMDIOE(Exception):
    pass

class EX_CMDIOE(Exception):
    pass

class EX_UNWCOD(Exception):
    pass

class EX_ENOGRP(Exception):
    pass

class EX_INVCMD(Exception):
    pass

class EX_INVMOD(Exception):
    pass

class EX_ENORMT(Exception):
    pass

class EX_ENAMLG(Exception):
    pass

class EX_ERANGE(Exception):
    pass

class EX_ENOMEM(Exception):
    pass

class EX_ENODEV(Exception):
    pass

class EX_ENOENT(Exception):
    pass

class EX_OPTINV(Exception):
    pass

class EX_INVNAM(Exception):
    pass

class EX_ATTDBG(Exception):
    pass

class EX_ATTHOR(Exception):
    pass

class EX_UNWOPT(Exception):
    pass

class EW_UNWOPT(Exception):
    pass

class EW_INVARG(Exception):
    pass

class EX_INVARG(Exception):
    pass

class EX_REQARG(Exception):
    pass

class EX_COMERR(Exception):
    pass

cci_exceptions_table_by_code = {
    # There are 7 131's ?
    250: EX_ATTDBG,
    251: EX_ATTHOR
}

cci_exceptions_table = {
    'EW_ENESCR': { 'return_value': 131, 'Exception': EW_ENESCR },
    'EW_ENFILE': { 'return_value': 131, 'Exception': EW_ENFILE },
    'EW_INVOPA': { 'return_value': 131, 'Exception': EW_INVOPA },
    'EW_INVOPT': { 'return_value': 131, 'Exception': EW_INVOPT },
    'EW_LNGARG': { 'return_value': 131, 'Exception': EW_LNGARG },
    'EW_MAXARG': { 'return_value': 131, 'Exception': EW_MAXARG },
    'EW_REQCMD': { 'return_value': 131, 'Exception': EW_REQCMD },
    'EX_CTXCHK': { 'return_value': 199, 'Exception': EX_CTXCHK },
    'EX_EACCES': { 'return_value': 200, 'Exception': EX_EACCES },
    'EX_ENAUTH': { 'return_value': 202, 'Exception': EX_ENAUTH },
    'EX_EPPERM': { 'return_value': 203, 'Exception': EX_EPPERM },
    'EX_ENQCLP': { 'return_value': 204, 'Exception': EX_ENQCLP },
    'EX_ENOOBJ': { 'return_value': 205, 'Exception': EX_ENOOBJ },
    'EX_ENOPOL': { 'return_value': 206, 'Exception': EX_ENOPOL },
    'EX_ESPERM': { 'return_value': 207, 'Exception': EX_ESPERM },
    'EX_EPRORT': { 'return_value': 208, 'Exception': EX_EPRORT },
    'EX_ESVOLD': { 'return_value': 209, 'Exception': EX_ESVOLD },
    'EX_ENOSUP': { 'return_value': 210, 'Exception': EX_ENOSUP },
    'EX_ERPERM': { 'return_value': 211, 'Exception': EX_ERPERM },
    'EX_ENQSIZ': { 'return_value': 212, 'Exception': EX_ENQSIZ },
    'EX_ENPERM': { 'return_value': 213, 'Exception': EX_ENPERM },
    'EX_ENQCTG': { 'return_value': 214, 'Exception': EX_ENQCTG },
    'EX_ENXCTG': { 'return_value': 215, 'Exception': EX_ENXCTG },
    'EX_EXTCTG': { 'return_value': 216, 'Exception': EX_EXTCTG },
    'EX_ENOCTG': { 'return_value': 217, 'Exception': EX_ENOCTG },
    'EX_ENQSER': { 'return_value': 218, 'Exception': EX_ENQSER },
    'EX_ENOUNT': { 'return_value': 219, 'Exception': EX_ENOUNT },
    'EX_INVMUN': { 'return_value': 220, 'Exception': EX_INVMUN },
    'EX_CMDRJE': { 'return_value': 221, 'Exception': EX_CMDRJE },
    'EX_INVVOL': { 'return_value': 222, 'Exception': EX_INVVOL },
    'EX_VOLCRE': { 'return_value': 223, 'Exception': EX_VOLCRE },
    'EX_VOLCUE': { 'return_value': 224, 'Exception': EX_VOLCUE },
    'EX_VOLCUR': { 'return_value': 225, 'Exception': EX_VOLCUR },
    'EX_INVRCD': { 'return_value': 226, 'Exception': EX_INVRCD },
    'EX_ENLDEV': { 'return_value': 227, 'Exception': EX_ENLDEV },
    'EX_INVSTP': { 'return_value': 228, 'Exception': EX_INVSTP },
    'EX_INCSTG': { 'return_value': 229, 'Exception': EX_INCSTG },
    'EX_UNWCMD': { 'return_value': 230, 'Exception': EX_UNWCMD },
    'EX_ESTMON': { 'return_value': 231, 'Exception': EX_ESTMON },
    'EX_EWSLTO': { 'return_value': 232, 'Exception': EX_EWSLTO },
    'EX_EWSTOT': { 'return_value': 233, 'Exception': EX_EWSTOT },
    'EX_EWSUSE': { 'return_value': 234, 'Exception': EX_EWSUSE },
    'EX_EVOLCE': { 'return_value': 235, 'Exception': EX_EVOLCE },
    'EX_ENQVOL': { 'return_value': 236, 'Exception': EX_ENQVOL },
    'EX_CMDIOE': { 'return_value': 237, 'Exception': EX_CMDIOE },
    'EX_CMDIOE': { 'return_value': 237, 'Exception': EX_CMDIOE },
    'EX_UNWCOD': { 'return_value': 238, 'Exception': EX_UNWCOD },
    'EX_ENOGRP': { 'return_value': 239, 'Exception': EX_ENOGRP },
    'EX_INVCMD': { 'return_value': 240, 'Exception': EX_INVCMD },
    'EX_INVMOD': { 'return_value': 241, 'Exception': EX_INVMOD },
    'EX_ENORMT': { 'return_value': 242, 'Exception': EX_ENORMT },
    'EX_ENAMLG': { 'return_value': 243, 'Exception': EX_ENAMLG },
    'EX_ERANGE': { 'return_value': 244, 'Exception': EX_ERANGE },
    'EX_ENOMEM': { 'return_value': 245, 'Exception': EX_ENOMEM },
    'EX_ENODEV': { 'return_value': 246, 'Exception': EX_ENODEV },
    'EX_ENOENT': { 'return_value': 247, 'Exception': EX_ENOENT },
    'EX_OPTINV': { 'return_value': 248, 'Exception': EX_OPTINV },
    'EX_INVNAM': { 'return_value': 249, 'Exception': EX_INVNAM },
    'EX_ATTDBG': { 'return_value': 250, 'Exception': EX_ATTDBG },
    'EX_ATTHOR': { 'return_value': 251, 'Exception': EX_ATTHOR },
    'EX_UNWOPT': { 'return_value': 252, 'Exception': EX_UNWOPT },
    'EW_UNWOPT': { 'return_value': 252, 'Exception': EW_UNWOPT },
    'EW_INVARG': { 'return_value': 253, 'Exception': EW_INVARG },
    'EX_INVARG': { 'return_value': 253, 'Exception': EX_INVARG },
    'EX_REQARG': { 'return_value': 254, 'Exception': EX_REQARG },
    'EX_COMERR': { 'return_value': 255, 'Exception': EX_COMERR }
}
