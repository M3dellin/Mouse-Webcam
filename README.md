# Mouse-Webcam

# Webcam Mouse Controller

## Description

The **Webcam Mouse Controller** is a Python project that allows you to control your mouse cursor using your webcam. By leveraging computer vision techniques, this application tracks your hand movements and translates them into cursor movements, providing a hands-free alternative to traditional mouse input.

## Features

- **Hand Tracking**: Utilizes computer vision to detect and track hand movements.
- **Cursor Control**: Move the cursor based on hand position.
- **Click Simulation**: Simulate mouse clicks using hand gestures.
- **Customizable Settings**: Adjust sensitivity and tracking parameters for a better user experience.

## Requirements

- Python 3.x
- Libraries: 
  - `opencv-python`
  - `mediapipe`
  - `numpy`
  
You can install the required libraries using pip:

```bash
pip install opencv-python mediapipe numpy
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/seu-usuario/webcam-mouse-controller.git
   ```
2. Navigate to the project directory:
   ```bash
   cd webcam-mouse-controller
   ```
3. Run the script:
   ```bash
   python webcam_mouse.py
   ```

4. Follow the on-screen instructions to calibrate the system and start using your webcam as a mouse.

## Controls

- **Hand Movement**: Move your hand to control the cursor.
- **Click**: Use specific hand gestures to simulate left and right clicks (details on gestures can be added here).

## Disclaimer

This project is for educational purposes and may require adjustments based on your webcam and lighting conditions for optimal performance.

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b minha-nova-feature
   ```
3. Make your changes and commit:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin minha-nova-feature
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, feel free to open an issue or contact [seu-email@example.com].
