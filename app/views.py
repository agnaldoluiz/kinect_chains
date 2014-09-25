from flask import render_template, flash, redirect, url_for
from app import app
from forms import EntriesForm
import math

#Routing. All the program is at the same address which can
#be interpreted in 2 different versions: /  and /index
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():

	#Default entries
	entry1 = 0
	entry2 = 0
	entry3 = 0
	entry4 = 0
	#Default length
	length = 10

	#Create object form
	form = EntriesForm()

	#Logic when the form is submitted and validated
	if form.is_submitted():
		if form.validate():
			#get entries from form
			entry1 = form.entry_1.data
			entry2 = form.entry_2.data
			entry3 = form.entry_3.data
			entry4 = form.entry_4.data
			#if length is input... else... use default already assigned
			if(form.length.data):
				length = float(form.length.data)

			#Logic for the angles and to find all the outputs
			#Very easy-reading
			aux_angle = float(entry1)

			output1x = length * math.cos(math.radians(aux_angle))
			output1y = length * math.sin(math.radians(aux_angle))

			aux_angle = aux_angle + float(entry2)

			output2x = length * math.cos(math.radians(aux_angle)) + output1x
			output2y = length * math.sin(math.radians(aux_angle)) + output1y

			aux_angle = aux_angle + float(entry3)

			output3x = length * math.cos(math.radians(aux_angle)) + output2x
			output3y = length * math.sin(math.radians(aux_angle)) + output2y

			aux_angle = aux_angle + float(entry4)

			output4x = length * math.cos(math.radians(aux_angle)) + output3x
			output4y = length * math.sin(math.radians(aux_angle)) + output3y

			return render_template("index.html",
				length = length,
				entry1 = entry1,
				entry2 = entry2,
				entry3 = entry3,
				entry4 = entry4,
				output1x = format(output1x, '.4f'),
				output1y = format(output1y, '.4f'),
				output2x = format(output2x, '.4f'),
				output2y = format(output2y, '.4f'),
				output3x = format(output3x, '.4f'),
				output3y = format(output3y, '.4f'),
				output4x = format(output4x, '.4f'),
				output4y = format(output4y, '.4f'),
				form = form)
		#If form is not validated, flash an error message
		else:
			flash('Enter all 4 entries')
			return redirect(url_for('index'))
	
	#inputs necessary for the template
	return render_template("index.html",
		length = length,
		entry1 = entry1,
		entry2 = entry2,
		entry3 = entry3,
		entry4 = entry4,
		form = form)