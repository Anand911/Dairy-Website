from datetime import datetime
def get_month():
    months={1:"JAN",2:"FEB",3:"MAR",4:"APR",5:"MAY",6:"JUN"
           ,7:"JUL",8:"AUG",9:"SEP",10:"OCT",11:"NOV",12:"DEC"}
    month=datetime.now().month
    print(months[month])
get_month()