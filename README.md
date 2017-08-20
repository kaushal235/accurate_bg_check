# accurate_bg_check
Python client for accurate background check

### Accessing the API
Create the `BgCheck` client object before you make any calls to Accurate Background Check. Setup the client connection using the `CLIENT_KEY` and `CLIENT_SECRET`

```python
  from accurate_bg_check.client import BgCheck
  client = BgCheck('CLIENT_KEY, CLIENT_SECRET')
```
  
### Get Candidate List
```python
from accurate_bg_check.candidate import Candidate
candidate = Candidate(client=client)
print(candidate.list())
```

### Create Candidate
```python
from accurate_bg_check.candidate import Candidate
candidate = Candidate(client=client)
payload = {
    "firstName": "Test name Albert {0}".format(random.randint(1,999)),
    "lastName": "Einstein",
    "middleName": 'A',
    "dateOfBirth": "1972-05-26",
    "ssn": "000-00-000",
    "email": "noemail_{0}@somenoemailsomenoemail.com".format(random.randint(1000,9999999999)),
    "phone": "000-000-0000",
    'address': 'address 1',
    'city': 'Burbank',
    "region": "CA",
    "country": "US",
    'postalCode': 91501
}
response = candidate.create(payload)  # pass json object
print(response)
```
