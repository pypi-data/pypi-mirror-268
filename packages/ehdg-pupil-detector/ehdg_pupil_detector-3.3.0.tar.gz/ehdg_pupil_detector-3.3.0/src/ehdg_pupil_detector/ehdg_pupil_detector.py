import cv2
import numpy as np
from scipy import ndimage
import time


class Detector:
    def __init__(self, config=None, reflection_removal=True,
                 reflection_removal_lower_limit=0,
                 reflection_removal_upper_limit=255,
                 gaussian_blur=True, binary_fill_hole=True):
        if reflection_removal:
            self.reflection_fill = True
            self.reflection_removal_lower_limit = reflection_removal_lower_limit
            self.reflection_removal_upper_limit = reflection_removal_upper_limit
        else:
            self.reflection_fill = False
            self.reflection_removal_lower_limit = reflection_removal_lower_limit
            self.reflection_removal_upper_limit = reflection_removal_upper_limit
        if type(gaussian_blur) is bool:
            self.gaussian_blur = gaussian_blur
        else:
            self.gaussian_blur = True
            raise ValueError("Gaussian blur input must be boolean type.")
        if type(binary_fill_hole) is bool:
            self.binary_fill_hole = binary_fill_hole
        else:
            self.binary_fill_hole = True
            raise ValueError("Binary fill hole input must be boolean type.")
        if config is not None:
            if type(config) is not dict:
                raise ValueError("The config input must be dictionary type.")
            else:
                for key, value in config.items():
                    self.update_config_by_name(key, value)
        else:
            self.min_circular_ratio = 0.9
            self.max_circular_ratio = 1.9
            self.ksize_height = 13
            self.ksize_width = 13
            self.min_binary_threshold = 20
            self.max_binary_threshold = 255
            self.reflection_fill_dilation_index = 25
            self.reflection_fill_square_dimension = 200
            self.min_pupil_size = 50
            self.max_pupil_size = 150

    def update_config(self, config_dict_input):
        if type(config_dict_input) is not dict:
            raise ValueError("The config input must be dictionary type.")
        else:
            for key, value in config_dict_input.items():
                self.update_config_by_name(key, value)

    def update_config_by_name(self, attribute_name, attribute_value):
        if attribute_name == "min_circular_ratio":
            if type(attribute_value) is float or type(attribute_value) is int:
                self.min_circular_ratio = round(float(attribute_value), 1)
            else:
                raise ValueError(f"{attribute_name} must be float or integer.")
        elif attribute_name == "max_circular_ratio":
            if type(attribute_value) is float or type(attribute_value) is int:
                self.max_circular_ratio = round(float(attribute_value), 1)
            else:
                raise ValueError(f"{attribute_name} must be float or integer.")
        elif attribute_name == "ksize_height":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.ksize_height = attribute_value
        elif attribute_name == "ksize_width":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.ksize_width = attribute_value
        elif attribute_name == "min_binary_threshold":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.min_binary_threshold = attribute_value
        elif attribute_name == "max_binary_threshold":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.max_binary_threshold = attribute_value
        elif attribute_name == "reflection_fill_dilation_index":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.reflection_fill_dilation_index = attribute_value
        elif attribute_name == "reflection_fill_square_dimension":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.reflection_fill_square_dimension = attribute_value
        elif attribute_name == "min_pupil_size":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.min_pupil_size = attribute_value
        elif attribute_name == "max_pupil_size":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.max_pupil_size = attribute_value
        else:
            print(f"Detector attribute type {attribute_name} could not find in detector attributes.")

    def reflection_removal(self, removal_bool, lower_limit, upper_limit):
        if type(removal_bool) is bool:
            self.reflection_fill = removal_bool
            self.reflection_removal_lower_limit = lower_limit
            self.reflection_removal_upper_limit = upper_limit

    def gaussian_blur(self, gaussian_blur_bool):
        if type(gaussian_blur_bool) is bool:
            self.gaussian_blur = gaussian_blur_bool

    def binary_fill(self, binary_fill_bool):
        if type(binary_fill_bool) is bool:
            self.binary_fill_hole = binary_fill_bool

    def get_config_info(self):
        temp_dict = {}
        temp_dict["min_circular_ratio"] = self.min_circular_ratio
        temp_dict["max_circular_ratio"] = self.max_circular_ratio
        temp_dict["ksize_height"] = self.ksize_height
        temp_dict["ksize_width"] = self.ksize_width
        temp_dict["min_binary_threshold"] = self.min_binary_threshold
        temp_dict["max_binary_threshold"] = self.max_binary_threshold
        temp_dict["reflection_fill_dilation_index"] = self.reflection_fill_dilation_index
        temp_dict["reflection_fill_square_dimension"] = self.reflection_fill_square_dimension
        temp_dict["min_pupil_size"] = self.min_pupil_size
        temp_dict["max_pupil_size"] = self.max_pupil_size
        return temp_dict

    def detect(self, frame_input):
        frame_shape = frame_input.shape
        frame_width = frame_shape[1]
        frame_height = frame_shape[0]

        # Checking it is rbg/bgr image or not
        # If yes, then change to grayscale image
        if len(frame_shape) == 3:
            frame_input = cv2.cvtColor(frame_input, cv2.COLOR_BGR2GRAY)

        if self.reflection_fill:
            dilation_index = self.reflection_fill_dilation_index
            square_dimension = self.reflection_fill_square_dimension

            _, reflection_shape = cv2.threshold(frame_input,
                                                self.reflection_removal_lower_limit,
                                                self.reflection_removal_upper_limit,
                                                cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            kernel = np.ones((dilation_index, dilation_index), np.uint8)

            dilated_reflection_shape = cv2.dilate(reflection_shape, kernel, iterations=1)

            hh, ww = dilated_reflection_shape.shape
            # shsp = square height start point, shep = square height end point
            shsp = int(hh / 2 - (square_dimension / 2))
            shep = int(hh / 2 + (square_dimension / 2))

            # shsp = square width start point, shep = square width end point
            swsp = int(ww / 2 - (square_dimension / 2))
            swep = int(ww / 2 + (square_dimension / 2))

            cropped_dilated_reflection_shape = dilated_reflection_shape[shsp:shep, swsp:swep]

            cloned_black_frame = np.copy(frame_input)
            cloned_black_frame.fill(0)
            cloned_black_frame[shsp:shep, swsp:swep] = cropped_dilated_reflection_shape

            reflection_shape_index = list(zip(*np.where(cloned_black_frame == 255)))

            # fill black color in pupil reflection area
            for position in reflection_shape_index:
                frame_input[position[0], position[1]] = 0

        if self.gaussian_blur:
            frame_input = cv2.GaussianBlur(frame_input, (self.ksize_height, self.ksize_width), 0)

        _, black_white_filter_frame = cv2.threshold(frame_input,
                                                    self.min_binary_threshold,
                                                    self.max_binary_threshold,
                                                    cv2.THRESH_BINARY_INV)

        if self.binary_fill_hole:
            binary_filled_frame = ndimage.binary_fill_holes(black_white_filter_frame).astype(np.uint8)
            binary_filled_frame[binary_filled_frame == 1] = 255
            try:
                contours, _ = cv2.findContours(binary_filled_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            except ValueError:
                contours = None
        else:
            try:
                contours, _ = cv2.findContours(black_white_filter_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            except ValueError:
                contours = None

        if contours is not None:
            contours = sorted(contours, key=lambda xx: cv2.contourArea(xx), reverse=True)

            min_circular_ratio = self.min_circular_ratio
            max_circular_ratio = self.max_circular_ratio
            largest_dia = 0.0
            largest_con_ind = 0
            error_string = None
            center_of_pupil = (0.0, 0.0)
            reversed_center_of_pupil = (0.0, 0.0)
            axes_of_pupil = (0.0, 0.0)
            average_diameter_of_pupil = 0.0
            angle_of_pupil = 0.0
            circular_con_count = 0
            for ind, cc in enumerate(contours):
                try:
                    cc = cv2.convexHull(cc)
                    (x, y), (MA, ma), angle = cv2.fitEllipse(cc)
                    con_ratio = ma / MA
                    # print(con_ratio)
                    if min_circular_ratio <= con_ratio <= max_circular_ratio:
                        avg_dia = (ma + MA) / 2
                        if avg_dia >= largest_dia:
                            largest_dia = avg_dia
                            largest_con_ind = ind
                            center_of_pupil = (float(x), float(y))
                            reversed_center_of_pupil = (float(frame_width - x), float(frame_height - y))
                            axes_of_pupil = (float(MA / 2), float(ma / 2))
                            average_diameter_of_pupil = avg_dia
                            angle_of_pupil = float(angle)
                            circular_con_count += 1
                except Exception as e:
                    error_string = str(e)
                    pass

            try:
                largest_circle = contours[largest_con_ind]
            except IndexError:
                largest_circle = None

            if largest_circle is not None:
                if self.min_pupil_size <= average_diameter_of_pupil <= self.max_pupil_size:
                    temp_dict = {}
                    temp_dict["detector_timestamp"] = time.time()
                    temp_dict["center_of_pupil"] = center_of_pupil
                    temp_dict["reversed_center_of_pupil"] = reversed_center_of_pupil
                    temp_dict["axes_of_pupil"] = axes_of_pupil
                    temp_dict["angle_of_pupil"] = angle_of_pupil
                    temp_dict["average_diameter_of_pupil"] = average_diameter_of_pupil
                    return temp_dict
                else:
                    temp_dict = {}
                    temp_dict["detector_timestamp"] = time.time()
                    temp_dict["center_of_pupil"] = (0.0, 0.0)
                    temp_dict["reversed_center_of_pupil"] = (0.0, 0.0)
                    temp_dict["axes_of_pupil"] = (0.0, 0.0)
                    temp_dict["angle_of_pupil"] = 0.0
                    temp_dict["average_diameter_of_pupil"] = 0.0
                    return temp_dict
            else:
                temp_dict = {}
                temp_dict["detector_timestamp"] = time.time()
                temp_dict["center_of_pupil"] = (0.0, 0.0)
                temp_dict["reversed_center_of_pupil"] = (0.0, 0.0)
                temp_dict["axes_of_pupil"] = (0.0, 0.0)
                temp_dict["angle_of_pupil"] = 0.0
                temp_dict["average_diameter_of_pupil"] = 0.0
                return temp_dict
        else:
            temp_dict = {}
            temp_dict["detector_timestamp"] = time.time()
            temp_dict["center_of_pupil"] = (0.0, 0.0)
            temp_dict["reversed_center_of_pupil"] = (0.0, 0.0)
            temp_dict["axes_of_pupil"] = (0.0, 0.0)
            temp_dict["angle_of_pupil"] = 0.0
            temp_dict["average_diameter_of_pupil"] = 0.0
            return temp_dict


class PimDetector:
    def __init__(self, config=None, gaussian_blur=True, binary_fill_hole=True):
        if type(gaussian_blur) is bool:
            self.gaussian_blur = gaussian_blur
        else:
            self.gaussian_blur = True
            raise ValueError("Gaussian blur input must be boolean type.")
        if type(binary_fill_hole) is bool:
            self.binary_fill_hole = binary_fill_hole
        else:
            self.binary_fill_hole = True
            raise ValueError("Binary fill hole input must be boolean type.")
        if config is not None:
            if type(config) is not dict:
                raise ValueError("The config input must be dictionary type.")
            else:
                for key, value in config.items():
                    self.update_config_by_name(key, value)
        else:
            self.ksize_height = 13
            self.ksize_width = 13
            self.min_binary_threshold = 30
            self.max_binary_threshold = 255
            # self.min_pupil_size = 50
            # self.max_pupil_size = 150
            self.roi_start_point_x = 30
            self.roi_start_point_y = 40
            self.roi_width = 132
            self.roi_height = 140

    def update_config(self, config_dict_input):
        if type(config_dict_input) is not dict:
            raise ValueError("The config input must be dictionary type.")
        else:
            for key, value in config_dict_input.items():
                self.update_config_by_name(key, value)

    def update_config_by_name(self, attribute_name, attribute_value):
        if attribute_name == "ksize_height":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.ksize_height = attribute_value
        elif attribute_name == "ksize_width":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.ksize_width = attribute_value
        elif attribute_name == "min_binary_threshold":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.min_binary_threshold = attribute_value
        elif attribute_name == "max_binary_threshold":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.max_binary_threshold = attribute_value
        # elif attribute_name == "min_pupil_size":
        #     if type(attribute_value) is not int:
        #         raise ValueError(f"{attribute_name} must be integer.")
        #     else:
        #         self.min_pupil_size = attribute_value
        # elif attribute_name == "max_pupil_size":
        #     if type(attribute_value) is not int:
        #         raise ValueError(f"{attribute_name} must be integer.")
        #     else:
        #         self.max_pupil_size = attribute_value
        elif attribute_name == "roi_start_point_x":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.roi_start_point_x = attribute_value
        elif attribute_name == "roi_start_point_y":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.roi_start_point_y = attribute_value
        elif attribute_name == "roi_width":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.roi_width = attribute_value
        elif attribute_name == "roi_height":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.roi_height = attribute_value
        else:
            print(f"Detector attribute type {attribute_name} could not find in detector attributes.")

    def get_config_info(self):
        temp_dict = {}
        temp_dict["ksize_height"] = self.ksize_height
        temp_dict["ksize_width"] = self.ksize_width
        temp_dict["min_binary_threshold"] = self.min_binary_threshold
        temp_dict["max_binary_threshold"] = self.max_binary_threshold
        # temp_dict["min_pupil_size"] = self.min_pupil_size
        # temp_dict["max_pupil_size"] = self.max_pupil_size
        temp_dict["roi_start_point_x"] = self.roi_start_point_x
        temp_dict["roi_start_point_y"] = self.roi_start_point_y
        temp_dict["roi_width"] = self.roi_width
        temp_dict["roi_height"] = self.roi_height
        return temp_dict

    def detect(self, frame_input):
        frame_input = np.copy(frame_input)
        frame_shape = frame_input.shape
        frame_width = frame_shape[1]
        frame_height = frame_shape[0]

        # Checking it is rbg/bgr image or not
        # If yes, then change to grayscale image
        if len(frame_shape) == 3:
            frame_input = cv2.cvtColor(frame_input, cv2.COLOR_BGR2GRAY)

        if self.gaussian_blur:
            frame_input = cv2.GaussianBlur(frame_input, (self.ksize_height, self.ksize_width), 0)

        white_background_image = np.copy(frame_input)
        white_background_image.fill(255)
        x = int(self.roi_start_point_x)
        y = int(self.roi_start_point_y)
        w = int(self.roi_width)
        h = int(self.roi_height)
        cropped_image = frame_input[y:(y + h), x:(x + w)]
        white_background_image[y:(y + h), x:(x + w)] = cropped_image
        frame_input = white_background_image

        _, black_white_filter_frame = cv2.threshold(frame_input,
                                                    self.min_binary_threshold,
                                                    self.max_binary_threshold,
                                                    cv2.THRESH_BINARY_INV)

        if self.binary_fill_hole:
            binary_filled_frame = ndimage.binary_fill_holes(black_white_filter_frame).astype(np.uint8)
            binary_filled_frame[binary_filled_frame == 1] = 255
            try:
                contours, _ = cv2.findContours(binary_filled_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            except ValueError:
                contours = None
        else:
            try:
                contours, _ = cv2.findContours(black_white_filter_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            except ValueError:
                contours = None

        ch_circles = []
        if contours is not None:
            contours = sorted(contours, key=lambda xx: cv2.contourArea(xx), reverse=True)

            largest_dia = 0.0
            largest_con_ind = 0
            error_string = None
            center_of_pupil = (0.0, 0.0)
            reversed_center_of_pupil = (0.0, 0.0)
            axes_of_pupil = (0.0, 0.0)
            average_diameter_of_pupil = 0.0
            angle_of_pupil = 0.0
            circular_con_count = 0

            for ind, cc in enumerate(contours):
                try:
                    cc = cv2.convexHull(cc)

                    (x, y), (MA, ma), angle = cv2.fitEllipse(cc)
                    avg_dia = (ma + MA) / 2
                    if avg_dia >= largest_dia:
                        ch_circles.append(cc)
                        largest_dia = avg_dia
                        largest_con_ind = ind
                        center_of_pupil = (float(x), float(y))
                        reversed_center_of_pupil = (float(frame_width - x), float(frame_height - y))
                        axes_of_pupil = (float(MA / 2), float(ma / 2))
                        average_diameter_of_pupil = avg_dia
                        angle_of_pupil = float(angle)
                        circular_con_count += 1
                except Exception as e:
                    error_string = str(e)
                    pass

            try:
                largest_circle = contours[largest_con_ind]
            except IndexError:
                largest_circle = None

            if largest_circle is not None:
                temp_dict = {}
                temp_dict["detector_timestamp"] = time.time()
                temp_dict["center_of_pupil"] = center_of_pupil
                temp_dict["reversed_center_of_pupil"] = reversed_center_of_pupil
                temp_dict["axes_of_pupil"] = axes_of_pupil
                temp_dict["angle_of_pupil"] = angle_of_pupil
                temp_dict["average_diameter_of_pupil"] = average_diameter_of_pupil
                return temp_dict
            else:
                temp_dict = {}
                temp_dict["detector_timestamp"] = time.time()
                temp_dict["center_of_pupil"] = (0.0, 0.0)
                temp_dict["reversed_center_of_pupil"] = (0.0, 0.0)
                temp_dict["axes_of_pupil"] = (0.0, 0.0)
                temp_dict["angle_of_pupil"] = 0.0
                temp_dict["average_diameter_of_pupil"] = 0.0
                return temp_dict
        else:
            temp_dict = {}
            temp_dict["detector_timestamp"] = time.time()
            temp_dict["center_of_pupil"] = (0.0, 0.0)
            temp_dict["reversed_center_of_pupil"] = (0.0, 0.0)
            temp_dict["axes_of_pupil"] = (0.0, 0.0)
            temp_dict["angle_of_pupil"] = 0.0
            temp_dict["average_diameter_of_pupil"] = 0.0
            return temp_dict
