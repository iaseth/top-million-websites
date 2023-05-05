import json
import os

import requests

CSV_PATH = "raw/top-1m.csv"


def sanitize(ch):
	return ch if ch.isalpha() else "-"


def downloadMeta(website):
	website = website.lower()
	codeName = "".join([sanitize(ch) for ch in website])
	htmlPath = f"cache/{codeName}.html"
	if os.path.isfile(htmlPath):
		print(f"\tFound: {htmlPath}")
	else:
		print(f"\tNot found: {htmlPath}")


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
