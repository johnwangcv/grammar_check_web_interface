from flask import render_template

from flask import request

from flask import url_for

from markupsafe import escape

from flask import Flask

import language_tool_python
tool = language_tool_python.LanguageToolPublicAPI('es') # use the public API, language Spanish

app = Flask(
    __name__
    )


@app.route(
	'/spanish_grammar_checker',
	methods = [
		'POST',
		'GET',
		])

def spanish_grammar_checker():
	if request.method == 'POST':
		input_text = request.form['input_text']

		try:
			corrected_text = tool.correct(input_text)

			matches = '<br><br>'.join([f'{m.context}:<br>-> {m.message}' for m in tool.check(input_text)])

			#print(matches)

		except:
			corrected_text = ''
			matches = ''

		return render_template(
			"spanish_grammar_checker.html",
			corrected_text = corrected_text,
			input_text = input_text,
			matches = matches,
			)
	else:
		return render_template(
			"spanish_grammar_checker.html")


'''

# start the service

sudo yum install python-pip

pip3 install language_tool_python

rm -r -f grammar_check_web_interface

git clone https://github.com/johnwangcv/grammar_check_web_interface.git

cd grammar_check_web_interface

flask --app grammar_check_web_interface --debug run --host=0.0.0.0 --port=6912 



flask --app grammar_checker_web_interface --debug run --port=6912 --host=0.0.0.0

# user the service 

http://127.0.0.1:6912/spanish_grammar_checker

localhost:6912/spanish_grammar_checker

'''