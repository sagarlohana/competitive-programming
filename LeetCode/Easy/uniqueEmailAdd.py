class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            splitted_email = email.split('@')
            splitted_email[0] = splitted_email[0].replace('.', '')
            index_plus = splitted_email[0].find('+')
            if index_plus != -1:
                splitted_email[0] = splitted_email[0][:index_plus]
            email_set.add("@".join(splitted_email))
        return len(email_set)