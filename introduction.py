name = "Trupti Palande"
email="abc@gmail.com"
city = "Mumbai"
profession = "Software Engineer"
degree = "Bachelar in Electronics Engineering"
college = "Mumabi University"
experience = "20+ years of experience in hardware, R&D, software developemnt and devops"
skills = ".net windows and web application, ios development, sql , Git, azure devops, Machine Learning, REST APIs, Geneartive AI"
goal = "I want to become a professional AI Engineer and build intellegent automation systems."
hobby = "Reading Tech blogs, Travelling, gardening"
Func_fact="I started my career as hardware engineer, develop automation system for textile process automation and flow detection for railway for testing rail track. Later on work as team leader for developing software systems like ERP For Diamond Industry, WEb application, Business Intellegent solutions, and now AI Automation for Data Entry."
Country="India"

#demonstrate print of string
print(name)

# labelled printing using f-string and variable_name
print("Qualification :" ,degree)

# Write paragraph using f string and variables into paragraph

introduction = f"""
                Hi, my name is {name}. I am from {city}, I warok as a {profession} with {experience}.
                I completed ny {degree}. My technical skills include {skills}. My goal: {goal}. I enjoy {hobby}. """

print(introduction)

# slicing : extracting using substrings
username = email[0:3]
domain = email[4:]

print(username)
print(domain)

#cancatenation : will combine string using + operator
complete_Email = username + "@" + domain

print(complete_Email)

print("Length:", len(complete_Email))





