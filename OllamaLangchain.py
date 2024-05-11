from langchain_community.llms import Ollama
import sys
prompt_model = sys.argv[1]
prompt_input = sys.argv[2]
llm = Ollama(model=prompt_model)
#print(llm.invoke("Tell me a joke"))
print(llm.invoke(prompt_input))
