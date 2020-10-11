from tkinter import *
import pandas as pd
from pytrends.request import TrendReq
from datetime import date
import os
import matplotlib.pyplot as plt
from tkcalendar import DateEntry
import tkentrycomplete
from PIL import ImageTk, Image

#Crea un diccionario con el codigo ISO para cada pais.
countryDict = {'World': '', 'Aruba': 'AW', 'Afghanistan': 'AF', 'Angola': 'AO', 'Anguilla': 'AI', 'Åland Islands': 'AX', 'Albania': 'AL', 'Andorra': 'AD', 'United Arab Emirates': 'AE', 'Argentina': 'AR', 'Armenia': 'AM', 'American Samoa': 'AS', 'Antarctica': 'AQ', 'French Southern Territories': 'TF', 'Antigua and Barbuda': 'AG', 'Australia': 'AU', 'Austria': 'AT', 'Azerbaijan': 'AZ', 'Burundi': 'BI', 'Belgium': 'BE', 'Benin': 'BJ', 'Bonaire, Sint Eustatius and Saba': 'BQ', 'Burkina Faso': 'BF', 'Bangladesh': 'BD', 'Bulgaria': 'BG', 'Bahrain': 'BH', 'Bahamas': 'BS', 'Bosnia and Herzegovina': 'BA', 'Saint Barthélemy': 'BL', 'Belarus': 'BY', 'Belize': 'BZ', 'Bermuda': 'BM', 'Bolivia, Plurinational State of': 'BO', 'Brazil': 'BR', 'Barbados': 'BB', 'Brunei Darussalam': 'BN', 'Bhutan': 'BT', 'Bouvet Island': 'BV', 'Botswana': 'BW', 'Central African Republic': 'CF', 'Canada': 'CA', 'Cocos (Keeling) Islands': 'CC', 'Switzerland': 'CH', 'Chile': 'CL', 'China': 'CN', "Côte d'Ivoire": 'CI', 'Cameroon': 'CM', 'Congo, The Democratic Republic of the': 'CD', 'Congo': 'CG', 'Cook Islands': 'CK', 'Colombia': 'CO', 'Comoros': 'KM', 'Cabo Verde': 'CV', 'Costa Rica': 'CR', 'Cuba': 'CU', 'Curaçao': 'CW', 'Christmas Island': 'CX', 'Cayman Islands': 'KY', 'Cyprus': 'CY', 'Czechia': 'CZ', 'Germany': 'DE', 'Djibouti': 'DJ', 'Dominica': 'DM', 'Denmark': 'DK', 'Dominican Republic': 'DO', 'Algeria': 'DZ', 'Ecuador': 'EC', 'Egypt': 'EG', 'Eritrea': 'ER', 'Western Sahara': 'EH', 'Spain': 'ES', 'Estonia': 'EE', 'Ethiopia': 'ET', 'Finland': 'FI', 'Fiji': 'FJ', 'Falkland Islands (Malvinas)': 'FK', 'France': 'FR', 'Faroe Islands': 'FO', 'Micronesia, Federated States of': 'FM', 'Gabon': 'GA', 'United Kingdom': 'GB', 'Georgia': 'GE', 'Guernsey': 'GG', 'Ghana': 'GH', 'Gibraltar': 'GI', 'Guinea': 'GN', 'Guadeloupe': 'GP', 'Gambia': 'GM', 'Guinea-Bissau': 'GW', 'Equatorial Guinea': 'GQ', 'Greece': 'GR', 'Grenada': 'GD', 'Greenland': 'GL', 'Guatemala': 'GT', 'French Guiana': 'GF', 'Guam': 'GU', 'Guyana': 'GY', 'Hong Kong': 'HK', 'Heard Island and McDonald Islands': 'HM', 'Honduras': 'HN', 'Croatia': 'HR', 'Haiti': 'HT', 'Hungary': 'HU', 'Indonesia': 'ID', 'Isle of Man': 'IM', 'India': 'IN', 'British Indian Ocean Territory': 'IO', 'Ireland': 'IE', 'Iran, Islamic Republic of': 'IR', 'Iraq': 'IQ', 'Iceland': 'IS', 'Israel': 'IL', 'Italy': 'IT', 'Jamaica': 'JM', 'Jersey': 'JE', 'Jordan': 'JO', 'Japan': 'JP', 'Kazakhstan': 'KZ', 'Kenya': 'KE', 'Kyrgyzstan': 'KG', 'Cambodia': 'KH', 'Kiribati': 'KI', 'Saint Kitts and Nevis': 'KN', 'Korea, Republic of': 'KR', 'Kuwait': 'KW', "Lao People's Democratic Republic": 'LA', 'Lebanon': 'LB', 'Liberia': 'LR', 'Libya': 'LY', 'Saint Lucia': 'LC', 'Liechtenstein': 'LI', 'Sri Lanka': 'LK', 'Lesotho': 'LS', 'Lithuania': 'LT', 'Luxembourg': 'LU', 'Latvia': 'LV', 'Macao': 'MO', 'Saint Martin (French part)': 'MF', 'Morocco': 'MA', 'Monaco': 'MC', 'Moldova, Republic of': 'MD', 'Madagascar': 'MG', 'Maldives': 'MV', 'Mexico': 'MX', 'Marshall Islands': 'MH', 'North Macedonia': 'MK', 'Mali': 'ML', 'Malta': 'MT', 'Myanmar': 'MM', 'Montenegro': 'ME', 'Mongolia': 'MN', 'Northern Mariana Islands': 'MP', 'Mozambique': 'MZ', 'Mauritania': 'MR', 'Montserrat': 'MS', 'Martinique': 'MQ', 'Mauritius': 'MU', 'Malawi': 'MW', 'Malaysia': 'MY', 'Mayotte': 'YT', 'Namibia': 'NA', 'New Caledonia': 'NC', 'Niger': 'NE', 'Norfolk Island': 'NF', 'Nigeria': 'NG', 'Nicaragua': 'NI', 'Niue': 'NU', 'Netherlands': 'NL', 'Norway': 'NO', 'Nepal': 'NP', 'Nauru': 'NR', 'New Zealand': 'NZ', 'Oman': 'OM', 'Pakistan': 'PK', 'Panama': 'PA', 'Pitcairn': 'PN', 'Peru': 'PE', 'Philippines': 'PH', 'Palau': 'PW', 'Papua New Guinea': 'PG', 'Poland': 'PL', 'Puerto Rico': 'PR', "Korea, Democratic People's Republic of": 'KP', 'Portugal': 'PT', 'Paraguay': 'PY', 'Palestine, State of': 'PS', 'French Polynesia': 'PF', 'Qatar': 'QA', 'Réunion': 'RE', 'Romania': 'RO', 'Russian Federation': 'RU', 'Rwanda': 'RW', 'Saudi Arabia': 'SA', 'Sudan': 'SD', 'Senegal': 'SN', 'Singapore': 'SG', 'South Georgia and the South Sandwich Islands': 'GS', 'Saint Helena, Ascension and Tristan da Cunha': 'SH', 'Svalbard and Jan Mayen': 'SJ', 'Solomon Islands': 'SB', 'Sierra Leone': 'SL', 'El Salvador': 'SV', 'San Marino': 'SM', 'Somalia': 'SO', 'Saint Pierre and Miquelon': 'PM', 'Serbia': 'RS', 'South Sudan': 'SS', 'Sao Tome and Principe': 'ST', 'Suriname': 'SR', 'Slovakia': 'SK', 'Slovenia': 'SI', 'Sweden': 'SE', 'Eswatini': 'SZ', 'Sint Maarten (Dutch part)': 'SX', 'Seychelles': 'SC', 'Syrian Arab Republic': 'SY', 'Turks and Caicos Islands': 'TC', 'Chad': 'TD', 'Togo': 'TG', 'Thailand': 'TH', 'Tajikistan': 'TJ', 'Tokelau': 'TK', 'Turkmenistan': 'TM', 'Timor-Leste': 'TL', 'Tonga': 'TO', 'Trinidad and Tobago': 'TT', 'Tunisia': 'TN', 'Turkey': 'TR', 'Tuvalu': 'TV', 'Taiwan, Province of China': 'TW', 'Tanzania, United Republic of': 'TZ', 'Uganda': 'UG', 'Ukraine': 'UA', 'United States Minor Outlying Islands': 'UM', 'Uruguay': 'UY', 'United States': 'US', 'Uzbekistan': 'UZ', 'Holy See (Vatican City State)': 'VA', 'Saint Vincent and the Grenadines': 'VC', 'Venezuela, Bolivarian Republic of': 'VE', 'Virgin Islands, British': 'VG', 'Virgin Islands, U.S.': 'VI', 'Viet Nam': 'VN', 'Vanuatu': 'VU', 'Wallis and Futuna': 'WF', 'Samoa': 'WS', 'Yemen': 'YE', 'South Africa': 'ZA', 'Zambia': 'ZM', 'Zimbabwe': 'ZW'}
countryList = ['World', 'Aruba', 'Afghanistan', 'Angola', 'Anguilla', 'Åland Islands', 'Albania', 'Andorra', 'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antarctica', 'French Southern Territories', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Bonaire, Sint Eustatius and Saba', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas', 'Bosnia and Herzegovina', 'Saint Barthélemy', 'Belarus', 'Belize', 'Bermuda', 'Bolivia, Plurinational State of', 'Brazil', 'Barbados', 'Brunei Darussalam', 'Bhutan', 'Bouvet Island', 'Botswana', 'Central African Republic', 'Canada', 'Cocos (Keeling) Islands', 'Switzerland', 'Chile', 'China', "Côte d'Ivoire", 'Cameroon', 'Congo, The Democratic Republic of the', 'Congo', 'Cook Islands', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curaçao', 'Christmas Island', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea', 'Western Sahara', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'Falkland Islands (Malvinas)', 'France', 'Faroe Islands', 'Micronesia, Federated States of', 'Gabon', 'United Kingdom', 'Georgia', 'Guernsey', 'Ghana', 'Gibraltar', 'Guinea', 'Guadeloupe', 'Gambia', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'French Guiana', 'Guam', 'Guyana', 'Hong Kong', 'Heard Island and McDonald Islands', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'British Indian Ocean Territory', 'Ireland', 'Iran, Islamic Republic of', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jersey', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati', 'Saint Kitts and Nevis', 'Korea, Republic of', 'Kuwait', "Lao People's Democratic Republic", 'Lebanon', 'Liberia', 'Libya', 'Saint Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao', 'Saint Martin (French part)', 'Morocco', 'Monaco', 'Moldova, Republic of', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Montserrat', 'Martinique', 'Mauritius', 'Malawi', 'Malaysia', 'Mayotte', 'Namibia', 'New Caledonia', 'Niger', 'Norfolk Island', 'Nigeria', 'Nicaragua', 'Niue', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Pitcairn', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', "Korea, Democratic People's Republic of", 'Portugal', 'Paraguay', 'Palestine, State of', 'French Polynesia', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'South Georgia and the South Sandwich Islands', 'Saint Helena, Ascension and Tristan da Cunha', 'Svalbard and Jan Mayen', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Saint Pierre and Miquelon', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovakia', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Tokelau', 'Turkmenistan', 'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Tuvalu', 'Taiwan, Province of China', 'Tanzania, United Republic of', 'Uganda', 'Ukraine', 'United States Minor Outlying Islands', 'Uruguay', 'United States', 'Uzbekistan', 'Holy See (Vatican City State)', 'Saint Vincent and the Grenadines', 'Venezuela, Bolivarian Republic of', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Viet Nam', 'Vanuatu', 'Wallis and Futuna', 'Samoa', 'Yemen', 'South Africa', 'Zambia', 'Zimbabwe']



#Creo un directorio en el cual guardo las imagenes y los DF en formato csv
os.makedirs('files', exist_ok = True)
os.chdir('.\\files')

#Estas opciones hacen que se puedan leer todos los datos dentro de la consola.
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


#Consigue el dia de hoy como opcion para el search de googleTrendsData
today = date.today() 


#Crea el window de tkinter
root = Tk()
root.title('Google Trends GUI')



#Llevar 3 parametros a un date que me sirva
def formatDate(year, month, day):
	return date(year, month, day)



def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


#Esta funcion consigue los datos actuales del input
def getTkInput(tkObject, mode = 'input'):
	if mode == 'input':
		return tkObject.get()

	elif mode == 'date':
		return tkObject.get_date()


#Esta clase tiene la funcionalidad de buscar datos para una lista de keywords.
class googleTrendsData:
	def __init__(self):
		pass


	def addModifierToKWList(self, modifier, keywords):
		#Modifica todos los keywords por una constante.
		for i in range(len(keywords)):
			keywords[i] += ' ' + modifier

		return keywords


	def search(self, timeFrom, keywords, country = '', modifier = None, timeTo = today):
		if modifier != None or modifier != '':
			keywords = self.addModifierToKWList(modifier, keywords)

		#Crea el objeto pytrend y consigue un dataframe con los datos dados.
		pytrend = TrendReq()
		pytrend.build_payload(keywords, timeframe = '%s %s' % (timeFrom, timeTo), geo = country)

		df = pytrend.interest_over_time()

		#Elimina la ultima columna de isPartial.
		df.drop('isPartial', axis = 1, inplace = True)


		df.index.rename('date', inplace = True)

		return df.reset_index()





#Esta clase purifica, guarda, visualiza y escribe visualizaciones del dataframe de google trends.
class dataFrameOperations:
	def __init__(self):
		pass



	#Reemplaza valores 0 por un promedio de la columna, hace un return del % de falta de datos
	def replaceLackOfData(self, df):
		#Consigue el % de los datos que se reemplazo (Datos que faltan)
		lineas, columnas = df.shape

		cuentas = []

		for i in df:
			if i != 'date':
				try:
					cuenta = df[i].value_counts()[0]
				except:
					cuenta = 0

				cuentas.append(int(cuenta/columnas))



		#Este loop reemplaza los 0 por el promedio
		for i in df:
			if i != 'date':
				promedioColumna = int(df[i].mean())
				df[i] = df[i].replace([0], promedioColumna)


		#Devuelve el % del error para que se sepa lo que falla
		n = 0
		errorList = []
		for i in df:
			if i != 'date':
				name = str(i) + ' error : ' + str(cuentas[n]) + ' %'
				errorList.append(name)

				n += 1

		return errorList




	#Toma un promedio del tiempo en un rango de filas
	def mergeByTime(self, df, weeks = 0, months = 0):
		skipTimes = weeks + 4 * months

		dfList = []

		#Esto convierte el DF en una lista de listas manejable
		for row in df.itertuples():
		    Index = True
		    chunk = []

		    for i in row:
		        if not Index:
		            chunk.append(i)

		        Index = False

		    dfList.append(chunk)


		#This calculates the average of 4 rows and takes the last date as the row name.
		n = skipTimes
		properDFList = chunks(dfList, n)

		purifiedList = [[]]

		for i in df:
			purifiedList[0].append(i)


		for chunk in properDFList:
		    averagedRow = [chunk[0][0]]
		    for x in chunk:
		        del(x[0])

		    avg = [float(sum(col))/len(col) for col in zip(*chunk)]
		    for number in avg:
		    	averagedRow.append(int(number))

		    purifiedList.append(averagedRow)

		headers = purifiedList.pop(0)

		purifiedDF = pd.DataFrame(purifiedList, columns = headers)

		for i in df:
			df[i] = purifiedDF[i]

		noNullDF = df.dropna(inplace = True)
		



	#Visualize produce un objeto imagen para despues visualizarlo con tkinter
	def savePlotVisualization(self, df, name, title = ''):
		plt.cla()
		ax = plt.gca()

		plt.title(title)

		colors = ['blue', 'red', 'green', 'black', 'purple']
		n = 0

		for i in df:
			if str(i) != 'date':
				df.plot(x = 'date', y = i, ax = ax, color = colors[n])

			n += 1


		fileName = '%s.png' % name

		plt.savefig(fileName)

		return fileName




	#Guardar el archivo como csv
	def saveFile(self, name, df):
		df.to_csv('%s.csv' % name, index = False)



	def compareDFValues(self, dfList, column, countryList):
		newDFList = [dfList[0]['date']]

		i = 0
		for df in dfList:
			#Conseguir la columna sin errores
			for x in df:
				if column in x:
					properColumn = x
					break

			dfToCompare = df[properColumn]
			dfToCompare.rename(column + (' (%s)' % countryList[i]), inplace=True)
			i += 1

			newDFList.append(dfToCompare)


		properDF = pd.concat(newDFList, axis = 1)

		
		return properDF





#Esta clase visualiza una lista de archivos png que contengan imagenes
class dfVisualizator:
	def __init__(self, plotList):
		self.top = Toplevel(root)

		self.imageFrame = LabelFrame(self.top)
		self.imageFrame.pack()

		self.currentPlot = 0
		self.plotList = plotList



	def visualize(self):
		self.purishFrame()

		file = Image.open(self.plotList[self.currentPlot])
		img = ImageTk.PhotoImage(file)
		panel = Label(self.imageFrame, image = img)
		panel.image = img
		panel.grid(row = 0, column = 0, columnspan = 3)


		backButton = Button(self.imageFrame, text = '<<', command = self.backPlot)
		nextButton = Button(self.imageFrame, text = '>>', command = self.nextPlot)

		if self.currentPlot > 0:
			backButton.grid(row = 1, column = 0)

		if (self.currentPlot + 1) < len(self.plotList):
			nextButton.grid(row = 1, column = 2)



	def backPlot(self):
		self.currentPlot -= 1
		self.visualize()


	def nextPlot(self):
		self.currentPlot += 1
		self.visualize()


	def purishFrame(self):
		self.imageFrame.destroy()
		self.imageFrame = LabelFrame(self.top)
		self.imageFrame.pack()





#Clase gui de la cual se consiguen los datos a buscar (La gran clase que une todo el resto del programa)
class gui:
	def __init__(self):
		self.operations = dataFrameOperations()
		self.trends = googleTrendsData()
		self.commonOperationsFrame = LabelFrame(root, text = 'Trends Operations')
		self.dataframe = []




	#Este metodo lleva a root todos los widgets que luego ramifican en distintos metodos.
	def run(self):
		#Frame with all general Data.
		generalDataFrame = LabelFrame(root, text = 'General Data')
		generalDataFrame.pack()


		#Keyword widgets
		#Frame for aesthetic purposes
		KwMdFrame = LabelFrame(generalDataFrame, borderwidth = 0)
		KwMdFrame.pack()


		kwLabel = Label(KwMdFrame, text = 'Keywords: ')
		kwInput = Entry(KwMdFrame)
		kwHelp = Label(KwMdFrame, text = '   Up to 5 keywords separated by a coma.  ')

		kwLabel.grid(row = 0, column = 0, sticky = 'W', pady = 2)
		kwInput.grid(row = 0, column = 1)
		kwHelp.grid(row = 0, column = 2, sticky = 'W')

		#Help Button
		helpButton = Button(KwMdFrame, text = 'Help', command = self.displayHelp)
		helpButton.grid(row = 0, column = 3, sticky = 'W', padx = 13)




		#Modifier widgets
		mdLabel = Label(KwMdFrame, text = 'Modifier: ')
		mdInput = Entry(KwMdFrame)
		mdHelp = Label(KwMdFrame, text = 'Adds a piece of text to all the keywords.')

		mdLabel.grid(row = 1, column = 0, sticky = 'W', pady = 2)
		mdInput.grid(row = 1, column = 1)
		mdHelp.grid(row = 1, column = 2)


		#Useful variable
		properKWList = kwInput.get().split(',')



		#Date widgets
		#Frame for aesthetic purposes
		dtFrame = LabelFrame(generalDataFrame, borderwidth = 0)
		dtFrame.pack(anchor = 'w')

		dtFromLabel = Label(dtFrame, text = 'From date: ')
		dtFromInput = DateEntry(dtFrame, selectMode = 'day', year = today.year, month = today.month, mindate = formatDate(2005, 1, 1), maxdate = today)
		dtToLabel = Label(dtFrame, text = 'To: ')
		dtToInput = DateEntry(dtFrame, selectMode = 'day', year = today.year, month = today.month, mindate = formatDate(2005, 1, 1), maxdate = today)


		dtFromLabel.grid(row = 1, column = 0, sticky = 'W', pady = 2)
		dtFromInput.grid(row = 1, column = 1, sticky = 'W') 
		dtToLabel.grid(row = 1, column = 2, sticky = 'W')
		dtToInput.grid(row = 1, column = 3, sticky = 'W') 



		#Popularity time merge widgets
		#Frame for aesthetic purposes
		popFrame = LabelFrame(generalDataFrame, borderwidth = 0)
		popFrame.pack(anchor = 'w')

		#Scrolldown menu data required
		options = [
			'Week(s)',
			'Month(s)'
		]

		variable = StringVar(popFrame)
		variable.set(options[1])

		popLabel = Label(popFrame, text = 'Average popularity every ')
		popInteger = Entry(popFrame, width = 4)
		popTimeUnit = OptionMenu(popFrame, variable, *options)

		popLabel.grid(row = 0, column = 0, pady = 2)
		popInteger.grid(row = 0, column = 1)
		popTimeUnit.grid(row = 0, column = 2, padx = 3)		


		#Button Widgets
		#Labelframe for aesthetic purposes
		buttonFrame = LabelFrame(generalDataFrame, borderwidth = 0)
		buttonFrame.pack(anchor = 'w')


		#Buttons for searching a single country or many.
		singleCountryButton = Button(buttonFrame, text = 'Trends for Single Country', command = lambda : (self.singleCountryTrends(keyWordList = getTkInput(kwInput).split(','), dateFrom = getTkInput(dtFromInput, mode = 'date'), dateTo = getTkInput(dtToInput, mode = 'date'), popularityTimeUnit = getTkInput(variable), popularityTimeModule = getTkInput(popInteger), modifier = getTkInput(mdInput))))
		multipleCountriesButton = Button(buttonFrame, text = 'Trends for Multiple Countries', command = lambda : (self.multipleCountryTrends(keyWordList = getTkInput(kwInput).split(','), dateFrom = getTkInput(dtFromInput, mode = 'date'), dateTo = getTkInput(dtToInput, mode = 'date'), popularityTimeUnit = getTkInput(variable), popularityTimeModule = getTkInput(popInteger), modifier = getTkInput(mdInput))))

		singleCountryButton.grid(row = 0, column = 0, pady = 8, padx = 30)
		multipleCountriesButton.grid(row = 0, column = 1, pady = 8, padx = 30)








	#Este metodo consigue los datos para un pais especifico y da las ramificaciones a las operaciones sobre ese data frame
	def singleCountryTrends(self, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier):
		#Este if condition se fija si los datos son correctos, de no serlo el metodo no hace nada mas.
		if keyWordList == [''] or popularityTimeModule == '' or keyWordList[0] == '' or len(keyWordList) > 4:
			#Run error method.
			return None



		#Deletes data within the common operations labelFrame
		self.deleteOperationsFrameData()



		#Country selection widget.
		countryLabel = Label(self.commonOperationsFrame, text = 'Select a country to find Trends or input "World": ')

		variable = StringVar(self.commonOperationsFrame)
		variable.set('World')

		countrySelection = tkentrycomplete.AutocompleteCombobox(self.commonOperationsFrame, textvariable = variable)
		countrySelection.set_completion_list(countryList)

		countryLabel.grid(row = 0, column = 0)
		countrySelection.grid(row = 0, column = 1)



		#Functionality Widgets.
		saveButton = Button(self.commonOperationsFrame, text = 'Save as csv', command = lambda : self.saveSingleDF(keyWordList, dateFrom, dateTo, popularityTimeUnit, int(popularityTimeModule), modifier, getTkInput(variable)))
		visualizeButton = Button(self.commonOperationsFrame, text = 'Visualize data', command = lambda : self.visualizeDF(keyWordList, dateFrom, dateTo, popularityTimeUnit, int(popularityTimeModule), modifier, getTkInput(variable)))

		saveButton.grid(row = 1, column = 0)
		visualizeButton.grid(row = 1, column = 1)







	def multipleCountryTrends(self, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier):
		#Este if condition se fija si los datos son correctos, de no serlo el metodo no hace nada mas.
		if keyWordList == [''] or popularityTimeModule == '' or keyWordList[0] == '' or len(keyWordList) > 4:
			#Run error method.
			return None



		#Deletes data within the common operations labelFrame
		self.deleteOperationsFrameData()



		#Multiple country input and widgets
		countryLabel = Label(self.commonOperationsFrame, text = 'Select up to 4 countries:')



		variable1 = StringVar(self.commonOperationsFrame)
		variable1.set('')
		countrySelection1 = tkentrycomplete.AutocompleteCombobox(self.commonOperationsFrame, textvariable = variable1)
		countrySelection1.set_completion_list(countryList)

		variable2 = StringVar(self.commonOperationsFrame)
		variable2.set('')

		variable3 = StringVar(self.commonOperationsFrame)
		variable3.set('')

		variable4 = StringVar(self.commonOperationsFrame)
		variable4.set('')

		variable1 = StringVar(self.commonOperationsFrame)
		variable1.set('')
		countrySelection1 = tkentrycomplete.AutocompleteCombobox(self.commonOperationsFrame, textvariable = variable1)
		countrySelection1.set_completion_list(countryList)

		countrySelection2 = tkentrycomplete.AutocompleteCombobox(self.commonOperationsFrame, textvariable = variable2)
		countrySelection2.set_completion_list(countryList)

		countrySelection3 = tkentrycomplete.AutocompleteCombobox(self.commonOperationsFrame, textvariable = variable3)
		countrySelection3.set_completion_list(countryList)

		countrySelection4 = tkentrycomplete.AutocompleteCombobox(self.commonOperationsFrame, textvariable = variable4)
		countrySelection4.set_completion_list(countryList)



		countryLabel.grid(row = 0, column = 0, padx = 10)

		countrySelection1.grid(row = 0, column = 1)
		countrySelection2.grid(row = 0, column = 2)
		countrySelection3.grid(row = 1, column = 1)
		countrySelection4.grid(row = 1, column = 2)



		#Buttons for functionality
		saveButton = Button(self.commonOperationsFrame, text = 'Save as csv', command = lambda : self.saveMultipleDF(keyWordList, dateFrom, dateTo, popularityTimeUnit, int(popularityTimeModule), modifier, [getTkInput(variable1),getTkInput(variable2),getTkInput(variable3),getTkInput(variable4)]))
		visualizeButton = Button(self.commonOperationsFrame, text = 'Visualize', command = lambda : self.visualizeMultipleDF(keyWordList, dateFrom, dateTo, popularityTimeUnit, int(popularityTimeModule), modifier, [getTkInput(variable1),getTkInput(variable2),getTkInput(variable3),getTkInput(variable4)]))

		#Compare es toda su funcionalidad separada
		compareButton = Button(self.commonOperationsFrame, text = 'Compare', command = lambda : self.compareDF(keyWordList, dateFrom, dateTo, popularityTimeUnit, int(popularityTimeModule), modifier, [getTkInput(variable1),getTkInput(variable2),getTkInput(variable3),getTkInput(variable4)]))

		saveButton.grid(row = 2, column = 0)
		visualizeButton.grid(row = 2, column = 1)
		compareButton.grid(row = 2, column = 2)





	def deleteOperationsFrameData(self):
		self.commonOperationsFrame.destroy()
		self.commonOperationsFrame = LabelFrame(root, text = 'Trends Operations')		
		self.commonOperationsFrame.pack(anchor = 'w')
		self.dataframe = []






	def saveSingleDF(self, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, country):
		self.dataframe = []

		self.getDF(keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, country)

		self.operations.saveFile(keyWordList[0] + ' ' + country, self.dataframe[0])




	def getDF(self, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifierr, countryy):
		#Elimina el modifier que por una razon desconocida se sigue appendeando a los valores de la lista original
		properKWList = keyWordList
		q = 0
		for i in properKWList:
			if modifierr in i and modifierr != '':
				properKWList[q] = properKWList[q].replace(' ' + modifierr, '')

			q += 1



		df = self.trends.search(dateFrom, properKWList, country = countryDict[countryy], modifier = modifierr, timeTo = dateTo)

		if popularityTimeUnit == 'Month(s)':
			self.operations.mergeByTime(df, months = popularityTimeModule)
		else:
			self.operations.mergeByTime(df, weeks = popularityTimeModule)


		self.dataframe.append(df)




	def visualizeDF(self, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, country):
		self.dataframe = []

		self.getDF(keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, country)

		fileName = self.operations.savePlotVisualization(self.dataframe[0], '1', title = country)

		visualizator = dfVisualizator([fileName])
		visualizator.visualize()





	def saveMultipleDF(self, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, countries):
		for country in countries:
			if country != '':
				self.saveSingleDF(keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, country)




	def visualizeMultipleDF(self, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, countries):
		self.dataframe = []
		fileNames = []

		n = 0
		for country in countries:
			if country != '':
				self.getDF(keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, country)

				fileName = self.operations.savePlotVisualization(self.dataframe[n], str(n), title = country)
				fileNames.append(fileName)
				n += 1

		visualizator = dfVisualizator(fileNames)
		visualizator.visualize()		




	def compareDF(self, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, countries):
		#Nueva ventana donde estan las opciones de visualizacion para el usuario.
		top = Toplevel(root)


		#Widgets para elegir keywords
		selectionLabel = Label(top, text = 'Select a keyword to compare between countries: ')

		variable = StringVar(top)
		variable.set(keyWordList[0])

		keywordSelection = OptionMenu(top, variable, *keyWordList)

		selectionLabel.grid(row = 0, column = 0, pady = 10)
		keywordSelection.grid(row = 0, column = 1, padx = 5)



		#Functionality buttons
		saveButton = Button(top, text = 'Save as csv', command = lambda : self.saveCompare(getTkInput(variable), keyWordList, dateFrom, dateTo, popularityTimeUnit, int(popularityTimeModule), modifier, countries))
		visualizeButton = Button(top, text = 'Visualize', command = lambda : self.visualizeCompare(getTkInput(variable), keyWordList, dateFrom, dateTo, popularityTimeUnit, int(popularityTimeModule), modifier, countries))


		saveButton.grid(row = 1, column = 0)
		visualizeButton.grid(row = 1, column = 1)




	def getComparisonDF(self, selectedKeyword, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, countries):
		self.dataframe = []

		for country in countries:
			if country != '':
				self.getDF(keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, country)


		comparisonDF = self.operations.compareDFValues(self.dataframe, selectedKeyword + ' ' + modifier, countries)

		return comparisonDF




	def saveCompare(self, selectedKeyword, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, countries):
		comparisonDF = self.getComparisonDF(selectedKeyword, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, countries)
		if modifier != '':
			self.operations.saveFile(selectedKeyword + ' ' + modifier + ' Country Comparison', comparisonDF)
		else:
			self.operations.saveFile(selectedKeyword + ' Country Comparison', comparisonDF)


		



	def visualizeCompare(self, selectedKeyword, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, countries):
		comparisonDF = self.getComparisonDF(selectedKeyword, keyWordList, dateFrom, dateTo, popularityTimeUnit, popularityTimeModule, modifier, countries)

		fileName = self.operations.savePlotVisualization(comparisonDF, '1')

		visualizator = dfVisualizator([fileName])
		visualizator.visualize()		






	def displayHelp(self):
		top = Toplevel(root)
		helpMethodology = Label(top, text = 'METHODOLOGY')
		helpLine0 = Label(top, text = "Google trend's methodology for calculating popularity consists in comparing popularity RELATIVE")
		helpLine01 = Label(top, text = "to the keyword's highest peak. When comparing 2 keywords or more, popularity is going to be relative")
		helpLine02 = Label(top, text = "to all of them. E.G: Obama may reach a 100 pop. peak in 2016 without comparison, but when contrasted")
		helpLine03 = Label(top, text = "to Donald Trump, that peak becomes only 3/4 as large and the referential peak becomes Trump's search volume")
		helpLine04 = Label(top, text = "in 2016. Woody Allen may have very little search volume in Argentina, but since popularity is relative to the")
		helpLine05 = Label(top, text = "keyword's highest peak in a specific region, when compared to the US, both countries may reach a peak at the same time.")
		helpLine06 = Label(top, text = "There is no relative comparison between countries, only keywords.\n\n")
		helpTutorial = Label(top, text = 'HOW TO USE')
		helpLine1 = Label(top, text = 'This app uses a google trends api to graph and download data in ways the website')
		helpLine2 = Label(top, text = 'does not allow you. Input up to 5 keywords separated by a coma to find')
		helpLine3 = Label(top, text = 'their popularity over time (From x date, to y date). The modifier appends')
		helpLine4 = Label(top, text = 'a string to all the keywords. E.g: Keywords = [obama, trump, bush] +')
		helpLine5 = Label(top, text = 'modifier = "aproval rating" => keywords = [obama aproval rating, trump aproval...')
		helpLine6 = Label(top, text = 'Leaving the modifier blank is fine.')
		helpLine7 = Label(top, text = '\n"Average popularity every X months/weeks" takes an average of the popularity every')
		helpLine8 = Label(top, text = '4 weeks * X months or every X weeks. It essentially makes the graph easier to read.')
		helpLine9 = Label(top, text = '\nThe "Trends for single country" button is self-explanatory (To reset general data click it again).')
		helpLine10 = Label(top, text = 'The "Trends for multiple countries" button allows for comparison between countries')
		helpLine11 = Label(top, text = 'and for saving/visualizing up to 5 country dataframes simultaneously (To reset general data click it again).')
		helpLine12 = Label(top, text = '\nCSV files saved in "files" folder created where the .exe or .py file is located.')
		helpLine13 = Label(top, text = '\nIf you find bugs or grammar errors and send it to https://sourceforge.net/u/whimscott/profile')
		helpLine14 = Label(top, text = "I'll be grateful :)")



		helpMethodology.pack(); helpLine0.pack() ;helpLine01.pack() ;helpLine02.pack() ;helpLine03.pack() ;helpLine04.pack() ; helpLine05.pack(); helpLine06.pack(); helpTutorial.pack()
		helpLine1.pack() ;helpLine2.pack() ;helpLine3.pack() ;helpLine4.pack() ;helpLine5.pack(); helpLine6.pack(); helpLine7.pack(); helpLine8.pack(); helpLine9.pack(); helpLine10.pack()
		helpLine11.pack(); helpLine12.pack(); helpLine13.pack(); helpLine14.pack()





app = gui()
app.run()


root.mainloop()
exit()