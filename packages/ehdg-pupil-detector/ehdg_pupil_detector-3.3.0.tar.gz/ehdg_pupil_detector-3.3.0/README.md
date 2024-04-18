# EYE HEALTH DIAGNOSTIC GROUP'S PUPIL DETECTOR (ehdg_pupil_detector)
This is the python package libray pupil detector created by eye health diagnostic group.

## Installtion
```
pip install ehdg_pupil_detector
```

## Updating
```
pip install ehdg_pupil_detector -U
```

## Class Initialization and Attributes
### Class Initialization with defaults
```
from ehdg_pupil_detector import ehdg_pupil_detector

detector = ehdg_pupil_detector.Detector()
```
If you do not specify any argument, it will use default vales are as follows:  
1.  config  
    Default = None  
    If it is None then it will use following config parameters:  
    1.  min_circular_ratio = 0.9  
    2.  max_circular_ratio = 1.9  
    3.  ksize_height = 13  
    4.  ksize_width = 13  
    5.  min_binary_threshold = 20  
    6.  max_binary_threshold = 255  
    7.  reflection_fill_dilation_index = 25  
    8.  reflection_fill_square_dimension = 200  
2.  reflection_fill_color_index  
    Default = 0  (black)  
    0 means black and 255 means white in the gray scale.  
    It will cover the reflection on the pupil with black before using any other filters.  
3.  gaussian_blur  
    Default = True    
    It will use gaussian blur filter.  
5.  binary_fill_hole  
    Default = True   
    It will use binary fill hole function filter.  

### Class Initialization with custom values
```
from ehdg_pupil_detector import ehdg_pupil_detector

custom_config = {
    "min_circular_ratio": 0.9,
    "max_circular_ratio": 1.9,
    "ksize_height": 13,
    "ksize_width": 13,
    "min_binary_threshold": 20,
    "max_binary_threshold": 255,
    "reflection_fill_dilation_index": 25,
    "reflection_fill_square_dimension": 200
}

detector = ehdg_pupil_detector.Detector(config=custom_config, reflection_fill_color_index=0, gaussian_blur=True,
                                        binary_fill_hole=True)
```
The reflection_fill_color_index must be between 0 and 255.  
It is indexing how black or white gonna cover on the reflection of the pupil.  
0 index is blackest and 255 index is whitest.  
If you wanna turn off reflection fill function, add
```
reflection_fill_color_index=False
```
instead of
```
reflection_fill_color_index=0
```

### Class Function
#### get_config_info()
It is to check the current config information.
```
from src.ehdg_pupil_detector import ehdg_pupil_detector

custom_config = {
    "min_circular_ratio": 0.9,
    "max_circular_ratio": 1.9,
    "ksize_height": 13,
    "ksize_width": 13,
    "min_binary_threshold": 20,
    "max_binary_threshold": 255,
    "reflection_fill_dilation_index": 25,
    "reflection_fill_square_dimension": 200
}

detector = ehdg_pupil_detector.Detector(config=custom_config, reflection_fill_color_index=0, gaussian_blur=True,
                                        binary_fill_hole=True)

for info in detector.get_config_info():
    print(f"{info}: {detector.get_config_info()[info]}")

```
Output will be:
```
min_circular_ratio: 0.9
max_circular_ratio: 1.9
ksize_height: 13
ksize_width: 13
min_binary_threshold: 20
max_binary_threshold: 255
reflection_fill_dilation_index: 25
reflection_fill_square_dimension: 200
```

