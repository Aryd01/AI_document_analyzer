from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import os 
from dotenv import load_dotenv
load_dotenv()
def get_text_chunks(text):
  text_splitter = CharacterTextSplitter(separator="\n", chunk_size=500,chunk_overlap=150,length_function=len)
  chunks =  text_splitter.split_text(text)
  return chunks

def get_vector_store(chunks):
  embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("openai_api_key"))
  vectorstore =FAISS.from_texts(texts=chunks,embedding=embeddings)
  return vectorstore

def get_conversation_chain(vectorstore):
  llm = ChatOpenAI(openai_api_key=os.getenv("openai_api_key"))
  memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
  conversation_chain= ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever(),memory=memory)
  return conversation_chain
def handle_input(prompt):
  response = conversation({'question':prompt})
#   print(response)
#   print("user1:"+response['question'])
#   print("bot1:" + response['answer'])
  chat_history = response["chat_history"]
  print(chat_history[-1].content)
  # for i , message in enumerate(chat_history):
  #   if i%2==0:
  #       pass
  #       # print("user:"+ message.content)
  #       # print()
  #   else:
  #     print("bot:" + message.content)
  #     print()


file = open("document.txt","r")
text = ""
for i in file:
  text+=i

chunks = get_text_chunks(text)
print(len(chunks))

vectorstore = get_vector_store(chunks)

conversation = get_conversation_chain(vectorstore)
flag= True

while flag:
    question = input("user:enter a prompt :")
    print()
    val = handle_input(question)
    follow = input("want to continue conversation y or n: ")
    print()
    if (follow=="n" or follow =="N"):
       flag = False
















