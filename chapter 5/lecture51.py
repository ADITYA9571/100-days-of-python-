"""seek() tell() and truncate()"""
# with open('file.txt','r') as f:
#     print(type(f))
#     f.seek(7) -- seek will move the index to the mentioned
#     print(f.tell()) -- it will mention the current index
#     data = f.read(5)
#     print(data)
######truncate()
# with open('file.txt','w') as f:
#     f.write('hello world!!')
#     f.truncate(5)
# with open('file.txt','r') as f:
#     print(f.read())
######truncate part 2
# with open('file.txt','a') as f:
#     f.truncate(5)
# with open('file.txt','r') as f:
#     print(f.read())
######to cut off in a range 
with open('file.txt', 'r+') as f:
    content = f.read()
    updated = content[:3] + content[6:]
    
    f.seek(0)          # Go back to start
    f.write(updated)   # Overwrite with updated content
    f.truncate()       # Cut off any leftover data
