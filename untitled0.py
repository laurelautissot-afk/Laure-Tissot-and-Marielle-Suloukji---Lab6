# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 22:12:48 2025

@author: laure
"""
import seaborn as sns
#4
import matplotlib.pyplot as plt

#5

####Relationship life expectancy and greenhouse gas
#sns.relplot(data=our_data , x="Life expectancy, female" , y="Greenhouse gas emissions" , kind="scatter")
#plt.title("Female life expectancy vs Greenhouse gas emissions")
#plt.show()
sns.relplot(data=our_data , x="Life expectancy, male" , y="Greenhouse gas emissions" , kind="scatter")
plt.title("Male life expectancy vs Greenhouse gas emissions")
plt.show()

#6

##a)
our_data["emissions_per_capita"] = (our_data["Greenhouse gas emissions"] / our_data["Population"])
sns.lmplot(data=our_data , x="emissions_per_capita" , y="Internet use") #to look at a linear regression relationship
sns.relplot(data=our_data , x="emissions_per_capita" , y="Internet use" , kind="scatter") #only a scatter plot relationship
plt.title("Emissions per capita vs Internet use")

##b)
filtered_values_for_emissions = our_data[our_data['emissions_per_capita'] > 0.03]
print(filtered_values_for_emissions ['Country Name'])


##c)


