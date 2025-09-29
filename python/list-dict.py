""" import requests

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
 """
""" def take_request(url):
    response = requests.get(url)
    return response

# verify if the request was successful
if response.status_code == 200:
    print("Request was successful")
    pull_requests = response.json()

    pr_creators = {}clear
    for pr in pull_requests:
        creator = pr['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    print(pr_creators) """
    

""" def build(snacks):
        for i in range(len(snacks)):
            item = snacks[i]
            name = item[0]
            calories = item[1]
            print(f'#{i+1} {name} : {calories}')

    # list of tuples
snacks = [('bacon', 350), 
              ('donut', 200),
              ('muffin', 100)]
    
build(snacks)

def build(snacks):
      for i, item, value in enumerate(snacks, i):
            print(f'# i {item}: {value}')

flavor_list = ['vanila', 'choclate', 'pecan', 'strawberry']
for flavor in flavor_list:
      print(f'{flavor} is delicious')


def max_count(names):
    max_count = 0
    for i in range(len(names)):
          if len(names[i]) > max_count:
                longest_string = names[i]
                max_count = len(names[i])
    return max_count

names = ['Cecilia', 'Lise', 'Marie']
print(max_count(names))


def sort_numbers(numbers):
      numbers.sort()
      print(numbers)

numbers = [11, 68, 70, 86]
sort_numbers(numbers) """

class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name}, {self.weight})'
    
tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25)
]
print('Unsorted:', str(tools))
tools.sort(key=lambda x: x.name)
print('\nSorted: ', tools)

tools.sort(key = lambda x: (x.weight, x.name))
for tool in tools:
   print(tool.__repr__()) 


places = ['home', 'work', 'New York', 'Paris']
