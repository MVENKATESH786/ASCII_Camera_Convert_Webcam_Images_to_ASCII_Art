
# ASCII Camera - Convert Webcam Pictures to ASCII Art

This code uses Python to capture images from a webcam and convert them into ASCII art in real-time. The project leverages OpenCV for webcam access and PIL (Pillow) for image processing.

## Features

- Accesses the webcam to capture live images.
- Converts images to grayscale.
- Resizes the images while maintaining the aspect ratio.
- Transforms the pixels into ASCII characters to create ASCII art.
- Displays the ASCII art in the terminal.

## Prerequisites

To run this project, you'll need to have Python installed along with the following libraries:

1. **OpenCV** – For capturing webcam images.
2. **Pillow** – For image manipulation.
3. **NumPy** – A powerful numerical library for handling arrays (used by OpenCV).

Install the required libraries using pip:

```bash
pip install opencv-python Pillow numpy
```

## How to Use

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/MVENKATESH786/ASCII_Camera_Convert_Webcam_Images_to_ASCII_Art.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ascii-camera
    ```

3. Run the `ascii_camera.py` file:

    ```bash
    python ascii_camera.py
    ```

4. Your webcam will open. To capture an image and convert it to ASCII art, press the **`q`** key.

5. The ASCII art will be printed in the terminal window.

## Code Overview

- **resize_image(image, new_width=100)**: Resizes the input image to a fixed width while maintaining the aspect ratio.
- **grayify(image)**: Converts the input image to grayscale.
- **pixels_to_ascii(image)**: Converts the grayscale image pixels into ASCII characters.
- **image_to_ascii(image)**: Combines resizing, grayscaling, and pixel conversion to generate the final ASCII art.
- **main()**: Captures frames from the webcam and prints the ASCII art when `q` is pressed.

## Example Output

The script generates an ASCII representation of the webcam image that might look something like this:

``` 
@@@@@###**+=---....
@@@###***++==---...
@@@###***++===---..
@@@###***++===---..
...
```

## Contribution

Feel free to submit issues, fork the repository, or make pull requests. Contributions are welcome!

### Steps to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin new-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

You can modify the URLs and project title based on how you name your repository.
