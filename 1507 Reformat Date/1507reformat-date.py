class Solution(object):
    def reformatDate(self, datee):
        month_map = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
        
        date, month , year = datee.split()
        date = date[:-2] #strip the terms "st" "nd" ,"th"
        date = date.zfill(2) #zfill is used to addzero to the left until it reaches a specific width
        
        month = month_map[month]
        
        return"{}-{}-{}".format(year, month, date)
            