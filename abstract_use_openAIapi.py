from download_file.dowloadand_transcribe import download_file , trnscribe
from openai import OpenAI
import os



def abstract(text:str):
    os.environ.get("OPENAI_API_KEY")
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": f"請幫我摘要這個投資節目的逐字稿並且條列式 回傳的摘要文字逐條間要加上換行符號:{text}"}
    ]
    )
    print(completion.choices[0].message.content)

    return(completion.choices[0].message.content)

if __name__=="__main__":
    url = input("please input youtube url")
    mp3_file_name = download_file(url=url)
    abstract_text = trnscribe(mp3_file_name,model_type="medium")
    abstract(abstract_text)
    print("finish")