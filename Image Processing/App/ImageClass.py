import math
import cv2
import numpy as np
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from skimage.color import *
from PIL import Image
from skimage.segmentation import felzenszwalb
import heapq
from collections import defaultdict

class ImageClass:
    def __init__(self, image):
        self.image = image

    # Binarisation

    def negatif(self,img):
        return (255-img)

    def Otsu(self):
        pixel_number = self.image.shape[0] * self.image.shape[1]
        mean_weigth = 1.0 / pixel_number
        his, bins = np.histogram(self.image, np.arange(0, 257))
        final_thresh = -1
        final_value = -1
        intensity_arr = np.arange(256)
        # This goes from 1 to 254 uint8 range (Pretty sure wont be those values)
        for t in bins[1:-1]:
            pcb = np.sum(his[:t])
            pcf = np.sum(his[t:])
            Wb = pcb * mean_weigth
            Wf = pcf * mean_weigth

            mub = np.sum(intensity_arr[:t] * his[:t]) / float(pcb)
            muf = np.sum(intensity_arr[t:] * his[t:]) / float(pcf)
            # print mub, muf
            value = Wb * Wf * (mub - muf) ** 2

            if value > final_value:
                final_thresh = t
                final_value = value
        final_img = self.image.copy()
        final_img[self.image > final_thresh] = 255
        final_img[self.image < final_thresh] = 0
        return final_img



    def rotate_image(self, angle):
        # Get the image size
        # No that's not an error - NumPy stores image matricies backwards
        image_size = (self.image.shape[1], self.image.shape[0])
        image_center = tuple(np.array(image_size) / 2)

        # Convert the OpenCV 3x2 rotation matrix to 3x3
        rot_mat = np.vstack(
            [cv2.getRotationMatrix2D(image_center, angle, 1.0), [0, 0, 1]]
        )

        rot_mat_notranslate = np.matrix(rot_mat[0:2, 0:2])

        # Shorthand for below calcs
        image_w2 = image_size[0] * 0.5
        image_h2 = image_size[1] * 0.5

        # Obtain the rotated coordinates of the image corners
        rotated_coords = [
            (np.array([-image_w2, image_h2]) * rot_mat_notranslate).A[0],
            (np.array([image_w2, image_h2]) * rot_mat_notranslate).A[0],
            (np.array([-image_w2, -image_h2]) * rot_mat_notranslate).A[0],
            (np.array([image_w2, -image_h2]) * rot_mat_notranslate).A[0]
        ]

        # Find the size of the new image
        x_coords = [pt[0] for pt in rotated_coords]
        x_pos = [x for x in x_coords if x > 0]
        x_neg = [x for x in x_coords if x < 0]

        y_coords = [pt[1] for pt in rotated_coords]
        y_pos = [y for y in y_coords if y > 0]
        y_neg = [y for y in y_coords if y < 0]

        right_bound = max(x_pos)
        left_bound = min(x_neg)
        top_bound = max(y_pos)
        bot_bound = min(y_neg)

        new_w = int(abs(right_bound - left_bound))
        new_h = int(abs(top_bound - bot_bound))

        # We require a translation matrix to keep the image centred
        trans_mat = np.matrix([
            [1, 0, int(new_w * 0.5 - image_w2)],
            [0, 1, int(new_h * 0.5 - image_h2)],
            [0, 0, 1]
        ])

        # Compute the tranform for the combined rotation and translation
        affine_mat = (np.matrix(trans_mat) * np.matrix(rot_mat))[0:2, :]

        # Apply the transform
        result = cv2.warpAffine(
            self.image,
            affine_mat,
            (new_w, new_h),
            flags=cv2.INTER_LINEAR
        )
        img = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        return result



    def etire(self):
        self.image = cv2.cvtColor(self.image,cv2.COLOR_RGB2GRAY)
        MaxV = np.max(self.image)
        MinV = np.min(self.image)
        Y = np.zeros_like(self.image)
        m = self.image.shape

        for i in range(m[0]):
            for j in range(m[1]):
                Y[i, j] = (255 / (MaxV - MinV) * (self.image[i, j] - MinV))
        return Y
    


    def split_merge(self,img,min_size=100, max_stddev=20.0):

        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        height, width, _ = img.shape
        regions = [[(0, 0), (height, width)]]
        for i, region in enumerate(regions):
            if region[1][0] - region[0][0] < 2 or region[1][1] - region[0][1] < 2:
                continue
            mask = np.zeros((height, width), np.uint8)
            mask[region[0][0]:region[1][0], region[0][1]:region[1][1]] = 255
            mean, stddev = cv2.meanStdDev(lab, mask=mask)
            if stddev[0] > max_stddev or stddev[1] > max_stddev or stddev[2] > max_stddev:
                x, y, w, h = cv2.boundingRect(mask)
                regions.append([(region[0][0], region[0][1]), (y+h, x+w)])
                regions.append([(region[0][0], x+w), (y+h, region[1][1])])
                regions.append([(y+h, region[0][1]), (region[1][0], x+w)])
                regions.append([(y+h, x+w), (region[1][0], region[1][1])])
        output = np.zeros_like(img)
        for region in regions:
            if region[1][0] - region[0][0] < min_size or region[1][1] - region[0][1] < min_size:
                continue
            mask = np.zeros((height, width), np.uint8)
            mask[region[0][0]:region[1][0], region[0][1]:region[1][1]] = 255
            output_mask = np.zeros((height+2, width+2), np.uint8)
            cv2.floodFill(output_mask, mask, (0, 0), 255)
            output_mask = output_mask[1:height+1, 1:width+1]
            mean = cv2.mean(img, mask=output_mask)
            output[mask != 0] = mean
        return output





    def huffman_encode(self, arr):
        freq = {}
        arr = arr.tolist()

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if tuple(arr[i][j]) not in freq:
                    freq[tuple(arr[i][j])] = 1
                else:
                    freq[tuple(arr[i][j])] += 1


        heap = [[wt, [sym, ""]] for sym, wt in freq.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

        codes = {}
        for pair in heap[0][1:]:
            codes[pair[0]] = pair[1]

        encoded = ""
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                encoded += codes[tuple(arr[i][j])]

        pad_len = (8 - len(encoded) % 8) % 8
        encoded += '0' * pad_len

        encoded_bytes = bytearray()
        for i in range(0, len(encoded), 8):
            encoded_byte = int(encoded[i:i + 8], 2)
            encoded_bytes.append(encoded_byte)

        return encoded_bytes, codes

    def huffman_decode(self, encoded_bytes, codes):
        encoded_bits = ""
        for byte in encoded_bytes:
            encoded_bits += "{0:08b}".format(byte)

        pad_len = encoded_bits[-8:]
        if pad_len != '00000000':
            encoded_bits = encoded_bits[:-int(pad_len, 2)]

        decoded = []
        code = ""
        for bit in encoded_bits:
            code += bit
            if code in codes.values():
                sym = list(codes.keys())[list(codes.values()).index(code)]
                decoded.append(sym)
                code = ""

        return decoded