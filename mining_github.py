# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:19:55 2019

@author: z3525552
"""
import requests
import json


username = '' # Your GitHub username
password = '' # Your GitHub password

# Note that credentials will be transmitted over a secure SSL connection
url = 'https://api.github.com/authorizations'
note = 'tensorflow'
post_data = {'scopes':['repo'],'note': note }

response = requests.post(
    url,
    auth = (username, password),
    data = json.dumps(post_data),
    )   

print("API response:", response.text)
print()
print("Your OAuth token is", response.json()['token'])


# An unauthenticated request that doesn't contain an ?access_token=xxx query string
url = "https://api.github.com/repos/tensorflow/tensorflow"
response = requests.get(url)

# Display one stargazer
print(json.dumps(response.json()[0], indent=1))
print()

# Display headers
for (k,v) in response.headers.items():
    print(k, "=>", v)
    
#Get the access token for data mining    
ACCESS_TOKEN = ''
#user details for the data mining
USER = ''
#Repo details for data exploration
REPO = ''

from github import Github

client = Github(ACCESS_TOKEN, per_page=100)

user = client.get_user(USER)

repo = user.get_repo(REPO)

stargazers = [ s for s in repo.get_stargazers() ]
print("Number of stargazers", len(stargazers))

import networkx as nx # pip install networkx

# Create a directed graph

g = nx.DiGraph()

# Add an edge to the directed graph from X to Y

g.add_edge('X', 'Y')

# Print some statistics about the graph

print(nx.info(g))




print("Nodes:", g.nodes())
print("Edges:", g.edges())
print()

# Get node properties

print("X props:", g.node['X'])
print("Y props:", g.node['Y'])
print()

# Get edge properties

print("X=>Y props:", g['X']['Y'])
print()


g.node['X'].update({'prop1' : 'value1'})
print("X props:", g.node['X'])
print()

# Update an edge property

g['X']['Y'].update({'label' : 'label1'})
print("X=>Y props:", g['X']['Y'])


g = nx.DiGraph()
g.add_node(repo.name + '(repo)', type='repo', lang=repo.language, owner=user.login)

for sg in stargazers:
    g.add_node(sg.login + '(user)', type='user')
    g.add_edge(sg.login + '(user)', repo.name + '(repo)', type='gazes')


