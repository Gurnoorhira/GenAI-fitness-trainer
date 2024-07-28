#import openai to interact with the OpenAI GPT-3.5 Turbo model, gradio to create an interface for chatbot
import openai
import gradio

#open api key to allow requests to be made to GPT-3.5 Turbo model
openai.api_key = ""
#messages list to set context of conversation, informs GPT-3.5 turbo model that its a fitness expert
messages = [{"role": "system", "content": "You are a fitness expert that specializes in weight loss and muscle building"}]
#chatbox function to handle conversation with chatbot, taking in user_input argument which is user's message
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input}) #add user input to messages list with role user
    response = openai.ChatCompletion.create( 
    #api call to openAI taking entire conversation history of messages list as input and generating response          
        model = "gpt-3.5-turbo",
        messages = messages
    )
    #response stored in chatGPT_reply, then added to messages list with role assistane then returned
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply
#gradio.interface created to display interactive chat window for user
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Personal Trainer")

#allows a gradio link that can be shared 
demo.launch(share=True)
