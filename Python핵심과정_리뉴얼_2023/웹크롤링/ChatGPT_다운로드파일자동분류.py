import os
import shutil

# Define the paths to the download folder and the four destination folders
download_folder = '/Users/user/Downloads'
image_folder = '/Users/user/Downloads/Images'
pdf_folder = '/Users/user/Downloads/PDFs'
dataset_folder = '/Users/user/Downloads/Datasets'
video_folder = '/Users/user/Downloads/Videos'

# Create the destination folders if they don't exist
for folder in [image_folder, pdf_folder, dataset_folder, video_folder]:
    if not os.path.exists(folder):
        os.mkdir(folder)

# Loop over all the files in the download folder and classify them based on their extension
for filename in os.listdir(download_folder):
    extension = os.path.splitext(filename)[1]
    if extension in ['.jpeg', '.png']:
        shutil.move(os.path.join(download_folder, filename), os.path.join(image_folder, filename))
        print(f"Moved {filename} to Images folder")
    elif extension == '.pdf':
        shutil.move(os.path.join(download_folder, filename), os.path.join(pdf_folder, filename))
        print(f"Moved {filename} to PDFs folder")
    elif extension in ['.csv', '.xlsx', '.json']:
        shutil.move(os.path.join(download_folder, filename), os.path.join(dataset_folder, filename))
        print(f"Moved {filename} to Datasets folder")
    elif extension == '.mp4':
        shutil.move(os.path.join(download_folder, filename), os.path.join(video_folder, filename))
        print(f"Moved {filename} to Videos folder")
