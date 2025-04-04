# Google Sheets API

## Prerequisites
- Have python & pip working
    - Might need to type `pip3` instead of `pip`?
        - `> pip3 install ...` instead of `> pip install ...` 
        
- Set up virtual environment (if not using clion)
    - \> `python3 -m venv venv` *[run in terminal]*
    - \> `source venv/bin/activate` *[run in terminal]*
    - Should say *(venv)* before terminal entries now if it worked

## Steps
1. Make a Google form, and have the responses save to Google sheets
    - You need the ID if this sheet later, which is this part of the url:
        - ***docs.google.com/spreadsheets/d/***`1EmozOHR-QQGPJ6bn7PnuTBzbWDqNUDW_KA9hFfXAwcE`***/edit?resourcekey=&gid=952402027#gid=952402027***
    - Question 1 should ask their name, and question 2 should them to select the standards. For example: [Example Form](https://docs.google.com/forms/d/e/1FAIpQLSd3cn5URTaTVjfcwmNPv-vDJNApgGQ7Zyb-XFFJhgGB7nOPRg/viewform?usp=header)
    
2. Follow these instructions to get Google Cloud & everything set up: [Python Sheets Quickstart](https://developers.google.com/workspace/sheets/api/quickstart/python)
    - You don't have to run their actual quickstart program, but do every other step since the setup for this program is the same

# Example
```python
student_standards = get_student_standards("1EmozOHR-QQGPJ6bn7PnuTBzbWDqNUDW_KA9hFfXAwcE")

for student, standards in student_standards.items():
  print(f"Name:\t\t{student}")
  print(f"Standards:\t{standards}\n")
```

## Troubleshooting

### *Access blocked: <project_name> has not completed the Google verification process*
> - This may be because you didn't set your Google Console app to internal, but it doesn't let you set it to internal if you don't have a Google Workspace. If so, follow these steps:
>   1. Go to [Google Cloud app Audience](https://console.cloud.google.com/auth/audience?project=newest-test-454414)
>   2. Scroll down to **Test users**, and click `+ Add users`
>   3. Enter your email address and any other authorized test users, then click **Save**

### *Error: zsh: command not found: pip*
> -  Might need to type `pip3` instead of `pip`
>       - **Try:** `pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

### *ModuleNotFoundError: No module named 'oauth2client'*
> - **Run:** `pip3 install --upgrade google-api-python-client oauth2client`

### *FileNotFoundError: [Errno 2] No such file or directory: 'credentials.json'*
> - Make sure you put the .json file you downloaded earlier in your project folder
> - Make sure you *renamed* the file to `credentials.json`
    - or change file name in code to match what it is


### Misc
- [Troubleshoot authentication & authorization issues](https://developers.google.com/workspace/forms/api/troubleshoot-authentication-authorization)