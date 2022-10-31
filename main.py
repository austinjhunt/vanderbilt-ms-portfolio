mystr = """Python, Java, Bash, PowerShell, PHP, HTML5, JS, TS, CSS3, Sass, Jinja2, EJS, Apache
                                Velocity, GraphQL, YAML, Markdown, JSON, nuXmv, React, jQuery"""

mystr2 = """Ubuntu, CentOS, RHEL, Windows, MacOS"""

mystr3 = """Django, Express, Spring, Node.js, Flask, React, Twilio, Apache Web Server, Nginx Web
                                Server, Heroku, Cloudflare, DNS Management, SSL certificate
                                configuration and renewal"""
mystr4 = """Git, GitHub, GitHub Actions, Travis CI, Docker, Docker Compose, Kubernetes, SSH &amp;
                                associated security practices, Ansible, Google Cloud Platform,
                                Grafana, Icinga 2, Cron, Splunk, NCPA, SNMP, WebGME (modeling &amp;
                                metamodeling), AWS IAM, AWS Serverless Application Model (SAM), AWS CloudFormation, AWS
                                EC2, AWS Cloudwatch, AWS Lambda, AWS S3, AWS API Gateway, Webhooks, Linode (IaaS), Azure
                                Active Directory, OAuth configuration, Microsoft Graph, Power Automate"""
mystr5 = """SharePoint Online, Microsoft Teams, Zoom, Webex, Wrike, Basecamp, Slack, Keybase, Azure
                                DevOps, TeamDynamix ITSM, ServiceNow, VPN"""


def split_into_skills(s):
    _s = [x.strip() for x in s.split(',')]
    _s = [f'<span class="skill">{x}</span>' for x in _s]
    return ''.join(_s)


for s in [mystr, mystr2, mystr3, mystr4, mystr5]:
    print()
    print(split_into_skills(s))
