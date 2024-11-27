# log file


# write a logging solution to store each log from some program and generate the report
# based on number of events in a day, success, failure etc

"""
timestamp command: command, result: pass/fail, started
timestamp command: command, result: pass/fail, stopped, error: Network timout

generate
trigger
build
"""
import re

command_pattern = re.compile(r'coomand: (\w+),')
result_pattern = re.compile(r'result: (\S+),')
error_pattern = re.compile(r'error: ([A-Z0-9_-]+)')

# tool-23-8-24.log

def read_log(logfile):

    command_store = []
    result_store = []
    error_store = []

    with open(logfile, 'r') as logs:
        lines = logs.readlines()

        for line in lines:

            command_match = command_pattern.match(line)
            if command_match:
                commad = command_match.group(1)
                command_store.append(commad)
            
            match2 = result_pattern.search(line)

            if match2:
                result = match2.groups(1)
                result_store.append(result)

            match3 = error_pattern.search(line)
            if match3:
                error = match3.group(1)
                error_store.append(error)

    return command_store, result_store, error_store



def generate_report(input_data: tuple):

    title = "Tool Report".center(50)
    print(title)

    command_info, result_info, error_info = input_data

    for info in zip(command_info, result_info, error_info):
        if info[2]:
            print(f"Command Executed: {info[0]}, Result: {info[1]}, error: {info[2]}")
        else:
            print(f"Command Executed: {info[0]}, Result: {info[1]}")


if "__main__" == __name__:

    input_log_file = "random-23-8-24.log"
    extracted_data = read_log(input_log_file)
    generate_report(extracted_data)
            

