from datetime import datetime
import pytz
def get_datetime_sp():
    return datetime.now(pytz.timezone('Brazil/East'))
