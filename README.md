# IRCTC-Automation-Tatkal-and-General-Ticket-Booking-
IRCTC Automation with GUI For booking Tatkal/General ticket with COD option(Verified).

Please fill all the details in the GUI form and click Book Tatkal ticket. It will automatically book the ticked with COD option.
Run this script at 11 O'Clock for Sleeper and at 10 O'Clock for AC tickets.

Note: Please put same station name as well as date mentioned in IRCTC.
Basic Requirement Selenium module, and Web driver for chrome

For Captcha , Waiting timing is provided. Provide it witin 10s so everything will work fast and properly.

Please Use latest chrome extension for script to work.
As well Script need modification as webpage has been changed over the time.

![GUI](https://github.com/PrajinkyaPimpalghare/IRCTC-Automation-Tatkal-and-General-Ticket-Booking-/blob/master/GUI.PNG)

# IRCTC Automation with GUI using Selenium and Python

## Overview

This Python script allows you to automate the process of booking Tatkal or General train tickets on the Indian Railways IRCTC website using a graphical user interface (GUI). It uses the Selenium library to interact with the website and Chrome WebDriver as the browser automation driver.

## Prerequisites

Before running the script, you need to have the following installed:

1. **Python 3:** If you don't have Python 3 installed, you can download it from [python.org](https://www.python.org/downloads/).

2. **Selenium:** Install the Selenium library using pip:

    ```bash
    pip install selenium
    ```

3. **Chrome WebDriver:** Download the Chrome WebDriver that matches your Chrome browser version. You can download it from the official ChromeDriver page: [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).

   - Extract the downloaded WebDriver executable and place it in a directory that is included in your system's PATH environment variable. Alternatively, you can specify the path to the WebDriver executable in the script.

## Usage

1. Clone this repository or download the script (`irctc_automation.py`) to your local machine.

2. Make sure you have met the prerequisites mentioned above.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Run the script using Python:

    ```bash
    python irctc_automation.py
    ```

5. The GUI for IRCTC automation will open. Fill in all the required fields with your IRCTC login and passenger details.

6. Click the "Book Tatkal Ticket" button to start the automation process.

7. The script will automate the IRCTC website to book the ticket according to the provided details. It will choose the Cash on Delivery (COD) option.

8. After the booking process is complete, the script will exit.

## Disclaimer

This script is provided for educational and personal use only. The use of automated scripts to book tickets on IRCTC may be against their terms of service. Use it responsibly and at your own risk.

## License

This script is released under the MIT License. See the [LICENSE](LICENSE) file for details.
