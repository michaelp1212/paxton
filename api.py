import sys
import os
sys.path.append('/home/me/Workspace')

from flask import redirect, render_template, url_for, flash, request, Flask, send_file, jsonify, send_from_directory
app = Flask(__name__)

PATH = '/home/me/Workspace/paxton';
@app.route("/", methods = ['GET', 'POST'])
def index():

    if request.method =='POST':
        address = ''
        nunit = ''
        showers = ''
        bathroom_sinks = ''
        kitchen_sinks = ''
        dishwashers = ''
        uclothes_washer = ''

        cclothes_washer = ''
        slop_sink = ''
        path = ''
        total_fu = ''
        gpm = ''
        cv = ''

        if request.method == 'POST':
            bathroom_sinks = request.values['bathroom_sinks']
            address = request.values['address']
            nunit = request.values['nunit']
            showers = request.values['showers']
            kitchen_sinks = request.values['kitchen_sinks']
            dishwashers = request.values['dishwashers']
            uclothes_washer = request.values['uclothes_washer']
            cclothes_washer = request.values['cclothes_washer']
            slop_sink = request.values['slop_sink']
            path = ''  # request.values['path']

            total_fu = request.values['fu']
            gpm = request.values['g']
            cv = request.values['c']

        url_path = "'http://localhost:5000/report?address={}&nunit={}&showers={}&bathroom_sinks={}&kitchen_sinks={}&dishwashers={}&uclothes_washer={}&cclothes_washer={}&slop_sink={}&path={}&fu={}&g={}&c={}'".format(
            address,
            nunit,
            showers,
            bathroom_sinks,
            kitchen_sinks,
            dishwashers,
            uclothes_washer,
            cclothes_washer,
            slop_sink,
            path,
            total_fu,
            gpm,
            cv
        )

        pdf_path = "'{}/Pdf/{}.pdf'".format(PATH, address)
        cmd = "{}  {} {}".format('/usr/local/bin/wkhtmltopdf', url_path, pdf_path)
        a = os.system(cmd)
        return send_from_directory(directory='Pdf', filename=address + '.pdf', as_attachment=True)
    return render_template('index.html')

@app.route("/pdf", methods=['GET', 'POST'])
def pdf():
    address = ''
    nunit = ''
    showers = ''
    bathroom_sinks = ''
    kitchen_sinks = ''
    dishwashers = ''
    uclothes_washer = ''

    cclothes_washer = ''
    slop_sink = ''
    path = ''
    total_fu = ''
    gpm = ''
    cv = ''

    if request.method == 'POST':
        bathroom_sinks = request.values['bathroom_sinks']
        address = request.values['address']
        nunit = request.values['nunit']
        showers = request.values['showers']
        kitchen_sinks = request.values['kitchen_sinks']
        dishwashers = request.values['dishwashers']
        uclothes_washer = request.values['uclothes_washer']
        cclothes_washer = request.values['cclothes_washer']
        slop_sink =request.values['slop_sink']
        path = ''#request.values['path']

        total_fu = request.values['fu']
        gpm = request.values['g']
        cv = request.values['c']

    url_path = "'http://localhost:5000/report?address={}&nunit={}&showers={}&bathroom_sinks={}&kitchen_sinks={}&dishwashers={}&uclothes_washer={}&cclothes_washer={}&slop_sink={}&path={}&fu={}&g={}&c={}'".format(
        address,
        nunit,
        showers,
        bathroom_sinks,
        kitchen_sinks,
        dishwashers,
        uclothes_washer,
        cclothes_washer,
        slop_sink,
        path,
        total_fu,
        gpm,
        cv
    )

    pdf_path = "'{}/Pdf/{}.pdf'".format(PATH, address)
    cmd = "{}  {} {}".format('/usr/local/bin/wkhtmltopdf', url_path, pdf_path)
    a = os.system(cmd)


    return render_template('pdf.html',
                           address = address,
                           nunit = nunit,
                           showers = showers,
                           bathroom_sinks = bathroom_sinks,
                           kitchen_sinks = kitchen_sinks,
                           dishwashers = dishwashers,
                           uclothes_washer = uclothes_washer,
                           cclothes_washer = cclothes_washer,
                           slop_sink = slop_sink,
                           path = path,
                           total_fu = total_fu,
                           gpm = gpm,
                           cv = cv)

@app.route("/report", methods=['GET'])
def report():
    address = ''
    nunit = ''
    showers = ''
    bathroom_sinks = ''
    kitchen_sinks = ''
    dishwashers = ''
    uclothes_washer = ''

    cclothes_washer = ''
    slop_sink = ''
    path = ''
    total_fu = ''
    gpm = ''
    cv = ''

    if request.method == 'GET':
        bathroom_sinks = request.values['bathroom_sinks']
        address = request.values['address']
        nunit = request.values['nunit']
        showers = request.values['showers']
        kitchen_sinks = request.values['kitchen_sinks']
        dishwashers = request.values['dishwashers']
        uclothes_washer = request.values['uclothes_washer']
        cclothes_washer = request.values['cclothes_washer']
        slop_sink =request.values['slop_sink']
        path = ''#request.values['path']

        total_fu = request.values['fu']
        gpm = request.values['g']
        cv = request.values['c']

    return render_template('pdf.html',
                           address = address,
                           nunit = nunit,
                           showers = showers,
                           bathroom_sinks = bathroom_sinks,
                           kitchen_sinks = kitchen_sinks,
                           dishwashers = dishwashers,
                           uclothes_washer = uclothes_washer,
                           cclothes_washer = cclothes_washer,
                           slop_sink = slop_sink,
                           path = path,
                           total_fu = total_fu,
                           gpm = gpm,
                           cv = cv)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)