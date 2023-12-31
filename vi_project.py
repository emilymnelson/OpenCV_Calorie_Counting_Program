
## packages to import/constant variables ##
## do not modify any code below: ##
import cv2 as cv
import pprint as pp
import numpy as np
from matplotlib import pyplot as py
from google.colab.patches import cv2_imshow
from tabulate import tabulate
r_c = 10680
red_bins = 128
green_bins = 128
blue_bins = 64
dime_diameter = 0.6875
##


## here is where your images are imported ##
## please enter the title of your image within single quotes like such: ##
## image1 = cv.imread('YOURIMAGENAME.JPG', cv.IMREAD_COLOR) ##

apple_color = cv.imread('/content/apple.jpg', cv.IMREAD_COLOR)
orange_color = cv.imread('/content/orange.jpg', cv.IMREAD_COLOR)
banana_color = cv.imread('/content/banana.jpg', cv.IMREAD_COLOR)
img1 = cv.imread('/content/apple.jpg', cv.IMREAD_COLOR)
img2 = cv.imread('/content/orange.jpg', cv.IMREAD_COLOR)
img3 = cv.imread('/content/banana.jpg', cv.IMREAD_COLOR)
apple_bw = cv.imread('/content/apple.jpg')
orange_bw = cv.imread('/content/orange.jpg')
banana_bw = cv.imread('/content/banana.jpg')
apple_copy = apple_bw.copy()
banana_copy = banana_bw.copy()
orange_copy = orange_bw.copy()

## here is the databased used to identify your food item. ##
## do not modify any code below: ##

apple_bw = cv.cvtColor(apple_bw, cv.COLOR_BGR2GRAY)
orange_bw = cv.cvtColor(orange_bw, cv.COLOR_BGR2GRAY)
banana_bw = cv.cvtColor(banana_bw, cv.COLOR_BGR2GRAY)

img4 = cv.imread('train_apple1.jpg', cv.IMREAD_COLOR)
img5 = cv.imread('train_apple2.jpg', cv.IMREAD_COLOR)
img6 = cv.imread('train_apple3.jpg', cv.IMREAD_COLOR)
img7 = cv.imread('train_apple4.jpg', cv.IMREAD_COLOR)
img8 = cv.imread('train_apple5.jpg', cv.IMREAD_COLOR)
img9 = cv.imread('train_orange1.jpg', cv.IMREAD_COLOR)
img10 = cv.imread('train_orange2.jpg', cv.IMREAD_COLOR)
img11 = cv.imread('train_orange3.jpg', cv.IMREAD_COLOR)
img12 = cv.imread('train_orange4.jpg', cv.IMREAD_COLOR)
img13 = cv.imread('train_orange5.jpg', cv.IMREAD_COLOR)
img14 = cv.imread('train_banana1.jpg', cv.IMREAD_COLOR)
img15 = cv.imread('train_banana2.jpg', cv.IMREAD_COLOR)
img16 = cv.imread('train_banana3.jpg', cv.IMREAD_COLOR)
img17 = cv.imread('train_banana4.jpg', cv.IMREAD_COLOR)
img18 = cv.imread('train_banana5.jpg', cv.IMREAD_COLOR)

for i in range(1, 19):
  exec('hist%s = cv.calcHist([img%s],[0,1,2],None,[red_bins, green_bins, blue_bins],[0,256, 0, 256, 0, 256])' % (i, i))

for i in range(1, 4):
  differences = []
  for j in range(1, 19):
    hist_diff = eval('hist%s - hist%s' % (i,j) )
    difference = sum(sum(sum(abs(hist_diff))))
    difference = difference/r_c
    differences.append(difference)
  differences = np.argsort(differences)
  #print(differences)
  #print("Query number:", i)
  #for x in range(1,10):
    #print("Image number: ", differences[x]+1)

ret, apple_bw = cv.threshold(apple_bw, 110, 300, cv.THRESH_BINARY)
ret, orange_bw = cv.threshold(orange_bw, 110, 300, cv.THRESH_BINARY)
ret, banana_bw = cv.threshold(banana_bw, 110, 300, cv.THRESH_BINARY)


contours1, hierarchy1 = cv.findContours(apple_bw, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours2, hierarchy1 = cv.findContours(orange_bw, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours3, hierarchy1 = cv.findContours(banana_bw, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

all_areas1 = []
all_areas2 = []
all_areas3 = []

for cnt in contours1:
  area = cv.contourArea(cnt)
  all_areas1.append(area)

for cnt in contours2:
  area = cv.contourArea(cnt)
  all_areas2.append(area)

for cnt in contours3:
  area= cv.contourArea(cnt)
  all_areas3.append(area)


sorted_contours1 = sorted(contours1, key=cv.contourArea, reverse= True)
sorted_contours2 = sorted(contours2, key=cv.contourArea, reverse= True)
sorted_contours3 = sorted(contours3, key=cv.contourArea, reverse= True)

largest_two_apple = []
largest_two_orange = []
largest_two_banana = []


largest_two_apple.append(sorted_contours1[0])
largest_two_apple.append(sorted_contours1[1])
largest_two_orange.append(sorted_contours2[0])
largest_two_orange.append(sorted_contours2[1])
largest_two_banana.append(sorted_contours3[0])
largest_two_banana.append(sorted_contours3[1])

approx_apple = cv.approxPolyDP(largest_two_apple[0],0.01*cv.arcLength(cnt,True),True)
approx_orange = cv.approxPolyDP(largest_two_orange[0],0.01*cv.arcLength(cnt,True),True)
approx_banana = cv.approxPolyDP(largest_two_banana[0],0.01*cv.arcLength(cnt,True),True)


x_dime,y_dime,w_dime,h_dime = cv.boundingRect(largest_two_apple[1])

x_apple,y_apple,w_apple,h_apple = cv.boundingRect(largest_two_apple[0])

cv.drawContours(apple_copy, largest_two_apple, -1, (0,255,0), 3)
cv.rectangle(apple_copy,(x_apple,y_apple),(x_apple+w_apple,y_apple+h_apple),(0,255,0),2)

dime_pixels = w_dime

pixel_inch_ratio = dime_pixels/dime_diameter

apple_diameter = h_apple

apple_inches = apple_diameter/pixel_inch_ratio



apple_calorie_ratio = 95/3
banana_calorie_ratio = 15
orange_calorie_ratio = 19

##here is where you change the calorie ratio for different foods##
##if checking a banana, please input like such without changing the second parameter ##
## num_of_calories = round(banana_calorie_ratio*apple_inches) ##

num_of_calories = round(apple_calorie_ratio*apple_inches)

num_of_calories = str(num_of_calories)

num_of_calories + 'calories'

new_image = cv.putText(apple_copy, num_of_calories, (250, 150), cv.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 2, cv.LINE_AA)

cv2_imshow(new_image)
