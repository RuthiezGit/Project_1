from flask import Flask, request, render_template
import com
from com import sketch, convtogcode, run_gcode

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('rob_art.html')

@app.route('/page2')
def page2():
    return render_template('style_Art.html')


@app.route('/generate', methods=['POST'])
def generate():
    file = request.files['file']
    file.save(r"C:\Users\USER\Desktop\RAIN\Project1\Presentation\new\Web_App\image1.jpg")
    com.sketch()
    com.convtogcode()
    com.run_gcode()
    return 'File uploaded and processed successfully'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=False)
