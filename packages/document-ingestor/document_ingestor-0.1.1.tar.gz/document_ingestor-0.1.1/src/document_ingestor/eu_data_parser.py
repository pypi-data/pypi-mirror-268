
import json
import tiktoken
from pinecone import Pinecone
import os
from openai import OpenAI
import csv
encoding = tiktoken.get_encoding("cl100k_base" )
def count_tokens(text):
    return len(encoding.encode(text))
    

def ingest_eu_data(file_path, output_csv_file_path, openai_api_key= "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", pinecone_api_key="f65cb3a9-0fb8-4137-b3aa-2d6bcf95d597", pinecone_index = "test"):
    doc_name = file_path.split("/")[-1]
    with open(file_path, "r", encoding = "utf8") as file:
        text = file.read()
    splited_text = []
    if count_tokens(text) > 8000:
        lines = text.split(".")
        new_text = ""
        tokens = 0
        for line in lines:
            tokens+= count_tokens(line)
            if tokens > 7000:
                splited_text.append(new_text)
                new_text = ""
                tokens = 0
            new_text += line
        if new_text:
            splited_text.append(new_text)
    else:
        splited_text.append(text)

    pc = Pinecone(api_key=pinecone_api_key)
    index = pc.Index(pinecone_index)
    last_index = index.describe_index_stats().total_vector_count
    os.environ["OPENAI_API_KEY"] = openai_api_key
    client = OpenAI()
    model = "text-embedding-ada-002"
    

    with open(output_csv_file_path, 'a', newline='') as file:
        for idx, text in enumerate(splited_text):
            response = client.embeddings.create(model=model, input=[text]).data[0]
            index.upsert([{"id": doc_name+"_"+str(idx), "values": response.embedding}])
            print("Ingested document: ", doc_name+"_"+str(idx))
            writer = csv.writer(file)
            new_entry = [doc_name+"_"+str(idx), "","", text]
            writer.writerow(new_entry)
    
            


                    


