""" # Server Configuration File

# Network Settings
PORT = 8080
MAX_CONNECTIONS=600
TIMEOUT = 30

# Security Settings
SSL_ENABLED = true
SSL_CERT = /path/to/certificate.pem

# Logging Settings
LOG_LEVEL = INFO
LOG_FILE = /var/log/server.log

# Other Settings
ENABLE_FEATURE_X = true """


def update_server_config_file(config_file, key, value):
    try:
        with open(config_file, 'r') as file:
            lines = file.readlines()

        with open(config_file, 'w') as file:
            for line in lines:
                if key in line:
                    file.write(key +  "=" + value + "\n")
                else:
                    file.write(line)
    except Exception as e:
        print(f"An error occurred: {e}")
       
                
if __name__ == "__main__":
    config_file = 'server_config.txt'
    update_server_config_file(config_file, 'MAX_CONNECTIONS', '1000')

