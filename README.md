## TEAM iSPY - Dell Product Recommendation System

The participants are required to fork this repository and create a private Gitlab repository under their own username (Single repository per team). The following created sections in this README.md need to be duly filled, highlighting the denoted points for the solution/implementation. Please feel free to create further sub-sections in this markdown, the idea is to understand the gist of the components in a singular document.

### Project Overview
----------------------------------

A brief description of 
>>Problem Statement: Design an Improved Product Recommendation System Engine based on user’s browsing habits across various IT domains.

>>Proposed Solution: Analysing the user's web browsing habits based on factors like his browsing history and cookie data and then implementing web scraping to get the kind of products the user is interested in and also the price range for the same. 
    Based on the sraped data, and the model dataset developed by our team using real time Data from Dell's website, implemented a Random Forest machine learning model to accurately predict the kind of Dell products, the user would most likely buy on a front end webpage designed in HTML+CSS with Flask. 

### Solution Description
----------------------------------

*  Out of the user's past 3 days browser history, we filter out all the e-commercial websites like Amazon, Flipkart, E-bay, HP, Lenovo, etc. ie. the sites where the users generally tend to search, compare and buy computing technologies like laptops, desktops, monitors etc. 


*  Then using the links we perform web scraping to get the data from these webpages to get the actions performed by the user in these websites and draw conclusions on the kind of products and the price range the user is interested in buying. 


*  We developed a real time dataset comprising of all the products Dell has to offer, group them by the price range, and the kind of product (gaming/non gaming laptops, desktops, monitors, all in 1 computers etc.)


*  After that we used a Random Forest algorithm to develop a machine learning model to accurately predict the kind of Dell products the user would most likely be interseted in. 


*  All of the backend scripting has been done in Python.


*  The front-end to host our solution has been designed in HTML and CSS and the backend has been integrated using Flask. 


#### Architecture Diagram



#### Technical Description

An overview of 
* Technologies/versions were used: 
    Python3 along with the libraries:
                                    numpy
                                    pandas
                                    sciKit learn
                                    beautiful soup 
                                    browser history
                                    requests
                                    lxml
    HTML5
    CSS
    Bootstrap 4.0
    Flask 1.1.1

* Setup/Installations required to run the solution:
    Python should be installed on the system to run the scripting in the backend.   
    Along with Python, all the libraries mentioned should also be involved. 


* Instructions to run the submitted code:
    Run the HTML file given in the application code folder.

### Team Members
----------------------------------

List of team member names and email IDs with their contributions: 

*  Akshat Gupta (ag555@snu.edu.in): Back-end development (machine learning models and dataset accumulation) + Ideation + Modelling

*  Nara Pratap (na189@snu.edu.in): Back-end development (web scraping) + Ideation + Modelling

*  Rebhav Guha (rg739@snu.edu.in): Back-end development (dataset accumulation and model training) + Ideation + Modelling

*  Daniel Vaz (dv415@snu.edu.in): Front end development + ideation + Modelling
