# Clothero

+<img src="https://github.com/ramsuthar305/Clothero/blob/master/ezgif.com-video-to-gif.gif?raw=true" width="800px" style="margin-auto">
* ## Introduction
    *  AI-based shopping assistance for both man and woman using transfer learning and statistics like Cosine and Pearson similarity metrics. The basic idea behind the project is passing image data through a Pre-trained model [Mobilenet_v2] for extracting feature vector which is flattened out in the end. The output from this goes through a comparison metric called cosine similarity metric which is computed between users choice of cloth and the database vectors, scrapped from amazon.in

* ## Pre-requisites
    1. Transfer Learning
         here we have used pre-trained model for feature extractor ,particularly
    2. Statistics
        Basic knowledge about similarity metrics like Cosine , Pearson
    3. Web-scrapping
         using webscraping various shopping sites for data for building the prototype using scrapy
    4. Web-technologies
        Baiscs of CSS, HTML, JAVASCRIPT , Flask ,JQuery
    5. Database
        No-sql database like Mongodb
   
* ## Installation requirements
    1. Python3
        * numpy
        * tensorflow
        * pandas
        * pymongo
        * scrapy
        * math
    2. Databse
        * Mongodb
    3. Backend
        * Flask
    4. Front
        * CSS
        * HTML
        * JAVASCRIPT
        * JQuery
* ## Intallation
    1. Clone the repository
    2. Install mongodb
    3. Preprocess data i.e create vectors of images path with the help of `Clothero.ipynb` in the root directory and sample data csv for preprocessing can be found in `img-databse` folder.
    4. Import processed csv file in your mongodb database
    5. Install the requirements
        * for Windows users
            > pip install -r requirements.txt

        * for Ubuntu users
            > pip3 install -r requirements.txt
           
    6. Start the server
      `cd server`
      `flask run`
* ## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



* ## Reach us

* Ram Suthar
[LinkedIn](https://www.linkedin.com/in/ramsuthar305/) | [Github](https://github.com/ramsuthar305)

* Krish Shah
[LinkedIn](https://www.linkedin.com/mwlite/in/krish-shah-20542817b) | [Github](https://github.com/krishshah99615)

    
