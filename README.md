# python_challenge
To setup and run this application, first, replace xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx with your own api key from https://ipstack.com . The free tier is adequate for the scope of this project.


I have included a requirements.txt, so you can install those manually or do:
```
pip install requirements.txt
```
And then:
```
python3 logTracev1.0.py -f <filename>
```

![image](https://user-images.githubusercontent.com/90003728/132078137-2bf91583-bcec-4bbc-b1f5-d1f32656e51f.png)






## This challenge is as follows:

###Goal: Create a program in Python that will read a given set of IPs, perform Geo IP and RDAP lookups, and return the data back to the user. Objectives: This exercise is designed to test your ability to:

	● Take abstract requirements and run with them 
	● Write isolated decoupled modules with strict input/output interfaces
	● Reading, parsing and extracting IP addresses from unstructured text in an efficient manner 

Technical Requirements: 

	● Each component (GeoIP/RDAP/Parsing) should be as decoupled from the others as possible while still being easy to use. 
	● The main function should parse a text file containing 5000 IP addresses spread throughout random text. 
	● Do not use 3rd party packages that provide complete solutions for GeoIP queries or RDAP queries. Libraries simplifying HTTP requests (Requests), data manipulation (JSON), etc. are acceptable. 
	● The application must be operational through a Command Line Interface 
	● Please include context in your readme.md on how to setup and run your application 
	● A method of optimization, such as caching, should be implemented. You are free to choose any method for optimizing the HTTP requests. Some examples of not acceptable modules. Try to use as much of your own code as possible. 
	● MaxMind 
  	● Pandas 
