#from flask import Flask, render_template, request
import flask
from SMS import SendSMS #activate when SMS function is ok
#from objectdetection_finalversion import run_detector_withDefinedModel
from commend_delect import price_finder, compare
import os
#import new_egg_detection

#compare(noOfS, item_name, store):
#price_finder(address, no, item_name)
SMSC = 1
phoneno = '51124927'

dp1 = 'web.html'
dp2 = 'web2.html'
dp3 = 'web3.html'
dp = [dp1, dp2, dp3]
img_path = "../999cccc/egg2.jpg" ##input image directory u want to detect

app = flask.Flask(__name__)



#@app.route('/<ip>')     #ESP wifi thing
#def redirect_to_link(ip):
#    return flask.redirect('ip')

#@app.route('/lan/<url>')    #ESP wifi THing
#def serve_from_lan(url):
#   r = flask.requests.get("http://"+url, allow_redirects=True)
#   return r.content

@app.route('/web')      #store 1
def web():
    return flask.send_file('web.html')

@app.route('/web2') #store 2
def web2():
    return flask.send_file('web2.html')

@app.route('/web3') #store 3
def web3():
    return flask.send_file('web3.html')

@app.route('/') #index
def index():

    return flask.send_file('index.html')
@app.route('/main') #home page
def main():
    if (SMSC == 1):
        
        result = flask.request.host_url  # get the address for sending sms
        result = f'This is the server address {result}'
        serverResponse = SendSMS(result, phoneno)
        print(serverResponse)
        print(result)
        return flask.render_template('main.html')
    else:
        return flask.render_template('main.html')
    
@app.route('/program1', methods=['GET', 'POST'])    #price finding
def program1():
    if flask.request.method == 'POST':
        tpath = flask.request.form.get('address')
        if tpath == ('1'):
            address = dp1
        else:
            if tpath == ('2'):
                address = dp2
            else:
                if tpath == ('3'):
                    address = dp3
                else:
                    address = tpath
        item_names = flask.request.form.getlist('item_name[]')

        result = []
        #print(item_names)
        for item_name in item_names:
            result.append(price_finder(address, item_name))

        return flask.render_template_string('<html><head><title>result1</title></head><body bgcolor=#FFFFED><h1>Result for price finding</h1><p>{{ result }}</p></html>', result=result)
    else:
        return flask.send_file('program1.html')
@app.route('/program2', methods=['GET', 'POST'])    #price comparison
def program2():
    #noOfS, item_name, store
    if flask.request.method == 'POST':
        store = flask.request.form.get('store')
        noOfS = flask.request.form.get('noOfS')
        item_name = flask.request.form.get('item_name')
        #return flask.render_template_string('<h1>Result for price compare</h1><p>{{ result }}</p>', result=noOfS)
        #print(noOfS)
        #print(item_name)
        #print(store)
        # Use the form data in your price_finder function
        result = compare(noOfS, item_name, store)
        print(result)
        #result = '\n'.join(map(str, result))

        # Return the result to a separate HTML page
        return flask.render_template_string('<html><head><title>result2</title></head><body bgcolor=#FFFFED><h1>Result for price compare</h1><p>{{ result }}</p></html>', result=result)
    else:
        return flask.send_file('program2.html')
@app.route('/receive_photo')
def receive_photo():
    #if 'photo' in request.files:
    #    photo = request.files['photo']
    #    photo.save('uploads/photo.jpg')  # Save the photo locally
    #    return flask.send_file('reveive_photo.html')
    #else:
        return flask.send_file('receive_photo.html')

@app.route('/show_result')  #ugo's thing
def show_result():
    return flask.send_file('ai.html')
#    try:
        # Run object detection and get the image path and results
        #image_path, results = run_detector_withDefinedModel(img_path)
#        image_path, results = run_detector_withDefinedModel("/home/ugo/FinalYearProject/999cccc/egg_test2.png")
        # Render the results in the result.html template
#        return flask.render_template('result.html', image_path=image_path, results=results)
#    except Exception as e:
        # Handle exceptions and render an error template if needed
#        return flask.render_template('error.html', error=str(e))
@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    #count = new_egg_detection()
    #result = f'{count} eggs left, refill it if you need'
    #if count <= 3:
    #    serverResponse = SendSMS(result, phoneno)
    #    print(serverResponse)
     #   print(result)
    return flask.render_template('cv.html')

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
