import os
import time


source_location = '/var/log/alienvault/devices/172.16.8.145/'
source_file = '172.16.8.145.log'
source_path = source_location + source_file
source_log = open(source_path, 'rb')
# Find the size of the file and move to the end
st_results = os.stat(source_path)
st_size = st_results[6]
source_log.seek(st_size)

while 1:
    where = source_log.tell()
    line = source_log.readline()
    if not line:
        time.sleep(1)
        source_log.seek(where)
    else:
        print(line)
