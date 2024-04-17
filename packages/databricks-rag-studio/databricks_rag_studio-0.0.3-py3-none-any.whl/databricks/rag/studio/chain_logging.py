import mlflow


def set_chain(chain):
    """
    After defining your LangChain in a Python file or notebook, call
    set_chain() so that it can be identified later when logging the
    chain with the log_model() method.

    :param chain: The LangChain model instance that is defined in a
                  Python notebook or file.
    """
    mlflow.langchain._rag_utils._set_chain(chain)
