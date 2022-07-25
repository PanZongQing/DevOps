from django.http import HttpResponse
from common.models import Customer
from django.template import engines

html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话号码</th>
        <th>地址</th>
        </tr>

        {% for customer in customers %}
            <tr>

            {% for name, value in customer.items %}            
                <td>{{ value }}</td>            
            {% endfor %}

            </tr>
        {% endfor %}

        </table>
    </body>
</html>
'''

django_engine = engines['django']
template = django_engine.from_string(html_template)

def listorders(request):
    return HttpResponse('下面是系统中所有的订单信息...')

def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values()

    ph = request.GET.get('phonenumber',None)

    if ph:
        qs = qs.filter(phonenumber=ph)

    # 定义返回字符串
    # retStr = ''
    tableContent = ''
    for customer in qs:
        tableContent += '<tr>'
        for name,value in customer.items():
            # retStr += f'{name} : {value} | '
            tableContent += f'<td>{value}</td>'

        tableContent += '</tr>'

    return HttpResponse(html_template%tableContent)


# Create your views here.
