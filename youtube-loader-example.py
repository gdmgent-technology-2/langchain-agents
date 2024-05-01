# Langchain
from langchain.document_loaders import YoutubeLoader

loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=v2AC41dglnM&pp=ygUFQUMvREM%3D", add_video_info=True)
result = loader.load()
print (type(result))
print (f"Found video from {result[0].metadata['author']} that is {result[0].metadata['length']} seconds long")
print ("")
print (result)