import pandas as pd
import matplotlib.pyplot as plt
from builtins import list
import matplotlib
matplotlib.style.use('ggplot')
import numpy as np

df2_FB = pd.read_excel('dataBL2015.xlsx',sheetname= 'FB')

#Vor Einführung des Mindestlohns April 2014
#Bruttolohn pro Stunde
brutto_lohn_h_2014_vollzeit_FB = df2_FB.get_value(16, 4, takeable=True)
brutto_lohn_h_2014_teilzeit_FB = df2_FB.get_value(17, 4, takeable=True)
brutto_lohn_h_2014_mini_FB = df2_FB.get_value(18, 4, takeable=True)
# print(brutto_lohn_h_2014_vollzeit_FB)
# print(brutto_lohn_h_2014_teilzeit_FB)
# print(brutto_lohn_h_2014_mini_FB)

#Arbeitsstunden pro Woche
aSt_woche_mittel_2014_vollzeit_FB = df2_FB.get_value(20, 4, takeable=True)
aSt_woche_mittel_2014_teilzeit_FB = df2_FB.get_value(21, 4, takeable=True)
aSt_woche_mittel_2014_mini_FB = df2_FB.get_value(22, 4, takeable=True)
# print(aSt_woche_mittel_2014_vollzeit_FB)
# print(aSt_woche_mittel_2014_teilzeit_FB)
# print(aSt_woche_mittel_2014_mini_FB)

#Durchschnittlicher Lohnverdienst pro Woche in €
#Reallohn (Nominallohn / Preisindex(106,5%)) in €
#https://www.destatis.de/DE/Publikationen/Thematisch/Preise/Verbraucherpreise/VerbraucherpreisindexLangeReihenPDF_5611103.pdf?__blob=publicationFile
preisindex_2014 = 106.6
reallohn_2014_vollzeit_FB = ((brutto_lohn_h_2014_vollzeit_FB * aSt_woche_mittel_2014_vollzeit_FB) / preisindex_2014) * 100
reallohn_2014_teilzeit_FB = ((brutto_lohn_h_2014_teilzeit_FB * aSt_woche_mittel_2014_teilzeit_FB) / preisindex_2014) * 100
reallohn_2014_mini_FB = ((brutto_lohn_h_2014_mini_FB * aSt_woche_mittel_2014_mini_FB) / preisindex_2014) * 100
# print('Reallohn Vollzeit 2014: ' + str(reallohn_2014_vollzeit_FB))
# print('Reallohn Teilzeit 2014: ' + str(reallohn_2014_teilzeit_FB))
# print('Reallohn Minijob 2014: ' + str(reallohn_2014_mini_FB))

#Nach Einführung des Mindestlohns April 2015 / für Mindestlohn berechtigt
#Bruttolohn pro Stunde
brutto_lohn_h_2015_vollzeit_FB = df2_FB.get_value(16, 2, takeable=True)
brutto_lohn_h_2015_teilzeit_FB = df2_FB.get_value(17, 2, takeable=True)
brutto_lohn_h_2015_mini_FB = df2_FB.get_value(18, 2, takeable=True)
# print(brutto_lohn_h_2015_vollzeit_FB)
# print(brutto_lohn_h_2015_teilzeit_FB)
# print(brutto_lohn_h_2015_mini_FB)
#Arbeitsstunden pro Woche
aSt_woche_mittel_2015_vollzeit_FB = df2_FB.get_value(20, 2, takeable=True)
aSt_woche_mittel_2015_teilzeit_FB = df2_FB.get_value(21, 2, takeable=True)
aSt_woche_mittel_2015_mini_FB = df2_FB.get_value(22, 2, takeable=True)
# print(aSt_woche_mittel_2015_vollzeit_FB)
# print(aSt_woche_mittel_2015_teilzeit_FB)
# print(aSt_woche_mittel_2015_mini_FB)

#Durchschnittlicher Lohnverdienst pro Woche in €
#Reallohn (Nominallohn / Preisindex(106,5%)) in €
#https://www.destatis.de/DE/Publikationen/Thematisch/Preise/Verbraucherpreise/VerbraucherpreisindexLangeReihenPDF_5611103.pdf?__blob=publicationFile
preisindex_2015 = 106.9
reallohn_2015_vollzeit_FB = ((brutto_lohn_h_2015_vollzeit_FB * aSt_woche_mittel_2015_vollzeit_FB) / preisindex_2015) * 100
reallohn_2015_teilzeit_FB = ((brutto_lohn_h_2015_teilzeit_FB * aSt_woche_mittel_2015_teilzeit_FB) / preisindex_2015) * 100
reallohn_2015_mini_FB = ((brutto_lohn_h_2015_mini_FB * aSt_woche_mittel_2015_mini_FB) / preisindex_2015) * 100
print('Reallohn Vollzeit 2015: ' + str(reallohn_2015_vollzeit_FB))
print('Reallohn Teilzeit 2015: ' + str(reallohn_2015_teilzeit_FB))
print('Reallohn Minijob 2015: ' + str(reallohn_2015_mini_FB))

#Nach Einführung des Mindestlohns April 2015 / für Mindestlohn nicht berechtigt
#Bruttolohn pro Stunde
brutto_lohn_h_2015_vollzeit_nb_FB = df2_FB.get_value(16, 3, takeable=True)
brutto_lohn_h_2015_teilzeit_nb_FB = df2_FB.get_value(17, 3, takeable=True)
brutto_lohn_h_2015_mini_nb_FB = df2_FB.get_value(18, 3, takeable=True)

#Arbeitsstunden pro Woche
aSt_woche_mittel_2015_vollzeit_nb_FB = df2_FB.get_value(20, 3, takeable=True)
aSt_woche_mittel_2015_teilzeit_nb_FB = df2_FB.get_value(21, 3, takeable=True)
aSt_woche_mittel_2015_mini_nb_FB = df2_FB.get_value(22, 3, takeable=True)

#Durchschnittlicher Lohnverdienst pro Woche in €
#Reallohn (Nominallohn / Preisindex(106,5%)) in €
#https://www.destatis.de/DE/Publikationen/Thematisch/Preise/Verbraucherpreise/VerbraucherpreisindexLangeReihenPDF_5611103.pdf?__blob=publicationFile
preisindex_2015 = 106.9
reallohn_2015_vollzeit_nb_FB = ((brutto_lohn_h_2015_vollzeit_nb_FB * aSt_woche_mittel_2015_vollzeit_nb_FB) / preisindex_2015) * 100
reallohn_2015_teilzeit_nb_FB = ((brutto_lohn_h_2015_teilzeit_nb_FB * aSt_woche_mittel_2015_teilzeit_nb_FB) / preisindex_2015) * 100
reallohn_2015_mini_nb_FB = ((brutto_lohn_h_2015_mini_nb_FB * aSt_woche_mittel_2015_mini_nb_FB) / preisindex_2015) * 100
print('Reallohn Vollzeit 2015 NB: ' + str(reallohn_2015_vollzeit_nb_FB))
print('Reallohn Teilzeit 2015 NB: ' + str(reallohn_2015_teilzeit_nb_FB))
print('Reallohn Minijob 2015 NB: ' + str(reallohn_2015_mini_nb_FB))

print('Here comes the plot: \n')

list_reallohn_2014_FB = [reallohn_2014_vollzeit_FB, reallohn_2014_teilzeit_FB, reallohn_2014_mini_FB]
list_reallohn_2015_FB = [reallohn_2015_vollzeit_FB, reallohn_2015_teilzeit_FB, reallohn_2015_mini_FB]
list_reallohn_2015_nb_FB = [reallohn_2015_vollzeit_nb_FB, reallohn_2015_teilzeit_nb_FB, reallohn_2015_mini_nb_FB]
list_names = ['Vollzeit pro Woche','Teilzeit pro Woche','Mini Job pro Woche']

list_reallohn_week_vollzeit = [reallohn_2014_vollzeit_FB, reallohn_2015_vollzeit_nb_FB, reallohn_2015_vollzeit_FB]
list_reallohn_week_teilzeit = [reallohn_2014_teilzeit_FB, reallohn_2015_teilzeit_nb_FB, reallohn_2015_teilzeit_FB]
list_reallohn_week_mini = [reallohn_2014_mini_FB, reallohn_2015_mini_nb_FB, reallohn_2015_mini_FB]


# # create plot
# n_groups = 2
# fig, ax = plt.subplots()
# fig.canvas.set_window_title('Mindestlohn Bundesweit')
#
# index = np.arange(n_groups)
# bar_width = 0.20
# opacity = 0.8
#
# list_reallohn_week_vollzeit = [-8.159698443426123, 11.395025597733763]
# list_reallohn_week_teilzeit = [-1.048913873322391, 28.99318154295449]
# list_reallohn_week_mini = [-7.552596893170488, 7.959096278017519]
#
#
# rects1 = plt.bar(index + 0.00, list_reallohn_week_vollzeit, bar_width,
#                  alpha=opacity,
#                  color='b',
#                  label='Vollzeit')
# rects2 = plt.bar(index + bar_width, list_reallohn_week_teilzeit, bar_width,
#                  alpha=opacity,
#                  color='g',
#                  label='Teilzeit')
# rects3 = plt.bar(index + bar_width * 2,list_reallohn_week_mini, bar_width,
#                  alpha = opacity,
#                  color='c',
#                  label='Mini Job')
#
# label_week_lists = ('2015 Nicht MdL berechtigt', '2015 mit MdL')
#
# plt.ylabel('EUR')
# plt.title('Differenzen der Reallöhne pro Woche')
# plt.xticks(index + bar_width, label_week_lists)
# plt.legend(bbox_to_anchor=(1, 1),
#            bbox_transform=plt.gcf().transFigure)
#
# def autolabel(rects, ax):
#     # Get y-axis height to calculate label position from.
#     (y_bottom, y_top) = ax.get_ylim()
#     y_height = y_top - y_bottom
#
#     for rect in rects:
#         # print(dir(rect))
#         height = 0
#
#         if rect.get_y() < 0:
#             height = rect.get_y()
#             # print(str(rect.get_y()))
#         else:
#             height = rect.get_height()
#             # print(rect.get_height())
#
#         print(str(rect.get_height()))
#         # Fraction of axis height taken up by this rectangle
#         p_height = (height / y_height)
#         # If we can fit the label above the column, do that;
#         # otherwise, put it inside the column.
#         if p_height > 0.95:  # arbitrary; 95% looked good to me.
#             label_position = height - (y_height * 0.05) if (height > 0) else height + (y_height * 0.05)
#         else:
#             label_position = height + (y_height * 0.01) if (height > 0) else height - (y_height * 0.001)
#
#         ax.text(rect.get_x() + rect.get_width() / 2.0, label_position,
#                 '%d' % int(height),
#                 ha='center', va='bottom')
#
# autolabel(rects1, ax)
# autolabel(rects2, ax)
# autolabel(rects3, ax)
#
# plt.tight_layout()
# plt.show()