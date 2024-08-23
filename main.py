from download_file.dowloadand_transcribe import trnscribe ,download_file
from abstract_use_openAIapi import abstract
from discord_connect import dc_abstract_notify

if __name__=="__main__":
    yt_url = input("please input youtube url")
    mp3_file_name = download_file(url=yt_url)
    text = trnscribe(mp3_file_name,model_type="medium")
    abstract_text = abstract(text)
    dc_abstract_notify(abstract_text=abstract_text,yt_url=yt_url)
    print("finish")