import sys
import platform

__title__ = 'cobra'
__description__ = 'Code Security Audit'
__url__ = 'https://github.com/wufeifei/cobra'
__issue_page__ = 'https://github.com/wufeifei/cobra/issues/new'
__python_version__ = sys.version.split()[0]
__platform__ = platform.platform()
__version__ = '1.0.0-mycobra'
__author__ = 'jiang'
__author_email__ = 'jiangying1110@outlook.com'
__license__ = 'MIT License'
__copyright__ = 'Copyright (C) 2017 jiang. All Rights Reserved'
__introduction__ = """
                ___      _               
  /\/\  _   _  / __\___ | |__  _ __ __ _ 
 /    \| | | |/ /  / _ \| '_ \| '__/ _` |
/ /\/\ \ |_| / /__| (_) | |_) | | | (_| |
\/    \/\__, \____/\___/|_.__/|_|  \__,_|
        |___/                             v{version}

GitHub: https://github.com/DurianCoder/MyCobra.git

Cobra is a static code analysis system that automates the detecting vulnerabilities and security issue.""".format(version=__version__)
__epilog__ = """Usage:
  python {m} -t {td}
  python {m} -t {td} -r cvi-100001,cvi-100002
  python {m} -t {td} -f json -o /tmp/report.json 
  python {m} -t {tg} -f json -o jiangying1110@outlook.com 
  python {m} -t {tg} -f json -o http://push.to.com/api 
  python {m} -H 127.0.0.1 -P 8888
""".format(m='cobra.py', td='tests/vulnerabilities', tg='https://github.com/ethicalhack3r/DVWA')
