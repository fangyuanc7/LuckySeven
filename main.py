import unicodecsv as csv
import sys
import getopt
import warnings
import web_scraping
import merge_csv

# do not output warnings
warnings.filterwarnings('ignore')

if "__main__" == __name__:   
      
    try:  
        opts,args = getopt.getopt(sys.argv[1:], "d:fm:", ["input"])
          
        print("============ opts ==================");         
        print(opts);  
      
        print("============ args ==================");  
        print(args);  

        #check all param  
        for opt in opts:
            if opt[0] == '-d':
                print(web_scraping.get_job_description(opt[1])[0])
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
            if opt[0] == '-m':
                path = opt[1]
                print("Merging csv files...")
                output, name = merge_csv.merge_csv(path)
                output.to_csv(name+'.csv', index=False)
                print('Done!')

          
    except getopt.GetoptError:  
        print("getopt error!")
        sys.exit(1)