# edds - The Central Bank of the Republic of Türkiye Electronic Data Distribution System Data Access Package

This package provides easy-to-use functions to retrieve data from the Central Bank of the Republic of Turkey (TCMB) Economic Data Distribution System (EDDS) web service.

# Features

## Get Categories:

Retrieve a list of all data categories in EVDS as a Pandas DataFrame.

## Get Data Groups:

Retrieve a list of data groups within a specific category as a Pandas DataFrame.

## Get Series:

Retrieve a list of series within a specific data group as a Pandas DataFrame.

## Get Data:

Retrieve data for a specific series and date range as a Pandas DataFrame.

## User-Friendly:

Functions use simple and intuitive parameters.

## Error Handling:

Improved error handling with custom exception classes (InputError, SerieNotFoundError).

# Installation

pip install edds

# Usage

from edds import edds

## Enter your API key

api_key = "YOUR_API_KEY"

## Create an edds object

evdsa = edds(api_key)

## Get categories

evdsa.categories

## Use the CATEGORY_ID of the category

evdsa.data_groups(CATEGORY_ID)

## Get series for the data_groups

evdsa.series("DATAGROUP_CODE")

## Get data for the series

evdsa.get_data('SERIE_CODE', startdate="START_DATE", enddate="END_DATE")

# EXAMPLE

evdsa = edds('api_key')

evdsa.categories evdsa.data_groups(23)

evdsa.series("bie_tisguc")

evdsa.get_data('TP.TIG04', startdate="01-01-2014", enddate="01-01-2020")

# License

This package is licensed under the MIT License.

# Contact

Please contact us for any questions or feedback.
