# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:50:23 2021

@author: z3525552
"""
import datetime
import os
from pathlib import Path
import win32com.client as win32

class EmailsSender:
    def __init__(self):
        self.outlook = win32.Dispatch('Outlook.Application')

    def send_email(self, to_email_address, attachment_path):
        
        today_string = datetime.datetime.today().strftime('%b %d, %Y')
        mail = self.outlook.CreateItem(0)
        mail.To = to_email_address
        mail.Subject = today_string + ' Report'
        
        mail.Body = """Please find today's report attached."""
        mail.Attachments.Add(Source=attachment_path)
        # Use this to show the email
        mail.Display(True)
        # Uncomment to send
        mail.Send()