# RokuDigital 📺

![image](https://github.com/0xMxnTy/rokudigital/assets/166342298/d29515fc-4378-4066-bea8-40ca21c2078f)

`Welcome to **RokuDigital**, the ultimate CLI tool for controlling your Roku TV! Easily send commands to your Roku device using an interactive command prompt. 🚀`

## Features ✨

- **Interactive CLI**: Control your Roku TV using a command-line interface.
- **Easy Navigation**: Send keypress commands like `home`, `up`, `down`, and more.
- **App Launching**: Launch apps by their ID effortlessly.
- **Colorful Output**: Enjoy a vibrant and user-friendly interface with color-coded messages.

![image](https://github.com/0xMxnTy/rokudigital/assets/166342298/8adcbf28-8225-437f-815d-ad6e596f8bd5)

## Getting Started 🎬

### Prerequisites ⚙️

- Python 3.x
- `requests` library
- `colorama` library

Install the required libraries using pip:

`pip install requests colorama`

## Installation 🚀

Clone the repository:

```
git clone https://github.com/yourusername/rokudigital.git
cd rokudigital
```

## Usage ⚒️

Make the script executable (optional):

`chmod +x rokudigital.py`

Run the script:

`./rokudigital.py`

or

`python3 rokudigital.py`

## Interactive CLI Commands 📟

Once the script is running, use the following commands:

    Launch an App: launch <app_id>
    Send Keypress:
        home
        up
        down
        left
        right
        select
        play
        pause
    Exit CLI: exit

## Example 📝

```
Welcome to rokudigital! Enter your Roku IP address: 192.168.0.136
rokudigital> home
[+] Successfully sent command to http://192.168.0.136:8060/keypress/home
rokudigital> launch 837
[+] Successfully sent command to http://192.168.0.136:8060/launch/837
rokudigital> exit
Exiting...
```

## Contributing 🤝

Contributions are welcome! Please fork the repository and submit a pull request.

    Fork the repository
    Create your feature branch (git checkout -b feature/YourFeature)
    Commit your changes (git commit -m 'Add some feature')
    Push to the branch (git push origin feature/YourFeature)
    Open a pull request

## License 📜

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements 🙌

    Colorama for the colorful terminal output.
    Requests for handling HTTP requests.

Feel free to reach out if you have any questions or feedback.
