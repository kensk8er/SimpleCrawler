import json

__author__ = 'kensk8er'

if __name__ == '__main__':
    company_data = {}
    job_data = {}

    # load data from raw json file
    print 'load data...'
    FILE = open('result/raw.jl', 'r')
    for line in FILE:
        data = json.loads(line)

        # procedure for company_data
        if data.has_key('company_description'):
            company_name = data['company_name']

            if not company_data.has_key(company_name):
                company_data[company_name] = {}  # initialize

            company_data[company_name]['company_name'] = company_name
            company_data[company_name]['company_description'] = data['company_description']
            company_data[company_name]['url'] = data['url']

        # procedure for job_data
        if data.has_key('job_description'):
            job_name = data['job_name']

            if not job_data.has_key(job_name):
                job_data[job_name] = {}  # initialize

            job_data[job_name]['job_name'] = job_name
            job_data[job_name]['company_name'] = data['company_name']
            job_data[job_name]['job_description'] = data['job_description']
            job_data[job_name]['url'] = data['url']

    FILE.close()

    # reformat and write new json file
    print 'reformat and write into new json file...'
    new_data = {}
    for job_datum in job_data.values():
        job_name = job_datum['job_name']
        new_data[job_name] = {}  # initialize

        # assign new data (job data)
        new_data[job_name]['job_name'] = job_name
        new_data[job_name]['job_description'] = job_datum['job_description']
        new_data[job_name]['job_url'] = job_datum['url']

        # assign new data (company data)
        if company_data.has_key(job_datum['company_name']):  # some job posts don't have company data
            company_datum = company_data[job_datum['company_name']]
            new_data[job_name]['company_name'] = company_datum['company_name']
            new_data[job_name]['company_description'] = company_datum['company_description']
            new_data[job_name]['company_url'] = company_datum['url']
        else:
            # assign empty data if there isn't company data
            new_data[job_name]['company_name'] = ''
            new_data[job_name]['company_description'] = ''
            new_data[job_name]['company_url'] = ''

    FILEOUT = 'result/job_data.json'
    f = open(FILEOUT, 'w')
    json.dump(new_data, f)
    f.close()
