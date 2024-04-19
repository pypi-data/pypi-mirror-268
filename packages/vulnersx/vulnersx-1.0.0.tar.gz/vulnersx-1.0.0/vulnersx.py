"""
VulnersX : powerful tool for efficiently searching and analyzing software vulnerabilities.
"""

import requests
import sqlite3
import time
__version__ = "1.0.0"
class VulnersX:
    def __init__(self, db_path='vulnerabilities.db'):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS vulnerabilities (
                            id INTEGER PRIMARY KEY,
                            cve_id TEXT,
                            summary TEXT
                            )''')
        self.conn.commit()
    
    def search_vulnerabilities(self, package_name, after_date):
        try:
            url = f"https://access.redhat.com/labs/securitydataapi/cve.json?package={package_name}&after={after_date}"
            response = requests.get(url)
            response.raise_for_status()
            vulnerabilities = response.json()
            total_vulnerabilities = len(vulnerabilities)
            if total_vulnerabilities > 0:
                print("Found the following vulnerabilities:")
                for i, vulnerability in enumerate(vulnerabilities, start=1):
                    cve_id = vulnerability.get('CVE')
                    summary = vulnerability.get('bugzilla_description')
                    self.save_to_database(cve_id, summary)
                    self.save_to_text_file(i, cve_id, summary)
                    progress = i / total_vulnerabilities
                    self.update_progress_bar(progress)
                print("\nSearch complete.")
                print("Results saved.")
            else:
                print("No vulnerabilities found for the specified package after the specified date.")
        except requests.RequestException as e:
            print(f"Error occurred while connecting to Red Hat Security Data API: {e}")

    def save_to_database(self, cve_id, summary):
        try:
            self.cur.execute("INSERT INTO vulnerabilities (cve_id, summary) VALUES (?, ?)", (cve_id, summary))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error occurred while inserting data into the database: {e}")

    def save_to_text_file(self, counter, cve_id, summary):
        with open('cves.txt', 'a') as f:
            f.write(f"{counter}|{cve_id}|{summary}\n")

    def update_progress_bar(self, progress):
        bar_length = 50
        filled_length = int(bar_length * progress)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f"\rProgress: [{bar}] {int(progress * 100)}%", end='')
        time.sleep(0.1)

    def display_results(self):
        print("\nResults:")
        with open('cves.txt', 'r') as f:
            print(f.read())