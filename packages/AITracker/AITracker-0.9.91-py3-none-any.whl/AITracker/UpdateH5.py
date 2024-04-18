import os
import numpy as np
import h5py
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


def print_image_sizes(h5_file):
    images = h5_file['images'][:]
    for i, image in enumerate(images):
        print(f"Size of image {i + 1}: {image.shape}")

def compile_data(input_h5_files, output_train_h5_file, output_test_h5_file, test_size=0.2, random_state=42):
    # Initialize empty lists to store data from multiple files
    all_images = []
    all_labels = []

    # Loop through the list of input H5 files
    for input_h5_file in input_h5_files:
        # Open each input H5 file
        with h5py.File(input_h5_file, 'r') as h5_file:
            # Print the size of each image before compilation
            print(f"Printing sizes of images in {input_h5_file}:")
            print_image_sizes(h5_file)

            # Get the images and labels
            images = h5_file['images'][:]
            labels = h5_file['labels'][:]

            # Append data from the current file to the lists
            all_images.append(images)
            all_labels.append(labels)

    # Concatenate data from all files
    images = np.concatenate(all_images, axis=0)
    labels = np.concatenate(all_labels, axis=0)

    # Split the combined data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=test_size, random_state=random_state)

    # Create a single H5 file for training data
    with h5py.File(output_train_h5_file, 'w') as train_h5_file:
        train_h5_file.create_dataset('images', data=X_train)
        train_h5_file.create_dataset('labels', data=y_train)

    # Create a single H5 file for testing data
    with h5py.File(output_test_h5_file, 'w') as test_h5_file:
        test_h5_file.create_dataset('images', data=X_test)
        test_h5_file.create_dataset('labels', data=y_test)

def process_all_h5_files(input_dir, output_train_file, output_test_file):
    # Get a list of all H5 files in the input directory
    input_h5_files = [os.path.join(input_dir, file) for file in os.listdir(input_dir) if file.endswith('.h5')]

    # Process all H5 files and compile into single training and testing H5 files
    compile_data(input_h5_files, output_train_file, output_test_file)

# Updates labels in H5 files as they are saved in old data collection app
def update_labels(input_h5_path, output_h5_path, substring_to_label_mapping):
    # Open the input H5 file in read mode
    with h5py.File(input_h5_path, 'r') as h5_file:
        # Check if the 'labels' dataset exists
        if 'labels' not in h5_file:
            print("Error: 'labels' dataset not found in the H5 file.")
            return

        # Read the existing labels
        existing_labels = h5_file['labels'][:]

        # Update the labels based on the specified substrings
        updated_labels = []

        for old_label in existing_labels:
            updated_label = old_label

            for substring, new_label in substring_to_label_mapping.items():
                if substring.encode('utf-8') in old_label:
                    updated_label = new_label.encode('utf-8')
                    break

            updated_labels.append(updated_label)

        # Convert string labels to bytes using a loop
        updated_labels_bytes = np.array([label for label in updated_labels], dtype='S')

        # Create a new H5 file for the updated data
        with h5py.File(output_h5_path, 'w') as output_h5_file:
            # Copy other datasets from the input file to the output file
            for dataset_name in h5_file.keys():
                if dataset_name != 'labels':
                    h5_file.copy(dataset_name, output_h5_file)

            # Create a new 'labels' dataset with the updated labels as bytes
            output_h5_file.create_dataset('labels', data=updated_labels_bytes)

    print(f"Updated H5 file saved to '{output_h5_path}'.")

def image_to_numpy_arr(h5_file):
    # Open the HDF5 file
    with h5py.File(h5_file, 'r') as f:
        # Assuming the dataset containing images is named 'images'
        images_dataset = f['images']
        
        # Assuming the dataset containing labels is named 'labels'
        labels_dataset = f['labels']
        
        # Initialize an empty list to store grayscale images
        grayscale_images = []
        labels = []
        
        # Iterate over each image and label in the datasets
        for image_data, label in zip(images_dataset, labels_dataset):
            # Collapse the three channels into one by averaging
            grayscale_image = np.mean(image_data, axis=2)
            
            # Append the grayscale image to the list
            grayscale_images.append(grayscale_image)
            
            # Append the label to the list
            labels.append(label)

    # Convert the list of grayscale images and labels to numpy arrays
    grayscale_images = np.array(grayscale_images)
    labels = np.array(labels)
    
    os.remove(h5_file)

    # Open the HDF5 file again in write mode to save the processed data
    with h5py.File(h5_file, 'w') as f:
        # Create datasets for images and labels
        f.create_dataset('images', data=grayscale_images)
        f.create_dataset('labels', data=labels)


# Example usage:
substring_to_label_mapping = {
    'northwest': 'North West',
    'northeast': 'North East',
    'southwest': 'South West',
    'southeast': 'South East',
    'north': 'North',
    'south': 'South',
    'west': 'West',
    'east': 'East',
    'center': 'Center'
}
#
#
# # Specify the path to your input H5 file and the desired output path
# input_h5_path = 'H5Demo/eye_data.h5'
# output_h5_path = 'H5Demo/final_eye_data.h5'
#
# # Update labels using the custom_label_update function and save to a new path
# update_labels(input_h5_path, output_h5_path, substring_to_label_mapping)

# Read and display first few images and labels in an H5 file
def readH5(path):
    # Open the HDF5 file for reading
    h5f = h5py.File(path, 'r')

    # Read the 'images' and 'labels' datasets
    images = h5f['images'][:]
    labels = h5f['labels'][:]

    # Close the HDF5 file
    h5f.close()

    # Display the images
    for i in range(len(images)):
        label = labels[i].decode()  # Decode the label from bytes to string
        plt.figure()
        plt.imshow(images[i], cmap='gray')
        plt.title(f"Label: {label}")
        plt.show()

# readH5('H5Demo/g_eye_data.h5')

# Prints all labels in an H5 File
def print_labels(h5_file_path):
    # Open the H5 file in read mode
    with h5py.File(h5_file_path, 'r') as h5_file:
        # Check if the 'labels' dataset exists
        if 'labels' not in h5_file:
            print("Error: 'labels' dataset not found in the H5 file.")
            return

        # Read the labels
        labels = h5_file['labels'][:]

        # Print each label
        for label in labels:
            print(label.decode('utf-8'))

# # Example usage:
# h5_file_path = 'H5Demo/final_eye_data.h5'
# print_labels(h5_file_path)




# Combines two H5 files into a single H5 file
def combine_h5_files(input_h5_file1, input_h5_file2, output_h5_file):
    # Open the first input H5 file in read mode
    with h5py.File(input_h5_file1, 'r') as h5_file1:
        # Read data from the first file
        images1 = h5_file1['images'][:]
        labels1 = h5_file1['labels'][:]

    # Open the second input H5 file in read mode
    with h5py.File(input_h5_file2, 'r') as h5_file2:
        # Read data from the second file
        images2 = h5_file2['images'][:]
        labels2 = h5_file2['labels'][:]

    # Combine the data from the two files
    combined_images = np.concatenate((images1, images2), axis=0)
    combined_labels = np.concatenate((labels1, labels2), axis=0)

    # Create a new H5 file for the combined data
    with h5py.File(output_h5_file, 'w') as output_h5_file:
        # Create datasets in the new file
        output_h5_file.create_dataset('images', data=combined_images)
        output_h5_file.create_dataset('labels', data=combined_labels)

    print(f"Data from '{input_h5_file1}' and '{input_h5_file2}' combined and saved to '{output_h5_file}'.")




#
# input_h5_file1_path = 'H5Demo/image_collection2024-02-25_17-44-06.h5'
# input_h5_file2_path = 'H5Demo/TEMP_image_collection2024-03-18_21-07-37.h5'
# output_h5_file_path = 'H5Demo/eye_data.h5'
#
# combine_h5_files(input_h5_file1_path, input_h5_file2_path, output_h5_file_path)


import h5py
from PIL import Image
import numpy as np

def clean_label(label):
    # Remove any quotation marks from the label and decode it if it's in bytes
    cleaned_label = label.decode('utf-8').replace('"', '').replace("'", "") if isinstance(label, bytes) else label
    return cleaned_label

def h5_to_jpg_batch_with_labels(h5_file_path, output_folder):
    try:
        # Convert output_folder to string if it's a bytes-like object
        output_folder = output_folder.decode('utf-8') if isinstance(output_folder, bytes) else output_folder

        # Open the H5 file
        with h5py.File(h5_file_path, 'r') as h5_file:
            # Assuming the images are stored in a dataset named 'images' and labels in a dataset named 'labels'
            images_dataset = h5_file['images']
            labels_dataset = h5_file['labels']

            # Get the first 5 images and labels (assuming the dataset is 3D with dimensions: (num_images, height, width))
            for i in range(10):
                image_data = images_dataset[i]
                label = labels_dataset[i]

                # Clean the label by removing quotation marks and decoding it if it's in bytes
                cleaned_label = clean_label(label)

                # Convert the image data to a PIL Image
                pil_image = Image.fromarray(np.uint8(image_data))

                # Save the image as a JPEG file with the cleaned label as the filename and numbering
                output_path = f"{output_folder}/{cleaned_label}_image_{i + 1}.jpg"
                pil_image.save(output_path, format='JPEG')

                print(f"Successfully saved image {i + 1} with label '{cleaned_label}' as {output_path}")

    except Exception as e:
        print(f"Error: {e}")


# h5_file_path = 'H5Demo/final_eye_data.h5'
# output_folder = 'NetworkDemo'
# h5_to_jpg_batch_with_labels(h5_file_path, output_folder)

import h5py

def check_color_format(h5_file_path):
    # Open the H5 file in read mode
    with h5py.File(h5_file_path, 'r') as h5_file:
        # Iterate over all images in the file
        for idx, image in enumerate(h5_file['images']):
            # Check the number of color channels
            num_channels = image.shape[-1]

            # Print the color format
            if num_channels == 1:
                print(f"Image {idx + 1}: Grayscale")
            elif num_channels == 3:
                print(f"Image {idx + 1}: RGB")
            else:
                print(f"Image {idx + 1}: Unknown color format (number of channels: {num_channels})")

# # Example usage:
# h5_file_path = 'H5Demo/g_eye_data.h5'
# check_color_format(h5_file_path)

import h5py
import numpy as np

# **** DOESNT WORK PROPERLY YET
import h5py
import numpy as np

def convert_rgb_to_grayscale(h5_file_path, output_h5_path):
    # Open the original H5 file in read mode
    with h5py.File(h5_file_path, 'r') as input_h5_file:
        # Read data from the original file
        images_rgb = input_h5_file['images'][:]
        labels = input_h5_file['labels'][:]

    # Convert RGB images to single-channel grayscale
    images_gray = np.mean(images_rgb, axis=-1, keepdims=True)

    # Create a new H5 file for the converted data
    with h5py.File(output_h5_path, 'w') as output_h5_file:
        # Create datasets in the new file
        output_h5_file.create_dataset('images', data=images_gray)
        output_h5_file.create_dataset('labels', data=labels)

    print(f"RGB images in '{h5_file_path}' converted to grayscale and saved to '{output_h5_path}'.")


# # Example usage:
# h5_file_path = 'H5Demo/final_eye_data.h5'
# output_h5_path = 'H5Demo/TEMP.h5'
# convert_rgb_to_grayscale(h5_file_path, output_h5_path)

if __name__ == "__main__":
    # Specify the input directory containing H5 files
    input_directory = 'H5Demo'

    # Specify the output file paths for training and testing H5 files
    output_train_file_path = 'H5Demo/TEMP_output_train.h5'
    output_test_file_path = 'H5Demo/TEMP_output_test.h5'

    # Process all H5 files in the input directory
    # process_all_h5_files(input_directory, output_train_file_path, output_test_file_path)

    print("Data split and saved successfully.")

    substring_to_label_mapping = {
        'northwest': 'North West',
        'northeast': 'North East',
        'southwest': 'South West',
        'southeast': 'South East',
        'north': 'North',
        'south': 'South',
        'west': 'West',
        'east': 'East',
        'center': 'Center'
    }

    combine_h5_files('H5Demo/final_eye_data.h5', 'H5Demo/image_collection2024-03-19_09-54-18.h5', 'H5Demo/TEMP_combined_data.h5')
    # check_color_format('H5Demo/TEMP_combined_data.h5')
    update_labels('H5Demo/TEMP_combined_data.h5', 'H5Demo/NEW_final_eye_data.h5', substring_to_label_mapping)
    # print_labels('H5Demo/final_eye_data.h5')

    # Remove all H5 files except 'final_eye_data.h5'
    for file_name in os.listdir(input_directory):
        if file_name.startswith('TEMP'):
            os.remove(os.path.join(input_directory, file_name))
            print(f"Removed {file_name}.")

    # readH5('H5Demo/final_eye_data.h5')