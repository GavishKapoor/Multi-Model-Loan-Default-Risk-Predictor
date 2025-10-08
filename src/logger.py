import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log" # log file jabh banta hai tu usko samjhna k liya kabh run hua kya run hua uska liya date time

# abh log file kha generete hoga ya pta nhi kyuki uska folder nhi hai to hum folder bana denge logs_path 
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) #cwd -- current working directory logs is the folder bnn gya
# abh uski directory bna do
os.makedirs(logs_path, exist_ok=True) #exist_ok=True means if the folder already exists it will not give an error

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # path or file ko join krr diya 


logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"

)