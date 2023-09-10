# Resident Assistant Interaction Log Automation Bot

Automate the process of filling out interaction logs for Resident Assistants at Georgia Tech using Selenium.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration and Usage](#configuration-and-usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Selenium bot automates the tedious task of filling out interaction logs for Resident Assistants at Georgia Tech by reading data from an Excel sheet and entering it into the required form.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- A code editor of your choice (e.g., VS Code, PyCharm).
- Google Chrome Browser

## Getting Started

### Installation

- Donwload the code from this repository and open it in a code editor
-  Open your terminal at that location and install the requiremnts using this command

   ```bash
   pip install -r requirements.txt
   ```
### Configuration and Usage
-  Open the excel sheet in the folder and enter the data. Make sure you only fill the gray cells.
-  Run the code and wait for the bot to fill the forms.
    ```bash
   python interaction_log_bot.py
   ```
   
## Additional Notes
- Ensure that you have a stable internet connection while running the bot.
- Make sure to keep your Excel spreadsheet and Chrome version are up to date.

## Disclaimer
This bot is provided as-is and for improving efficency only. Use it responsibly and in compliance with Georgia Tech's policies and guidelines. Automated data generation may be subject to restrictions, and any misuse is your responsibility.

## Contributing
Contributions are welcome! Due to ever changing dependencies and variation of this form across deparetments, this project would need maintaince. Please feel free to submit issues and pull requests to help improve this project.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

