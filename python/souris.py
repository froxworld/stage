import cv2
import numpy as np

# creation dimage de 100x100
compteur = 0
nom = 'test'
chemin1 = './resultats/100/'
extension = '.jpg'
dessine = False
point1 = (0, 0)
point2 = ()

tailleX = 640
tailleY = 480
tailleCarre = 100

diminueP1X = 0
diminueP1Y = 0
diminueP2X = 0
diminueP2Y = 0

vide = np.zeros((tailleY, tailleX, 3), np.uint8)
derniereImage = np.zeros((tailleY, tailleX, 3), np.uint8)
retour = True


def nothing():
    pass


def sauvegardeImage():
    point1_x = int(diminueP1X) - 1
    point1_y = int(diminueP1Y) - 1
    point2_x = int(diminueP2X) - 1
    point2_y = int(diminueP2Y) - 1

    largeurRectangle = abs(point2_x - point1_x)
    hauteurRectangle = abs(point2_y - point1_y)

    chemin = chemin1 + str(compteur) + extension
    coin_haut_x = min(point1_x, point2_x)
    coin_haut_y = min(point1_y, point2_y)

    coin_bas_x = max(point1_x, point2_x)
    coin_bas_y = max(point1_y, point2_y)

    derniere_image = image

    print(chemin)
    for i in range(coin_haut_y, coin_bas_y + 1):
        for j in range(coin_haut_x, coin_bas_x + 1):
            vide[i, j] = derniere_image[i, j]

    #  print(coin_haut_x, coin_haut_y, coin_bas_x, coin_bas_y)
    #  print(diminueP2X, diminueP2Y)

    image_a_sauver = derniere_image[coin_haut_y:coin_haut_y + int(taille), coin_haut_x:coin_haut_x + int(taille)]
    cv2.imwrite(chemin, image_a_sauver)
    # cv2.imwrite(chemin,compteur, image)


def position_souris(evenement, x, y, flags, parametres):
    global point1, point2, diminueP1X, diminueP1Y, diminueP2X, diminueP2Y, dessine, compteur, image, tailleCarre
    if evenement == cv2.EVENT_LBUTTONDBLCLK:
        print('click 1')
        diminueP1X = x
        diminueP1Y = y
        point1 = (x, y)
        diminueP2X = x
        diminueP2Y = y
        sauvegardeImage()
        compteur = compteur + 1
    if evenement == cv2.EVENT_MOUSEMOVE:
        point1 = (x, y)
        point2 = (point1[0] + int(taille), point1[1] + int(taille))
        cv2.rectangle(image, point1, point2, (0, 255, 0))
        cv2.imshow('capturevideo', image)


capture = cv2.VideoCapture(0)
cv2.namedWindow('capturevideo')
cv2.setMouseCallback('capturevideo', position_souris)

cv2.createTrackbar('Taille', 'capturevideo', 0, 300, nothing)
cv2.createTrackbar('R', 'capturevideo', 0, 255, nothing)
cv2.createTrackbar('G', 'capturevideo', 0, 255, nothing)
cv2.createTrackbar('B', 'capturevideo', 0, 255, nothing)
cv2.createTrackbar('S', 'capturevideo', 0, 179, nothing)

while retour:

    taille = cv2.getTrackbarPos('Taille', 'capturevideo')
    rouge = cv2.getTrackbarPos('R', 'capturevideo')
    vert = cv2.getTrackbarPos('G', 'capturevideo')
    bleu = cv2.getTrackbarPos('B', 'captureVideo')
    saturation = cv2.getTrackbarPos('S', 'captureVideo')
    _, image = capture.read()
    lower_blue = np.array([int(rouge), int(vert), int(bleu)])
    upper_blue = np.array([255, 255, 255])

    sauration = cv2.getTrackbarPos('S', 'capturevideo')
    mask = cv2.inRange(image, lower_blue, upper_blue)
    res = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow('mask', res)

    # cv2.imshow('R V', thresh1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        retour = False  # ou break

capture.release()
cv2.destroyAllWindows()
