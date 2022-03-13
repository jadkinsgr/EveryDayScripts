from datetime import datetime
ct = datetime.now().strftime('%H:%M:%S')

def timeframe():
    if ct >= '00:00:00' and ct <= '11:59:59':
        return 'Good Morning'
    elif ct >= '12:00:00' and ct <= '16:59:59':
        return 'Good Afternoon'
    elif ct >= '17:00:00' and ct <= '23:59:59':
        return 'Good Evening'

print(timeframe())
