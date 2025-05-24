from ._anvil_designer import Form1Template
from anvil import *
import random 

class Form1(Form1Template):

  def reset_operands(self):
    self.label_2.text = str(random.randint(0,9))
    self.label_3.text = str(random.randint(0,9))
    self.drop_down_1.selected_value = random.choice(['+','-','*','/'])
    if (self.drop_down_1.selected_value == '/') and (self.label_3.text == '0'):
      self.reset_operands()
    self.text_box_1.text = ''
    self.text_box_1.focus()

  def __init__(self, **properties):
    self.init_components(**properties)
    self.reset_operands()

  def button_1_click(self, **event_args):
    answertext = (
      self.label_2.text + ' ' + 
      self.drop_down_1.selected_value + ' ' + 
      self.label_3.text
    )
    answer = str(eval(answertext))
    if self.text_box_1.text == answer:
      alert('Correct!')
    else:
      alert('Incorrect')
    self.reset_operands()
      