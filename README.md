![Imgur](https://i.imgur.com/OTF8YaPm.png?1)

RASA is a open source ChatBot development framework, which consists of all required components to develop and deploy a cahabot. 

In this project i'm developing a Conversation agent(Chatbot) from scratch using by assuming user journey of a customer.

There two important components of Conversational agent is 
       
         1) Natural Language Understanding module
            The responcibility of NLU module is to predict the user intention and to extract the additional avialable information such as entities.
         2) Dialogue Manager
            The responcibility of DM module is to maintain the contextual conversation by considering previous conversation using intent and entities.

**Project Enviroment: **
Use the conda command **conda env create -f enviroment.yml**, to replace the training.

**Data: **
Training data required for RASA 
     1) NLU data(intent and entity) is in **data/nlu** file.
     2) DM data is in **data/core** file.

**Models: **
The trained models are in **models** folder.

**Run Chatbot :**
To run the chatbot, create the project enviroment from above conda command.
After creating enviroment use following rasa commands in seperate terminals. 
1) **rasa run actions**
2) **rasa x --endpoints endpoints.yml**



