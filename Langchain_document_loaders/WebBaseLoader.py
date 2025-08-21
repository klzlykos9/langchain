from langchain_community.document_loaders import WebBaseLoader
import os



url = 'https://www.amazon.in/HP-i3-1315U-Anti-Glare-Micro-Edge-fd0573TU/dp/B0F4R3GFMQ/ref=sr_1_4?adgrpid=94221362531&ext_vrnc=hi&hvadid=590450674960&hvdev=c&hvlocphy=9300861&hvnetw=g&hvqmt=e&hvrand=8038718193082432984&hvtargid=kwd-353766051967&hydadcr=16601_2163995&mcid=1c11e2187bb238fb8c38026e68aa3fa6&sr=8-4'

loader = WebBaseLoader(url)


docs = loader.load()

print(len(docs))

print(docs[0].page_content)