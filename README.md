# Clothero
* ### Introduction
    *  Web-based Image cloth recommendation for both man and woman using transfer learning and statistics like Cosine and Pearson similarity metrics. The basic idea behind the recommendation system is passing image data through a Pre-trained model [Mobilenet_v2] for extracting feature vector which is flattened out in the end. The output from this goes through a comparison metric called cosine similarity metric which is computed between users choice of cloth and the database vectors, scrapped from amazon.in

* ### Pre-requisites
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
    
* ### Intallation requirements
    1. Python
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
* ### Intallation 
    1. Clone the repository
    
    2. Install the requirements
        * for Windows users
            > pip install -r requirements.txt

        * for Ubuntu users
            > pip3 install -r requirements.txt
            
    3. Start the server
        * for Windows users
            > cd server
            
            > python app.py
        
        * for Ubuntu users
            > cd server
            
            > python3 app.py



    
