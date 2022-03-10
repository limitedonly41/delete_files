import os, shutil
import requests

# program = '''import os, shutil
# folder = '/Users/tair/Freelance/anti_scam/test'
# print('hi')
# for  i in range(5):
#     print(i)
# for filename in os.listdir(folder):
#     file_path = os.path.join(folder, filename)
#     print(file_path)
#     print('ok')
#     try:
#         print(file_path)
#     except Exception as e:
#         print('Failed to delete %s. Reason: %s' % (file_path, e))'''
# exec(program)



folder = '/Users/tair/Freelance/anti_scam/test'
files = [f for f in os.listdir(folder)]
print(files)
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
        continue