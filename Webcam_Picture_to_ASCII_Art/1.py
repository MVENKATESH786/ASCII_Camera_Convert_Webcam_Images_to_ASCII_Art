import cv2
from PIL import Image
import numpy as np

# ASCII characters used to build the output text
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    """
    Resizes the image while maintaining aspect ratio.
    """
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    """
    Converts the image to grayscale.
    """
    return image.convert("L")

def pixels_to_ascii(image):
    """
    Converts pixels to ASCII characters.
    """
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 32] for pixel in pixels])
    return ascii_str

def image_to_ascii(image):
    """
    Converts the image to ASCII art.
    """
    image = resize_image(image)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    # Create ASCII art line by line
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"
    return ascii_img

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        # Display the webcam frame
        cv2.imshow('Webcam', frame)

        # Capture the image and convert it to ASCII art on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            ascii_img = image_to_ascii(pil_image)
            print(ascii_img)
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
