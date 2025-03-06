# email-settings


Looking for a simple way to check for support of SPF, DKIM and DMARC

SPF Record Check: nslookup -type=txt mydomain.com

DKIM Record Check: nslookup -type=txt selector._domainkey.example.com

DMARC Record Check: nslookup -type=txt _dmarc.example.com

## But what if we could automate this?

Lets explore the options in Python using dns.resolver

Install the dnspython library if you don’t have it already

<kbd>pip install dnspython</kbd>

## Running

<kbd>python exploremail.py</kbd>

Will checks only one domain

<kbd>python emailcheck.py</kbd>

Reads the domains.txt file (One domain per line) and creates results.txt

<kbd>python emailcheck_unkown.py</kbd>

Same as emailcheck.py but tests using three selectors (default, selector1, selector2)

### Ongoing

What if the selector is not known?

We could test with multiply values eg: using emailcheck_unkown.py
