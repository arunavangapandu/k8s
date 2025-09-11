import requests

#/repos/{owner}/{repo}/pulls
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
#print(response.json())

output = response.json()
print(output[0]['url'])
for user_data in output:
    print(user_data['url'])
    print(user_data['user']['login'])
    print(user_data['user']['url'])
    print("----")
#print(output[0]['user']['login'])                              
for i in range(len(output)):
    print(output[i]['user']['login'])

server_config = {
    'server1': {'ip':'192.168.1.1', 'port':8080, 'status':'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}
def get_active_status(server_name):
    return server_config.get(server_name, {}).get('status', 'server not found')

server_name = 'server2'
status = get_active_status(server_name)
print(f"{server_name} status: {status}")

def take_request(url):
    response = requests.get(url)
    return response

# verify if the request was successful
if response.status_code == 200:
    print("Request was successful")
    pull_requests = response.json()

    pr_creators = {}
    for pr in pull_requests:
        creator = pr['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    print(pr_creators)
    