

post = dict(meg='a',country = 'india',language = 'many')
def reverse_lookup():
    for key in post.keys():
        value = post[key]
        try:
            pad = str(input("Enter the value:"))
            print(post[pad])
        except Keyerror:
            print("keyword not found")
        print(post,'\n',key)
reverse_lookup()






