def make_album(singer,name):
    album = {'singername':singer,'songname':name}
    return album
while True:
    print("Please tell me the message.")
    getsinger = input("Singername:")
    getsongname = input("Songname:")

    result = make_album(getsinger,getsongname)
    print(result)

    #8-9
def show_magicians(names):
    magicians = ["魔术师的名字为：" + names]
    return magicians
a = show_magicians("James")
print(a)
