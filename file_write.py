append = '======================================================================'
def write_to_file(data):
     with open('storage\list.txt', 'a') as f:
         f.write(data + '\n' + append  + '\n') 

