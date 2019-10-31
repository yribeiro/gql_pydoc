import json
import requests

introspection_query = """{
    __schema{
        queryType{
            name
            fields{
                name
                description
            }
        }
    }
}"""

if __name__ == "__main__":
    # try and send request to the hacker news online API
    val = requests.post("https://countries.trevorblades.com", json={"query": introspection_query})
    content = json.loads(val.content.decode("utf-8"))

    print(json.dumps(content, indent=4))
