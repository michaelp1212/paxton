import sys
sys.path.append('/home/me/Workspace')

from pyxero.xero import Xero
from pyxero.xero.auth import PrivateCredentials
from PyBambooHR.PyBambooHR import PyBambooHR
import os

BAMBOO_KEY = '43933574de57f2ab8634387531ab7dc77c850b8e'
BAMBOO_DOMAIN = 'barkteam'
XERO_CONSUMER_KEY = 'NJ0EBBCFUUPABFOXJMXIYAAPSR9HUJ'

with open('/home/me/server.key') as keyfile:
    rsa_key = keyfile.read()
    credentials = PrivateCredentials(XERO_CONSUMER_KEY, rsa_key)
    xero = Xero(credentials)

    payrun = xero.payrollAPI.payruns.all()
    employess = xero.payrollAPI.employees.all()
    last_payrun = payrun[len(payrun) - 1]
    payrun_id = last_payrun['payRunID']
    
    detail_payrun = xero.payrollAPI.payruns.get(payrun_id)
    startdate = detail_payrun['payRun']['periodStartDate']
    enddate = detail_payrun['payRun']['periodEndDate']
    paymentdate = detail_payrun['payRun']['paymentDate']
    message = detail_payrun['payRun']['payslipMessage']

    bamboo = PyBambooHR(subdomain='barkteam', api_key=BAMBOO_KEY)

    empls = []
    employees = bamboo.get_users()

    for id in list(employees):
        item = employees[id]
        id = item['employeeId']

        empls.append(bamboo.get_employee(id))
        #employee_number = empl['employeeNumber']

    for payslip in detail_payrun['payRun']['paySlips']:
        employee_id = payslip['employeeID']
        payslip_id = payslip['paySlipID']

        detail_payslip = xero.payrollAPI.payslips.get(payslip_id)

        PARAMS = {
            'payrun': payrun_id,
            'payslip': payslip_id,
        }

        url_path = "'http://localhost:5000/pdf?payrun={}&payslip={}&employee={}&startdate={}&enddate={}&paymentdate={}&message={}'".format(payrun_id, payslip_id, employee_id, startdate,
                                                                                                                                           enddate, paymentdate, message)
        pdf_path = "'/home/me/Workspace/xero/Pdf/{}.pdf'".format(payslip_id)
        cmd = "sudo {}  {} {}".format('/usr/bin/wkhtmltopdf', url_path, pdf_path)
        a= os.system(cmd)

        for empl in empls:
            id = empl['id']
            employee_number = empl['employeeNumber']
            if employee_number == employee_id:
                #pass
                pdf_path = "/home/me/Workspace/XeroApi/Pdf/{}.pdf".format(payslip_id)
                res = bamboo.upload_employee_file(id, pdf_path, 19, False)
        pass