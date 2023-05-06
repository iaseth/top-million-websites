import json
import os

import requests
from bs4 import BeautifulSoup

CSV_PATH = "raw/top-1m.csv"
session = requests.session()


def sanitize(ch):
	return ch if ch.isalnum() else "-"


def downloadMeta(website):
	website = website.lower()
	websiteURL = "https://" + website
	codeName = "".join([sanitize(ch) for ch in website])
	htmlPath = f"cache/{codeName}.html"

	if os.path.isfile(htmlPath):
		print(f"\tFound: {htmlPath}")
		if os.path.getsize(htmlPath) == 0:
			print(f"\t\tFile is empty!")
			return
	else:
		try:
			print(f"\tDownloading {websiteURL} ...")
			res = session.get(websiteURL, timeout=5)
			with open(htmlPath, "w") as f:
				f.write(res.text)
			print(f"\t\tSaved: {htmlPath}")
		except Exception as e:
			with open(htmlPath, "w") as f:
				f.write("")
			print(f"\t\tSaved empty file: {htmlPath}")
			return

	soup = BeautifulSoup(open(htmlPath), "lxml")
	metaTags = soup.find_all("meta")
	ogImage = soup.find("meta", attrs={"property": "og:image"})
	if ogImage:
		print(ogImage)
	for metaTag in metaTags:
		# print(metaTag)
		pass


def main():
	with open(CSV_PATH) as file:
		lineNumber = 1
		for line in file:
			parts = line.strip().split(",")
			idx, website = [p.strip() for p in parts]
			print(f"{idx}. {website}")
			downloadMeta(website)

			if lineNumber >= 10:
				break
			else:
				lineNumber += 1


if __name__ == '__main__':
	main()
