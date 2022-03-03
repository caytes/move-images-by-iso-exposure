import os
import shutil
import sys

# import exif
from PIL import Image
from PIL.ExifTags import TAGS

# image_file = 'test_images/image1.JPG'
# Create image objects from class and store in list
# OR
# Walk directory, check image metadata, if match criteria, then move to other folder

directory = 'test_images'
exif_data = {}
move_files_list = []
new_folder = 'moved_files/'
iso = 0
iso_match = 500
exposure = 0
exposure_match = 5.0

# iterate over files in
# that directory
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)  # join the path with the filename

    # try to open the image
    try:
        image = Image.open(file)
    # failure if not opened
    except IOError:
        print('Could not open file or path: ', file)
        pass

    # extract metadata to a dictionary
    for tag, value in image._getexif().items():
        if tag in TAGS:
            # store tags and values in a dictionary
            exif_data[TAGS[tag]] = value

    # print the filename before the metadata
    print('\nFilename: ', file, '\n')
    # if it's a file then check metadata
    print('**------------------The metadata------------------**')

    # prints all metadata for each found file
    for tag, value in exif_data.items():
        # need to use value and ExposureTime
        if TAGS.get(tag, tag) == 'ISOSpeedRatings':
            iso = value
        if TAGS.get(tag, tag) == 'ExposureTime':
            exposure = value
            if iso == iso_match and exposure == exposure_match:
                move_files_list.append(file)
    print('List of matching files: ', move_files_list)
    '''
        if TAGS.get(tag, tag) == 'ISOSpeedRatings':
            iso = value
            print('The ISO is: ', iso)
        if TAGS.get(tag, tag) == 'ExposureTime':
            exposure = value
            print('The Exposure is: ', exposure)
    
    if exposure == 5.0:
        move_files_list.append(file)
    print(move_files_list)
    '''
    '''
        # if iso and exposure equal the specified criteria then move to another file
        shutil.copy(file, new_folder)
        print('Successfully moved!')
    else:
        print('Not successfully moved due to an error or no matches found.')
    '''

    '''
    dirListing = os.listdir(path)
    editFiles = []
    for item in dirListing:
        if ".txt" in item:
            editFiles.append(path + '\\' + item)
    print editFiles
    '''


# checking if it is a file
    '''if os.path.isfile(file):
        print(file)
        # grab filename and store in a variable '''