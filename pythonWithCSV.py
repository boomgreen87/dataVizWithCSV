import csv
import numpy as np
import matplotlib.pyplot as plt

# Figure out what data we want to use
categories = [] # These are the column headers in the CSV file
installs = [] # This is the installs column
ratings = [] # This is the ratings column

with open('data/googeplaystore.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		# Move the page column headers out of the actual data to get a clean dataset
		if line_count is 0: # This will be text, not data
			print ('Pushing categories into a separate array')
			categories.append(row) # Push the text into this array
			line_count += 1 # Increment the line count for the next loop
		else:
			# Grab the ratings and push them into the ratings array
			ratingsData = row[2]
			ratingsData = ratingsData.replace("NaN", "0")
			ratings.append(float(ratingsData))#float will turn a string into a number
			# print('Pushing rating data into the ratings array')
			installData = row[5]
			installData = installData.replace(",", "") # Get rid of the commas

			# Get rid of the trailing "+"
			installs.append(np.char.strip(installData, "+")) 
			line_count += 1

# Get some values we can work with
# How many ratings are 4+?
# How many are below 2?
# How many are in the middle?
np_ratings = np.array(ratings) # Turn a plain Python list into a Numpy array
popular_apps = np_ratings > 4
print("Popular apps:", len(np_ratings[popular_apps]))

percent_popular = len(np_ratings[popular_apps]) / len(np_ratings) * 100
print(percent_popular)

np_ratings = np.array(ratings) # Turn a plain Python list into a Numpy array
unpopular_apps = np_ratings < 4
print("Unpopular apps:", len(np_ratings[unpopular_apps]))

percent_unpopular = len(np_ratings[unpopular_apps]) / len(np_ratings) * 100
print(percent_unpopular)

kinda_popular = 100 - (percent_unpopular + percent_popular)
print(kinda_popular)

# Do a visualization with out shiny new data
labels = "Garbo", "Ight", "Daaaaaamn"
sizes = [percent_unpopular, kinda_popular, percent_popular]
colors = ['yellowgreen', 'lightgreen', 'lightskyblue']
explode = (0.2, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Does It Suck?: Google Play Apps")
plt.xlabel("User Ratings - App Installs (10,000+ apps)")
plt.show()
