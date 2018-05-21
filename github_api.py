# Github API example
import requests

url_assignees = "https://api.github.com/repos/saltstack/salt/assignees"
# saltstack - organization name
# salt - repo name
req = requests.get(url_assignees)
print("Status code:", req.status_code)
# 200 is OK

response_dict = req.json()
print("SALT REPO ASSIGNEES: ")
for i in response_dict:
    print("LOGIN " + i['login'])
# SALT REPO ASSIGNEES:
# LOGIN aaronfrost
# LOGIN alexey-zhukovin
# LOGIN alexpeay
# LOGIN basepi
# LOGIN bertdawg76
# LOGIN brejoc
# LOGIN bronzeswallow
# LOGIN cachedout
# LOGIN cavalheiro
# LOGIN Ch3LL
# LOGIN cro
# LOGIN damon-atkins
# LOGIN davegiles
# LOGIN dincamihai
# LOGIN DmitryKuzmenko
# LOGIN dmurphy18
# LOGIN doesitblend
# LOGIN dubb-b
# LOGIN dwoz
# LOGIN frogunder
# LOGIN garethgreenaway
# LOGIN geek-at-heart
# LOGIN grichmond-salt
# LOGIN gtmanfred
# LOGIN isbm
# LOGIN jacobhammons
# LOGIN jaronimo99
# LOGIN jeffblair
# LOGIN jrporcaro
# LOGIN jsbalrog
