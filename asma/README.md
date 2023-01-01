To use this script you need python installed in your machine.

## _**Installation steps**_

1.  clone this repo: `git clone https://github.com/cs-fedy/submit-crm`
2.  change your current directory to `submit-crm` dir: `cd submit-crm`
3.  install the virtualenv package if you don't have it: `pip install virtualenv`
4.  create new virtualenv: `virtualenv venv`
5.  install the required packages: `pip install -r requirements.txt`
6.  make sure you have the `.env` file containing your api key respecting this format: `API_KEY="YOUR API KEY HERE"`
7.  write your main function that uses the provided functions
8.  run the script: `python main.py`