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

def check_dkim(domain):
    selectors = ["default", "selector1", "selector2"]  # Add more potential selectors if needed
    for selector in selectors:
        try:
            dkim_domain = f"{selector}._domainkey.{domain}"
            answers = dns.resolver.resolve(dkim_domain, 'TXT')
            for rdata in answers:
                return f"DKIM record found for selector '{selector}': {rdata}"
        except dns.resolver.NoAnswer:
            continue  # Try the next selector
        except Exception as e:
            return f"Error checking DKIM for selector '{selector}': {e}"
    return "No DKIM record found."

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
def batch_process(file_path):
    try:
        with open(file_path, 'r') as file:
            domains = file.readlines()

        with open('results.txt', 'w') as results:
            for domain in domains:
                domain = domain.strip()
                if domain:
                    results.write(f"Domain: {domain}\n")
                    results.write(check_spf(domain) + "\n")
                    results.write(check_dkim(domain) + "\n")
                    results.write(check_dmarc(domain) + "\n")
                    results.write("\n")  # Add spacing for readability
    except Exception as e:
        print(f"Error during batch processing: {e}")

# Example usage
file_path = "domains.txt"  # File containing the list of domains
batch_process(file_path)
