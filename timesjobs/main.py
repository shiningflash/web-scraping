import json

import requests
from bs4 import BeautifulSoup


def save_response(data, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=4))
    print(f'Response saved in {filename}')


def find_jobs(my_skill):
    suitable_jobs = []
    
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    
    for job in jobs:
        published_date = ' '.join(job.find('span', class_='sim-posted').span.text.split())
        if not "few" in published_date.lower():
            continue
        skills = ' '.join(job.find('span', class_='srp-skills').text.split()).replace(' ,', ',')
        if my_skill.strip().lower() not in skills.lower():
            continue
        company_name = ' '.join(job.find('h3', class_='joblist-comp-name').text.split())
        more_info = job.header.h2.a['href']

        suitable_jobs.append({
            'company_name': company_name,
            'required_skills': skills,
            'more_info': more_info
        })
    save_response(suitable_jobs, 'jobs.json')


if __name__ == '__main__':
    print('Search with your skill')
    my_skill = input('>')
    print(f'Filtering out {my_skill}...\n')
    
    find_jobs(my_skill)
    
