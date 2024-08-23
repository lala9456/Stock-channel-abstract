from pytubefix import YouTube
from pytubefix.cli import on_progress
import re
import whisper
import os
import torch

def download_file(url:str):
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)
    mp3_file_name = re.sub(r'[\/:*?"<>|[\]#]', '_', yt.title)
    ys = yt.streams.get_audio_only()
    print(f"Starting to download {yt.title}")
    ys.download(mp3=True,output_path="./mp3file",filename=mp3_file_name) # pass the parameter mp3=True to save in .mp3
    print(f"{yt.title} has been download successfully and been saved as {mp3_file_name}.mp3")
    return(f"{mp3_file_name}.mp3")

def trnscribe(mp3_file_name:str,model_type):
    device = "cuda" if torch.cuda.is_available() else "cpu" 
    model_path = os.path.join(os.getcwd(),"model",f"{model_type}.pt")
    print("loading model")
    print(f"device:{device}")
    print("-"*20)
    model = whisper.load_model(model_path,device=device)
    print("Starting to transcribe")
    result = model.transcribe(os.path.join(os.getcwd(),"mp3file",mp3_file_name))
    print("Transcribe successfully")
    
    print(result["text"])
    print("Writing into txt............")
    output_file_name = mp3_file_name.replace(".mp3",".txt")
    with open(os.path.join(os.getcwd(),"subtitle",output_file_name), "w", encoding="utf-8") as f:
        f.write(result["text"])
    return(result["text"])



if __name__=="__main__":
    # url = "https://www.youtube.com/watch?v=sxpFspYPL8M"
    url = input("please input youtube url")
    mp3_file_name = download_file(url=url)
    trnscribe(mp3_file_name,model_type="medium")
    print("finish")