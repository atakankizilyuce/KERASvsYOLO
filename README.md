# KERASvsYOLO
I have developed a program that allows you to see your Keras and YOLO results on a single photo on the project you are working on. This way you can save a lot of time. I briefly showed how to use the program in the video.  For more information use README file


Required steps:<br>
In the KERAS.txt and YOLO.txt files, save your information in the format: photo name, class, x1,y1,x2,y2, for the relevant libraries.<br>
(Do not put a comma after "y2" in KERAS.txt. Only put a comma after "y2" for YOLO.txt.)<br>
Example: --YOLO.txt<br>
image1.jpg,cat, 723.0, 429.0, 1278.0, 690.0,<br>
image1.jpg,bowl, 76.0, 145.0, 148.0, 196.0,<br>
image1.jpg,dog, 101.0, 54.0, 467.0, 469.0,<br>
--KERAS.txt<br>
image1.jpg,cat, 728, 434, 1283, 695<br>
image1.jpg,bowl, 81, 150, 153, 201<br>
image1.jpg,dog, 106, 59, 482, 474<br>

After saving the information, start the program by running the main.py file.<br>
Click "File" in the top left and select "Open from Directory". (only photos should be in the folder you choose)
Click any or both of the Keras, YOLO buttons at the bottom and click the ">>>" sign.<br>
You can see the results on the screen. Green results represent Keras, yellow results YOLO.<br>
