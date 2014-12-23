'''
feature_functions.py
Implements the feature generation mechanism for RER
'''

from nltk import sent_tokenize, word_tokenize
import nltk
import json
import numpy
import pickle
import datetime


#lists tags
phones = ["phone", "phones", "smartphone", "smartphones", "mobile", "tablet", "tablets", "phablet", "phablets"]
org_list = ['Samsung', 'Apple', 'Microsoft', 'Nokia', 'Sony', 'LG', 'HTC', 'Motorola', 'Huawei', 'Lenovo', 'Xiaomi', 'Acer', 'Asus', 'BlackBerry', 'Alcatel', 'ZTE', 'Toshiba', 'Vodafone', 'T-Mobile', 'Gigabyte', 'Pantech', 'XOLO', 'Lava', 'Micromax', 'BLU', 'Spice', 'Prestigio', 'verykool', 'Maxwest', 'Celkon', 'Gionee', 'vivo', 'NIU', 'Yezz', 'Parla', 'Plum']
org_list1 = [m.lower() for m in org_list]
os_list = ["iOS", "Android", "Windows", "Symbian", "Bada", "Unix", "Linux", "Ubuntu", "OS", "RIM", "Firefox"]
os_list1 = [m.lower() for m in os_list]
currency_symbols = ["rs", "inr", "$", "usd", "cents", "rupees"]
size_list = ["inch", "cm", "inches", "cms", r'"', "''", "pixel", "px", "mega", "gb", "mb", "kb", "kilo", "giga", "mega-pixel", " Front Camera", "Rear Camera", "Dual SIM", "Flash Light", "Built-in", "Screen", "Display", "Memory", "Battery", "RAM"]
size_list1 = [m.lower() for m in size_list]
version_list = ["Kitkat", "Ice Cream Sandwich", "Lollipop", "Jelly Bean", "Ginger Bread", "Grand", "S4", "mini", "S5", "Note 3", "Ace", "Z3", "A065"]
version_list1 = [m.lower() for m in version_list]
family_list = ["Galaxy", "Moto", "Nexus", "Titanium", "Unite", "Torch", "Bolt", "Desire", "Redmi", "Lumia"]
family_list1 = [m.lower() for m in family_list]
other_list = ["I","Suggest","me","want","buy","a","new","release","Bangalore","Mumbai","market","Thailand","USA","Switzerland","India",
"China","Bangalore","Dubai","California","US","Arab","Kenya","November","month","Dec","week","tomorrow","January","Febraury","March","April","May","June","July","August","September","October","app","Whatsapp","Facebook","TrueCaller","Angry Birds","Twitter","Google","Maps","GPS","2014","ShareIt"]


#lists relations
interests = ["looking","buy","need","buying","interested"]



class FeatureFunctions(object):
	def __init__(self,di={},supported_tags=[],supported_rel=[]) :
		self.di = di
		self.supported_tags = supported_tags
		self.supported_rel = supported_rel

	##################FUNCTIONS####################

	def f

