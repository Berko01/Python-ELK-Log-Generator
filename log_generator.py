import time
import random
import os

log_file_path = os.getenv("LOG_FILE_PATH", "/usr/share/logstash/temp/inlog.log")

log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
messages = [
    "User logged in",
    "User logged out",
    "File not found",
    "Error while processing request",
    "Data saved successfully",
    "Connection lost",
    "Reconnected to the server"
]

def generate_log_message():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_level = random.choice(log_levels)
    message = random.choice(messages)
    log_message = f"{timestamp} - {log_level} - {message}\n"
    return log_message

def write_log_to_file(log_message):
    with open(log_file_path, "a") as log_file:
        log_file.write(log_message)

if __name__ == "__main__":
    while True:
        log_message = generate_log_message()
        print(log_message.strip())  # Optional: print log message to console
        write_log_to_file(log_message)
        time.sleep(5)  # Wait for 5 seconds before generating the next log message
