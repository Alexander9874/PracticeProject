import face_recognition_api
import Functions
import cv2
import os
import pickle
import numpy as np
import warnings
import os
import time

video_capture = cv2.VideoCapture(0)

# Load Face Recogniser classifier
fname = 'classifier.pkl'
if os.path.isfile(fname):
    with open(fname, 'rb') as f:
        (le, clf) = pickle.load(f)
else:
    print('\x1b[0;37;43m' + "Classifier '{}' does not exist".format(fname) + '\x1b[0m')
    quit()

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

prevtable = None
prevID = None

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition_api.face_locations(small_frame)
            face_encodings = face_recognition_api.face_encodings(small_frame, face_locations)

            face_names = []
            predictions = []
            if len(face_encodings) > 0:
                closest_distances = clf.kneighbors(face_encodings, n_neighbors=1)
            
                is_recognized = [closest_distances[0][i][0] <= 0.6 for i in range(len(face_locations))]
            
                # predict classes and cull classifications that are not with high confidence
                predictions = [(le.inverse_transform([int(pred)])[0] , loc) 
                		 if rec 
               		 else ("Unknown", loc) 
             			 for pred, loc, rec in
            		        zip(clf.predict(face_encodings), face_locations, is_recognized)]

        process_this_frame = not process_this_frame

        # Display the results
        for name, (top, right, bottom, left) in predictions:
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 2)

        #cv2.imshow('Video', frame)

        		# MY PART
        
        table = 0  
        blue1 = 255
        green1 =0
        blue2=255
        green2=0
        
        if str(predictions) != '[]':
        
          newID= name
	
        
          ###DETECTING TABLE###
          if right<400 and bottom<520 and left>120 and top>240:
            table = 1
            blue1 = 0
            green1 = 255
            #print("table 1")
        	
          elif right<1000 and bottom<520 and left>720 and top>240:
            table=2
            blue2 = 0
            green2 = 255
            #print("table 2")

          #print (table)

        ### DRAW TABLES ###

        cv2.rectangle(frame, (400, 240), (120, 520), (blue1, green1, 0), 2)
        cv2.rectangle(frame, (400, 490), (120, 520), (blue1, green1, 0), cv2.FILLED)
        cv2.putText(frame, 'Table 1', (126, 514), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 2)
        
        cv2.rectangle(frame, (1000, 240), (720, 520), (blue2, green2, 0), 2)
        cv2.rectangle(frame, (1000, 490), (720, 520), (blue2, green2, 0), cv2.FILLED)
        cv2.putText(frame, 'Table 2', (726, 514), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 2)
                     
        # Display the resulting image
        #print(predictions, table, frame)
        cv2.imshow('Video', frame)

        if table != 0 and newID == 'Unknown':
            # создаем уникальное имя из года месяца числа с форматом png	
            newID = time.strftime("%Y%m%d%H%M%S")
            newID = 'x'+newID
            photo_name ="{}.png".format(newID)
            
            # готовим адресс куда будем сохранять папку с фотографиями и создаем ее
            path = './training-images/{}'.format(newID)
            os.mkdir(path)
            
            # делаем 3 фотогафии с промежутком 0.3 секунды
            cv2.imwrite(os.path.join(path , "1.png"), frame)
            #time.sleep(0.3) #!!не работает!!
            #cv2.imshow('Video', frame)
            cv2.imwrite(os.path.join(path , "2.png"), frame)
            #time.sleep(0.3) #!!не работает!!
            #cv2.imshow('Video', frame)
            cv2.imwrite(os.path.join(path , "3.png"), frame)
          
            print("Created directory ./train-images/{} and photos in it".format(photo_name))
            print('New ID. NO DATA')
            prevID = newID
            Functions.Create(newID)
            
            # Release handle to the webcam
            video_capture.release()
            cv2.destroyAllWindows()
          
            break
            
        elif table != 0 and (prevID != newID or prevtable != table):
            prevID = newID
            prevtable = table
            Functions.Write(newID, table)
            
        elif cv2.waitKey(1) & 0xFF == ord('q'):
          
            # Release handle to the webcam
            video_capture.release()
            cv2.destroyAllWindows()
          
            break


    if name == 'Unknown' and table != 0:
      
      # запускаем обработку фотографий
      os.system('python3 create_encodings.py')     
          
			# END MY PART
