import datetime
from dhi.platform.base.exceptions import MikeCloudException
from .constants import DATETIMEFORMAT_SECONDS_URL
from .constants import DATETIMEFORMAT
from .constants import DATETIMEFORMAT_SECONDS

def sanitize_from_to(from_:datetime.datetime=None, to:datetime.datetime=None):
    #if not (from_ or to):
    #    raise MikeCloudException("At least one of from_ and to parameters must be specified")
    
    if (from_ and to) and  (to < from_):
        raise MikeCloudException("Parameter from_ must be lower than parameter to")

    if from_:
        from_ = datetime.datetime.strftime(from_, DATETIMEFORMAT_SECONDS_URL)
    
    if to:
        to = datetime.datetime.strftime(to, DATETIMEFORMAT_SECONDS_URL)
    
    return (from_, to)

def parse_datetime(date_str, formats=None):
    if formats is None:
        formats = [DATETIMEFORMAT, DATETIMEFORMAT_SECONDS]

    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str[:26], fmt)
        except ValueError:
            continue
    raise ValueError(f"date_str does not match any supported format: {date_str}")
