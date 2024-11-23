import os

# folder path
dir_path = 'Data/BadPosture/badform-samples'
badform = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        badform += 1
print('Badform count:', badform)

# folder path
dir_path2 = 'Data/GoodPosture/goodform-samples'
goodform = 0
# Iterate directory
for path in os.listdir(dir_path2):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path2, path)):
        goodform += 1
print('Goodform count:', goodform)

# folder path
dir_path3 = 'Data/Idle'
idle1 = 0
# Iterate directory
for path in os.listdir(dir_path3):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path3, path)):
        idle1 += 1
print('Idle 1 count:', idle1)

# folder path
dir_path4 = 'Data/Idle2'
idle2 = 0
# Iterate directory
for path in os.listdir(dir_path4):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path4, path)):
        idle2 += 1
print('Idle 2 count:', idle2)