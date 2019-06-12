import yaml
dict = yaml.load(open('domain.yml'))
for i in dict:
    print(dict[i])
