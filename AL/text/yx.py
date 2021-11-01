import yagmail
y=yagmail.SMTP(user='36883438@qq.com',password='gxhxmmaoawugbjbh',host='smtp.qq.com')
y.send(to='3164992481@qq.com',subject='日志,报告',contents='日志,报告',attachments=[r'bg.py',r'rizhi.py'])

