from tensorflow.keras.applications.vgg16 import preprocess_input
from patchify import patchify
import numpy as np

class ImageUtil:
    IMAGE_SIZE = (224, 224, 3)  # Define the image size as a class-level constant

    @staticmethod
    def get_patch_images(images:list):     
        patches = patchify(images, ImageUtil.IMAGE_SIZE, step=224)
        print(patches.shape)
        all_patches = []
        all_preprocessed_patches = []
        for i in range(patches.shape[0]):
            for j in range(patches.shape[1]):
                single_patch_img = patches[i, j, :, :]
                single_patch_img = patches[i, j, 0]
                all_patches.append(single_patch_img)
                all_preprocessed_patches.append(preprocess_input(single_patch_img))
        return np.array(all_patches),np.array(all_preprocessed_patches)
