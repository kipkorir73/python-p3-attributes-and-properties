#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]


class Person:
    def __init__(self,name="",job="Sales") :
        if not(type(name)in (str,)) and (1<=len(name)<=25):
            print(f"Name must be string between 1 and 25 characters.")
        elif job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.") 
        else:
            self.name=name
            self.job=job
               
