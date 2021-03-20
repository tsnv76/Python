import re
import os

parsed_raw = ()

i = 0
nginx_log = 'nginx_log.txt'
if os.path.exists(nginx_log):
    with open(nginx_log) as log:
        for line in log:
            if i == 100:
                break
            PARSE_LINE = list(re.findall(r'(\d+.\d+.\d+.\d+) (\w+|\-) (\w+|\-) \[(.+)\] \"(.+)\" (\d+) (\d+)', line)[0])
            remote_addr = PARSE_LINE[0]
            request_datetime = PARSE_LINE[3]
            request_type = PARSE_LINE[4].split(' ')[0]
            requested_resource = PARSE_LINE[4].split(' ')[1]
            response_code = PARSE_LINE[5]
            response_size = PARSE_LINE[5]
            parsed_raw = (remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)
            str_parse = ', '.join(map(str, parsed_raw))
            print(parsed_raw)
            i +=1
