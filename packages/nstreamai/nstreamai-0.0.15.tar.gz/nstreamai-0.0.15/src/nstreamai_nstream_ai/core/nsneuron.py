from ..utils.logger import logger


class NstreamLLM(object):

    def __init__(self) -> None:
        logger.info("Initializing NstreamLLM")
        pass

    @staticmethod
    def feret_v1():
        logger.info("Fetching FERET_V1 model name")
        return "FERET_V1"

    @staticmethod
    def llama2_7b():
        logger.info("Fetching LLAMA2_7B model name")
        return "LLAMA2_7B"

    @staticmethod
    def mistral_7b():
        logger.info("Fetching MISTRAL_7B model name")
        return "MISTRAL_7B"


class NsNeuron(object):

    def __init__(self, llm: str) -> None:
        logger.info(f"Initializing NsNeuron with LLM: {llm}")
        self.llm = llm
        pass
