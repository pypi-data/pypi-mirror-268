from langchain_community.llms import Bedrock

llm = Bedrock(model_id="anthropic.claude-v2:1",
              region_name="us-east-1",
              )


def count_token(message):
    num_token = llm.get_num_tokens(message)
    print("Num of Token Found", num_token)
    return num_token


def send(message, token, client_id):
    return message + ":" + token + ":" + client_id


def receive(client_id):
    return client_id + ":" + "Hello"
