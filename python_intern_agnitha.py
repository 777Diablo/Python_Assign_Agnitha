import requests
import csv
import argparse
from typing import List, Dict, Any

papers_list = []
def fetch_pubmed_details(query:str):
        print(query)
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
                "db": "pubmed",
                "term": query,
                "retmode": "json",
                "retmax": 100 
            }
            
        response = requests.get(base_url, params=params)
        response.raise_for_status()
            
        data = response.json()
        paper_ids = data.get("esearchresult", {}).get("idlist", [])
        
        if paper_ids:
            details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            params = {
                    "db": "pubmed",
                    "id": ",".join(paper_ids),
                    "retmode": "json"
                }
                
            response = requests.get(details_url, params=params)

            response.raise_for_status()
                
            papers_data = response.json().get("result", {})
            
                
            for paper_id in paper_ids:
                    paper = papers_data.get(paper_id, {})
                    # print(paper)
                    papers_list.append({
                        "PubMedID": paper.get("uid", ""),
                        "Title": paper.get("title", ""),
                        "Publication Date": paper.get("pubdate", ""),
                        "Authors": [author.get("name", "") for author in paper.get("authors",[])],
                        "Company Affiliation(s)": paper.get("source", ""),
                        "Corresponding Author Email": paper.get("corresponding_email", "")
                    })
# papers=papers_list
def save_to_csv(papers: List[Dict[str, Any]], filename: str) -> None:
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=papers[0].keys())
        writer.writeheader()
        writer.writerows(papers)

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file name.", default="output.csv")
    # parser.add_argument("-h", "--help", action="help", help="Display usage instructions.")
    args = parser.parse_args()
    # papers_list = []
    # print(args.query,papers_list)
    fetch_pubmed_details(args.query)
    papers=papers_list
    if papers:
        save_to_csv(papers, args.file)
        print(f"Saved {len(papers)} papers to {args.file}")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()

# print(papers_list)
