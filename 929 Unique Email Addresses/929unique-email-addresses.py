class Solution(object):
    def numUniqueEmails(self, emails):
        uniqueset= set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            
            local = local.replace('.', "")
            
            uniqueset.add(local+'@'+domain) 
        return len(uniqueset)
        