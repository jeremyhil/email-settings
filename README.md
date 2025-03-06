# email-settings


Looking for a simple way to check for support of SPF, DKIM and DMARC

SPF Record Check: nslookup -type=txt mydomain.com
DKIM Record Check: nslookup -type=txt selector._domainkey.example.com
DMARC Record Check: nslookup -type=txt _dmarc.example.com

## But what if we could automate this?

Lets explore the options in Python using dns.resolver

Install the dnspython library if you don’t have it already

pip install dnspython

## Running

python exploremail.py
Will checks only one domain

python emailcheck.py
Reads the domains.txt file (One domain per line) and creates results.txt

### Ongoing

What if the selector is not known?
Could we test for it?