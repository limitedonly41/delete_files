
for i in range(5):
    print(i)
    try:
        print(i**5)
    except:
        print('oops')
        continue