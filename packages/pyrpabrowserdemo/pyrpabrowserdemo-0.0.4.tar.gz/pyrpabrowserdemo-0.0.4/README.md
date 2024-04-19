# pyrpabrowserdemo

pyrpabrowserdemo is a Python library for web automation tasks using the Robot Process Automation (RPA) approach. It provides a simplified interface for interacting with web pages using Selenium WebDriver and HTTP requests.

## Features

- **Browser Automation**: Automate web interactions such as opening browsers, navigating to URLs, clicking elements, filling forms, and more.
- **Frame Handling**: Easily switch between frames within a web page.
- **File Download**: Download files from URLs using HTTP requests.
- **Element Interaction**: Click on elements by XPath, ARIA labels, or select elements within frames.
- **Wait Conditions**: Wait for elements to become visible before interacting with them.

## Installation

You can install pyrpabrowserdemo via pip:

```bash
pip install pyrpabrowserdemo
```

## Usage

```python
from pyrpabrowserdemo import Browser

# Create a browser instance
browser = Browser()

# Open a browser and navigate to a URL
browser.open_browser("https://example.com")

# Fill a form field
browser.fill("//input[@id='username']", "my_username")

# Click on a button by ARIA label
browser.click_by_aria_label("Submit")

# Switch to a frame by XPath
browser.change_to_frame("//iframe[@class='frame']")

# Click on an element by XPath
browser.click("//button[@id='submit']")

# Download a file from a URL
browser.download_file("https://example.com/download/file.pdf")
```