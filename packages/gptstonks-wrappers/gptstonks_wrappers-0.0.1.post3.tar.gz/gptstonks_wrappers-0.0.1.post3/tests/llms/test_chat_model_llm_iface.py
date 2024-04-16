import os
from collections import namedtuple
from unittest.mock import patch

from gptstonks.wrappers.llms.chat_model_llm_iface import ChatModelWithLLMIface
from langchain.chat_models import ChatOpenAI


@patch.object(ChatOpenAI, "_generate", return_value=namedtuple("output", "generations")([]))
def test_chat_model_llm_iface(mocked_generate):
    os.environ["OPENAI_API_KEY"] = "randomkeyfortesting"
    chat = ChatModelWithLLMIface(chat_model=ChatOpenAI(temperature=0))
    chat._generate(["Generate some random story"])

    mocked_generate.assert_called_once()
