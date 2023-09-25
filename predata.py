import os
import numpy as np
import shutil

def split(dir = 'data',split_size = [.8,.2]):
    #generate the splits
    name_files = [file.split('.')[0] for file in os.listdir(f'{dir}/labels')]
    split = np.random.randint(len(name_files),size = len(name_files))
    train_size = int(len(name_files)*split_size[0])
    val_size = len(name_files)-train_size
    train_data,val_data = split[:train_size],split[-val_size:]
    #dirs
    parent_dir = f'{os.getcwd()}/procc_data'
    if os.path.exists(parent_dir):
        shutil.rmtree(parent_dir)
    split_dirs,type_dirs = ['train','val'],['images','labels']
    for split_dir in split_dirs:
        for type_dir in type_dirs:
            os.makedirs(f'{parent_dir}/{split_dir}/{type_dir}')
    #copy files
    for file_idx in train_data:
        name_file = name_files[file_idx]
        scr_images = f'{dir}/images/{name_file}.jpg'
        scr_labels = f'{dir}/labels/{name_file}.txt'
        dst_images = f'{parent_dir}/train/images/{name_file}.jpg'
        dst_labels = f'{parent_dir}/train/labels/{name_file}.txt'
        shutil.copyfile(scr_images, dst_images)
        shutil.copyfile(scr_labels, dst_labels)
    for file_idx in val_data:
        name_file = name_files[file_idx]
        scr_images = f'{dir}/images/{name_file}.jpg'
        scr_labels = f'{dir}/labels/{name_file}.txt'
        dst_images = f'{parent_dir}/val/images/{name_file}.jpg'
        dst_labels = f'{parent_dir}/val/labels/{name_file}.txt'
        shutil.copyfile(scr_images, dst_images)
        shutil.copyfile(scr_labels, dst_labels)
if __name__ == '__main__':
    split()
