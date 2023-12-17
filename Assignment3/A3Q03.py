month_name=input('Enter the month name:')

if month_name=='January' or month_name=='March' or month_name=='May' or month_name=='July' or month_name=='August' \
   or month_name=='October' or month_name=='December': 
    days=31
elif month_name=='February':
    year=input('Enter the year (yyyy): ')
    if(year%400==0) or (year%4==0 and year%100!=0):
        days=29
    else:
        days=28
if month_name=='April' or month_name=='June' or month_name=='September' or month_name=='November':
    days=30

if days is not None:
    print(month_name,'has',days,'days')
else:
    print('Invalid month name')
