import requests
import time
def scan_file(api_key, file_path):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    files = {'file': (file_path, open(file_path, 'rb'))}
    params = {'apikey': api_key}
    
    response = requests.post(url, files=files, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"error while trying to conect the scan {response.status_code}")
        return None

def get_file_report(api_key, resource_id):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': api_key, 'resource': resource_id}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"error while reciving the report {response.status_code}")
        return None

def main(path):
    api_key = '58efaa60ccc808b014510b665e85c04d102b76992f55d58d2d578f27c2121e74'
    for file in path:
        scan_data = scan_file(api_key, file)
        if scan_data:
            print("pre scan results:")
            print(scan_data)

            resource_id = scan_data['resource']

            time.sleep(15)

            report_data = get_file_report(api_key, resource_id)
            if report_data:
                print(f"scan report of file {file}:")
                for key in report_data:
                    if str(key) != "scans":
                        print(key,":",report_data[key])
                scan_num=0
                for key in report_data["scans"].keys():
                    scan_num+=1
                    print (scan_num,". ",key,":", report_data["scans"][key])
            time.sleep(1.5)

if __name__ == "__main__":
    main()