#Args and Kwargs

#Args
def print_name(*args):
    for name in args:
        print(f'Hello {name}')
    if not args:
        print("Please add a name to say hello")
print_name()

#Kwarks
def user_info(**kwargs):
    print(kwargs)

user_info(name="Juliana",age=35, address="Ramat Gan")


def task_manager(*args):
    if args:
        for task in args:
            print(f'I need to {task}')
    else:
        print("Please pass a task as argument")
task_manager(" Cook", " work")
task_manager()

#using *args and **kwargs together
def party_planner(*args, **kwargs):
    if args:
        for arg in args:
            print(arg)
    else:
        print("There is no food to buy")
    
    if kwargs:
        print("Party details:")
        for key, value in kwargs.items():
            print(f'Key={key}, value= {value}')
    else:
        print("There is no details for this party")
party_planner(["Coke","milk"],address="Ben Yehuda",num="25")
party_planner("Coke","milk")
print("Hi")
party_planner(address="Ben Yehuda",num="25")