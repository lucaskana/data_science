import yaml
from yaml.loader import SafeLoader

def readConfigYml(fileName='config.yml'):
    with open(fileName) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data