# dictionary = a collection of key-value pairs

capitals = {
    "USA": "Washington, D.C.",
    "India": "New Delhi",
    "China": "Beijing",
}

dir(capitals)  # This will show you all the methods available for dictionaries
help(capitals)  # This will show you the documentation for dictionaries

capitals["USA"]  # This will return "Washington, D.C."
capitals.get("India")  # This will return "New Delhi"
capitals.update({"Germany": "Berlin"})  # This will add a new key-value pair to the dictionary
capitals.pop("China")  # This will remove the key-value pair for "China"
capitals.popitem()  # This will remove the last inserted key-value pair from the dictionary
capitals.clear()  # This will remove all key-value pairs from the dictionary
capitals.keys()  # This will return a list of all the keys in the dictionary
capitals.values()  # This will return a list of all the values in the dictionary
