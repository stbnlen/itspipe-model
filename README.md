# ItsPipe Model

This Flask application is a form that uses inputs and a previously trained machine learning model to predict the outcome of a League of Legends match. The information about the player is extracted from a web scraper.

## Installation

To install the application, use the following command:

```
pip install -r requirements.txt
```
This command will install all the necessary dependencies required to run the application.

## Running the Application

To run the application, use the following command:

```
gunicorn main:app
```

This command will start the Gunicorn server and the application will be available at http://localhost:8000.

## How to Use

Once the application is running, go to http://localhost:8000 to access the form. Enter the required information and submit the form. The machine learning model will process the information and predict the outcome of the match.

## Credits

The machine learning model was trained using [OPGG Scraperr](https://github.com/stbnlen/opgg-scraper).

## License

This application is licensed under the MIT License.