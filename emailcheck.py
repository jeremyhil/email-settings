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

# Batch processing
def batch_process(file_path, selector):
    try:
        with open(file_path, 'r') as file:
            domains = file.readlines()

        with open('results.txt', 'w') as results:
            for domain in domains:
                domain = domain.strip()
                if domain:
                    results.write(f"Domain: {domain}\n")
                    results.write(check_spf(domain) + "\n")
                    results.write(check_dkim(selector, domain) + "\n")
                    results.write(check_dmarc(domain) + "\n")
                    results.write("\n")  # Add spacing for readability
    except Exception as e:
        print(f"Error during batch processing: {e}")

# Example usage
file_path = "domains.txt"  # File containing the list of domains
selector = "default"       # Replace with the correct DKIM selector
batch_process(file_path, selector)
