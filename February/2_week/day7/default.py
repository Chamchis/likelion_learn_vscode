from dataclasses import dataclass
@dataclass
class AppConfig:
    debug : bool = False
    database_url : str ='some_url'
    port : int = 8000

defult_config = AppConfig()
print(defult_config)
custom_config = AppConfig(debug=True,database_url='google.com',port=45000)
print(custom_config)