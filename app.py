import re
import math
import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler


# Function to preprocess the expression for different mathematical symbols
def preprocess_expression(expression):
    # Handle factorial 'n!'
    expression = re.sub(r'(\d+)!', r'math.factorial(\1)', expression)
    
    # Handle square root symbol √ (example: √4 -> math.sqrt(4))
    expression = re.sub(r'√(\d+)', r'math.sqrt(\1)', expression)

    # Handle pi symbol π (example: π -> math.pi)
    expression = expression.replace('π', 'math.pi')

    # Handle Euler's number e (example: e -> math.e)
    expression = expression.replace('e', 'math.e')

    # Handle power operator ^ (example: 2^3 -> 2**3)
    expression = expression.replace('^', '**')

    # Handle trigonometric functions
    expression = re.sub(r'sin\((.*?)\)', r'math.sin(\1)', expression)
    expression = re.sub(r'cos\((.*?)\)', r'math.cos(\1)', expression)
    expression = re.sub(r'tan\((.*?)\)', r'math.tan(\1)', expression)

    # Handle logarithms (log base 10 and natural log)
    expression = re.sub(r'log\((.*?)\)', r'math.log(\1)', expression)
    expression = re.sub(r'log10\((.*?)\)', r'math.log10(\1)', expression)

    # Handle modulus (example: 10%3 -> 10 % 3)
    expression = expression.replace('%', ' % ')

    return expression


# Safe evaluation of the expression
def safe_eval(expression):
    try:
        processed_expression = preprocess_expression(expression)
        return eval(processed_expression, {"math": math})
    except Exception as e:
        return str(e)


# Tool for calculating mathematical expressions
def math_tool(expression):
    return safe_eval(expression)


# Set up the Streamlit app
st.set_page_config(page_title="Text To Math Problem Solver And Data Search Assistant", page_icon="🧮")
st.title("Text To Math Problem Solver Using Google Gemma 2")

# Input for the Groq API key
groq_api_key = st.sidebar.text_input(label="Groq API Key", type="password")

if not groq_api_key:
    st.info("Please add your Groq API key to continue")
    st.stop()

# Initialize the Groq LLM
llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# Initialize the Wikipedia tool
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the Internet to find various information on the topics mentioned."
)

# Initialize the Math tool using the safe_eval function
calculator = Tool(
    name="Calculator",
    func=math_tool,
    description="A tool for answering math-related questions. Only input valid mathematical expressions."
)

# Create a prompt template for logical reasoning and math explanations
prompt = """
You are an agent tasked with solving users' mathematical questions. Logically arrive at the solution and provide a detailed explanation, 
displaying it point by point for the question below.
Question: {question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

# Initialize the reasoning tool using the LLM chain
chain = LLMChain(llm=llm, prompt=prompt_template)
reasoning_tool = Tool(
    name="Reasoning Tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

# Initialize the agent with all the tools
assistant_agent = initialize_agent(
    tools=[wikipedia_tool, calculator, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# Initialize chat history if not already in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a Math chatbot who can answer all your math questions!"}
    ]

# Display the chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input for the user's question
question = st.text_area("Enter your question:")

# Handle the question submission
if st.button("Find my answer"):
    if question.strip():  # Ensure the question isn't empty or just whitespace
        with st.spinner("Generating response..."):
            # Append user's question to chat history
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            # Generate the response from the assistant agent
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])

            # Append assistant's response to chat history and display it
            st.session_state.messages.append({'role': 'assistant', 'content': response})
            st.write('### Response:')
            st.success(response)
    else:
        st.warning("Please enter a valid question.")
