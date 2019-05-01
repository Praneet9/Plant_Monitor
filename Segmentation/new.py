def process_image(self, path, purpose):
        imgs = self.read_images(path, purpose)
        trainingImgs = []
        for img in imgs:
            blurImg = cv2.GaussianBlur(img, (5, 5), 0)   
            hsvImg = cv2.cvtColor(blurImg, cv2.COLOR_BGR2HSV)  
            lower_green = (25, 40, 50)
            upper_green = (75, 255, 255)
            mask = cv2.inRange(hsvImg, lower_green, upper_green)  
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            bMask = mask > 0  
            clear = np.zeros_like(img, np.uint8)
            clear[bMask] = img[bMask]
            trainingImgs.append(clear)
        trainingImgs = np.asarray(trainingImgs)
        trainingImgs = trainingImgs / 255
        return trainingImgs
