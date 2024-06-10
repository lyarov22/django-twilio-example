# DJANGO + TWILIO SMS & WhatsApp OTP Code Verification Example

This project demonstrates how to implement SMS and WhatsApp OTP (One-Time Password) code verification using Django and Twilio.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/lyarov22/django-twilio-example
    cd django-twilio-example
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    
    # On Linux
    source venv/bin/activate
    
    # On Windows
    venv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure your Twilio keys and numbers:
    Open `twiliotutorial/twiliotutorial/settings.py` and update lines 129-133 with your Twilio account details.

5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Pages

- **Registration Page:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Check Verified Status:** [http://127.0.0.1:8000/home](http://127.0.0.1:8000/home)

## Original Tutorial

This project is based on the tutorial from the [Twilio blog](https://www.twilio.com/en-us/blog/enable-multiple-otp-methods-django#Create-the-connection-between-Django-and-Twilio).
