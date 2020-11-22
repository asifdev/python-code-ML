#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 01:05:33 2020

@author: anttor
"""
import pandas as pd
cols = ['commit_hash','author', 'authored_datetime','committed_datetime', 'line_deletions', 'line_insertions', 'total_lines', 'files_changed']
lst = []
#import requests
#import json
#r = requests.get('https://api.github.com/events')
#pretty_json = json.loads(r.text)
#print (json.dumps(pretty_json, indent=2))

import git

#git.Repo.clone_from('https://github.com/OpenLiberty/open-liberty', '/Users/anttor/projects/open-liberty')

repo = git.Repo('/Users/anttor/projects/open-liberty')
#if my_repo.is_dirty(untracked_files=True):
#    print('Changes detected.')

#print(repo.git.status())

#log = repo.git.log()
#print(log)

commits = list(repo.iter_commits("origin/integration", max_count=10))
#commits = list(repo.iter_commits("origin/integration"))
print(len(commits))
print(commits[0].stats.total)
#print(commits[0].stats.files)
#print(dir(commits[0]))
    

#for commit in commits: 
#    print(commit.author)
#    print(commit.hexsha)
#    print(commit.authored_datetime)
#    print(commit.committed_datetime)
#    print(commits.stats.total)
#    print(commits.stats.files)
#    lst.append([commit.hexsha, commit.author, commit.message, commit.authored_datetime, commit.committed_datetime])

for i in range(0,len(commits)):
#    print i
#    print(commits[i].stats.total)
#    print(commits[i].stats.total.get('insertions')) 
#    lst.append(commits[i].stats.total)
    commit = commits[i]
    lst.append([commit.hexsha, commit.author, commit.authored_datetime, commit.committed_datetime, commit.stats.total.get('deletions'), commit.stats.total.get('insertions'), commit.stats.total.get('lines'), commit.stats.total.get('files')])


#log = repo.git.log()
#print(log[0].author)

df = pd.DataFrame(lst, columns=cols)

df.to_csv('commit_summary_final.csv', index=False)
