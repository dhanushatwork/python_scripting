# Create a function generate_env_file(env_vars: dict) 
# that takes a dictionary of environment variables and writes them to a .env file in the format:

def generate_env_file():
    with open("env.vars", "x") as ev_file:
        print(ev_file)

    with open(ev_file, "w"):
        ev_file.write()