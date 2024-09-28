from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# One way to use langchain
system_template = "Translate the following from English into Italian"
system_template_extra = "Translate this into swahili, but add another word"
# shows two ways to add variables
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
prompt_template_2 = ChatPromptTemplate.from_messages(
    [("system", system_template_extra), ("user", "{text}")]
)
result = prompt_template.invoke({"language": "italian", "text": "hi"})

result.to_messages()
print(result)

#chains go in this direction start -> finish
chain = prompt_template | model | prompt_template_2 | model | parser

print(chain.invoke({"language": "italian", "text": "hi"}))
# A different way to use langchain
# messages = [
#     SystemMessage(content=system_template),
#     HumanMessage(content="hi!"),
# ]

# # result = model.invoke(messages)
# # print(parser.invoke(result))
# # Chains model into parser
# chain = model | parser
# print(chain.invoke(messages))
