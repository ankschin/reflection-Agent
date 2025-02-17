from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI


## creating chains for reflection and generation of tweets

reflection_prompt= ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "you are a viral twitter influencer grading a tweet."
              "Generate critique and recommendations for the user's tweet"
            "Always provide detailed recommendations, including requests for length, variality, style, etc."
        ),
        MessagesPlaceholder(variable_name="messages"),

    ]
)

generation_prompt= ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "you are a twitter techie influencer assistant tasked with writing excellent twitter posts."
            "generate the best twitter post possible for the user's request"
            "If the user provides a critique, respond with a revised version of your previous attempt."

        ),
        MessagesPlaceholder(variable_name="messages")

    ]
)

llm= ChatOpenAI()
generate_chain= generation_prompt | llm

reflect_chain= reflection_prompt | llm



