# importing required modules 
from pyclbr import Class
import PyPDF2
import pandas as pd
import csv
import re
import glob
import json

with open('addressdata.json') as f:
   jsondata = json.load(f)


class property():
    def __init__(self, property_address, payment_due_date, principal, interest):
        self.property_address = property_address
        self.payment_due_date = payment_due_date
        self.principal = principal
        self.interest = interest
        

class uwm():
    def get_payment_due_date_data(raw_data):
        result = re.findall('PAYMENTDUEDATE.{10}', raw_data)
        payment_due_date_data = re.search(r'\d+\/\d+\/\d+', result[0]).group()
        return payment_due_date_data
    def get_principal_data(raw_data):
        result = re.findall('PRINCIPAL.{10}', raw_data)
        principal_data = re.search(r'\$\d+\.\d+', result[1]).group()
        return principal_data
    def get_interest_data(raw_data):
        result = re.findall('INTEREST.{10}', raw_data)
        interest_data = re.search(r'\$\d+\.\d+', result[1]).group()
        return interest_data

class mm():
    def get_payment_due_date_data(raw_data):
        result = re.findall('PAYMENTDUEDATE.{10}', raw_data)
        payment_due_date_data = re.search(r'\d+\/\d+\/\d+', result[0]).group()
        return payment_due_date_data
    def get_principal_data(raw_data):
        result = re.findall('PRINCIPAL.{10}', raw_data)
        principal_data = re.search(r'\$\d+\.\d+', result[2]).group()
        return principal_data
    def get_interest_data(raw_data):
        result = re.findall('INTEREST.{10}', raw_data)
        interest_data = re.search(r'\$\d+\.\d+', result[2]).group()
        return interest_data

class cooper():
    def get_payment_due_date_data(raw_data):
        result = re.findall('PAYMENTDUEDATE.{10}', raw_data)
        payment_due_date_data = re.search(r'\d+\/\d+\/\d+', result[0]).group()
        return payment_due_date_data
    def get_principal_data(raw_data):
        result = re.findall('PRINCIPAL.{10}', raw_data)
        principal_data = re.search(r'\$\d+\.\d+', result[4]).group()
        return principal_data
    def get_interest_data(raw_data):
        result = re.findall('INTEREST.{8}', raw_data)
        interest_data = re.search(r'\$\d+\.\d+', result[5]).group()
        return interest_data


class chase():
    def get_payment_due_date_data(raw_data):
        result = re.findall('AUTOMATICALLYSCHEDULEDTOBEPAIDON.{10}', raw_data)
        payment_due_date_data = re.search(r'\d+\/\d+\/\d+', result[0]).group()
        return payment_due_date_data
    def get_principal_data(raw_data):
        result = re.findall('PRINCIPAL.{10}', raw_data)
        principal_data = re.search(r'\$\d+\.\d+', result[5]).group()
        return principal_data
    def get_interest_data(raw_data):
        result = re.findall('INTEREST.{8}', raw_data)
        interest_data = re.search(r'\$\d+\.\d+', result[2]).group()
        return interest_data



filelist = glob.glob("*.pdf")


for file in filelist:
    
    pdfFileObj = open(file, 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    pageObj = pdfReader.getPage(0) 
    raw_data = ""
    raw_data = pageObj.extractText().replace(" ", "").replace("\n", "").replace(",", "").upper()
    


    for entry in jsondata:
        # print(entry["address"])
        if (entry["address"] in raw_data):
            document = entry["document"]
            specific_address = entry["address"]
        


    # print(document)
    # print(specific_address)
    
    new_property = property(specific_address, locals()[document].get_payment_due_date_data(raw_data),  locals()[document].get_principal_data(raw_data),  locals()[document].get_interest_data(raw_data))

    # print(new_property.__dict__)

    new_dict = {"property address data" :  new_property.property_address,
                    "payment due date data" : new_property.payment_due_date,
                    "principal date data" : new_property.principal,
                    "interest date data" : new_property.interest
                    }

    with open(str(specific_address) + '.csv', 'w') as f:
        for key in new_dict.keys():
            f.write("%s,%s\n"%(key,new_dict[key]))

    pdfFileObj.close() 









