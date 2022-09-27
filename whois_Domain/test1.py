import whois

domain = whois.whois('revive.cn')
print(domain.__dict__)

print(domain.expiration_date)
