**ServiceNow GENAI solution using Ollama API**
Ollama provides a way to locally run LLM (large language models), using this approach it is possible to interact with a LLM from Servicenow midserver and inturn integrate with ServiceNow platform, in this post I am going to provide steps involved in this implementation.
Download and install Ollama on Midserver
Full list of instructions are provided here ollama/README.md at main · ollama/ollama · GitHub
In order to download on a windows machine download Ollama exe from https://ollama.com/download/OllamaSetup.exe
Install Ollama by running the exe file.
Go to command prompt and check if Ollama is correctly installed by executing ollama -v

![image](https://github.com/anilvaranasi/ollamaIntegration/assets/29941323/d086802b-8e87-451a-a3dd-8dcab606098e)

Download required LLM models, full list of available models is listed here : https://ollama.com/library
In order to download gemma DB model execute following command ollama run gemma:2b
Check list of available models using ollama list
C:\Users\Administrator>ollama list
NAME            ID              SIZE    MODIFIED
gemma:2b        b50d6c999e59    1.7 GB  3 hours ago
llama3:latest   a6990ed6be41    4.7 GB  25 hours ago
mistral:latest  61e88e884507    4.1 GB  23 hours ago
phi3:latest     a2c89ceaed85    2.3 GB  26 hours ago

Run a model using ollama run gemma:2b
Once model starts running it gives a prompt to interact with the model, enter a sample text to test the model
![image](https://github.com/anilvaranasi/ollamaIntegration/assets/29941323/43c49ce4-84f9-4dce-a4b8-3a15935695fe)
Once model is up and running and responding to the prompt, next step is to check if Ollama API is running, to do that open following url in any browser http://127.0.0.1:11434/
![image](https://github.com/anilvaranasi/ollamaIntegration/assets/29941323/45edb2bd-6c35-4324-aca0-27d7bc52ef32)
Next step is to create a simple REST API action in ServiceNow to communicate with Ollama API.
Open ServiceNow flow designer and create a new action, this action communicates with Ollama API using ServiceNow midserver, so ensure that midserver is running on same VM as the one that is running Ollama server.
![image](https://github.com/anilvaranasi/ollamaIntegration/assets/29941323/e920d2dc-1ccf-482e-aba6-ac0bd9aba774)
![image](https://github.com/anilvaranasi/ollamaIntegration/assets/29941323/f4fb1633-8716-47c1-9d7d-65216b98c58c)
![image](https://github.com/anilvaranasi/ollamaIntegration/assets/29941323/165dea4d-e313-4e2c-829b-498686d80472)
Once action is created, its time to test it, provide input text as the payload to API call.
{
  "model": "gemma:2b",
  "prompt": "Why is the sky blue?",
  "stream": false
}
![image](https://github.com/anilvaranasi/ollamaIntegration/assets/29941323/8102708b-1d1c-489d-87b0-0c8a25b271c7)
Output would look like below
![image](https://github.com/anilvaranasi/ollamaIntegration/assets/29941323/be61a350-84b9-43b7-88fe-8e51f81ba007)
{"model":"gemma:2b","created_at":"2024-05-09T13:35:14.3128433Z","response":"The sky appears blue due to Rayleigh scattering. Rayleigh scattering is the scattering of light by particles that have a size similar to the wavelength of light. This means that blue light, which has a shorter wavelength, is scattered more than other colors, giving the sky its characteristic blue color.","done":true,"context":[106,1645,108,4385,603,573,8203,3868,235336,107,108,106,2516,108,651,8203,8149,3868,3402,577,153902,38497,235265,153902,38497,603,573,38497,576,2611,731,16071,674,791,476,2395,3968,577,573,35571,576,2611,235265,1417,3454,674,3868,2611,235269,948,919,476,25270,35571,235269,603,30390,978,1178,1156,9276,235269,7385,573,8203,1277,17930,3868,2881,235265,107,108],"total_duration":109165898200,"load_duration":5010221800,"prompt_eval_count":15,"prompt_eval_duration":3284640000,"eval_count":57,"eval_duration":100860248000}
In above output we got response as single string vs a stream of chat because we have set the stream parameter to false.
Create a table to send the prompt and receive the response.
![image](https://github.com/anilvaranasi/ollamaIntegration/assets/29941323/53d14a49-127a-4f8b-a8d1-7787ce0fa0a2)
Update the action to update the prompt record with response
![image](https://github.com/anilvaranasi/ollamaIntegration/assets/29941323/021e5684-0dd0-4ddf-976f-b5ae4cd51161)
**Bringing it all together**
1.	Install Ollama on midserver VM
2.	Download required LLM such as gemma
3.	Create a flow designer action in ServiceNow to invoke Ollama server REST API
4.	Create a ServiceNow table to enter prompt and see response.
5.	Create a business rule on the table to invoke action created in step 3.
6.	Give a test prompt and check the response.


**Troubleshooting**
In order to run Ollama model review minimum CPU requirements for each model here : ollama/docs/gpu.md at main · ollama/ollama · GitHub
If Model is not responding or responding with socket error trying running a smaller model or running a model on a larger size machine
Check task manager if it a windows machine to see CPU and memory usage when the model is running.
![image](https://github.com/anilvaranasi/ollamaIntegration/assets/29941323/80097358-c785-44e8-af65-d5cfb4576e0d)
![image](https://github.com/anilvaranasi/ollamaIntegration/assets/29941323/058b028b-4e2b-4391-a199-7231e599ad97)











