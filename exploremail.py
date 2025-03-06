import dns.resolver

def check_spf(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            if str(rdata).startswith('"v=spf1'):
                return f"SPF record found: {rdata}"
        return "No SPF record found."
    except Exception as e:
        return f"Error checking SPF: {e}"

def check_dkim(selector, domain):
    try:
        dkim_domain = f"{selector}._domainkey.{domain}"
        answers = dns.resolver.resolve(dkim_domain, 'TXT')
        for rdata in answers:
            return f"DKIM record found: {rdata}"
        return "No DKIM record found."
    except Exception as e:
        return f"Error checking DKIM: {e}"

def check_dmarc(domain):
    try:
        dmarc_domain = f"_dmarc.{domain}"
        answers = dns.resolver.resolve(dmarc_domain, 'TXT')
        for rdata in answers:
            return f"DMARC record found: {rdata}"
        return "No DMARC record found."
    except Exception as e:
        return f"Error checking DMARC: {e}"

# Example usage:
domain = "example.com"
selector = "default"  # Replace with the DKIM selector used for the domain

print(check_spf(domain))
print(check_dkim(selector, domain))
print(check_dmarc(domain))
