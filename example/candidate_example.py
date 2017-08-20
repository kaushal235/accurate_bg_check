import sys
import random
from candidate import Candidate
from .client import client

payload = {
    "firstName": "Test name Albert {0}".format(random.randint(1,999)),
    "lastName": "Einstein",
    "middleName": 'Z',
    "dateOfBirth": "1972-05-26",
    "ssn": "531-90-1234",
    "email": "noemail_{0}@somenoemailsomenoemail.com".format(random.randint(1000,9999999999)),
    "phone": "000-000-0000",
    'address': 'address 1',
    'city': 'Burbank',
    "region": "CA",
    "country": "US",
    'postalCode': 91501
}


if __name__ == '__main__':
    len_sys_args = len(sys.argv)
    if len_sys_args < 2:
        raise Exception('Parameter missing')

    candidate = Candidate(client)
    file, opr = sys.argv
    opr = int(opr)
    if opr == 1:
        candidate.create(payload)

    if opr == 2:
        candidate_list = candidate.list()
        print(candidate_list)
        print("total candidate ", len(candidate_list))