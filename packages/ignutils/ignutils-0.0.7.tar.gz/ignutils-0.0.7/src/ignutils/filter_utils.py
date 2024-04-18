import cv2
import numpy as np

def get_len_brd_filter_cntrs(cntrs, length_threshold, breadth_threshold, parent_width):
    """Return filetered contours based on length and breadth thresh"""
    filtered_cntrs = []
    for contr in cntrs:
        rect = cv2.minAreaRect(np.array(contr, dtype="int"))
        length = max(rect[1])
        breadth = min(rect[1])
        breadth_perc = (breadth / parent_width) * 100
        length_perc = (length / parent_width) * 100
        if (breadth_perc > breadth_threshold) and (length_perc > length_threshold):
            filtered_cntrs.append(contr)
        else:
            print("Removed")
            
    return filtered_cntrs
    
def get_max_area_cntr(cntrs):
    """Returns [contour] with maximum area"""
    max_area = 0
    max_index = 0
    for index, cntr in enumerate(cntrs):  # Looping to get max area index
        if len(cntr) >= 4:
            area = cv2.contourArea(np.array(cntr))
            if area >= max_area:
                max_area = area
                max_index = index
    max_cntr = cntrs[max_index]
    return [max_cntr]
