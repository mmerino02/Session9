def greet4(first_name= "John", last_name="Doe"):
    """

    :param first_name: first name of the person, default=John
    :param last_name: last name, default=Doe
    :return: None
    """
    print(f"Hello {first_name} {last_name}, this is pretty cool, right?")

greet4("Lucas", "Baptiste") # Change to the 2 given imputs (Lucas Baptiste)
greet4() # Default values (John Doe)
greet4("James") # Changes the name and uses the default last name  (James Doe)

