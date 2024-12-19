# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 21:53:29 2024

@author: bingl
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_salt_and_pepper_noise(image, amount=0.02):
    noisy_image = image.copy()
    num_salt = np.ceil(amount * image.size * 0.5).astype(int)
    num_pepper = np.ceil(amount * image.size * 0.5).astype(int)

    # Add salt noise
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 255

    # Add pepper noise
    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 0

    return noisy_image

def apply_gaussian_filter(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def apply_median_filter(image):
    return cv2.medianBlur(image, 5)

def blur_image(image):
    return cv2.blur(image, (5, 5))

def resize_image(image, scale):
    width = int(image.shape[1] * scale / 100)
    height = int(image.shape[0] * scale / 100)
    return cv2.resize(image, (width, height))

def recolor_image(image):
    return cv2.applyColorMap(image, cv2.COLORMAP_JET)

def crop_image(image, x_start, y_start, width, height):
    return image[y_start:y_start + height, x_start:x_start + width]

def display_images(original, processed, title):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    if len(original.shape) == 3:
        plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    else:
        plt.imshow(original, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title(title)
    if len(processed.shape) == 3:
        plt.imshow(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB))
    else:
        plt.imshow(processed, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("Image Processing Program")
        print("1. Add Salt and Pepper Noise")
        print("2. Apply Gaussian Filter")
        print("3. Apply Median Filter")
        print("4. Blur Image")
        print("5. Resize Image")
        print("6. Recolor Image")
        print("7. Crop Image")
    
        choice = int(input("Enter your choice: "))
        image_path = r"C:\Users\bingl\Downloads\pexels-flowerstofox-27082077.jpg"
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
        if image is None:
            print("Error: Could not load image.")
            return
    
        if choice == 1:
            noisy_image = add_salt_and_pepper_noise(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
            display_images(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), noisy_image, "Salt and Pepper Noise")
        elif choice == 2:
            filtered_image = apply_gaussian_filter(image)
            display_images(image, filtered_image, "Gaussian Filter")
        elif choice == 3:
            filtered_image = apply_median_filter(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
            display_images(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), filtered_image, "Median Filter")
        elif choice == 4:
            blurred_image = blur_image(image)
            display_images(image, blurred_image, "Blurred Image")
        elif choice == 5:
            scale = int(input("Enter scale percentage (e.g., 50 for 50%): "))
            resized_image = resize_image(image, scale)
            display_images(image, resized_image, "Resized Image")
        elif choice == 6:
            recolored_image = recolor_image(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
            display_images(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), recolored_image, "Recolored Image")
        elif choice == 7:
            x_start = int(input("Enter x start: "))
            y_start = int(input("Enter y start: "))
            width = int(input("Enter width: "))
            height = int(input("Enter height: "))
            cropped_image = crop_image(image, x_start, y_start, width, height)
            display_images(image, cropped_image, "Cropped Image")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
  