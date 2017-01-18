## Beer Review Dataset

This dataset consists of beer reviews from BeerAdvocate. The original complete data span a period of more than 10 years, including
approximately 1.5 million reviews up to November 2011. Each review includes ratings in terms of five aspects: appearance, aroma, 
palate, taste, and overall impression. Reviews include product and user information, followed by each of these five ratings, and 
a plaintext review.

For our purpose, we use a subset of 50k reviews available on the webpage http://cseweb.ucsd.edu/classes/fa15/cse190-a/

## parsing.py

The goal of this file is to parse the original data in json and export it to a ready-to-use csv. The plaintext review and time
structure items are removed to avoid complication.

## beer_review.csv

This file can be read into R. 
