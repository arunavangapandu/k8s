import os
from collections import defaultdict
#/Users/arunavangapandu/Software/k8s-minikube-app-deployment/python/nginx-file.txt
def log_file_processing(log_file_path):
    print("Current working directory:", os.getcwd())

   # script_dir = os.path.dirname(os.path.abspath(nginx-file.txt))
    #print("Script Directory", script_dir)

    # Nested dict: { timestamp: { response_code: count } }
    result_dict = defaultdict(lambda: defaultdict(int))

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                line = line.lower().strip()
                if not line:
                    continue

                # Assume timestamp is first token, e.g. '12:10:10'
                parts = line.split()
                timestamp = parts[0]

                # Check which response code(s) appear in the line
                for code in ['400', '504', '200']:
                    if code in line:
                        result_dict[timestamp][code] += 1
                        

        return dict(result_dict)  # convert defaultdict to dict for readability

    except FileNotFoundError:
        print(f"Log file '{log_file_path}' not found")
    except Exception as e:
        print(f"An error occurred while processing the log file: {e}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print("Script Directory", script_dir)
    log_file_path = os.path.join(script_dir, 'nginx-file.txt')
    if not os.path.exists(log_file_path):
        print(f"Log file '{log_file_path}' does not exist.")
        result = {}
    else:
        result = log_file_processing(log_file_path)

    print("\nResults:")
    for timestamp, codes in result.items():
        print(f"Timestamp: {timestamp}")
        for code, count in codes.items():
            print(f"  Response Code {code}: {count} hits")


