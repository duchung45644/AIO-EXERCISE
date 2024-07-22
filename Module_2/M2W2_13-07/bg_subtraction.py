import cv2
import numpy as np


def compute_difference(bg_img, input_img):
    difference_single_channel = cv2.absdiff(bg_img, input_img)
    difference_single_channel = np.sum(difference_single_channel, axis=2) / 3
    difference_single_channel = difference_single_channel.astype(np.uint8)
    return difference_single_channel


def compute_binary_mask(difference_single_channel):
    mask_bin = np.where(difference_single_channel > 10, 255, 0)
    mask_bin = np.stack((mask_bin, )*3, axis=-1)
    return mask_bin


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(
        bg1_image,
        ob_image
    )

    binary_mask = compute_binary_mask(difference_single_channel)

    output = np.where(binary_mask == 255, ob_image, bg2_image)

    return output


if __name__ == '__main__':

    # read image
    new_bg_image = cv2.imread(r'./Module_2/M2W2_13-07/NewBackground.jpg')
    green_bg_image = cv2.imread(r'./Module_2/M2W2_13-07/GreenBackground.png')
    obj_image = cv2.imread(r'./Module_2/M2W2_13-07/Object.png')

    # resize image
    width = 640
    height = 480
    new_bg_image = cv2.resize(new_bg_image, (width, height))
    green_bg_image = cv2.resize(green_bg_image, (width, height))
    obj_image = cv2.resize(obj_image, (width, height))

    new_image = replace_background(green_bg_image, new_bg_image, obj_image)
    cv2.imshow('New Image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
