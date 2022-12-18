import os
import sys
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURR_DIR)
import yolov7.utils.datasets
import yolov7.models.experimental
import yolov7.utils.datasets
import yolov7.utils.general
import yolov7.utils.plots
import yolov7.utils.torch_utils