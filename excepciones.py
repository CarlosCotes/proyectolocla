import traceback
from datetime import datetime

def log_error(exception):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_message = f"{timestamp}: {str(exception)}\n"
    with open("Errores.txt", "a") as file:
        file.write(error_message)
        traceback.print_exc(file=file)