from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

#Form Class for the entries
#Entries are required. Length is optional
class EntriesForm(Form):
	length = TextField('Length')
	entry_1 = TextField('Entry 1', validators = [Required()])
	entry_2 = TextField('Entry 2', validators = [Required()])
	entry_3 = TextField('Entry 3', validators = [Required()])
	entry_4 = TextField('Entry 4', validators = [Required()])
