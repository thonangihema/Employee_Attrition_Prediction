#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system(' pip install xgboost')


# In[ ]:


import tkinter as tk
from tkinter import ttk
import joblib
import sklearn
sklearn.externals.joblib = joblib

print(sklearn.externals.joblib)
# Load the model
model = joblib.load('C:\\Users\\Hema\\Desktop\\Attrition\\y_pred (2).joblib')

def Predict_Attrition():
    DailyRate = int(a1.get())
    TotalWorkingYears= int(a2.get())
    YearsAtCompany= int(a3.get())
    YearsInCurrentRole = int(a4.get())
    YearsWithCurrManager = int(a5.get())
    Age=int(a6.get())
    if a7.get() == "No":
        OverTime=0
    elif a7.get() == "Yes":
        OverTime=1
    DistanceFromHome= int(a8.get())
    StockOptionLevel= int(a9.get())
    JobLevel=int(a10.get())
    if a11.get() == "Single":
        MaritalStatus=0
    elif a11.get() == "Divorced":
        MaritalStatus=1
    elif a11.get() == "Married":
        MaritalStatus=2

    if a12.get() == "Healthcare Representative":
        JobRole=0
    elif a12.get() == "Human Resources":
        JobRole=1
    elif a12.get() == "Laboratory Technician":
        JobRole=2
    elif a12.get() == "Manager":
        JobRole=3
    elif a12.get() == "Manufacturing Director":
        JobRole=4
    elif a12.get() == "Research Director":
        JobRole=5
    elif a12.get() == "Research Scientist":
        JobRole=6
    elif a12.get() == "Sales Executive":
        JobRole=7
    elif a12.get() == "Sales Representative":
        JobRole=8
    YearsSinceLastPromotion=int(a13.get())
    JobSatisfaction=int(a14.get())
    EnvironmentSatisfaction=int(a15.get())
    NumCompaniesWorked=int(a16.get())
    JobInvolvement=int(a17.get())
    HourlyRate=int(a18.get())
    PercentSalaryHike=int(a19.get())

    xy_pred = model.predict([[DailyRate,TotalWorkingYears,YearsAtCompany,YearsInCurrentRole,YearsWithCurrManager, Age, OverTime,DistanceFromHome,StockOptionLevel,JobLevel,MaritalStatus, JobRole ,YearsSinceLastPromotion,JobSatisfaction,EnvironmentSatisfaction,NumCompaniesWorked,JobInvolvement,HourlyRate,PercentSalaryHike]])

  
    if xy_pred == 1:
        result_label.config(text="Employee may leave")
    else:
        result_label.config(text="Employee will stay")

window = tk.Tk()



window.title("Employee Attrition Prediction")


a1_label = tk.Label(window, text="DailyRate : ")
a1_label.grid(row=0, column=0, padx=10, pady=10)
a1 = tk.Entry(window)
a1.grid(row=0, column= 1, padx=10, pady=10)

a2_label = tk.Label(window, text="TotalWorkingYears : ")
a2_label.grid(row=1, column=0, padx=10, pady=10)
a2 = tk.Entry(window)
a2.grid(row=1, column=1, padx=10, pady=10)

a3_label = tk.Label(window, text="YearsAtCompany : ")
a3_label.grid(row=2, column=0, padx=10, pady=10)
a3 = tk.Entry(window)
a3.grid(row=2, column=1, padx=10, pady=10)

a4_label = tk.Label(window, text="YearsInCurrentRole : ")
a4_label.grid(row=3, column=0, padx=10, pady=10)
a4 = tk.Entry(window)
a4.grid(row=3, column=1, padx=10, pady=10)

a5_label = tk.Label(window, text="YearsWithCurrManager : ")
a5_label.grid(row=4, column=0, padx=10, pady=10)
a5 = tk.Entry(window)
a5.grid(row=4, column=1, padx=10, pady=10)

a6_label = tk.Label(window, text="Age :")
a6_label.grid(row=5, column=0, padx=10, pady=10)
a6 = tk.Entry(window)
a6.grid(row=5, column=1, padx=10, pady=10)

a7_label = tk.Label(window, text="OverTime : ")
a7_label.grid(row=6, column=0, padx=10, pady=10)
a7 = ttk.Combobox(window,width="18",values=("No","Yes"))
a7.grid(row=6, column=1, padx=10, pady=10)

a8_label = tk.Label(window, text="DistanceFromHome : ")
a8_label.grid(row=7, column=0, padx=10, pady=10)
a8 = tk.Entry(window)
a8.grid(row=7, column=1, padx=10, pady=10)

a9_label = tk.Label(window, text="StockOptionLevel: ")
a9_label.grid(row=8, column=0, padx=10, pady=10)
a9 = tk.Entry(window)
a9.grid(row=8, column=1, padx=10, pady=10)

a10_label = tk.Label(window, text="JobLevel : ")
a10_label.grid(row=9, column=0, padx=10, pady=10)
a10 = tk.Entry(window)
a10.grid(row=9, column=1, padx=10, pady=10)

a11_label = tk.Label(window, text="MaritalStatus : ")
a11_label.grid(row=0, column=2, padx=10, pady=10)
a11 = ttk.Combobox(window, width="18", values=("Single","Divorced","Married"))
a11.grid(row=0, column=3, padx=10, pady=10)

a12_label = tk.Label(window, text="JobRole : ")
a12_label.grid(row=1, column=2, padx=10, pady=10)
a12 = ttk.Combobox(window,width="18", values=("Health Care Representative","Human Resources","Laboratory Technician","Manager","Manufacturing Director","Research Director","Research Scientist","Sales Executive"))
a12.grid(row=1, column=3, padx=10, pady=10)

a13_label = tk.Label(window, text="YearsSinceLastPromotion : ")
a13_label.grid(row=2, column=2, padx=10, pady=10)
a13 = tk.Entry(window)
a13.grid(row=2, column=3, padx=10, pady=10)

a14_label = tk.Label(window, text="JobSatisfaction : ")
a14_label.grid(row=3, column=2, padx=10, pady=10)
a14 = tk.Entry(window)
a14.grid(row=3, column=3, padx=10, pady=10)

a15_label = tk.Label(window, text="EnvironmentSatisfaction : ")
a15_label.grid(row=4, column=2, padx=10, pady=10)
a15 = tk.Entry(window)
a15.grid(row=4, column=3, padx=10, pady=10)

a16_label = tk.Label(window, text="NumCompaniesWorked : ")
a16_label.grid(row=5, column=2, padx=10, pady=10)
a16 = tk.Entry(window)
a16.grid(row=5, column=3, padx=10, pady=10)

a17_label = tk.Label(window, text="JobInvolvement : ")
a17_label.grid(row=6, column=2, padx=10, pady=10)
a17 = tk.Entry(window)
a17.grid(row=6, column=3, padx=10, pady=10)

a18_label = tk.Label(window, text="HourlyRate : ")
a18_label.grid(row=7, column=2, padx=10, pady=10)
a18 = tk.Entry(window)
a18.grid(row=7, column=3, padx=10, pady=10)

a19_label = tk.Label(window, text="PercentSalaryHike : ")
a19_label.grid(row=8, column=2, padx=10, pady=10)
a19 = tk.Entry(window)
a19.grid(row=8, column=3, padx=10, pady=10)

#detect_button = tk.Button(window, text="Predict", command=Predict_Attrition)
detect_button = tk.Button(window)
detect_button.configure(text="Predict", command=Predict_Attrition)
detect_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)


result_label = tk.Label(window, text="")
result_label.grid(row=11,column=0, columnspan=2, padx=10, pady=10)

window.mainloop()


# In[ ]:





# In[ ]:




