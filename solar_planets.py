import cv2 as cv

img = cv.imread("solar-system.jpg")

cv.putText(img,
            "Sol",
            (100,80),
            cv.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
           )

cv.putText(img, "Mercurio", (100, 180), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (130,130,130))
cv.putText(img, "Venus", (200, 180), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (100,20,255))
cv.putText(img, "Tierra", (300, 180), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (100,255,50))
cv.putText(img, "Marte", (400, 180), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (100,100,255))
cv.putText(img, "Jupiter", (600, 180), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (255,255,255))
cv.putText(img, "Saturno", (800, 180), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (255,255,255))
cv.putText(img, "Urano", (980, 180), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (150,40,23))
cv.putText(img, "Neptuno", (1200, 180), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (255,255,0))

cv.imshow("mostrar imagen", img)


k = cv.waitKey(0)

cv.imwrite("Solar_systemwithname.jpg", img)