import io
import smtplib
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from cgi import escape
from email.mime.text import MIMEText



def render_to_pdf(template_src, context_dict, name):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    with io.open(name, 'wb') as f:
        f.write(result.getvalue())

if __name__ == "__main__":
    s = smtplib.SMTP('mail.rosti.cz')
    s.login('organizatori@sdhsvinov.cz', 'kotalikovna')
    
