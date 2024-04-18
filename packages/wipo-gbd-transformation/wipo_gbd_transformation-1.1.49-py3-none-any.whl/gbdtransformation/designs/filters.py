import re
from gbdtransformation.designs import st13_identifier
from gbdtransformation.common.filters import *

def parseStatus(status):
    """ Function is here to be overriden in child elements( e.g BRTM)"""
    return status

def st13(appnum, office, pos, type='Design', appdate=None, roffice=None, sanitize=True):
    if not appnum:
        return None
    # collections are usually office code followed with tm: xxtm
    collection = '%sid' % office.lower()

    module_pckg = load_collection_package('designs', collection)
    try:
        masks = getattr(module_pckg, 'appnum_mask')
        if not isinstance(masks, list): masks = [masks]
    except:
        masks = ['(.*)']

    try:
        source = getattr(module_pckg, 'source')
    except:
        source = 'national'
    matches = None
    for mask in masks:
        regex = re.compile('^%s$' % mask)
        matches = regex.search(appnum)
        if matches:
            break

    if not matches:
        raise Exception('could not apply appnum mask %s on %s' % (mask, appnum))

    #print(appnum, ''.join(matches.groups()))
    appnum = ''.join(matches.groups())

    prefix = st13_identifier[source.lower()][type.lower()]
    if sanitize:
        # remove special characters
        special_chars = re.compile(r'\W')
        appnum = special_chars.sub('', appnum)

    # reference office (only relevant for inerantional)
    if roffice:
        appnum = '%s%s' % (roffice.upper(), appnum)

    st13 = '%s%s' % (office.upper(), prefix)
    if appdate:
        st13 = '%s%s' % (st13, appdate[:4])

    # add application number and zfill till 17
    return '%s%s.%s' % (st13, appnum.zfill(17 - len(st13)), pos)
