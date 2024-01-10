import weaviate
import weaviate.classes as wvc
import os

client = weaviate.connect_to_wcs(
    cluster_url="https://juofherxrfgo1cki4ierfa.c1.europe-west3.gcp.weaviate.cloud",
    auth_credentials=weaviate.AuthApiKey("RfyaBcQcbicZifmJp4fi0AmgnvGM5bUJYYjm"),
    headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")  # Replace with your own API key
    },
)

movies = client.collections.get("Movie")

response = movies.query.bm25(  # Keyword search for the word "love"
    query="love",
    limit=3,
    return_metadata=wvc.query.MetadataQuery(score=True),
)

for o in response.objects:
    print(o.properties["title"])  # Show which titles were found
    print(o.properties["description"])  # Show the description
    print(f"{o.metadata.score:.3f}")  # What was the score?
    print()
