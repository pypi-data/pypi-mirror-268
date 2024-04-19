from typing import Optional


class EmailTemplate:
    @classmethod
    def get_email_format(cls, username: str) -> str:
        return f"""1. Email type: ["received" and "sent"]. If email type is "received", it means this email is received by "{username}". If email type is "sent", it means this email is written and sent by "{username}".\n2. Email sender: [user name and email]\n3. Email id: [unique identifier of the email]\n4. Email sent time: [datetime]\n5. Email subject: [subject of the email]\n6. Email body: [Email content delimited by triple quotes.]"""

    @classmethod
    def get_email_string(cls, *, username: str, email_body: str,
                         is_sender: bool,
                         from_: str,
                         date_str: Optional[str] = None,
                         subject: Optional[str] = None,
                         id_: Optional[str] = None,
                         ) -> str:
        email_type = "sent" if is_sender else "received"
        email_sender = f"<{from_}>" if email_type == 'received' else f"{username} <{from_}>"
        rows = [
            f"Email type: {email_type}",
            f"Email sender: {email_sender}",
            f'Email id: {id_}' if id_ else "",
            f"Email sent time: {date_str}" if date_str else '',
            f"Email subject: {subject}" if subject else "",
            f'Email body: \"\"\"{email_body}\"\"\"'
        ]
        return "\n".join([row for row in rows if row])

    @classmethod
    def get_email_pruner_subject(cls) -> str:
        return """Which rows belongs to previous conversation? Clean the email text, and remove any previous conversation. And last, your returned text should not include any prefix.\nHint1: all previous conversation are started with special characters, such as '>', '-', '='. '>' can appear multiple time as a prefix of each row. In otherword, '>>' is same as '>', and '>>>' is same as '>'. Same apply to other spcial characters. All previous conversation are consecutive rows. All past conversations always ended at the bottom of the email. \nHint2: Previous conversation can start after the first appearance of the sender's name or a closing statement. Therefore, any conversation after the sign of a closing statement should be consider as previous conversation.\nHint3: Previous conversation generally start with a sentence such as ""On [datetime], [sender name and email] wrote:""\nHint4: You are not asking to reply any email. Your task is to remove past emails from the given text.\nThe email i provided to you will be provided with a prefix "Email body: ", and delimited by triple quotes."""
