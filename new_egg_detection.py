import cv2
import numpy as np

img = cv2.imread('egg2.jpg')
img2 = img.copy()
imgc = img.copy()
imgtest = img.copy()
imgt = img.copy() # Gen image that for draw image in colour filtered
imgw = img.copy() # white egg filter

# Convert img to HSV image
imgh = cv2.cvtColor(imgc, cv2.COLOR_BGR2HSV) 

bound1 = np.array([10, 100, 20])
bound2 = np.array([20, 255, 200])

wbound1 = np.array([0, 0, 200])
wbound2 = np.array([55, 80, 255])

# Filt the image with the bound 1 and 2
filter_ = cv2.inRange(imgh, bound1, bound2)

wfilter_ = cv2.inRange(imgh, wbound1, wbound2)

contours1, _ = cv2.findContours(filter_ ,cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)

contours2, _ = cv2.findContours(wfilter_ ,cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)

con1 = 0
con2 = 0

# Loob for find countour in the colour filter image
for contour1 in contours1:
    con1 += 1
    # Draw a bounding box around the detected contour
    x, y, w, h = cv2.boundingRect(contour1)
    cv2.rectangle(imgt, (x, y), (x + w, y + h), (0, 0, 255), 5)
    # Add text with the contour
    cv2.putText(imgt, str(con1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

for contour2 in contours2:
    con2 += 1
    # Draw a bounding box around the detected contour
    x, y, w, h = cv2.boundingRect(contour2)
    cv2.rectangle(imgw, (x, y), (x + w, y + h), (0, 0, 255), 5)
    # Add text with the contour
    cv2.putText(imgw, str(con2), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

print("Con2 =", con2)
cv2.imwrite("imgw.jpg", imgw)

con1 = con1 + con2

print("Number of Contours found = " + str(len(contours1)))

max_countour_area = 279732

# Filter out small contours
min_contour_area = 11000  # Minimum contour area to consider as an egg
egg_count = 0

#count egg with filtering out smal contours
for contour in contours1:
    if (cv2.contourArea(contour) > min_contour_area) and (cv2.contourArea(contour) < max_countour_area):
        egg_count += 1
        # Draw a bounding box around the detected egg
        x, y, w, h = cv2.boundingRect(contour)
        print(f"{egg_count} area: {cv2.contourArea(contour)}")
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 5)
        # Add text with the egg count
        cv2.putText(img2, str(egg_count), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

min_contour_area = 100000  # Minimum contour area to consider as an egg
max_countour_area = 202367

for contour in contours2:
    if (cv2.contourArea(contour) > min_contour_area) and (cv2.contourArea(contour) < max_countour_area):
        egg_count += 1
        # Draw a bounding box around the detected egg
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 5)
        print(f"{egg_count} area: {cv2.contourArea(contour)}")
        # Add text with the egg count
        cv2.putText(img2, str(egg_count), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


print("the number of egg", egg_count)
cv2.imwrite('filtered.jpg', filter_)
cv2.imwrite('withoutfilter.jpg', imgtest)
cv2.imwrite("img2.jpg", img2)   #with square
return egg_count
