import requests

def get_cve(cpe_name):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName={cpe_name}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Here, you would process the JSON data to extract relevant information
        # For demonstration, let's assume we're simply returning the raw data
        return data
    else:
        return None
    
def process_cve_data(json_data):
    vulnerabilities_info = []

    for vuln in json_data['vulnerabilities']:
        cve_info = {
            'cve_id': vuln['cve']['id'],
            'published': vuln['cve']['published'],
            'last_modified': vuln['cve']['lastModified'],
            'description': vuln['cve']['descriptions'][0]['value'] if vuln['cve']['descriptions'] else 'No description available.',
        }
        vulnerabilities_info.append(cve_info)

    return vulnerabilities_info

