# Journal for the project of Alchemist, a recipe generation web application #

## Namman Shukla (14088198) - Advanced Software Engineering - CP3407
### Overview 
This journal is my developement journey through coding this recipe web application, my side of the work handles producing the code for the locally hosted llm, training it to make it suitable for the requirements (recipe generation) and involving this in the web gui. 

### Resource Allocation
In terms of resources, the first thing that comes to mind is the 'openai' library which is essential to communicate with the LLM and parse through responses.
hosting of the llm will be on 'LM Studio'. training would be done on either hugging face or tensorflow. 

### Risk Management
As for risks, there are some to mention...the first one comes with the hardware as llms' can be extensively demanding to run so to have a model that runs on a medium-spec pc (so that it is accesible by anyone) while not effecting the generation capabilities of the model (look more into quantization). 
secondly, if the llm might cause an issue working with further there are plans to assist the web application with a web-scrapper instead.

### Personal Notes
20/3/24, 4:17 am : I am currently trying to scout a good model for recipe generation and check it's specs. the exact specs im looking for might jump around atleast 12 layers and 768 hidden units per layers. Pre-trained (so its easier to start with) using adam optimizer; rate of learning set to 1e-4 and batch size 32 for 10 epochs. I was thinking of fine tuning it using seq. lenght of 512 tokens and a perplexity loss function so its apt for reciepe generation because i need to think about the different cultural cuisine and dietary preferences with creativity control on the responses (maybe use a temprature sampling strategy).




