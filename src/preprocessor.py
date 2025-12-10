import cv2
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Preprocessor:
    def __init__(self):
        pass

    def load_image(self, image_path):
        self.image = cv2.imread(image_path)
        if self.image is None:
            logging.error("Error: Could not read image file")
        return self.image
    
    def to_grayscale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    def denoise(self, image):
        dst = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
        return dst
    
    def resize(self, image, width=200):
        (h,w) = image.shape[:2]

        #calculate ratio of new width to old width
        ratio = width / float(w)
        new_height = int(h * ratio)

        dim = (width, new_height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        return resized
    
    def preprocess(self, image_path):
        image = self.load_image(image_path)
        resized_image = self.resize(image, width=1200)
        denoised_image = self.denoise(resized_image)
        grayscaled_image = self.to_grayscale(denoised_image)
        return grayscaled_image
    


    

if __name__ == "__main__":

    image_path = "../images/a.jpg"
    obj = Preprocessor()

    cv2.imshow("Original Image", cv2.imread(image_path))
    cv2.imshow("Denoised Image", obj.preprocess(image_path=image_path))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
