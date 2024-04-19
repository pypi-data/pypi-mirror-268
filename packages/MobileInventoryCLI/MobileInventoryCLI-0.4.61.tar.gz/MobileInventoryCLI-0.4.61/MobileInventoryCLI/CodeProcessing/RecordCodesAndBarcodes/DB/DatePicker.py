import sys,os,calendar
from datetime import datetime,date,timedelta
from datetime import time as TM
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DB.Prompt import *
from datetime import datetime,timedelta
import pint
from colored import Fore,Style
from pathlib import Path

def mkint(text,TYPE):
    try:
        if text not in ['',]:
            drange=calendar.monthrange(date.today().year,date.today().month)
            if TYPE == 'day':
                if int(text) not in [i+1 for i in range(*drange)]:
                    raise Exception(f"Not in {drange}")
            elif TYPE == 'month':
                if int(text) not in [i for i in range(12)]:
                    raise Exception(f"Not in {[i for i in range(12)]}")
            elif TYPE == 'year':
                pass
            elif TYPE == 'hour':
                if int(text) not in [i for i in range(24)]:
                    raise Exception(f"Not in {[i for i in range(24)]}")
            elif TYPE == 'minute':
                if int(text) not in [i for i in range(60)]:
                    raise Exception(f"Not in {[i for i in range(60)]}")
            elif TYPE == 'second':
                if int(text) not in [i for i in range(60)]:
                    raise Exception(f"Not in {[i for i in range(60)]}")
            elif TYPE == 'float':
                return float(text)
            return int(text)
        else:
            if TYPE == 'day':
                return datetime.now().day
            elif TYPE == 'month':
                return datetime.now().month
            elif TYPE == 'year':
                return datetime.now().year
            elif TYPE == 'hour':
                return datetime.now().hour
            elif TYPE == 'minute':
                return datetime.now().minute
            elif TYPE == 'second':
                return datetime.now().second
            elif TYPE == 'float':
                return float(0)
            else:
                return 0
    except Exception as e:
        print(e)
        if TYPE == 'day':
            return datetime.now().day
        elif TYPE == 'month':
            return datetime.now().month
        elif TYPE == 'year':
            return datetime.now().year
        elif TYPE == 'hour':
            return datetime.now().hour
        elif TYPE == 'minute':
            return datetime.now().minute
        elif TYPE == 'second':
            return datetime.now().second
        else:
            return 0


def DatePkr():
    while True:
        try:
            pass
            year=Prompt.__init2__(None,func=mkint,ptext=f"Year[Default:{date.today().year}]",helpText="year to be used in date returned",data='year')
            if year in [None,]:
                return None
            break
        except Exception as e:
            print(e)
        
    while True:
        try:
            pass
            month=Prompt.__init2__(None,func=mkint,ptext=f"Month[0..12|Default:{date.today().month}]",helpText="month to be used in date returned",data='month')
            if month in [None,]:
                return None
            break
        except Exception as e:
            print(e)
        
    while True:
        try:
            pass
            day=Prompt.__init2__(None,func=mkint,ptext=f"Day[{'..'.join([str(i) for i in calendar.monthrange(date.today().year,date.today().month)])}|Default:{date.today().day}]",helpText="day to be used in date returned",data='day')
            if day in [None,]:
                return None
            break
        except Exception as e:
            print(e)
        
    return date(year,month,day)


def TimePkr():
    while True:
        try:
            pass
            hour=Prompt.__init2__(None,func=mkint,ptext=f"hour [0..24|Default:{datetime.now().hour}]",helpText="hour to be used in date returned",data='hour')
            if hour in [None,]:
                return None
            break
        except Exception as e:
            print(e)
        print(hour)
        
    while True:
        try:
            pass
            minute=Prompt.__init2__(None,func=mkint,ptext=f"minute [0..59|Default:{datetime.now().minute}]]",helpText="minute to be used in date returned",data='minute')
            if minute in [None,]:
                return None
            break
        except Exception as e:
            print(e)
        
    while True:
        try:
            pass
            second=Prompt.__init2__(None,func=mkint,ptext=f"second [0..59|Default:Current Second of The Clock]",helpText="second to be used in date returned",data='second')
            if second in [None,]:
                return None
            break
        except Exception as e:
            print(e)
        
    return TM(hour,minute,second)



def DateTimePkr():
    tm=TimePkr()
    if not tm:
        raise Exception("Time is Missing!")
    dt=DatePkr()
    if not dt:
        raise Exception("Date is Missing!")

    return datetime(dt.year,dt.month,dt.day,tm.hour,tm.minute,tm.second)

def CalculateEarnings(tax_percent_dec=0.178):
    try:
        reg=pint.UnitRegistry()
        month=datetime.now().month
        year=datetime.now().year
        today=datetime.now().day
        tomorrow=today+1
        s=None
        while True:
            try:
                print(f"{Fore.cyan}Please enter the shift Start data.{Style.reset}")
                s=DateTimePkr()
                if not s:
                    raise Exception("Must Have a Start DateTime")
                break
            except Exception as ee:
                print(ee)
                return
        e=None
        while True:
            try:
                print(f"{Fore.cyan}Please enter the shift End data.{Style.reset}")
                e=DateTimePkr()
                if not e:
                    raise Exception("Must have a End DateTime")
                break
            except Exception as ee:
                print(ee)
                return
        d=e-s
        while True:
            try:
                period=Prompt.__init2__(None,func=mkint,ptext="Lunch Length in minutes [0..59]",helpText="how long your lunch was in minutes upto 59 minutes",data="minute")
                break
            except Exception as e:
                print(e)

        lunch=timedelta(seconds=60*period)
        d=d-lunch

        while True:
            try:
                rate=Prompt.__init2__(None,func=mkint,ptext="Your payrate per hour?",helpText="$/Hr rate",data="float")
                break
            except Exception as e:
                print(e)
        
        gross=round(rate*float(reg.convert(d.total_seconds(),'seconds','hours')),2)

        while True:
            try:
                tdays=Prompt.__init2__(None,func=mkint,ptext="Total Days?",helpText="$/Hr rate",data="integer")
                break
            except Exception as e:
                print(e)

        fourdayg=round(gross*tdays,2)
        tax=round(fourdayg*0.178,2)
        union=10
        msg=f'''
{Fore.cyan}duration{Style.reset}:
 {d} =
 {Fore.light_red}({e}(end) {Style.reset}
 -{Fore.green_yellow}{s}(start)){Style.reset}
 -{Fore.light_yellow}{lunch}(lunch){Style.reset}
{Fore.light_green}gross{Style.reset}:
 {Fore.light_green}1 Shift Gross ${gross}{Style.reset}={Fore.light_magenta}$/Hr(${rate})*duration in Hr's ({d}){Style.reset}
{Fore.green}Total ({tdays}) Days Total Gross{Style.reset}:
 {Fore.green}Gross = ${fourdayg}{Style.reset}=days({tdays}) *{Fore.light_green}gross(${gross})
{Fore.cyan}{Style.bold}Net{Style.reset}:
{Fore.cyan}-tax{Style.reset} = (${Fore.green}{fourdayg}{Style.reset}*{Fore.yellow}0.178(Rough Estimate for 17.8%)){Style.reset} = {Fore.dark_goldenrod}${round(tax,2)}{Style.reset}
{Fore.cyan}-union{Style.reset} = {Fore.medium_violet_red}${union}{Style.reset}
{Fore.cyan}Net{Style.reset} = ${fourdayg-tax-union}
'''
        print(msg)
    except Exception as e:
        print(e)

def MadeInTime():
    registry=pint.UnitRegistry()
    def mkSeconds(text,data):
        try:
            return pint.Quantity(text).m_as('hours'),text
        except Exception as e:
            raise e

    while True:
        try:
            forwards,text=Prompt.__init2__(None,func=mkSeconds,ptext="amount of time to calculate pay for?",helpText="amount of time to add to now, the number with h(hour),m(minutes),s(seconds), nothing will assume h(hour)",data=None)
            if forwards in [None,]:
                return None
           
            while True:
                try:
                    rate=Prompt.__init2__(None,func=mkint,ptext="Your payrate per hour?",helpText="$/Hr rate",data="float")
                    break
                except Exception as e:
                    print(e)
            if rate in [None,]:
                return

            gross=round(float(forwards)*rate,2)

            print(f'{Fore.light_green}${rate}/Hr * ({Fore.light_yellow}{text}) -> {Fore.light_red}${gross}{Style.reset}')
            return
        except Exception as e:
            print(e)

def ProjectMyTime():
    registry=pint.UnitRegistry()
    def mkSeconds(text,data):
        try:
            return pint.Quantity(text).m_as('seconds'),text
        except Exception as e:
            raise e

    while True:
        try:
            forwards,text=Prompt.__init2__(None,func=mkSeconds,ptext="amount of time to add to now?",helpText="amount of time to add to now, the number with h(hour),m(minutes),s(seconds), nothing will assume h(hour)",data=None)
            if forwards in [None,]:
                return None
            now=datetime.now()
            projected=now+timedelta(seconds=forwards)
            print(f'{Fore.light_green}{now} ({Fore.light_yellow}{text}) -> {Fore.light_red}{projected}{Style.reset}')
            break
        except Exception as e:
            print(e)

