from langchain_core.prompts import PromptTemplate
template=PromptTemplate.from_template(
    "Explain {topic} in simple language."
)
print(template.format(topic="Machine Learning"))