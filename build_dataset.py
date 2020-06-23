import os
import shutil

data_dir = 'ArASL_Database_54K_Final'




if os.path.isdir(os.path.join(data_dir, 'val')):
    print('file exists')
else:
    os.mkdir(os.path.join(data_dir, 'val'))

classes = os.listdir(os.path.join(data_dir, 'train'))
print(f'Number of classes: {len(classes)}')
for c in classes:
    # get the files names
    files = os.listdir(os.path.join(data_dir, 'train', c))
    # split data
    split_1 = int(0.8 * len(files))
    train_files = files[:split_1]
    val_files = files[split_1:]
    print(f'Class: {c}: ')
    print(f'train len: {len(train_files)}, val len: {len(val_files)}')
    
    # Move the data to new directories
    os.mkdir(os.path.join(data_dir, 'val', c)) # Create new dir for each class
    for f in val_files:
        shutil.move(os.path.join(data_dir, 'train', c, f), os.path.join(data_dir, 'val', c, f))
