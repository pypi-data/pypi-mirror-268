import pickle
import json
import os
from openai import OpenAI
import tiktoken
import time
from pinecone import Pinecone


def generate_embedding(data, openai_api_key="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"):
    # get rid of non-informative texts
    # for item in data:
    #     text_list = []
    #     for text in item['text']:
    #         # if number of words in text is less than 6 then delete that text
    #         if len(text.split()) > 6:
    #             text_list.append(text)
    #     item['text'] = text_list

    os.environ["OPENAI_API_KEY"] = openai_api_key
    client_openai = OpenAI()
    encoding = tiktoken.get_encoding("cl100k_base")
    embeddings = []
    model = "text-embedding-ada-002"
    vectors = []
    text_vectors = []
    metadata_vectors = []
    i = 0
    mxm_toen = 0
    token_count = 0
    min_toen = 5000
    for idx, item in enumerate(data):
        texts = item['text']
        curr_num_tokens = 0
        concatnd_text = ""
        for text in texts:
            curr_num_tokens = len(encoding.encode(text)) + curr_num_tokens
            concatnd_text = concatnd_text + "\n" + text
            if curr_num_tokens >= 5000:
                current_item = {k: v for k, v in item.items() if k != 'text'}
                current_item = {**current_item, "text": concatnd_text}
                text_vectors.append((text, current_item))
                token_count += curr_num_tokens
                curr_num_tokens = 0
                concatnd_text = ""
            # response= client.embeddings.create(input = [text], model=model).data[0].embedding
            # make a dictionary with everything except the 'text' from item and current text named current_item
            # current_item = {k: v for k, v in item.items() if k != 'text'}
            # current_item = {**current_item, "text": text}

            # text_vectors.append((text, current_item))
            # num_tokens = len(encoding.encode(text))
            # mxm_toen = max(mxm_toen, num_tokens)
            # min_toen = min(min_toen, num_tokens)
            # token_count += num_tokens
        if curr_num_tokens > 0:
            current_item = {k: v for k, v in item.items() if k != 'text'}
            current_item = {**current_item, "text": concatnd_text}
            text_vectors.append((text, current_item))
            token_count += curr_num_tokens
            curr_num_tokens = 0
            concatnd_text = ""
        if token_count > 60000:
            print("Token count exceeded")
            print("Token count: ", token_count)
            print("Index: ", i)
            print("idx:", idx)
            print("Total tokens: ", token_count)
            print("Text vectors: ", len(text_vectors))
            # print("Metadata vectors: ", len(metadata_vectors))
            text_contents = [row[0] for row in text_vectors]
            print(mxm_toen)
            print(min_toen)
            min_toen = 5000
            mxm_toen = 0
            try:
                response = client_openai.embeddings.create(
                    input=text_contents, model=model).data
            except:
                time.sleep(120)
                try:
                    response = client_openai.embeddings.create(
                        input=text_contents, model=model).data
                except:
                    print(
                        "OpenAI API request error! Please check your openAI credits or try after sometime.")
                    return None
            for idx, response in enumerate(response):
                vectors.append(
                    {"id": str(i), "values": response.embedding, "metadata": text_vectors[idx][1]})
                i += 1
            text_vectors = []
            token_count = 0
            # sleep for 1 min
            time.sleep(60)
    try:
        response = client_openai.embeddings.create(
            input=[row[0] for row in text_vectors], model=model).data
    except:
        time.sleep(120)
        try:
            response = client_openai.embeddings.create(
                input=[row[0] for row in text_vectors], model=model).data
        except:
            print(
                "OpenAI API request error! Please check your openAI credits or try after sometime.")
            return None

    for idx, response in enumerate(response):
        vectors.append({"id": str(i), "values": response.embedding,
                       "metadata": text_vectors[idx][1]})
        i += 1
    print("token_count:"+str(token_count))
    print('Embeddings generated successfully!')
    return vectors


def upload_embedding(vectors, pinecone_index_key="44951cc0-28e3-4cc2-a169-5125fcae1a88", index_name="test", namespace="ns1"):
    # encode the metadata as string in the vector from dict type
    for item in vectors:
        for key, value in item['metadata'].items():
            if isinstance(value, str):

                item['metadata'][key] = value
            else:
                item['metadata'][key] = value[0]

    # start a pinecone collection
    pc = Pinecone(api_key=pinecone_index_key)
    index = pc.Index(index_name)
    # get the last index of the current index
    last_index = index.describe_index_stats().total_vector_count

    # increase the id of all the vectors by the last Id
    for vector in vectors:
        vector['id'] = str(int(vector['id']) + last_index)

    # upsert into pinecone 5000 vectors per minute
    batch_size = 100
    for i in range(0, len(vectors), batch_size):
        batch = vectors[i:i+batch_size]
        index.upsert(batch)
        # time.sleep(60)
    print('Embeddings uploaded successfully!')
