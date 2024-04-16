import csv
import os
import argparse
import importlib.metadata
from importlib.resources import files
import cv2
import commentjson
from ehdg_pupil_detector import ehdg_pupil_detector
from ehdg_tools.ehdg_buffers import TinyFillBuffer
import numpy as np


# This function is to get built-in config location with new library (from importlib.resources import files)
def get_config_location(module_name, config_file_name):
    config_dir = files(module_name).joinpath(config_file_name)
    return str(config_dir)


# This function is create the data dict by given data, frame info, event id and trial direction
def get_data_dict(data_input, frame_rate, frame_width, frame_height, direction_input=None):
    d_ts = float(data_input["timestamp"])
    record_timestamp = float(data_input["record_timestamp"])
    x_value = float(data_input["x_value"])
    y_value = float(data_input["y_value"])
    major_axis = float(data_input["major_axis"])
    minor_axis = float(data_input["minor_axis"])
    angle_of_pupil = float(data_input["angle_of_pupil"])
    diameter_of_pupil = float(data_input["diameter_of_pupil"])
    confidence = float(data_input["confidence"])
    ellipse_axis_a = major_axis
    ellipse_axis_b = minor_axis
    ellipse_angle = angle_of_pupil
    diameter = diameter_of_pupil
    frame_rate_input = float(frame_rate)
    sensor_time_stamp = d_ts
    temp_dict = {}
    temp_dict["x_value"] = x_value
    temp_dict["y_value"] = y_value
    temp_dict["x_nom"] = x_value / frame_width
    temp_dict["y_nom"] = 1 - (y_value / frame_height)
    temp_dict["record_timestamp"] = record_timestamp
    temp_dict["sensor_timestamp"] = sensor_time_stamp
    temp_dict["frame_rate"] = frame_rate_input
    if direction_input is not None:
        temp_dict["direction"] = direction_input
    temp_dict["confidence"] = confidence
    temp_dict["diameter"] = diameter
    temp_dict["ellipse_axis_a"] = ellipse_axis_a
    temp_dict["ellipse_axis_b"] = ellipse_axis_b
    temp_dict["ellipse_angle"] = ellipse_angle

    return temp_dict


# This function is to redetect with pupil detector by given detector and tiny fill buffer
def opm_detect(trial_video, out_folder, config_dict, buffer_length_input, direction_input=None):
    out_csv_dir = os.path.join(out_folder, "result.csv")
    out_video_dir = os.path.join(out_folder, "result.mp4")

    detector = ehdg_pupil_detector.Detector()
    buffer = TinyFillBuffer(buffer_length_input)
    detector.update_config(config_dict)
    updated_properties = detector.get_config_info()
    print("<Detector Properties>")
    for info in updated_properties:
        print(f"{info} : {updated_properties[info]}")

    cap = cv2.VideoCapture(trial_video)
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    print(f"frame_rate:{frame_rate}")
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(f"frame_width:{frame_width}")
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"frame_height:{frame_height}")
    frame_count = 0

    print("")
    print(f"Detecting {trial_video} with opm detector")

    if direction_input is None:
        column_header_array = ["x_value", "y_value", "x_nom", "y_nom",
                               "record_timestamp", "sensor_timestamp",
                               "frame_rate", "confidence", "diameter",
                               "ellipse_axis_a", "ellipse_axis_b",
                               "ellipse_angle"]
    else:
        column_header_array = ["x_value", "y_value", "x_nom", "y_nom",
                               "record_timestamp", "sensor_timestamp",
                               "frame_rate", "direction", "confidence", "diameter",
                               "ellipse_axis_a", "ellipse_axis_b",
                               "ellipse_angle"]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    v_writer = cv2.VideoWriter(out_video_dir, fourcc, frame_rate, (frame_width, frame_height))
    with open(out_csv_dir, mode='w', newline="") as destination_file:
        header_names = column_header_array
        csv_writer = csv.DictWriter(destination_file, fieldnames=header_names)
        csv_writer.writeheader()

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                frame_count += 1
                frame_time = frame_count / frame_rate
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                result = detector.detect(gray)
                d_ts = result["detector_timestamp"]
                center_of_pupil = result["center_of_pupil"]
                center_of_pupil_x = int(center_of_pupil[0])
                center_of_pupil_y = int(center_of_pupil[1])
                reversed_center_of_pupil = result["reversed_center_of_pupil"]
                x_value = float(reversed_center_of_pupil[0])
                y_value = float(reversed_center_of_pupil[1])
                axes_of_pupil = result["axes_of_pupil"]
                major_axis = float(axes_of_pupil[0])
                minor_axis = float(axes_of_pupil[1])
                angle_of_pupil = float(result["angle_of_pupil"])
                diameter_of_pupil = float(result["average_diameter_of_pupil"])
                confidence = 0 if x_value <= 0 and y_value <= 0 else 1

                center_of_pupil = (int(center_of_pupil_x), int(center_of_pupil_y))
                detected_frame = np.copy(frame)
                if center_of_pupil != (0, 0):
                    cv2.ellipse(
                        detected_frame,
                        center_of_pupil,
                        (int(major_axis), int(minor_axis)),
                        int(angle_of_pupil),
                        0, 360,  # start/end angle for drawing
                        (0, 0, 255)  # color (BGR): red
                    )
                v_writer.write(detected_frame)

                pupil_data = {}
                pupil_data["x_value"] = x_value
                pupil_data["y_value"] = y_value
                pupil_data["major_axis"] = major_axis
                pupil_data["minor_axis"] = minor_axis
                pupil_data["angle_of_pupil"] = angle_of_pupil
                pupil_data["diameter_of_pupil"] = diameter_of_pupil
                pupil_data["confidence"] = confidence
                pupil_data["timestamp"] = d_ts
                pupil_data["record_timestamp"] = frame_time
                return_data = buffer.add(pupil_data)
                if return_data is not None:
                    temp_dict = get_data_dict(return_data, frame_rate, frame_width, frame_height, direction_input)
                    csv_writer.writerow(temp_dict)
            else:
                got_first_data = False
                for return_data in buffer.buffer:
                    if not got_first_data:
                        got_first_data = True
                    else:
                        temp_dict = get_data_dict(return_data, frame_rate, frame_width, frame_height, direction_input)
                        csv_writer.writerow(temp_dict)
                destination_file.close()
                v_writer.release()
                print(f"Result folder dir: {out_folder}.")
                print(f"Result csv dir: {out_csv_dir}.")
                print(f"Result video dir: {out_video_dir}.")
                break


def main():
    parser = argparse.ArgumentParser(prog='opmtrack',
                                     description='OKNTRACK package.')
    opmtrack_version = importlib.metadata.version('ehdg_pupil_detector')
    parser.add_argument('--version', action='version', version=opmtrack_version),
    parser.add_argument("-i", dest="input_video", required=False, default=None,
                        metavar="input video")
    parser.add_argument("-o", dest="output_folder", required=False, default=None,
                        metavar="output folder")
    parser.add_argument("-c", dest="opm_config", required=False, default=None,
                        metavar="opm detector config")
    parser.add_argument("-d", dest="direction_input", required=False, default=None,
                        metavar="direction input")
    parser.add_argument("-bl", dest="buffer_length", required=False, default=None,
                        metavar="buffer length")

    args = parser.parse_args()
    input_video = args.input_video
    output_folder = args.output_folder
    opm_config = args.opm_config
    direction_input = args.direction_input
    buffer_length = args.buffer_length

    default_buffer_length = 7

    if not os.path.isfile(input_video):
        print(f"Input video is invalid.")
        print(f"Input video: {input_video} is invalid.")
        return

    input_video_name = os.path.basename(input_video)
    output_directory = str(input_video).replace(input_video_name, str(output_folder))
    if os.path.isfile(output_directory):
        print(f"Output directory must be directory not file.")
        print(f"Output directory: {output_directory}.")
        return
    else:
        if not os.path.isdir(output_directory):
            try:
                os.mkdir(output_directory)
                print(f"Output directory is created.")
                print(f"Output directory: {output_directory}.")
            except FileNotFoundError:
                print(f"Output directory cannot be created.")
                print(f"Output directory: {output_directory}.")
                return
            except OSError:
                print(f"Output directory cannot be created.")
                print(f"Output directory: {output_directory}.")
                print(f"Invalid output folder input.")
                print(f"Output folder input: {output_folder}.")
                return

    if opm_config is None:
        opm_config = get_config_location("ehdg_pupil_detector", "opm_detector_config.json")
        try:
            with open(opm_config) as opm_config_info:
                opm_config_dict = commentjson.load(opm_config_info)
        except FileNotFoundError:
            raise FileNotFoundError(f"Error opening built-in opm config file:{opm_config}!")
    else:
        try:
            with open(opm_config) as opm_config_info:
                opm_config_dict = commentjson.load(opm_config_info)
        except FileNotFoundError:
            raise FileNotFoundError(f"Error opening opm config file:{opm_config}!")

    if direction_input is not None:
        if str(direction_input).lower() == "right":
            direction_to_be_used = 1
        elif str(direction_input).lower() == "left":
            direction_to_be_used = -1
        else:
            try:
                direction_to_be_used = int(direction_input)
                if direction_to_be_used == 1 or direction_to_be_used == -1:
                    pass
                else:
                    raise ValueError(f"Invalid direction input {direction_input}.")
            except ValueError:
                raise ValueError(f"Invalid direction input {direction_input}.")
        print(f"There is direction input {direction_input}.")
        print(f"Therefore, direction: {direction_to_be_used} will be added to csv as a column.")
    else:
        direction_to_be_used = None

    if buffer_length is not None:
        try:
            buffer_length_to_be_used = int(buffer_length)
            print("There is buffer length input.")
            print(f"OPM detector will be using Tiny Fill Buffer with length:{buffer_length_to_be_used}.")
        except ValueError:
            buffer_length_to_be_used = default_buffer_length
            print(f"There is buffer length input but it is invalid: {buffer_length}.")
            print(f"OPM detector will be using Tiny Fill Buffer with default length:{buffer_length_to_be_used}.")
    else:
        buffer_length_to_be_used = default_buffer_length
        print("There is no buffer length input.")
        print(f"OPM detector will be using Tiny Fill Buffer with default length:{buffer_length_to_be_used}.")

    opm_detect(input_video, output_directory, opm_config_dict,
               buffer_length_to_be_used, direction_input=direction_to_be_used)
