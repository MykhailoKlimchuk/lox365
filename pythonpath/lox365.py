# import functools
import json
import pprint
import urllib
import urllib.request

ERR_CALC = '#CALC!'
ERR_NA = '#N/A'

def format_data(func):
    def inner(*args, **kwargs):
        data = func(*args, **kwargs)
        return ((data, ),)
    return inner


@format_data
def tbacc(audit_id, token, account_code, host, total):
    url = f'{host}/api/v1/trial_balance/{audit_id}'

    req = urllib.request.Request(
        url,
        method="POST",
        data=json.dumps({
            "account": account_code,
            "total": total
        }).encode('utf-8'),
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
        }
    )
    try:
        response = urllib.request.urlopen(req)
    except:
        return "Bad request"
    data = response.read()

    return ((data.decode('utf-8').replace("\n", ""), ),)


# Too slow
# def XLOOKUP_old1(lookup_value, lookup_array, return_array, if_not_found):
#     lookup_item = (lookup_value,)
#     for index, item in enumerate(lookup_array):
#         if item == lookup_item: return (return_array[index],)
#     return ((if_not_found,),)
