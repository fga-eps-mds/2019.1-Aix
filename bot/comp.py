import yaml
with open('domain.yml', 'r') as domain:
    domain_data = yaml.safe_load(domain)
for i in domain_data:
    print(domain_data[i])