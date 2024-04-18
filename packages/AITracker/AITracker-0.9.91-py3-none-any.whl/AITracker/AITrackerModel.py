'''
Load and make predictions on the AITracker neural network model, as well as process images to fit the network's needs.
'''
import h5py
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import cv2
import dlib
import os
from scipy.spatial import distance as dist

class AITrackerModel():
    '''
    Load and make predictions on the AITracker neural network model, as well as process images to fit the network's expectations.
    '''
    def __init__(self, verbose: int, dlib_landmarks_path: str):
        '''
        Initialize an AITrackerModel object.
        
        Parameters:
        -----------
            verbose (int): A value 0 or 1. 1 prints predictions to console, 0 doesn't.
            dlib_landmarks_path (str): A path to the dlib facial landmarks file.
            
        Raises:
        -------
            ValueError: If the verbose parameter isn't 0 or 1.
        '''
        # check verbose parameter
        if verbose > 1 or verbose < 0:
            raise ValueError("Error: Verbose parameter isn't 0 or 1!")
        self._verbose = verbose
        
        # imaging process constants
        self._eyes_detector = dlib.get_frontal_face_detector()
        self._predictor = dlib.shape_predictor(dlib_landmarks_path)
        self._image_size = (190, 80)

        # the points for the EAR calculation
        self._eye_points = None
        self._EAR = None

        # load the model into the program
        self._model = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), 'image_classifier6.model'))
        
        # load necessary labels into program
        _label_encoder = LabelEncoder()
        _label_encoder.fit_transform(['North', 'West', 'East', 'South', 'Center', 'North West', 'North East', 'South West', 'South East'])
        self._class_names = _label_encoder.classes_
    
    @property
    def image_size(self):
        return self._image_size
    
    @property
    def EAR(self):
        return self._EAR
    
    # make a prediction on a direction through the network
    def predict_direction(self, image):
        '''
        Predict a direction for a given image.
        '''
        prediction = self._model.predict(np.array([image]), verbose=self._verbose)
        predicted_class = self._class_names[np.argmax(prediction)]
        
        # return string representation of prediction
        return predicted_class

    # takes the image, crops the eyes, puts it into the template, resizes to our network's image input size      
    def process_image(self, image):
        '''
        Process the image before sending it to the neural network.
        '''
        # grayscale image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # if a face is detected
        faces = self._eyes_detector(gray)
        if len(faces) > 0:
            landmarks = self._predictor(gray, faces[0])
            
            # calculate EAR
            self._EAR = self._eye_distance(landmarks)
            
            pad = 5
            left_eye = (
                #left width, top height
                landmarks.part(36).x - pad, landmarks.part(37).y - pad,
                #right width, bottom height
                landmarks.part(39).x + pad, landmarks.part(41).y + pad
            )
            
            right_eye = (
                #left width, top height
                landmarks.part(42).x - pad, landmarks.part(43).y - pad,
                #right width, bottom height
                landmarks.part(45).x + pad, landmarks.part(47).y + pad
            )
            
            # get separate images for each eye
            # [start_y:end_y, start_x:end_x]
            left_eye_region = gray[left_eye[1]:left_eye[3], left_eye[0]:left_eye[2]]
            right_eye_region = gray[right_eye[1]:right_eye[3], right_eye[0]:right_eye[2]]
            
            # put eyes into template similar to our training data
            template = self._eye_template(left_eye_region, right_eye_region)
            
            # return resized image and true indicating it can be used for input in our network
            return (cv2.resize(template, self._image_size), True)
        
        # no eyes means no EAR
        self._EAR = None
        
        # if no faces are found return original image and false
        return (image, False)

    # makes the template with the regions specified by cropping the eyes
    def _eye_template(self, left_eye, right_eye):
        # composite image height and width
        height = max(left_eye.shape[0], right_eye.shape[0])
        width = left_eye.shape[1] + right_eye.shape[1]

        # create a blank image to put data into
        composite_image = np.zeros((height, width), dtype=np.uint8)

        # put left and right eyes in the image side by side
        composite_image[:left_eye.shape[0], :left_eye.shape[1]] = left_eye
        composite_image[:right_eye.shape[0], left_eye.shape[1]:] = right_eye

        # return the composite image
        return composite_image
    
    # calculate the distance between the top and bottom of each eye and return it as a tuple
    def _eye_distance(self, landmarks):
        if landmarks:
            # extract points for EAR calculation
            left_eye_points = (
                # horizontal
                (landmarks.part(36).x, landmarks.part(36).y),
                (landmarks.part(39).x, landmarks.part(39).y),
                
                # left vertical
                (landmarks.part(37).x, landmarks.part(37).y),
                (landmarks.part(41).x, landmarks.part(41).y),
                
                # right vertical
                (landmarks.part(38).x, landmarks.part(38).y),
                (landmarks.part(40).x, landmarks.part(40).y)
            )
            
            right_eye_points = (
                # horizontal
                (landmarks.part(42).x, landmarks.part(42).y),
                (landmarks.part(45).x, landmarks.part(45).y),
                
                # left vertical
                (landmarks.part(43).x, landmarks.part(43).y),
                (landmarks.part(47).x, landmarks.part(47).y),
                
                # right vertical
                (landmarks.part(44).x, landmarks.part(44).y),
                (landmarks.part(46).x, landmarks.part(46).y)
            )
            return (self._calculateEAR(left_eye_points), self._calculateEAR(right_eye_points))
        return (-1, -1)
    
    # https://www.geeksforgeeks.org/eye-blink-detection-with-opencv-python-and-dlib/
    def _calculateEAR(self, eye_points):
        horizontal_distance = dist.euclidean(eye_points[0], eye_points[1])
        y_dist_1 = dist.euclidean(eye_points[2], eye_points[3])
        y_dist_2 = dist.euclidean(eye_points[4], eye_points[5])
        
        return (y_dist_1 + y_dist_2) / horizontal_distance