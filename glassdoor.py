import argparse
import unicodecsv as csv
import requests
from bs4 import BeautifulSoup
import time

def get_job_list(place: str, keyword: str) -> list:
    import requests
    from bs4 import BeautifulSoup
    import time
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
        'referer': 'https://www.glassdoor.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive'
    }
    
    location_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.01',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
        'referer': 'https://www.glassdoor.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive'
    }

    data = {"term": place,
            "maxLocationsToReturn": 10}
    
    location_url = "https://www.glassdoor.co.in/findPopularLocationAjax.htm?"
    
    try:
        # get location id for search location
        location_response = requests.post(location_url, headers=location_headers, data=data).json()
        place_id = location_response[0]['locationId']
        job_list_url = 'https://www.glassdoor.com/Job/jobs.htm'
        absolute_url = 'https://www.glassdoor.com'
        data = {
            'clickSource': 'searchBtn',
            'sc.keyword': keyword,
            'locT': 'C',
            'locId': place_id,
            'jobType': ''
        }
        
        result_list = list()
        
        if place_id:
            for i in range(30):     # don't know why, the website can only show the first 30 pages
                response = requests.post(job_list_url, headers=headers, data=data)
                results_page = BeautifulSoup(response.content,'lxml')
                jobs = results_page.find('', class_='jlGrid hover').find_all('li')
                
                for job in jobs:
                    # get the attributes of the job
                    job_name = job.find('div', class_='flexbox jobTitle').find('a').get_text()
                    job_url = absolute_url+job.find('div', class_='flexbox jobTitle').find('a').get('href')
                    company_location = job.find('div', class_='flexbox empLoc').find('div').get_text().split(' – ')
                    job_company = company_location[0][1:]
                    job_city = company_location[1].split(', ')[0]
                    job_state = company_location[1].split(', ')[1]
                    if job.find('span', class_='green small'):
                        job_salary = job.find('span', class_='green small').get_text()[1:]
                    else:
                        job_salary = ''
                    result_list.append((job_name, job_company, job_city, job_state, job_salary, job_url))
                    
                if not results_page.find('li', class_='next'):
                    break   # only one page
                if not results_page.find('li', class_='next').find('a'):
                    break   # reach the end page
                # next page
                job_list_url = absolute_url + results_page.find('li', class_='next').find('a').get('href')
                time.sleep(2)
                    
            return result_list         
        else:
            print('Location not available.')
              
    except:
        print('Fail to find jobs.')


if __name__ == "__main__":

	''' eg-:python glassdoor.py "Android developer", "los angeles" '''

	argparser = argparse.ArgumentParser()
	argparser.add_argument('keyword', help='job name', type=str)
	argparser.add_argument('place', help='job location', type=str)
	args = argparser.parse_args()
	keyword = args.keyword
	place = args.place
	print("Fetching job details...")
	result = get_job_list(place, keyword)
	if result:
		print("Writing data to output file...")
		job_list = list()
		for job in result:
		    job_list.append({'Name': job[0], 
		                     'Company': job[1], 
		                     'City': job[2],
		                     'State': job[3],
		                     'Salary': job[4], 
		                     'Url': job[5]})
		with open('%s-%s-job-results.csv' % (keyword, place), 'wb') as csvfile:
		    fieldnames = ['Name', 'Company', 'City', 'State', 'Salary', 'Url']
		    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
		    writer.writeheader()
		    for job in job_list:
		        writer.writerow(job)
		print('Done!')
	else:
		print("Unable to find jobs for %s, in %s"%(keyword,place))

