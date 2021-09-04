# python_challenge
This program will read a given set of IPs, perform Geo IP and RDAP lookups, and return the data back to the user.
To setup and run this application, first, replace xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx with your own api key from https://ipstack.com . The free tier is adequate for the scope of this project.


I have included a requirements.txt, so you can install those manually or do:
```
pip install requirements.txt
```
And then:
```
python3 logTracev1.0.py -f <filename>
```

Sample Result:
![image](https://user-images.githubusercontent.com/90003728/132078733-dbef153b-03b1-45b5-a825-f546e894aba8.png)


# P.S. this is designed to extract any found IP addresses, and works on any txt log or even .eml (email files)!


