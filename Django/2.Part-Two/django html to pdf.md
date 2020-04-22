# জ্যাঙ্গো সাইটে HTML পেজ থেকে PDF ফাইল তৈরি করা


```python
xhtml2pdf এবং Reportlab লাইব্রেরী ব্যাবহার করে খুব সহজে html পেজ কে pdf ফাইলে রূপান্তর করা যায়।
Reportlab, xhtml2pdf, html5lib, pypdf ইন্সটল করে ফেলুন।

pip install ...

from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape

# Render pdf
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()

    # pdf name generate with date    
    date = datetime.date.today()
    tmpName = template_src.split('.')[0]
    pdfName=tmpName + "-"+ str(date)

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename='+pdfName+'.pdf'        
        return response
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
    
    
def student_information_pdf(request):
    students = StudentAdmit.objects.all()
    deparments = Department.objects.filter(active=True)
    context = {
        'students': students,
        'departments': deparments
        } 
    pdf = render_to_pdf("html_to_pdf.html", context)
    download = request.GET.get('download')
    if download:
        return pdf 
    return HttpResponse(pdf, content_type='application/pdf')
    
    This code add to view section
```







