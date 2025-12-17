import docker

client = docker.from_env()

print("Listing all Docker containers")
containers = client.containers.list()

if not containers:
    print("No containers running")
else:
    for container in containers:
        print(F" Name : {container.name}, status : {container.status}")

