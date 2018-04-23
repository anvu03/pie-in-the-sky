import route_finder


output_file = open('output.txt', 'w')
error_file = open('error.txt', 'w')
print('=======================')
with open('input.txt', 'r') as file:


    for line in file:
        route_finder.handler(line)

print('=======================')
output_file.close()
error_file.close()