#from .frontend.questions import age, gender, employer, income, location

gender = "M"
age = 22
higher_education ="yes"
employer = "State Farm"
income = 33000
location = "miami, florida"
dependents = 0
ethnicity= "Hispanic"
prompt= f"""Given the information provided, gender:{gender},age:{age}, currently in college:{higher_education},
salary:{income},employer:{employer},location of person:{location}, number of dependents:{dependents},ethnicity:{ethnicity},
give me specific website links that this person can access to get finiancial help or benefits for themselves."""

prompt2= f"""Given the information provided from the last prompt: can you provide me three more specific ways 
to help this person get more finiancial help? please provide website links """

