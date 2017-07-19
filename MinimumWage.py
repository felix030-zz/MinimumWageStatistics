import pandas as pd
import matplotlib.pyplot as plt
from builtins import list
import matplotlib
matplotlib.style.use('ggplot')
import numpy as np

df = pd.read_excel('dataPM2015.xlsx')

#Vor Einführung des Mindestlohns April 2014
#Bruttolohn pro Stunde
brutto_lohn_h_2014_vollzeit = df.get_value(11,4,takeable=True)
print(brutto_lohn_h_2014_vollzeit)
brutto_lohn_h_2014_teilzeit = df.get_value(12,4,takeable=True)
brutto_lohn_h_2014_mini = df.get_value(13, 4, takeable=True)
#Arbeitsstunden pro Woche
aSt_woche_mittel_2014_vollzeit = df.get_value(15, 4, takeable=True)
aSt_woche_mittel_2014_teilzeit = df.get_value(16,4,takeable=True)
aSt_woche_mittel_2014_mini = df.get_value(17,4,takeable=True)
#Durchschnittlicher Lohnverdienst pro Woche in €
#Reallohn (Nominallohn / Preisindex(106,5%)) in €
#https://www.destatis.de/DE/Publikationen/Thematisch/Preise/Verbraucherpreise/VerbraucherpreisindexLangeReihenPDF_5611103.pdf?__blob=publicationFile
preisindex_2014 = 106.6
reallohn_2014_vollzeit = ((brutto_lohn_h_2014_vollzeit * aSt_woche_mittel_2014_vollzeit) / preisindex_2014) * 100
reallohn_2014_teilzeit = ((brutto_lohn_h_2014_teilzeit * aSt_woche_mittel_2014_teilzeit) / preisindex_2014) * 100
reallohn_2014_mini = ((brutto_lohn_h_2014_mini * aSt_woche_mittel_2014_mini) / preisindex_2014) * 100
print('Reallohn Vollzeit 2014: ' + str(reallohn_2014_vollzeit))
print('Reallohn Teilzeit 2014: ' + str(reallohn_2014_teilzeit))
print('Reallohn Minijob 2014: ' + str(reallohn_2014_mini))

#Nach Einführung des Mindestlohns April 2015 / für Mindestlohn berechtigt
#Bruttolohn pro Stunde
brutto_lohn_h_2015_vollzeit = df.get_value(11,2,takeable=True)
brutto_lohn_h_2015_teilzeit = df.get_value(12,2,takeable=True)
brutto_lohn_h_2015_mini = df.get_value(13, 2, takeable=True)
#Arbeitsstunden pro Woche
aSt_woche_mittel_2015_vollzeit = df.get_value(15, 2, takeable=True)
aSt_woche_mittel_2015_teilzeit = df.get_value(16,2,takeable=True)
aSt_woche_mittel_2015_mini = df.get_value(17,2,takeable=True)
#Durchschnittlicher Lohnverdienst pro Woche in €
#Reallohn (Nominallohn / Preisindex(106,5%)) in €
#https://www.destatis.de/DE/Publikationen/Thematisch/Preise/Verbraucherpreise/VerbraucherpreisindexLangeReihenPDF_5611103.pdf?__blob=publicationFile
preisindex_2015 = 106.9
reallohn_2015_vollzeit = ((brutto_lohn_h_2015_vollzeit * aSt_woche_mittel_2015_vollzeit) / preisindex_2015) *100
reallohn_2015_teilzeit = ((brutto_lohn_h_2015_teilzeit* aSt_woche_mittel_2015_teilzeit) / preisindex_2015)*100
reallohn_2015_mini = ((brutto_lohn_h_2015_mini * aSt_woche_mittel_2015_mini) / preisindex_2015) * 100
print('Reallohn Vollzeit 2015: '+ str(reallohn_2015_vollzeit))
print('Reallohn Teilzeit 2015: '+ str(reallohn_2015_teilzeit))
print('Reallohn Minijob 2015: ' + str(reallohn_2015_mini))

#Nach Einführung des Mindestlohns April 2015 / für Mindestlohn nicht berechtigt
#Bruttolohn pro Stunde
brutto_lohn_h_2015_vollzeit_nb = df.get_value(11,3,takeable=True)
brutto_lohn_h_2015_teilzeit_nb = df.get_value(12,3,takeable=True)
brutto_lohn_h_2015_mini_nb = df.get_value(13, 3, takeable=True)
#Arbeitsstunden pro Woche
aSt_woche_mittel_2015_vollzeit_nb = df.get_value(15, 3, takeable=True)
aSt_woche_mittel_2015_teilzeit_nb = df.get_value(16,3,takeable=True)
aSt_woche_mittel_2015_mini_nb = df.get_value(17,3,takeable=True)
#Durchschnittlicher Lohnverdienst pro Woche in €
#Reallohn (Nominallohn / Preisindex(106,5%)) in €
#https://www.destatis.de/DE/Publikationen/Thematisch/Preise/Verbraucherpreise/VerbraucherpreisindexLangeReihenPDF_5611103.pdf?__blob=publicationFile
preisindex_2015 = 106.9
reallohn_2015_vollzeit_nb = ((brutto_lohn_h_2015_vollzeit_nb * aSt_woche_mittel_2015_vollzeit_nb) / preisindex_2015) * 100
reallohn_2015_teilzeit_nb = ((brutto_lohn_h_2015_teilzeit_nb * aSt_woche_mittel_2015_teilzeit_nb) / preisindex_2015) * 100
reallohn_2015_mini_nb = ((brutto_lohn_h_2015_mini_nb * aSt_woche_mittel_2015_mini_nb) / preisindex_2015) * 100
print('Reallohn Vollzeit 2015 NB: '+ str(reallohn_2015_vollzeit_nb))
print('Reallohn Teilzeit 2015 NB: '+ str(reallohn_2015_teilzeit_nb))
print('Reallohn Minijob 2015 NB: ' + str(reallohn_2015_mini_nb))

print('Here comes the plot: \n')

list_reallohn_2014 = [reallohn_2014_vollzeit, reallohn_2014_teilzeit, reallohn_2014_mini]
list_reallohn_2015 = [reallohn_2015_vollzeit, reallohn_2015_teilzeit, reallohn_2015_mini]
list_reallohn_2015_nb = [reallohn_2015_vollzeit_nb, reallohn_2015_teilzeit_nb, reallohn_2015_mini_nb]
list_names = ['Vollzeit pro Woche','Teilzeit pro Woche','Mini Job pro Woche']

list_reallohn_week_vollzeit = [reallohn_2014_vollzeit,reallohn_2015_vollzeit_nb,reallohn_2015_vollzeit]
list_reallohn_week_teilzeit = [reallohn_2014_teilzeit,reallohn_2015_teilzeit_nb,reallohn_2015_teilzeit]
list_reallohn_week_mini = [reallohn_2014_mini,reallohn_2015_mini_nb,reallohn_2015_mini]



df_out = [list_names, list_reallohn_2014,list_reallohn_2015,list_reallohn_2015_nb]

df_out = pd.DataFrame(
    {'Index':list_names,
    'Reallohn 2014': list_reallohn_2014,
    'Reallohn 2015 NB': list_reallohn_2015_nb,
    'Reallohn 2015': list_reallohn_2015
    })
df_out.set_index('Index', inplace=True)

df_out.to_csv('reallohn.csv', index=False)
df_out.to_html('reallohn.html',index=False)


n_groups = 3

# create plot
fig, ax = plt.subplots()
fig.canvas.set_window_title('Mindestlohn Bundesweit')

index = np.arange(n_groups)
bar_width = 0.20
opacity = 0.8

rects1 = plt.bar(index + 0.00, list_reallohn_week_vollzeit, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Vollzeit')
rects2 = plt.bar(index + bar_width, list_reallohn_week_teilzeit, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Teilzeit')
rects3 = plt.bar(index + bar_width * 2,list_reallohn_week_mini, bar_width,
                 alpha = opacity,
                 color='c',
                 label='Mini Job')
label_week_lists = ('2014 vor MdL', '2015 Nicht MdL berechtigt', '2015 mit MdL')

plt.ylabel('EUR')
plt.title('Reallöhne pro Woche / Bundestweit')
plt.xticks(index + bar_width, label_week_lists)
plt.legend(bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure)

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        print('this is height: ' + str(rect.get_height()))
        # Fraction of axis height taken up by this rectangle
        p_height = (height / y_height)
        # If we can fit the label above the column, do that;
        # otherwise, put it inside the column.
        if p_height > 0.95: # arbitrary; 95% looked good to me.
            label_position = height - (y_height * 0.05)
        else:
            label_position = height + (y_height * 0.01)

        ax.text(rect.get_x() + rect.get_width() / 2., label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1, ax)
autolabel(rects2, ax)
autolabel(rects3, ax)

plt.show()

# create plot 2
n_groups = 2
fig, ax = plt.subplots()
fig.canvas.set_window_title('Mindestlohn Bundesweit')

index = np.arange(n_groups)
bar_width = 0.20
opacity = 0.8

list_reallohn_week_vollzeit = [-8.159698443426123, 11.395025597733763]
list_reallohn_week_teilzeit = [-1.048913873322391, 28.99318154295449]
list_reallohn_week_mini = [-7.552596893170488, 7.959096278017519]


rects1 = plt.bar(index + 0.00, list_reallohn_week_vollzeit, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Vollzeit')
rects2 = plt.bar(index + bar_width, list_reallohn_week_teilzeit, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Teilzeit')
rects3 = plt.bar(index + bar_width * 2,list_reallohn_week_mini, bar_width,
                 alpha = opacity,
                 color='c',
                 label='Mini Job')

label_week_lists = ('2015 Nicht MdL berechtigt', '2015 mit MdL')

plt.ylabel('EUR')
plt.title('Differenzen der Reallöhne pro Woche / Bundesweit')
plt.xticks(index + bar_width, label_week_lists)
plt.legend(bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure)

def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        # print(dir(rect))
        height = 0

        if rect.get_y() < 0:
            height = rect.get_y()
            # print(str(rect.get_y()))
        else:
            height = rect.get_height()
            # print(rect.get_height())

        print(str(rect.get_height()))
        # Fraction of axis height taken up by this rectangle
        p_height = (height / y_height)
        # If we can fit the label above the column, do that;
        # otherwise, put it inside the column.
        if p_height > 0.95:  # arbitrary; 95% looked good to me.
            label_position = height - (y_height * 0.05) if (height > 0) else height + (y_height * 0.05)
        else:
            label_position = height + (y_height * 0.01) if (height > 0) else height - (y_height * 0.001)

        ax.text(rect.get_x() + rect.get_width() / 2.0, label_position,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1, ax)
autolabel(rects2, ax)
autolabel(rects3, ax)

plt.tight_layout()
plt.show()




