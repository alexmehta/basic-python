if __name__ == '__main__':
    from PIL import Image
    import pytesseract
    from PIL import Image, ImageEnhance, ImageFilter
    import cv2

    cap = cv2.VideoCapture( 0 )  # video capture source camera (Here webcam of laptop)
    ret, frame = cap.read()  # return a single frame in variable `frame`

    import cv2




    camera = cv2.VideoCapture( 0 )
    i = 0
    while i < 1:


        input( 'Press Enter to capture' )
        return_value, image = camera.read()
        cv2.imwrite( 'temp.jpg', image )
        i += 1
        print('image frame captured'
              )

    del (camera)
    cv2.destroyAllWindows()
    img = Image.open( 'temp.jpg' )
    img.load()

    new_size = tuple( 2 * x for x in img.size )
    img = img.resize( new_size, Image.ANTIALIAS )
    img.save('temp.jpg')
    print( pytesseract.image_to_string( img ) )
