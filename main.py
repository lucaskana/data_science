from src.config.read_cfg import readConfigYml

def main(model, config_file):
    #Extraction, Transformation/Preprocessing and Analysis/Modelling
    print('1 - Extraction, Transformation')
    print('2 - Preprocessing and Analysis')
    print('1 - Modelling')

if __name__ == "__main__":
    #main()
    data = readConfigYml()
    print(data)
