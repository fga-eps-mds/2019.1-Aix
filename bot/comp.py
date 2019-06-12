import yaml
import sys
domain_data = {}
try:
    with open('domain.yml', 'r') as domain:
        domain_data = yaml.safe_load(domain)
    print(domain_data)
except:
    err_type, error, traceback = sys.exc_info()
    print(err_type, error, traceback)
    raise sys.exit(1)