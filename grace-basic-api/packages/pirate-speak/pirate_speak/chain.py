from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

_prompt = ChatPromptTemplate.from_messages(
    [
        # (
        #     "system",
        #     "Tell a joke. An",
        # ),
        ("human", "Tell me a joke about {topic}. "
                  "And answer me in {language}, even if my question is in a different language."),
    ]
)
_model = ChatOpenAI(model="gpt-4")

# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
chain = _prompt | _model
