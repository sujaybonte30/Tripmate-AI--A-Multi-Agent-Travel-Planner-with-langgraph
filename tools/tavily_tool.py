from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key= os.getenv("TAVILY_API_KEY")      
)


def tavily_search(query):
    response = client.search(
       query= query,
       max_results= 5 
    )

    results = []

    for i,r in enumerate(response["results"], 1):
        title  = r.get("title","Unknown")  
        url    = r.get("url","")
        sinppet = r.get("content","").strip()

        if len(sinppet) > 300:
         sinppet = sinppet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{i}. **{title}**\n  {url}\n  {sinppet}")   

    return "\n\n".join(results)    