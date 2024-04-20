########
# 
# visualization_utils.py
# 
# Core rendering functions shared across visualization scripts
#
########

#%% Constants and imports

import time
import numpy as np
import requests
import os

from io import BytesIO
from typing import Union
from PIL import Image, ImageFile, ImageFont, ImageDraw
from multiprocessing.pool import ThreadPool
from multiprocessing.pool import Pool
from tqdm import tqdm
from functools import partial

from md_utils.path_utils import find_images

from data_management.annotations import annotation_constants
from data_management.annotations.annotation_constants import (
    detector_bbox_category_id_to_name)

ImageFile.LOAD_TRUNCATED_IMAGES = True

# Maps EXIF standard rotation identifiers to degrees.  The value "1" indicates no
# rotation; this will be ignored.  The values 2, 4, 5, and 7 are mirrored rotations,
# which are not supported (we'll assert() on this when we apply rotations).
EXIF_IMAGE_NO_ROTATION = 1
EXIF_IMAGE_ROTATIONS = {
    3: 180,
    6: 270,
    8: 90
}

TEXTALIGN_LEFT = 0
TEXTALIGN_RIGHT = 1

# Convert category ID from int to str
DEFAULT_DETECTOR_LABEL_MAP = {
    str(k): v for k, v in detector_bbox_category_id_to_name.items()
}

# Retry on blob storage read failures
n_retries = 10
retry_sleep_time = 0.01
error_names_for_retry = ['ConnectionError']

DEFAULT_BOX_THICKNESS = 4
DEFAULT_LABEL_FONT_SIZE = 16


#%% Functions

def open_image(input_file: Union[str, BytesIO], ignore_exif_rotation=False) -> Image:
    """
    Opens an image in binary format using PIL.Image and converts to RGB mode.
    
    Supports local files or URLs.

    This operation is lazy; image will not be actually loaded until the first
    operation that needs to load it (for example, resizing), so file opening
    errors can show up later.  load_image() is the non-lazy version of this function.

    Args:
        input_file: str or BytesIO, either a path to an image file (anything
            that PIL can open), or an image as a stream of bytes

    Returns:
        A PIL image object in RGB mode
    """
    
    if (isinstance(input_file, str)
            and input_file.startswith(('http://', 'https://'))):
        try:
            response = requests.get(input_file)
        except Exception as e:
            print(f'Error retrieving image {input_file}: {e}')
            success = False
            if e.__class__.__name__ in error_names_for_retry:
                for i_retry in range(0,n_retries):
                    try:
                        time.sleep(retry_sleep_time)
                        response = requests.get(input_file)        
                    except Exception as e:
                        print(f'Error retrieving image {input_file} on retry {i_retry}: {e}')
                        continue
                    print('Succeeded on retry {}'.format(i_retry))
                    success = True
                    break
            if not success:
                raise
        try:
            image = Image.open(BytesIO(response.content))
        except Exception as e:
            print(f'Error opening image {input_file}: {e}')
            raise

    else:
        image = Image.open(input_file)
    if image.mode not in ('RGBA', 'RGB', 'L', 'I;16'):
        raise AttributeError(
            f'Image {input_file} uses unsupported mode {image.mode}')
    if image.mode == 'RGBA' or image.mode == 'L':
        # PIL.Image.convert() returns a converted copy of this image
        image = image.convert(mode='RGB')

    if not ignore_exif_rotation:
        # Alter orientation as needed according to EXIF tag 0x112 (274) for Orientation
        #
        # https://gist.github.com/dangtrinhnt/a577ece4cbe5364aad28
        # https://www.media.mit.edu/pia/Research/deepview/exif.html
        #
        try:
            exif = image._getexif()
            orientation: int = exif.get(274, None)  
            if (orientation is not None) and (orientation != EXIF_IMAGE_NO_ROTATION):
                assert orientation in EXIF_IMAGE_ROTATIONS, \
                    'Mirrored rotations are not supported'
                image = image.rotate(EXIF_IMAGE_ROTATIONS[orientation], expand=True)  
        except Exception:
            pass

    return image

# ...def open_image(...)


def exif_preserving_save(pil_image,output_file,quality='keep',default_quality=85,verbose=False):
    """
    Save [pil_image] to [output_file], making a moderate attempt to preserve EXIF
    data and JPEG quality.  Neither is guaranteed.
    
    Also see:
    
    https://discuss.dizzycoding.com/determining-jpg-quality-in-python-pil/
     
    ...for more ways to preserve jpeg quality if quality='keep' doesn't do the trick.

    The "quality" parameter should be "keep" (default), or an integer from 0 to 100. 
    This is only used if PIL thinks the the source image is a JPEG.  If you load a JPEG
    and resize it in memory, for example, it's no longer a JPEG.
    
    'default_quality' is used when quality == 'keep' and we are saving a non-JPEG source.
    'keep' is only supported for JPEG sources.
    """
    
    # Read EXIF metadata
    exif = pil_image.info['exif'] if ('exif' in pil_image.info) else None
    
    # Quality preservation is only supported for JPEG sources.
    if pil_image.format != "JPEG":
        if quality == 'keep':
            if verbose:
                print('Warning: quality "keep" passed when saving a non-JPEG source (during save to {})'.format(
                    output_file))
            quality = default_quality            
    
    # Some output formats don't support the quality parameter, so we try once with, 
    # and once without.  This is a horrible cascade of if's, but it's a consequence of
    # the fact that "None" is not supported for either "exif" or "quality".
        
    try:
        
        if exif is not None:
            pil_image.save(output_file, exif=exif, quality=quality)
        else:
            pil_image.save(output_file, quality=quality)
                
    except Exception:
        
        if verbose:
            print('Warning: failed to write {}, trying again without quality parameter'.format(output_file))
        if exif is not None:
            pil_image.save(output_file, exif=exif)            
        else:
            pil_image.save(output_file)
            
# ...def exif_preserving_save(...)


def load_image(input_file: Union[str, BytesIO], ignore_exif_rotation=False) -> Image:
    """
    Loads the image at input_file as a PIL Image into memory.

    Image.open() used in open_image() is lazy and errors will occur downstream
    if not explicitly loaded.

    Args:
        input_file: str or BytesIO, either a path to an image file (anything
            that PIL can open), or an image as a stream of bytes

    Returns: PIL.Image.Image, in RGB mode
    """
    
    image = open_image(input_file, ignore_exif_rotation=ignore_exif_rotation)
    image.load()
    return image


def resize_image(image, target_width, target_height=-1, output_file=None,
                 no_enlarge_width=False, verbose=False, quality='keep'):
    """
    Resizes a PIL image object to the specified width and height; does not resize
    in place. If either width or height are -1, resizes with aspect ratio preservation.
    
    None is equivalent to -1 for target_width and target_height.
    
    [image] can be a PIL image or a filename.
    
    If target_width and target_height are both -1, does not modify the image, but 
    will write to output_file if supplied.
    
    If no_enlarge_width is True, and the target width is larger than the original
    image width, does not modify the image, but will write to output_file if supplied.
    
    'quality' is passed to exif_preserving_save, see docs there.
    """

    image_fn = 'in_memory'
    if isinstance(image,str):
        image_fn = image
        image = load_image(image)
        
    if target_width is None:
        target_width = -1
    
    if target_height is None:
        target_height = -1
    
    resize_required = True
        
    # No resize was requested, this is always a no-op
    if target_width == -1 and target_height == -1:
        
        resize_required = False
    
    # Does either dimension need to scale according to the other?
    elif target_width == -1 or target_height == -1:

        # Aspect ratio as width over height
        # ar = w / h
        aspect_ratio = image.size[0] / image.size[1]

        if target_width != -1:
            # h = w / ar
            target_height = int(target_width / aspect_ratio)
        else:
            # w = ar * h
            target_width = int(aspect_ratio * target_height)
    
    # If we're not enlarging images and this would be an enlarge operation
    if (no_enlarge_width) and (target_width > image.size[0]):
        
        if verbose:
            print('Bypassing image enlarge for {} --> {}'.format(
                image_fn,str(output_file)))
        resize_required = False
        
    # If the target size is the same as the original size
    if (target_width == image.size[0]) and (target_height == image.size[1]):
        
        resize_required = False    
    
    if not resize_required:
        
        if output_file is not None:
            if verbose:
                print('No resize required for resize {} --> {}'.format(
                    image_fn,str(output_file)))
            exif_preserving_save(image,output_file,quality=quality,verbose=verbose)
        return image
    
    assert target_width > 0 and target_height > 0, \
        'Invalid image resize target {},{}'.format(target_width,target_height)
        
    # The antialiasing parameter changed between Pillow versions 9 and 10, and for a bit, 
    # I'd like to support both.
    try:
        resized_image = image.resize((target_width, target_height), Image.ANTIALIAS)
    except:
        resized_image = image.resize((target_width, target_height), Image.Resampling.LANCZOS)
        
    if output_file is not None:
        exif_preserving_save(resized_image,output_file,quality=quality,verbose=verbose)
        
    return resized_image

# ...def resize_image(...)


DEFAULT_COLORS = [
    'AliceBlue', 'Red', 'RoyalBlue', 'Gold', 'Chartreuse', 'Aqua', 'Azure',
    'Beige', 'Bisque', 'BlanchedAlmond', 'BlueViolet', 'BurlyWood', 'CadetBlue',
    'AntiqueWhite', 'Chocolate', 'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson',
    'Cyan', 'DarkCyan', 'DarkGoldenRod', 'DarkGrey', 'DarkKhaki', 'DarkOrange',
    'DarkOrchid', 'DarkSalmon', 'DarkSeaGreen', 'DarkTurquoise', 'DarkViolet',
    'DeepPink', 'DeepSkyBlue', 'DodgerBlue', 'FireBrick', 'FloralWhite',
    'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite', 'GoldenRod',
    'Salmon', 'Tan', 'HoneyDew', 'HotPink', 'IndianRed', 'Ivory', 'Khaki',
    'Lavender', 'LavenderBlush', 'LawnGreen', 'LemonChiffon', 'LightBlue',
    'LightCoral', 'LightCyan', 'LightGoldenRodYellow', 'LightGray', 'LightGrey',
    'LightGreen', 'LightPink', 'LightSalmon', 'LightSeaGreen', 'LightSkyBlue',
    'LightSlateGray', 'LightSlateGrey', 'LightSteelBlue', 'LightYellow', 'Lime',
    'LimeGreen', 'Linen', 'Magenta', 'MediumAquaMarine', 'MediumOrchid',
    'MediumPurple', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen',
    'MediumTurquoise', 'MediumVioletRed', 'MintCream', 'MistyRose', 'Moccasin',
    'NavajoWhite', 'OldLace', 'Olive', 'OliveDrab', 'Orange', 'OrangeRed',
    'Orchid', 'PaleGoldenRod', 'PaleGreen', 'PaleTurquoise', 'PaleVioletRed',
    'PapayaWhip', 'PeachPuff', 'Peru', 'Pink', 'Plum', 'PowderBlue', 'Purple',
    'RosyBrown', 'Aquamarine', 'SaddleBrown', 'Green', 'SandyBrown',
    'SeaGreen', 'SeaShell', 'Sienna', 'Silver', 'SkyBlue', 'SlateBlue',
    'SlateGray', 'SlateGrey', 'Snow', 'SpringGreen', 'SteelBlue', 'GreenYellow',
    'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White',
    'WhiteSmoke', 'Yellow', 'YellowGreen'
]


def crop_image(detections, image, confidence_threshold=0.15, expansion=0):
    """
    Crops detections above *confidence_threshold* from the PIL image *image*,
    returning a list of PIL images.

    *detections* should be a list of dictionaries with keys 'conf' and 'bbox';
    see bbox format description below.  Normalized, [x,y,w,h], upper-left-origin.

    *expansion* specifies a number of pixels to include on each side of the box.
    """

    ret_images = []

    for detection in detections:

        score = float(detection['conf'])

        if score >= confidence_threshold:

            x1, y1, w_box, h_box = detection['bbox']
            ymin,xmin,ymax,xmax = y1, x1, y1 + h_box, x1 + w_box

            # Convert to pixels so we can use the PIL crop() function
            im_width, im_height = image.size
            (left, right, top, bottom) = (xmin * im_width, xmax * im_width,
                                          ymin * im_height, ymax * im_height)

            if expansion > 0:
                left -= expansion
                right += expansion
                top -= expansion
                bottom += expansion

            # PIL's crop() does surprising things if you provide values outside of
            # the image, clip inputs
            left = max(left,0); right = max(right,0)
            top = max(top,0); bottom = max(bottom,0)

            left = min(left,im_width-1); right = min(right,im_width-1)
            top = min(top,im_height-1); bottom = min(bottom,im_height-1)

            ret_images.append(image.crop((left, top, right, bottom)))

        # ...if this detection is above threshold

    # ...for each detection

    return ret_images


def render_detection_bounding_boxes(detections, image,
                                    label_map={}, 
                                    classification_label_map=None, 
                                    confidence_threshold=0.15, thickness=DEFAULT_BOX_THICKNESS, expansion=0,
                                    classification_confidence_threshold=0.3,
                                    max_classifications=3,
                                    colormap=DEFAULT_COLORS,
                                    textalign=TEXTALIGN_LEFT,
                                    label_font_size=DEFAULT_LABEL_FONT_SIZE,
                                    custom_strings=None):
    """
    Renders bounding boxes, label, and confidence on an image if confidence is above the threshold.

    Boxes are in the format that's output from the batch processing API.

    Renders classification labels if present.

    Args:

        detections: detections on the image, example content:
            [
                {
                    "category": "2",
                    "conf": 0.996,
                    "bbox": [
                        0.0,
                        0.2762,
                        0.1234,
                        0.2458
                    ]
                }
            ]

            ...where the bbox coordinates are [x, y, box_width, box_height].

            (0, 0) is the upper-left.  Coordinates are normalized.

            Supports classification results, if *detections* has the format
            [
                {
                    "category": "2",
                    "conf": 0.996,
                    "bbox": [
                        0.0,
                        0.2762,
                        0.1234,
                        0.2458
                    ]
                    "classifications": [
                        ["3", 0.901],
                        ["1", 0.071],
                        ["4", 0.025]
                    ]
                }
            ]

        image: PIL.Image object

        label_map: optional, mapping the numerical label to a string name. The type of the numerical label
            (default string) needs to be consistent with the keys in label_map; no casting is carried out.
            If this is None, no labels are shown (not even numbers and confidence values).  If you want
            category numbers and confidence values without class labels, use {}.

        classification_label_map: optional, mapping of the string class labels to the actual class names.
            The type of the numerical label (default string) needs to be consistent with the keys in
            label_map; no casting is carried out.  If this is None, no classification labels are shown.

        confidence_threshold: optional, threshold above which boxes are rendered.  Can also be a dictionary
        mapping category IDs to thresholds.
        
        thickness: line thickness in pixels. Default value is 4.
        
        expansion: number of pixels to expand bounding boxes on each side.  Default is 0.
        
        classification_confidence_threshold: confidence above which classification result is retained.
        
        max_classifications: maximum number of classification results retained for one image.
        
        custom_strings: optional set of strings to append to detection labels, should have the
        same length as [detections].  Appended before classification labels, if classification
        data is provided.

    image is modified in place.
    """

    if custom_strings is not None:
        assert len(custom_strings) == len(detections), \
            '{} custom strings provided for {} detections'.format(
                len(custom_strings),len(detections))
            
    display_boxes = []
    
    # list of lists, one list of strings for each bounding box (to accommodate multiple labels)
    display_strs = []  
    
    # for color selection
    classes = []  

    for i_detection,detection in enumerate(detections):

        score = detection['conf']
        
        if isinstance(confidence_threshold,dict):
            rendering_threshold = confidence_threshold[detection['category']]
        else:
            rendering_threshold = confidence_threshold        
            
            
        # Always render objects with a confidence of "None", this is typically used
        # for ground truth data.        
        if score is None or score >= rendering_threshold:
            
            x1, y1, w_box, h_box = detection['bbox']
            display_boxes.append([y1, x1, y1 + h_box, x1 + w_box])
            clss = detection['category']
            
            # {} is the default, which means "show labels with no mapping", so don't use "if label_map" here
            # if label_map:
            if label_map is not None:
                label = label_map[clss] if clss in label_map else clss
                if score is not None:
                    displayed_label = ['{}: {}%'.format(label, round(100 * score))]
                else:
                    displayed_label = ['{}'.format(label)]
            else:
                displayed_label = ''

            if custom_strings is not None:
                custom_string = custom_strings[i_detection]
                if custom_string is not None and len(custom_string) > 0:
                    if isinstance(displayed_label,str):
                        displayed_label += ' ' + custom_string
                    else:
                        assert len(displayed_label) == 1
                        displayed_label[0] += ' ' + custom_string
                                    
            if 'classifications' in detection:

                # To avoid duplicate colors with detection-only visualization, offset
                # the classification class index by the number of detection classes
                clss = annotation_constants.NUM_DETECTOR_CATEGORIES + int(detection['classifications'][0][0])
                classifications = detection['classifications']
                if len(classifications) > max_classifications:
                    classifications = classifications[0:max_classifications]
                    
                for classification in classifications:
                    
                    classification_conf = classification[1]
                    if classification_conf is not None and \
                        classification_conf < classification_confidence_threshold:
                        continue
                    class_key = classification[0]
                    if (classification_label_map is not None) and (class_key in classification_label_map):
                        class_name = classification_label_map[class_key]
                    else:
                        class_name = class_key
                    if classification_conf is not None:
                        displayed_label += ['{}: {:5.1%}'.format(class_name.lower(), classification_conf)]
                    else:
                        displayed_label += ['{}'.format(class_name.lower())]
                    
                # ...for each classification

            # ...if we have classification results
                        
            display_strs.append(displayed_label)
            classes.append(clss)

        # ...if the confidence of this detection is above threshold

    # ...for each detection
    
    display_boxes = np.array(display_boxes)

    draw_bounding_boxes_on_image(image, display_boxes, classes,
                                 display_strs=display_strs, thickness=thickness, 
                                 expansion=expansion, colormap=colormap, textalign=textalign,
                                 label_font_size=label_font_size)

# ...render_detection_bounding_boxes(...)


def draw_bounding_boxes_on_image(image,
                                 boxes,
                                 classes,
                                 thickness=DEFAULT_BOX_THICKNESS,
                                 expansion=0,
                                 display_strs=None,
                                 colormap=DEFAULT_COLORS,
                                 textalign=TEXTALIGN_LEFT,
                                 label_font_size=DEFAULT_LABEL_FONT_SIZE):
    """
    Draws bounding boxes on an image.

    Args:
      image: a PIL.Image object.
      boxes: a 2 dimensional numpy array of [N, 4]: (ymin, xmin, ymax, xmax).
             The coordinates are in normalized format between [0, 1].
      classes: a list of ints or strings (that can be cast to ints) corresponding to the
               class labels of the boxes. This is only used for color selection.
      thickness: line thickness in pixels. Default value is 4.
      expansion: number of pixels to expand bounding boxes on each side.  Default is 0.
      display_strs: list of list of strings.
                             a list of strings for each bounding box.
                             The reason to pass a list of strings for a
                             bounding box is that it might contain
                             multiple labels.
    """

    boxes_shape = boxes.shape
    if not boxes_shape:
        return
    if len(boxes_shape) != 2 or boxes_shape[1] != 4:
        # print('Input must be of size [N, 4], but is ' + str(boxes_shape))
        return  # no object detection on this image, return
    for i in range(boxes_shape[0]):
        if display_strs:
            display_str_list = display_strs[i]
            draw_bounding_box_on_image(image,
                                       boxes[i, 0], boxes[i, 1], boxes[i, 2], boxes[i, 3],
                                       classes[i],
                                       thickness=thickness, expansion=expansion,
                                       display_str_list=display_str_list,
                                       colormap=colormap,
                                       textalign=textalign,
                                       label_font_size=label_font_size)

# ...draw_bounding_boxes_on_image(...)


def draw_bounding_box_on_image(image,
                               ymin,
                               xmin,
                               ymax,
                               xmax,
                               clss=None,
                               thickness=DEFAULT_BOX_THICKNESS,
                               expansion=0,
                               display_str_list=(),
                               use_normalized_coordinates=True,
                               label_font_size=DEFAULT_LABEL_FONT_SIZE,
                               colormap=DEFAULT_COLORS,
                               textalign=TEXTALIGN_LEFT):
    """
    Adds a bounding box to an image.

    Bounding box coordinates can be specified in either absolute (pixel) or
    normalized coordinates by setting the use_normalized_coordinates argument.

    Each string in display_str_list is displayed on a separate line above the
    bounding box in black text on a rectangle filled with the input 'color'.
    If the top of the bounding box extends to the edge of the image, the strings
    are displayed below the bounding box.

    Args:
    image: a PIL.Image object.
    ymin: ymin of bounding box - upper left.
    xmin: xmin of bounding box.
    ymax: ymax of bounding box.
    xmax: xmax of bounding box.    
    clss: str, the class of the object in this bounding box; should be either an integer
        or a string-formatted integer.
    thickness: line thickness. Default value is 4.
    expansion: number of pixels to expand bounding boxes on each side.  Default is 0.
    display_str_list: list of strings to display in box
        (each to be shown on its own line).
        use_normalized_coordinates: If True (default), treat coordinates
        ymin, xmin, ymax, xmax as relative to the image.  Otherwise treat
        coordinates as absolute.
    label_font_size: font size 
    
    Adapted from:
        
    https://github.com/tensorflow/models/blob/master/research/object_detection/utils/visualization_utils.py
    """
    
    if clss is None:
        # Default to the MegaDetector animal class ID (1)
        color = colormap[1]
    else:
        color = colormap[int(clss) % len(colormap)]

    draw = ImageDraw.Draw(image)
    im_width, im_height = image.size
    if use_normalized_coordinates:
        (left, right, top, bottom) = (xmin * im_width, xmax * im_width,
                                      ymin * im_height, ymax * im_height)
    else:
        (left, right, top, bottom) = (xmin, xmax, ymin, ymax)

    if expansion > 0:
        
        left -= expansion
        right += expansion
        top -= expansion
        bottom += expansion
        
        # Deliberately trimming to the width of the image only in the case where
        # box expansion is turned on.  There's not an obvious correct behavior here,
        # but the thinking is that if the caller provided an out-of-range bounding
        # box, they meant to do that, but at least in the eyes of the person writing
        # this comment, if you expand a box for visualization reasons, you don't want
        # to end up with part of a box.
        #
        # A slightly more sophisticated might check whether it was in fact the expansion
        # that made this box larger than the image, but this is the case 99.999% of the time
        # here, so that doesn't seem necessary.
        left = max(left,0); right = max(right,0)
        top = max(top,0); bottom = max(bottom,0)

        left = min(left,im_width-1); right = min(right,im_width-1)
        top = min(top,im_height-1); bottom = min(bottom,im_height-1)
        
    # ...if we need to expand boxes
    
    draw.line([(left, top), (left, bottom), (right, bottom),
               (right, top), (left, top)], width=thickness, fill=color)

    try:
        font = ImageFont.truetype('arial.ttf', label_font_size)
    except IOError:
        font = ImageFont.load_default()

    def get_text_size(font,s):

        # This is what we did w/Pillow 9
        # w,h = font.getsize(s)
        
        # I would *think* this would be the equivalent for Pillow 10
        # l,t,r,b = font.getbbox(s); w = r-l; h=b-t
        
        # ...but this actually produces the most similar results to Pillow 9
        # l,t,r,b = font.getbbox(s); w = r; h=b
        
        try:
            l,t,r,b = font.getbbox(s); w = r; h=b  
        except Exception:
            w,h = font.getsize(s)
        
        return w,h
    
    # If the total height of the display strings added to the top of the bounding
    # box exceeds the top of the image, stack the strings below the bounding box
    # instead of above.
    display_str_heights = [get_text_size(font,ds)[1] for ds in display_str_list]

    # Each display_str has a top and bottom margin of 0.05x.
    total_display_str_height = (1 + 2 * 0.05) * sum(display_str_heights)

    if top > total_display_str_height:
        text_bottom = top
    else:
        text_bottom = bottom + total_display_str_height

    # Reverse list and print from bottom to top.
    for display_str in display_str_list[::-1]:

        # Skip empty strings
        if len(display_str) == 0:
            continue
        
        text_width, text_height = get_text_size(font,display_str)
        
        text_left = left
        
        if textalign == TEXTALIGN_RIGHT:
            text_left = right - text_width
            
        margin = np.ceil(0.05 * text_height)

        draw.rectangle(
            [(text_left, text_bottom - text_height - 2 * margin), (text_left + text_width,
                                                              text_bottom)],
            fill=color)

        draw.text(
            (text_left + margin, text_bottom - text_height - margin),
            display_str,
            fill='black',
            font=font)

        text_bottom -= (text_height + 2 * margin)

# ...def draw_bounding_box_on_image(...)


def render_iMerit_boxes(boxes, classes, image,
                        label_map=annotation_constants.annotation_bbox_category_id_to_name):
    """
    Renders bounding boxes and their category labels on a PIL image.

    Args:
        boxes: bounding box annotations from iMerit, format is:
            [x_rel, y_rel, w_rel, h_rel] (rel = relative coords)
        classes: the class IDs of the predicted class of each box/object
        image: PIL.Image object to annotate on
        label_map: optional dict mapping classes to a string for display

    Returns:
        image will be altered in place
    """

    display_boxes = []
    
    # list of lists, one list of strings for each bounding box (to accommodate multiple labels)
    display_strs = []  
    
    for box, clss in zip(boxes, classes):
        if len(box) == 0:
            assert clss == 5
            continue
        x_rel, y_rel, w_rel, h_rel = box
        ymin, xmin = y_rel, x_rel
        ymax = ymin + h_rel
        xmax = xmin + w_rel

        display_boxes.append([ymin, xmin, ymax, xmax])

        if label_map:
            clss = label_map[int(clss)]
        display_strs.append([clss])

    display_boxes = np.array(display_boxes)
    draw_bounding_boxes_on_image(image, display_boxes, classes, display_strs=display_strs)


def render_megadb_bounding_boxes(boxes_info, image):
    """
    Args:
        boxes_info: list of dict, each dict represents a single detection
            {
                "category": "animal",
                "bbox": [
                    0.739,
                    0.448,
                    0.187,
                    0.198
                ]
            }
            where bbox coordinates are normalized [x_min, y_min, width, height]
        image: PIL.Image.Image, opened image
    """
    
    display_boxes = []
    display_strs = []
    classes = []  # ints, for selecting colors

    for b in boxes_info:
        x_min, y_min, w_rel, h_rel = b['bbox']
        y_max = y_min + h_rel
        x_max = x_min + w_rel
        display_boxes.append([y_min, x_min, y_max, x_max])
        display_strs.append([b['category']])
        classes.append(annotation_constants.detector_bbox_category_name_to_id[b['category']])

    display_boxes = np.array(display_boxes)
    draw_bounding_boxes_on_image(image, display_boxes, classes, display_strs=display_strs)

# ...def render_iMerit_boxes(...)


def render_db_bounding_boxes(boxes, classes, image, original_size=None,
                             label_map=None, thickness=DEFAULT_BOX_THICKNESS, expansion=0):
    """
    Render bounding boxes (with class labels) on [image].  This is a wrapper for
    draw_bounding_boxes_on_image, allowing the caller to operate on a resized image
    by providing the original size of the image; bboxes will be scaled accordingly.
    
    This function assumes that bounding boxes are in the COCO camera traps format,
    with absolute coordinates.
    """

    display_boxes = []
    display_strs = []

    if original_size is not None:
        image_size = original_size
    else:
        image_size = image.size

    img_width, img_height = image_size

    for box, clss in zip(boxes, classes):

        x_min_abs, y_min_abs, width_abs, height_abs = box[0:4]

        ymin = y_min_abs / img_height
        ymax = ymin + height_abs / img_height

        xmin = x_min_abs / img_width
        xmax = xmin + width_abs / img_width

        display_boxes.append([ymin, xmin, ymax, xmax])

        if label_map:
            clss = label_map[int(clss)]
            
        # need to be a string here because PIL needs to iterate through chars
        display_strs.append([str(clss)])  

    display_boxes = np.array(display_boxes)
    draw_bounding_boxes_on_image(image, display_boxes, classes, display_strs=display_strs,
                                 thickness=thickness, expansion=expansion)

# ...def render_db_bounding_boxes(...)


def draw_bounding_boxes_on_file(input_file, output_file, detections, confidence_threshold=0.0,
                                detector_label_map=DEFAULT_DETECTOR_LABEL_MAP,
                                thickness=DEFAULT_BOX_THICKNESS, expansion=0,
                                colormap=DEFAULT_COLORS,
                                label_font_size=DEFAULT_LABEL_FONT_SIZE,
                                custom_strings=None,target_size=None,
                                ignore_exif_rotation=False):
    """
    Render detection bounding boxes on an image loaded from file, writing the results to a
    new image file.
    
    "detections" is in the API results format:
        
    [{"category": "2","conf": 0.996,"bbox": [0.0,0.2762,0.1234,0.2458]}]
    
    ...where the bbox is:
        
    [x_min, y_min, width_of_box, height_of_box]
    
    Normalized, with the origin at the upper-left.
    
    detector_label_map is a dict mapping category IDs to strings.  If this is None, 
    no confidence values or identifiers are shown  If this is {}, just category indices and 
    confidence values are shown.
    
    custom_strings: optional set of strings to append to detection labels, should have the
    same length as [detections].  Appended before classification labels, if classification
    data is provided.
    
    target_size: tuple of (target_width,target_height).  Either or both can be -1,
    see resize_image for documentation.  If None or (-1,-1), uses the original image size.
    """
    
    image = open_image(input_file, ignore_exif_rotation=ignore_exif_rotation)
    
    if target_size is not None:
        image = resize_image(image,target_size[0],target_size[1])
        
    render_detection_bounding_boxes(
            detections, image, label_map=detector_label_map,
            confidence_threshold=confidence_threshold,
            thickness=thickness,expansion=expansion,colormap=colormap,
            custom_strings=custom_strings,label_font_size=label_font_size)

    image.save(output_file)


def draw_db_boxes_on_file(input_file, output_file, boxes, classes=None, 
                          label_map=None, thickness=DEFAULT_BOX_THICKNESS, expansion=0,
                          ignore_exif_rotation=False):
    """
    Render COCO bounding boxes (in absolute coordinates) on an image loaded from file, writing the
    results to a new image file.

    classes is a list of integer category IDs.
    
    detector_label_map is a dict mapping category IDs to strings.
    """
    
    image = open_image(input_file, ignore_exif_rotation=ignore_exif_rotation)

    if classes is None:
        classes = [0] * len(boxes)
        
    render_db_bounding_boxes(boxes, classes, image, original_size=None,
                                 label_map=label_map, thickness=thickness, expansion=expansion)

    image.save(output_file)
    

# ...def draw_bounding_boxes_on_file(...)


def gray_scale_fraction(image,crop_size=(0.1,0.1)):
    """
    Returns the fraction of the pixels in [image] that appear to be grayscale (R==G==B), 
    useful for approximating whether this is a night-time image when flash information is not
    available in EXIF data (or for video frames, where this information is often not available
    in structured metadata at all).
    
    [image] can be a PIL image or a file name.
    
    crop_size should be a 2-element list/tuple, representing the fraction of the image 
    to crop at the top and bottom, respectively, before analyzing (to minimize the possibility
    of including color elements in the image chrome).
    """
    
    if isinstance(image,str):
        image = Image.open(image)
    
    if image.mode == 'L':
        return 1.0
    
    if len(image.getbands()) == 1:
        return 1.0
    
    # Crop if necessary
    if crop_size[0] > 0 or crop_size[1] > 0:
        
        assert (crop_size[0] + crop_size[1]) < 1.0, \
            print('Illegal crop size: {}'.format(str(crop_size)))
            
        top_crop_pixels = int(image.height * crop_size[0])
        bottom_crop_pixels = int(image.height * crop_size[1])
        
        left = 0
        right = image.width
        
        # Remove pixels from the top
        first_crop_top = top_crop_pixels
        first_crop_bottom = image.height        
        first_crop = image.crop((left, first_crop_top, right, first_crop_bottom))
        
        # Remove pixels from the bottom
        second_crop_top = 0
        second_crop_bottom = first_crop.height - bottom_crop_pixels
        second_crop = first_crop.crop((left, second_crop_top, right, second_crop_bottom))
        
        image = second_crop
    
    # It doesn't matter if these are actually R/G/B, they're just names
    r = np.array(image.getchannel(0))
    g = np.array(image.getchannel(1))
    b = np.array(image.getchannel(2))
        
    gray_pixels = np.logical_and(r == g, r == b)
    n_pixels = gray_pixels.size
    n_gray_pixels = gray_pixels.sum()
    
    return n_gray_pixels / n_pixels

    # Non-numpy way to do the same thing, briefly keeping this here for posterity
    if False:
        
        w, h = image.size
        n_pixels = w*h
        n_gray_pixels = 0
        for i in range(w):
            for j in range(h):
                r, g, b = image.getpixel((i,j))
                if r == g and r == b and g == b:
                    n_gray_pixels += 1            


# ...def gray_scale_fraction(...)


def _resize_relative_image(fn_relative,
                          input_folder,output_folder,
                          target_width,target_height,no_enlarge_width,verbose,quality):
    """
    Internal function for resizing an image from one folder to another,
    maintaining relative path.
    """
    
    input_fn_abs = os.path.join(input_folder,fn_relative)
    output_fn_abs = os.path.join(output_folder,fn_relative)
    os.makedirs(os.path.dirname(output_fn_abs),exist_ok=True)
    try:
        _ = resize_image(input_fn_abs, 
                         output_file=output_fn_abs, 
                         target_width=target_width, target_height=target_height, 
                         no_enlarge_width=no_enlarge_width, verbose=verbose, quality=quality)
        status = 'success'
        error = None
    except Exception as e:
        if verbose:
            print('Error resizing {}: {}'.format(fn_relative,str(e)))
        status = 'error'
        error = str(e)
        
    return {'fn_relative':fn_relative,'status':status,'error':error}

# ...def _resize_relative_image(...)


def _resize_absolute_image(input_output_files,
                          target_width,target_height,no_enlarge_width,verbose,quality):
    
    """
    Internal wrappter for resize_image used in the context of a batch resize operation.
    """
    
    input_fn_abs = input_output_files[0]
    output_fn_abs = input_output_files[1]
    os.makedirs(os.path.dirname(output_fn_abs),exist_ok=True)
    try:
        _ = resize_image(input_fn_abs, 
                         output_file=output_fn_abs, 
                         target_width=target_width, target_height=target_height, 
                         no_enlarge_width=no_enlarge_width, verbose=verbose, quality=quality)
        status = 'success'
        error = None
    except Exception as e:
        if verbose:
            print('Error resizing {}: {}'.format(input_fn_abs,str(e)))
        status = 'error'
        error = str(e)
        
    return {'input_fn':input_fn_abs,'output_fn':output_fn_abs,status:'status',
            'error':error}

# ..._resize_absolute_image(...)


def resize_images(input_file_to_output_file,
                  target_width=-1, target_height=-1,
                  no_enlarge_width=False, verbose=False, quality='keep',
                  pool_type='process', n_workers=10):
    """
    Resize all images the dictionary [input_file_to_output_file].
    
    Defaults to parallelizing across processes.
    
    See resize_image() for parameter information.
    
    TODO: This is a little more redundant with resize_image_folder than I would like;
    refactor resize_image_folder to call resize_images.  Not doing that yet because
    at the time I'm writing this comment, a lot of code depends on resize_image_folder 
    and I don't want to rock the boat yet.
    """

    
    assert pool_type in ('process','thread'), 'Illegal pool type {}'.format(pool_type)
    
    input_output_file_pairs = []
    
    # Reformat input files as (input,output) tuples
    for input_fn in input_file_to_output_file:
        input_output_file_pairs.append((input_fn,input_file_to_output_file[input_fn]))
    
    if n_workers == 1:    
        
        results = []
        for i_o_file_pair in tqdm(input_output_file_pairs):
            results.append(_resize_absolute_image(i_o_file_pair,
                            target_width=target_width,
                            target_height=target_height,
                            no_enlarge_width=no_enlarge_width,
                            verbose=verbose,
                            quality=quality))

    else:
        
        if pool_type == 'thread':
            pool = ThreadPool(n_workers); poolstring = 'threads'                
        else:
            assert pool_type == 'process'
            pool = Pool(n_workers); poolstring = 'processes'
        
        if verbose:
            print('Starting resizing pool with {} {}'.format(n_workers,poolstring))
        
        p = partial(_resize_absolute_image,
                target_width=target_width,
                target_height=target_height,
                no_enlarge_width=no_enlarge_width,
                verbose=verbose,
                quality=quality)
        
        results = list(tqdm(pool.imap(p, input_output_file_pairs),total=len(input_output_file_pairs)))

    return results

# ...def resize_images(...)


def resize_image_folder(input_folder, output_folder=None,
                        target_width=-1, target_height=-1,
                        no_enlarge_width=False, verbose=False, quality='keep',
                        pool_type='process', n_workers=10, recursive=True,
                        image_files_relative=None):
    """
    Resize all images in a folder (defaults to recursive)
    
    Defaults to in-place resizing (output_folder is optional).
    
    Defaults to parallelizing across processes.
    
    See resize_image() for parameter information.
    """

    assert os.path.isdir(input_folder), '{} is not a folder'.format(input_folder)
    
    if output_folder is None:
        output_folder = input_folder
    else:
        os.makedirs(output_folder,exist_ok=True)
        
    assert pool_type in ('process','thread'), 'Illegal pool type {}'.format(pool_type)
    
    if image_files_relative is None:
        image_files_relative = find_images(input_folder,recursive=recursive,return_relative_paths=True)
        if verbose:
            print('Found {} images'.format(len(image_files_relative)))
    
    if n_workers == 1:    
        
        results = []
        for fn_relative in tqdm(image_files_relative):
            results.append(_resize_relative_image(fn_relative,
                                  input_folder=input_folder,
                                  output_folder=output_folder,
                                  target_width=target_width,
                                  target_height=target_height,
                                  no_enlarge_width=no_enlarge_width,
                                  verbose=verbose,
                                  quality=quality))

    else:
        
        if pool_type == 'thread':
            pool = ThreadPool(n_workers); poolstring = 'threads'                
        else:
            assert pool_type == 'process'
            pool = Pool(n_workers); poolstring = 'processes'
        
        if verbose:
            print('Starting resizing pool with {} {}'.format(n_workers,poolstring))
        
        p = partial(_resize_relative_image,
                input_folder=input_folder,
                output_folder=output_folder,
                target_width=target_width,
                target_height=target_height,
                no_enlarge_width=no_enlarge_width,
                verbose=verbose,
                quality=quality)
        
        results = list(tqdm(pool.imap(p, image_files_relative),total=len(image_files_relative)))

    return results

# ...def resize_image_folder(...)


#%% Test drivers

if False:
    
    #%% Recursive resize test
    
    from md_visualization.visualization_utils import resize_image_folder # noqa
    
    input_folder = r"C:\temp\resize-test\in"
    output_folder = r"C:\temp\resize-test\out"
    
    resize_results = resize_image_folder(input_folder,output_folder,
                         target_width=1280,verbose=True,quality=85,no_enlarge_width=True,
                         pool_type='process',n_workers=10)