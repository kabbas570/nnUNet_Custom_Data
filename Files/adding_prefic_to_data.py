import os

def main():
    folder_path = "C:/My_Data/M2M Data/data/data_2/val_1/"
    for count,filename in enumerate(sorted(os.listdir(folder_path))):
        dst = f"ABS_" + str(count).zfill(3) + ".nii.gz"
        
        src = f"{folder_path}/{filename}"
        dst = f"{folder_path}/{dst}"
        
        
        os.rename(src,dst)
        
        

if __name__ == '__main__':
    main()
