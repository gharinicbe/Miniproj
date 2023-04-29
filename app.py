import pandas as pd
import gspread as gs
from datetime import datetime,date

from flask import Flask

from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

@app.route('/')
def main1():
    #print('Hello World!')
    return ""

@app.route('/my-first-api')
def main():
    
    gc=gs.service_account(filename="myserviceacc.json")#to get client secrets JSON keyfile for your service account,activate google cloud API and after activation from keys find keyfile and download json file for your google account
    wb=gc.open_by_url("https://docs.google.com/spreadsheets/d/1WjbiDwgxrtP6HEBKKR6Lbz_EDefAZzaiCPS188phVpE/edit?usp=sharing")
    #creating object to the Spread sheet/workbook, it should be shared link and the access status should be access by anyone with link
    ws=wb.worksheet("Sheet1")#accessing particular sheet in the spread sheet
    df=pd.DataFrame(ws.get_all_records())
    #df.head()
    #df.describe()
    #df.info()
    def age(born):
        born = datetime.strptime(born, "%d/%m/%Y").date()
        today = date.today()
        return today.year - born.year - ((today.month, 
                                        today.day) < (born.month, 
                                                        born.day))
    
    df['Age'] = df['DOB'].apply(age)
    #df.head()
    #today and born are two datetime objects representing the current date and the person's birth date, respectively.
    # today.year - born.year calculates the difference between the current year and the birth year, which gives the person's age in years.
    # The expression (today.month, today.day) < (born.month, born.day) compares the current month and day to the birth month and day, respectively. If the current month and day are earlier than the birth month and day, it means the person has not yet had their birthday this year, so we subtract 1 from the age calculated in the previous step.
    # The entire expression is wrapped in parentheses to ensure that the comparison is done before the subtraction.
    # So the output of this code will be the person's age as an integer.
  
    def bmr(gen,wt,ht,ag):
        if gen=="Male":
            return (88.362 + (13.397 * wt) + (4.799 * ht) - (5.677 * ag))
        elif gen=="Female": 
            return (447.593 + (9.247  *wt) + (3.098 * ht) - (4.330 * ag))
        

    df["BMR"]=df.apply(lambda x: bmr(x["Gender"],x["Weight(Kgs)"],x["Height(cms)"],x["Age"]), axis=1)
    #df.head()
    #Men: BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) – (5.677 x age in years) Women: BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) – (4.330 x age in years)
    def dict_value(Key):
        dict_val={"Sedentary(no or little exercise)":1.15,
                "Light Activity(1-3 hrs execrise per week)":1.35,
                "Moderate Activity(4-6 hrs execrise per week)":1.55,
                "Very Active(7-9 hrs execrise per week)":1.75,
                "Extra Active(10+ hrs execrise per week)":1.95}
        return dict_val[Key]

    df["TDEE"]=df.apply(lambda x: dict_value(x["Activity Level"])+x["BMR"]+250+250, axis=1)
    #df.head()
    # TDEE: Total Daily Energy Expenditure
    # BMR: Basal Metabolic Rate
    # TEF: Thermic Effect of Food
    # EEE: Exercise Energy Expenditure
    # NEAT: Non-Exercise Activity Thermogenesis
    #TDEE = BMR + TEF + EEE + NEAT
    #TEF=BMR*0.1
    #EEE=250-500
    #NEAT=250-500
    
    df_list = df.values.tolist()
    df_header = df.columns.tolist()
    df_list_with_header = [df_header] + df_list
    print(df_list_with_header)
    ws.update('A1',df_list_with_header)
    return ""

#main()
