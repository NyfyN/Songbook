import configparser

class Config:
    def __init__(self, path: str):
        self.path = path
        self.config_dict = {}
        
    def configurate(self):
        config = configparser.ConfigParser()
        try:
            config.read(self.path)

            if "SETTINGS" in config:
                try:
                    for key in config["SETTINGS"]:
                        self.config_dict[key] = self.parser(config["SETTINGS"][key])
                except KeyError as e:
                    print(f"Klucz {e} nie został znaleziony w sekcji 'SETTINGS'.")
                except ValueError as e:
                    print(f"Błąd konwersji wartości: {e}")
            else:
                raise ValueError("Sekcja 'SETTINGS' nie została znaleziona w pliku konfiguracyjnym!")
        except configparser.Error as e:
            print(f"An error occurred while reading the configuration file: {e}")
        return self.config_dict
    
    def parser(self, config_item: str):
        return tuple(map(int, config_item.split(',')))
    
