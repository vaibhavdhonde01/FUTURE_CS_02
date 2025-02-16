# FUTURE_CS_02
# Password Strength Analyzer

## Description
The **Password Strength Analyzer** is a Python-based GUI application designed to evaluate the security of user-provided passwords. It analyzes password strength using the `zxcvbn` library, calculates entropy, generates SHA-256 hashes, and provides suggestions for improving weak passwords. The application is built with **Tkinter** and **ttkbootstrap** to provide a modern, visually appealing interface.

## Features
- **Real-time Password Strength Analysis** (Very Weak, Weak, Medium, Strong, Very Strong)
- **Entropy Calculation** for better security insights
- **SHA-256 Hash Generation** for secure representation
- **User-Friendly GUI** with an eye-catching background image
- **Suggestions for Improving Weak Passwords**

## Technologies Used
- **Python** (Core Language)
- **Tkinter** (GUI Development)
- **ttkbootstrap** (Modern Theming)
- **zxcvbn** (Password Strength Analysis)
- **hashlib** (SHA-256 Hashing)

## Installation
Ensure you have Python installed. Then, install the required dependencies:

bash
pip install ttkbootstrap 
pip install zxcvbn
```

## Usage
1. Run the script:
   bash
   python password_strength_analyzer.py
   ```
2. Enter a password in the input field.
3. Click **Analyze** to check its strength, entropy, and SHA-256 hash.
4. View password strength suggestions if applicable.
5. Click **Clear** to reset the input field.

## Files Included
- `password_strength_analyzer.py` - Main application script
- `background.png` - Background image for GUI
- `README.md` - Documentation for the project

## Screenshots
![image](https://github.com/user-attachments/assets/a2ba1527-5a90-4b65-ae46-491c5c1eb10e)

## License
This project is licensed under the MIT License.

## Author
Developed by **Vaibhav**

