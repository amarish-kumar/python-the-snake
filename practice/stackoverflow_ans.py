    >>> import json   
    >>>
    >>> # A simple attempt
    >>> s = "{\"description\":\"fdsafsa\"}"
    >>> python_dict = json.loads(s)
    >>> python_dict
    {u'description': u'fdsafsa'}
    >>> # Accessing value using key
    >>> python_dict["description"]
    u'fdsafsa'
    >>> 
    >>> # It worked, lets test our given string containing 2 dictionaries(in string form) one by one
    >>> # Converting 1st JSON string to Dict
    >>> s2 = "{\"description\":\"fdsafsa\",\"order\":\"1\",\"place\":\"22 Plainsman Rd, Mississauga, ON, Canada\",\"lat\":43.5969175,\"lng\":-79.7248744,\"locationDate\":\"03/24/2010\"}"
    >>> python_dict2 = json.loads(s2)                                                                                      >>> python_dict2
    {u'description': u'fdsafsa', u'order': u'1', u'place': u'22 Plainsman Rd, Mississauga, ON, Canada', u'lat': 43.5969175, u'lng': -79.7248744, u'locationDate': u'03/24/2010'}
    >>> 
    >>> # Converting 2nd JSON string to Dict
    >>> # remove comma(,) from end otherwise you will get the following error
    >>> s3 = "{\"description\":\"sadfdsa\",\"order\":\"2\",\"place\":\"50 Dawnridge Trail, Brampton, ON, Canada\",\"lat\":43.7304774,\"lng\":-79.8055435,\"locationDate\":\"03/26/2010\"},"
    >>> python_dict3 = json.loads(s3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/__init__.py", line 339, in loads
        return _default_decoder.decode(s)
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/decoder.py", line 367, in decode
        raise ValueError(errmsg("Extra data", s, end, len(s)))
    ValueError: Extra data: line 1 column 152 - line 1 column 153 (char 151 - 152)
    >>> 
    >>> # Now I removed comma(,) from end and retried, it worked
    >>> s3 = "{\"description\":\"sadfdsa\",\"order\":\"2\",\"place\":\"50 Dawnridge Trail, Brampton, ON, Canada\",\"lat\":43.7304774,\"lng\":-79.8055435,\"locationDate\":\"03/26/2010\"}"
    >>> python_dict3 = json.loads(s3) 
    >>> 
    >>> # So now we knew that we have not to include any extra comma at end in the string form of JSON
    >>> # For example (Correct form)
    >>> details_str = "{\"name\":\"Rishikesh Agrawani\", \"age\": 25}" 
    >>> details_dict = json.loads(details_str)
    >>> details_dict["name"]
    u'Rishikesh Agrawani'
    >>> details_dict["age"]
    25
    >>> # Now (Incorrect form), here comma(,) is at end, just after } 
    >>> details_str = "{\"name\":\"Rishikesh Agrawani\", \"age\": 25},"
    >>> details_dict = json.loads(details_str)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/__init__.py", line 339, in loads
        return _default_decoder.decode(s)
      File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/decoder.py", line 367, in decode
        raise ValueError(errmsg("Extra data", s, end, len(s)))
    ValueError: Extra data: line 1 column 41 - line 1 column 42 (char 40 - 41)
    >>> 
    >>> # The problem is the string does not denote any single python object 
    >>> # So we will convert the string into a list form by appending [ at beginning and ] at end
    >>> # Now our string will denote a single Pytohn object that is list of 2 dictioanaries
    >>> # Lets do this, here I am storing the given string into variable s4
    >>> data_str = "{\"description\":\"fdsafsa\",\"order\":\"1\",\"place\":\"22 Plainsman Rd, Mississauga, ON, Canada\",\"lat\":43.5969175,\"lng\":-79.7248744,\"locationDate\":\"03/24/2010\"},{\"description\":\"sadfdsa\",\"order\":\"2\",\"place\":\"50 Dawnridge Trail, Brampton, ON, Canada\",\"lat\":43.7304774,\"lng\":-79.8055435,\"locationDate\":\"03/26/2010\"},"
    >>> s5 = "[" + s4[0:1] + s4[1: len(s4)-1] + "]"
    >>> s5
    '[{"description":"fdsafsa","order":"1","place":"22 Plainsman Rd, Mississauga, ON, Canada","lat":43.5969175,"lng":-79.7248744,"locationDate":"03/24/2010"},{"description":"sadfdsa","order":"2","place":"50 Dawnridge Trail, Brampton, ON, Canada","lat":43.7304774,"lng":-79.8055435,"locationDate":"03/26/2010"}]'
    >>> # l is a list of 2 dictionaries
    >>> l = json.loads(s5)
    >>> l[0]
    {u'description': u'fdsafsa', u'order': u'1', u'place': u'22 Plainsman Rd, Mississauga, ON, Canada', u'lat': 43.5969175, u'lng': -79.7248744, u'locationDate': u'03/24/2010'}
    >>> 
    >>> l[1]
    {u'description': u'sadfdsa', u'order': u'2', u'place': u'50 Dawnridge Trail, Brampton, ON, Canada', u'lat': 43.7304774, u'lng': -79.8055435, u'locationDate': u'03/26/2010'}
    >>>                                                           