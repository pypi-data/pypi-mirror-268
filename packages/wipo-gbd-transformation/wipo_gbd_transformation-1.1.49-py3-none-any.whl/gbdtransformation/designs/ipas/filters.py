# standard gbd definitions
from gbdtransformation.designs import kinds as std_kinds
from gbdtransformation.designs import status as std_status

# namespaces defined in XML and to be ignored in procecssing
ignore_namespace = []


# -------------------------------------------------------------
# data translation helpers:
# translate values from office interpretation to gbd equivalent
# -------------------------------------------------------------

def translate_kind(kind):
    """translation of the kind of trademark to a
        multivalue gbd interpretation"""

    # out-of-the-box match
    if kind.capitalize() in std_kinds:
        return [kind.capitalize()]

    # __insert here__ : translation logic

    # raise Exception to recognize unmapped values
    raise Exception('kind "%s" is not mapped.' % kind)

# Expired trademarks with no Expiry date
# => get it from Expired event
def get_expiry_date(design, idstatus):
    if design.ExpiryDate:
        return design.ExpiryDate

    if not idstatus == 'Expired':
        return None

    # find the MarkEvent Expired and get its date
    events = design.get('MarkEventDetails', {}).get('MarkEvent', [])
    for event in events:
        if hasattr(event, 'MarkEventCode'):
            if(event.MarkEventCode == 'Expired'):
                return event.MarkEventDate


# Registered or Expired trademarks with no registration date
# => get it from Registered or Published Event
def get_registration_date(trademark, tmstatus):
    if trademark.RegistrationDate:
        return trademark.RegistrationDate

    if not tmstatus in ['Expired', 'Registered']:
        return None

    # find the MarkEvent Expired and get its date
    events = trademark.get('MarkEventDetails', {}).get('MarkEvent', [])

    # first priority is to get the Registered Event
    for event in events:
        if hasattr(event, 'MarkEventCode'):
            if event.MarkEventCode == 'Registered':
                return event.MarkEventDate
    # second priority is to get the Published Event
    for event in events:
        if hasattr(event, 'MarkEventCode'):
            if event.MarkEventCode == 'Published':
                return event.MarkEventDate

def translate_status(status):
    status = status.lower()

    if status == 'registered': return 'Registered'
    if status == 'active': return 'Registered'
    if status == 'reinstated': return 'Registered'
    if status == 'expired': return 'Expired'
    if status == 'inactive': return 'Expired'
    if status == 'published': return 'Pending'
    if status == 'examined': return 'Pending'
    if status == 'filed': return 'Pending'
    if status == 'converted': return 'Pending'
    if status == 'opposed': return 'Pending'
    if status == 'pending': return 'Pending'
    if status == 'appealed': return 'Pending'
    if status == 'awaiting court action': return 'Pending'
    if status == 'application published': return 'Pending'
    if status == 'abandoned': return 'Ended'
    if status == 'withdrawn': return 'Ended'
    if status == 'rejected': return 'Ended'
    if status == 'finalrefusal': return 'Ended'
    if status == 'suspended': return 'Ended'
    if status == 'invalidated': return 'Ended'
    if status == 'surrendered': return 'Ended'
    if status == 'suspended': return 'Ended'
    if status == 'renewed': return 'Registered'
    if status == 'renewalprocess': return 'Registered'
    if status == 'canceled': return 'Ended'
    if status == 'cancelled': return 'Ended'

    #return 'Unknown'
    raise Exception('Status "%s" not mapped.' % status)