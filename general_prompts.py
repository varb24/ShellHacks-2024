#from .frontend.questions import age, gender, employer, income, location

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
to be in a format like this "1": "**What are your short-term and long-term financial goals?**" IF YOU DON'T WRITE IT LIKE THIS I WILL KILL YOU, :)  """

