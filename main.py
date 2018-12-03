import unicodecsv as csv
import sys
import getopt
import warnings
import subprocess

# import local py files
import web_scraping
import merge_csv
import data_cleaning
import word_cloud

# do not output warnings
warnings.filterwarnings('ignore')

if "__main__" == __name__:   
      
    try:  
        opts,args = getopt.getopt(sys.argv[1:], "hd:fmsblqcw:", ["input"]) 

        #check all param  
        for opt in opts:
            # to get the help page
            if opt[0] == '-h':
                print('''
parameters:

-h                       show this help message and exit
-d <url>                 print the descrption of the job from url
-f <0/1> <title> <place> fetch job from glassdoor, 0/1: without/with description
                         eg: -f 0 "business analyst" "new orleans" 
-m                       merge local csv files
-c                       clean local BA_job.csv
-s                       output state heat map of ba jobs
-b                       output a barchart of average salary of ba jobs
-q                       output a barchart of salary range of ba jobs
-l                       job filter of ba jobs
-w <place>               output wordcloud for ba jobs in a specific city
                         eg: -w "new orleans"
                 ''')
                 

            # function to get job description from a url
            if opt[0] == '-d':
                print(web_scraping.get_job_description(opt[1])[0])

            # function to fetch job data from glass door
            if opt[0] == '-f':
                if int(args[0]):
                    # 0 stands for no need of description
                    keyword = args[1]
                    place = args[2]
                    print("Fetching job details...")
                    result = web_scraping.get_job_list_desc(place, keyword)
                    if result:
                        print("Writing data to output file...")
                        job_list = list()
                        for job in result:
                            job_list.append({'Name': job[0], 
                                             'Company': job[1], 
                                             'City': job[2],
                                             'State': job[3],
                                             'Salary': job[4], 
                                             'Description': job[5],
                                             'Url': job[6]})
                        # write results into a csv file
                        with open('%s-%s-job-results-desc.csv' % (keyword, place), 'wb') as csvfile:
                            fieldnames = ['Name', 'Company', 'City', 'State', 'Salary','Description', 'Url']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                            writer.writeheader()
                            for job in job_list:
                                writer.writerow(job)
                        print('Done!')
                    else:
                        print("Unable to find jobs for %s, in %s"%(keyword,place))
                else:
                    keyword = args[1]
                    place = args[2]
                    print("Fetching job details...")
                    result = web_scraping.get_job_list(place, keyword)
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
                        # write results into a csv file
                        with open('%s-%s-job-results.csv' % (keyword, place), 'wb') as csvfile:
                            fieldnames = ['Name', 'Company', 'City', 'State', 'Salary', 'Url']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
                            writer.writeheader()
                            for job in job_list:
                                writer.writerow(job)
                        print('Done!')
                    else:
                        print("Unable to find jobs for %s, in %s"%(keyword,place))

            # function to merge local csvs
            if opt[0] == '-m':
                print("Merging csv files...")
                output, name = merge_csv.merge_csv('./')
                output.to_csv(name+'.csv', index=False)
                print('Done!')

            # function to clean the dataset
            if opt[0] == '-c':
                data_cleaning.get_cleaned_dataset()

            # function to output graphs
            if opt[0] == '-s':
                import state_map
                state_map.get_graph()
            if opt[0] == '-b':
                import barchart_averagesalary
                barchart_averagesalary.get_barplot_average_salary()
            if opt[0] == '-q':
                import barchart_salaryrange
                barchart_salaryrange.get_barplot_salaryrange()

            # function to get the filters
            if opt[0] == '-l':
                subprocess.call("bokeh serve filters.py --show", shell=True)

            # function to output wordcloud
            if opt[0] == '-w':
                word_cloud.text_mining(opt[1])
          
    except getopt.GetoptError:  
        print("getopt error!")
        sys.exit(1)