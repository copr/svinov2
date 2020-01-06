# -*- coding: utf-8 -*-
import io
import smtplib
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from cgi import escape
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from stranky_sdhsvinov.secret import EMAIL_PASSWORD

email = 'organizatori@sdhsvinov.cz'
smtp_server = 'smtp.gmail.com'

def render_to_pdf(template_src, context_dict, name):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("utf-8")), result)
    with io.open(name, 'wb') as f:
        f.write(result.getvalue())

def create_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("utf-8")), result)
    return result

def send_summary_mail(to, organizer_mails, ticket):
    s = smtplib.SMTP(smtp_server)
    s.starttls()
    s.ehlo()
    s.login(email, EMAIL_PASSWORD)
    text = ('Shrnutí objednávky:\n'
            'Jméno a příjmení: ' + ticket.name + ' ' + ticket.surname + '\n'
            'Počet lístků: ' + str(ticket.number_of_tickets) + '\n'
            'Pokyny pro platbu: \n'
            'Číslo účtu: 2701521457/2010 \n'
            'Variabilní symbol: ' + str(ticket.id) + '\n'
            'Cena: ' + str(int(ticket.number_of_tickets) * ticket.event.price) + ' Kč\n'
            'Samotný lístek obdržíte alespoň tři dny před začátkem akce.')
    msg = MIMEText(text)
    recipients = organizer_mails
    recipients.append(to)
    recipients.append(email)
    msg['Subject'] = 'Shrnutí objednávky'
    msg['To'] = ", ".join(recipients)
    msg['From'] = email
    print(msg['to'])
    s.send_message(msg)
    s.quit()

def send_mail(fromm, to, subject, message, attachment=0):
    s = smtplib.SMTP(smtp_server)
    s.starttls()
    s.ehlo()
    s.login(mail, EMAIL_PASSWORD)
    msg = MIMEMultipart()
    msg.attach(MIMEText(message))
    if attachment:
        pdf = create_pdf('listek.html', {'ticket': {'name': 'martin',
                                                    'surname': 'kobersky'}})
        att = MIMEApplication(pdf.getvalue(), _subtype="pdf")
        att.add_header('Content-Disposition', 'attachment', filename='lupen.pdf')
        msg.attach(att)
#    msg = MIMEMultipart('alternative')
    msg['From'] = fromm
    msg['To'] = to
    msg['Subject'] = subject
    k = s.sendmail(fromm, to, msg.as_string())
    print(k)
    s.quit()

    
