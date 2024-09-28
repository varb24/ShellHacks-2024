from .frontend.questions import age, gender, employer, income, location, education, dependents, ethnicity
from .frontend.ai_questions import newresponse1, newresponse2, newresponse3
gender = "M"
age = 22
education ="yes"
employer = "HomeGoods"
income = 12000
location = "miami, florida"
dependents = 0
ethnicity= "Hispanic"
prompt= f"""Given the information provided, gender:{gender},age:{age}, currently in college:{education},
salary:{income},employer:{employer},location of person:{location}, number of dependents:{dependents},ethnicity:{ethnicity},
give me specific website links that this person can access to get finiancial help or benefits for themselves."""

prompt2= f"""Given the information provided from the last prompt: can you provide me three more questions
to ask this person to get more information and use that information to get other finiancial needs? can you format your json message
to be in a format like this "1": "**What are your short-term and long-term financial goals?**" """

prompt3=f""" Given the additional information provided ,{newresponse1},{newresponse2},{newresponse3}, and the last two prompts. 
Give me a new list of website links that this can acess to get finiancial help or benefits for themselves"""
