class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            if '+' in local_name:
                plus_index = local_name.index('+')
                local_name = local_name[:plus_index]
            local_name = local_name.replace('.', '')
            clean_email = local_name + '@' + domain_name
            unique_emails.add(clean_email)
        return len(unique_emails)