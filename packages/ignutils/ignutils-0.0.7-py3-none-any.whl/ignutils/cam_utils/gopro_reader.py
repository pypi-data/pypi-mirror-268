"""Reads web camera frames and set camera properties."""
import os
import cv2
import requests
import json 

class GoProReader:

    def __init__(self):
        # result_from_gopro = requests.get("http://172.26.103.51/gp/gpWebcam/START")
        self.start_stream()
        self.cap =  cv2.VideoCapture("udp://0.0.0.0:8554?overrun_nonfatal=1&fifo_size=50000000",cv2.CAP_FFMPEG)
        self.frame_no = 0
    
    def start_stream(self):
        result_from_gopro = requests.get("http://172.26.103.51/gp/gpWebcam/START")
    
    def live_stream(self):
        """
        Function to get Live stream from Gopro
        """
        print("Press 's' for saving current frame")
        cv2.namedWindow("Live", cv2.WINDOW_GUI_NORMAL)
        while(True):
            is_stream, frame = self.cap.read()
            if is_stream:
                cv2.imshow("Live", frame)
                k = cv2.waitKey(1)
                if k == ord('q'):
                    break
                if k == ord('s'):
                    cv2.imwrite("frame_{}.png".format(self.frame_no), frame)
                    self.frame_no+=1
            else:
                print("No Stream")
                break
    
    def next_frame(self, undist=True):
        """
        Function to get current frame from Gopro
        """
        is_stream, frame = self.cap.read()
        if is_stream:
            self.frame_no += 1
        return frame, self.frame_no

    def stop_stream(self):
        result_from_gopro = requests.get("http://172.26.103.51/gp/gpWebcam/STOP")


if __name__ == '__main__':

    gopro = GoProReader()
    gopro.live_stream()
    # img = gopro.next_frame()
    # print(img.shape)
