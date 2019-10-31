import os
import jinja2
import json
import requests

from gql_pydoc.gql_docs import introspection_query


class GqlPyDoc:
    """ Class to ping a graph endpoint and generate documentation from the schema """

    def __init__(self, endpoint: str):
        self._endpoint = endpoint

    def get_schema_info(self):
        val = requests.post(self._endpoint, json={"query": introspection_query})
        content = json.loads(val.content.decode("utf-8"))
        return content


if __name__ == "__main__":
    # try and send request to the hacker news online API
    docs = GqlPyDoc("https://countries.trevorblades.com")
    schema = docs.get_schema_info()

    print(json.dumps(schema, indent=4))

    # example code to render html templates
    with open(os.path.join(os.getcwd(), "..", "templates", "index.html"), "r") as fp:
        template = jinja2.Template(fp.read())
        print(template.render(title="My GraphQL Schema Page"))
