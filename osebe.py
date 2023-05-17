import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

df = pd.read_csv('baze/manjse/Osebe.csv')

mask_povzrocitelj = (df['Povzrocitelj'] == 'POVZROČITELJ') & (df['MeseciIzpita'] > 0) & (df['MeseciIzpita'] < 1000)
povzrocitelj = df[mask_povzrocitelj]

mask_udelezenec = (df['Povzrocitelj'] == 'UDELEŽENEC')
udelezenec = df[mask_udelezenec]


##############################################################################################################################################################
###                                                              POVZROČITELJI                                                                             ###
##############################################################################################################################################################



mask_mladi_voznik = (povzrocitelj['MeseciIzpita'] > 0) & (povzrocitelj['MeseciIzpita'] <= 24)
mladi_voznik = povzrocitelj[mask_mladi_voznik]

mask_stari_voznik = (povzrocitelj['Starost'] > 70) & (povzrocitelj['MeseciIzpita'] > 0) & (povzrocitelj['MeseciIzpita'] > 24)
stari_voznik = povzrocitelj[mask_stari_voznik]

# print(f"Povzročitel nesreče je maldi voznik: {len(mladi_voznik)}")
# print(f"Povzročitel nesreče je starostnik: {len(stari_voznik)}")

stat_ml= len(mladi_voznik)/len((povzrocitelj['MeseciIzpita'] > 0))*100
stat_st= len(stari_voznik)/len((povzrocitelj['MeseciIzpita'] > 0))*100

print(f"Procent nesreč, ki jih je povzročil mladi voznik: {stat_ml:.2f}%")
print(f"Procent nesreč, ki jih je povzročil stari voznik: {stat_st:.2f}%")

####################################################################################################################
#                                                                                                                  #
#               ali je bolj izkusen voznik veckrat v nesreči zaradi neprilagojene hitrosti?                        #
#                                                                                                                  #
####################################################################################################################

# preberemo datoteke
problemi_df = pd.read_csv("baze/manjse/Nesreca.csv")

skupi = pd.merge(povzrocitelj, problemi_df, on='ZaporednaStevilkaOsebeVPN')

test = skupi[skupi['VzrokNesrece'].str.contains('NEPRILAGOJENA HITROST')]
meseci_izpita_counts_hitrost = test['MeseciIzpita'].value_counts().sort_index()

# korelacijski koeficient in vrednost-P
corr_coef_h, p_value_h = pearsonr(meseci_izpita_counts_hitrost, meseci_izpita_counts_hitrost.index)
print(f"Correlation coefficient: {corr_coef_h:.2f}")
print('P-value:',p_value_h)

#graf dobljenih rezultatov razmera hitrost in leto izpita
# sns.set_style('whitegrid')
# sns.regplot(x=meseci_izpita_counts_hitrost.index, y=meseci_izpita_counts_hitrost,scatter_kws={'color': 'grey'}, line_kws={'color': 'orange'})
# plt.title('Razmerje med meseci izpita povzročitelja in številom nesreč povzročenih zaradi prekomerne hitrosti')
# plt.xlabel('Meseci izpita')
# plt.ylabel('Stevilo nesreč')

# plt.annotate('r = {:.2f}'.format(corr_coef_h), xy=(0.65, 0.94) , xycoords='axes fraction', fontsize=12)
# plt.annotate('p = {:.2e}'.format(p_value_h), xy=(0.65, 0.88) , xycoords='axes fraction', fontsize=12)

# plt.show()

#############################################################################################################
#                                                                                                           #
#                               katera skupina večkrat ne upošteva cestnih pravil?                          #
#                                                                                                           #
#############################################################################################################

sitnFolk = skupi[skupi['VzrokNesrece'].str.contains('NEUPOŠTEVANJE PRAVIL O PREDNOSTI')]
meseci_izpita_counts_porednezi = sitnFolk['MeseciIzpita'].value_counts().sort_index()

mask_leto_izpita = (sitnFolk['MeseciIzpita'] > 0) & (sitnFolk['MeseciIzpita'] <= 12)
mask_leti2_voznik = (sitnFolk['MeseciIzpita'] > 12) & (sitnFolk['MeseciIzpita'] <= 24)
mask_med_2_in_5 = (sitnFolk['MeseciIzpita'] > 24) & (sitnFolk['MeseciIzpita'] <= 60)
mask_med_5_in_10 = (sitnFolk['MeseciIzpita'] > 50) & (sitnFolk['MeseciIzpita'] <= 120)
mask_med_10_in_20 = (sitnFolk['MeseciIzpita'] > 120) & (sitnFolk['MeseciIzpita'] <= 240)
mask_vec_kot_20 = sitnFolk['MeseciIzpita'] > 240

leto_izpita = sitnFolk[mask_leto_izpita]
leti2_voznik = sitnFolk[mask_leti2_voznik]
med_2_in_5 = sitnFolk[mask_med_2_in_5]
med_5_in_10 = sitnFolk[mask_med_5_in_10]
med_10_in_20 = sitnFolk[mask_med_10_in_20]
vec_kot_20 = sitnFolk[mask_vec_kot_20]

layout = [leto_izpita['MeseciIzpita'].count(), leti2_voznik['MeseciIzpita'].count(), med_2_in_5['MeseciIzpita'].count(), med_5_in_10['MeseciIzpita'].count(), med_10_in_20['MeseciIzpita'].count(), vec_kot_20['MeseciIzpita'].count()]
grupe = ["1 leto", "2 leti", "2 - 5 let", "5 - 10 let", "10 - 20 let", "vec kot 20 let"]

total_count= len(sitnFolk)

leto_izpita_percentage = len(leto_izpita) / total_count * 100
leti2_voznik_percentage = len(leti2_voznik) / total_count * 100
med_2_in_5_percentage = len(med_2_in_5) / total_count * 100
med_5_in_10_percentage = len(med_5_in_10) / total_count * 100
med_10_in_20_percentage = len(med_10_in_20) / total_count * 100
vec_kot_20_percentage = len(vec_kot_20) / total_count * 100

# Normalizing the data
normalized_leto_izpita_percentage = leto_izpita_percentage / (leto_izpita_percentage + leti2_voznik_percentage + med_2_in_5_percentage + med_5_in_10_percentage + med_10_in_20_percentage + vec_kot_20_percentage)
normalized_leti2_voznik_percentage = leti2_voznik_percentage / (leto_izpita_percentage + leti2_voznik_percentage + med_2_in_5_percentage + med_5_in_10_percentage + med_10_in_20_percentage + vec_kot_20_percentage)
normalized_med_2_in_5_percentage = med_2_in_5_percentage / (leto_izpita_percentage + leti2_voznik_percentage + med_2_in_5_percentage + med_5_in_10_percentage + med_10_in_20_percentage + vec_kot_20_percentage)
normalized_med_5_in_10_percentage = med_5_in_10_percentage / (leto_izpita_percentage + leti2_voznik_percentage + med_2_in_5_percentage + med_5_in_10_percentage + med_10_in_20_percentage + vec_kot_20_percentage)
normalized_med_10_in_20_percentage = med_10_in_20_percentage / (leto_izpita_percentage + leti2_voznik_percentage + med_2_in_5_percentage + med_5_in_10_percentage + med_10_in_20_percentage + vec_kot_20_percentage)
normalized_vec_kot_20_percentage = vec_kot_20_percentage / (leto_izpita_percentage + leti2_voznik_percentage + med_2_in_5_percentage + med_5_in_10_percentage + med_10_in_20_percentage + vec_kot_20_percentage)

print("Percentage of leti_izpita:", normalized_leto_izpita_percentage)
print("Percentage of leti2_voznik:", normalized_leti2_voznik_percentage)
print("Percentage of med_2_in_5:", normalized_med_2_in_5_percentage)
print("Percentage of med_5_in_10:", normalized_med_5_in_10_percentage)
print("Percentage of med_10_in_20:", normalized_med_10_in_20_percentage)
print("Percentage of vec_kot_20:", normalized_vec_kot_20_percentage)

# plt.bar(grupe, layout, color='grey')
# plt.title('Količina PN zaradi neupoštevanja pravil o prednosti, po starostnih skupinah')
# plt.xlabel('Starostne skupine')
# plt.ylabel('količina')
# plt.show()

# print("Length of leto_izpita:", len(leto_izpita))
# print("Length of leti2_voznik:", len(leti2_voznik))
# print("Length of med_2_in_5:", len(med_2_in_5))
# print("Length of med_5_in_10:", len(med_5_in_10))
# print("Length of med_10_in_20:", len(med_10_in_20))
# print("Length of vec_kot_20:", len(vec_kot_20))

meseci_izpita_counts = povzrocitelj['MeseciIzpita'].value_counts().sort_index()

# korelacijski koeficient in vrednost-P
corr_coef, p_value = pearsonr(meseci_izpita_counts, meseci_izpita_counts.index)
print(f"Correlation coefficient: {corr_coef:.2f}")
print('P-value:',p_value)

#graf dobljenih rezultatov
# sns.set_style('whitegrid')
# sns.regplot(x=meseci_izpita_counts.index, y=meseci_izpita_counts,scatter_kws={'color': 'grey'}, line_kws={'color': 'orange'})
# plt.title('Razmerje med meseci izpita povzročitelja in številom nesreč')
# plt.xlabel('Meseci izpita')
# plt.ylabel('Stevilo nesrec')

# plt.annotate('r = {:.2f}'.format(corr_coef), xy=(0.65, 0.94) , xycoords='axes fraction', fontsize=12)
# plt.annotate('p = {:.2e}'.format(p_value), xy=(0.65, 0.88) , xycoords='axes fraction', fontsize=12)

# plt.show()




# #isti graf k zgorn sam da ni scatter
# # sns.histplot(x=povzrocitelj['MeseciIzpita'], kde=False)
# # plt.title('Porazdelitev mesecev izpita pri povzročiteljih nesreč')
# # plt.xlabel('Meseci izpita')
# # plt.ylabel('Število nesreč')
# # plt.show()

# # sns.histplot(x=povzrocitelj['Starost'], kde=False)
# # plt.title('Porazdelitev starosti pri povzročiteljih nesreč')
# # plt.xlabel('Starost')
# # plt.ylabel('Število nesreč')
# # plt.show()

# # sns.boxplot(x=povzrocitelj['MeseciIzpita'])
# # plt.title('Razmerje med meseci izpita in številom nesreč')
# # plt.xlabel('Meseci izpita')
# # plt.show()

# # sns.boxplot(x=povzrocitelj['Starost'])
# # plt.title('Razmerje med starostjo in številom nesreč')
# # plt.xlabel('Starost')
# # plt.show()

##############################################################################################################################################################
###                                                                UDELEŽENCI                                                                              ###
##############################################################################################################################################################

udelezenec['VrstaUdelezenca'].replace(['VOZNIK LAHKEGA MOTORNEGA VOZILA', 'VOZNIK MOTORNEGA KOLESA', 'VOZNIK MOPEDA DO 25 KM/H', 'VOZNIK MOPEDA'], 'VOZNIKI MOTORNIH VOZIL', inplace=True)
udelezenci_counts = udelezenec['VrstaUdelezenca'].value_counts()
top10 = udelezenec["VrstaUdelezenca"].value_counts().nlargest(10)

# # Create a bar plot
# sns.barplot(x=counts.index, y=counts.values)
# plt.xticks(rotation=90)
# plt.title("Counts of VrstaUdelezenca")
# plt.xlabel("VrstaUdelezenca")
# plt.ylabel("Counts")
# plt.show()

counts = udelezenec['VrstaUdelezenca'].value_counts()
total_count = counts.sum()
percentages = 100 * counts / total_count

other_count = percentages[percentages < 1.5].sum()
percentages = percentages[percentages >= 1.5]
percentages['OSTALO'] = other_count

labels = percentages.index
sizes = percentages.values

def my_autopct(pct):
    return '{:.1f}%'.format(pct) if pct >= 2 else ''

# colors = ['#FF8533','grey', '#FF983E', '#FFAA48', '#FFB34D',  '#FFBC52','#FFCE5C' ]
# explode = [0.1 if size > sum(sizes)*0.03 else 0 for size in sizes] # explode only if size is greater than 3%

# fig, ax = plt.subplots(figsize=(10, 6))
# ax.pie(sizes, labels=labels,autopct=my_autopct, colors=colors, startangle=90, explode=explode, pctdistance=0.8) # type: ignore
# ax.axis('equal') # equal aspect ratio ensures that pie is drawn as a circle
# ax.set_title('Udeleženci v prometni nesreči',y=1.08)

# adjust the spacing between subplots to move the pie chart to the left
# plt.subplots_adjust(top=0.85)
# plt.show()




######################################################################################################################################
#                                                                                                                                    #
#                               Ali spol in starost res vplivata na kakovost voznika?                                                #
#                                                                                                                                    #
######################################################################################################################################

starost_counts_porednezi = skupi['Starost'].value_counts().sort_index()

mask_18_25 = (skupi['Starost'] >= 18) & (skupi['Starost'] <= 25)
mask_25_30 = (skupi['Starost'] > 25) & (skupi['Starost'] <= 30)
mask_30_39 = (skupi['Starost'] > 30) & (skupi['Starost'] <= 39)
mask_40_49 = (skupi['Starost'] > 39) & (skupi['Starost'] <= 49)
mask_50_59 = (skupi['Starost'] > 49) & (skupi['Starost'] <= 59)
mask_60_69 = (skupi['Starost'] > 59) & (skupi['Starost'] <= 69)
mask_vec_kot_70 = (skupi['Starost'] > 69)

e_18_25 = skupi[mask_18_25]
e_25_30 = skupi[mask_25_30]
e_30_39 = skupi[mask_30_39]
e_40_49 = skupi[mask_40_49]
e_50_59 = skupi[mask_50_59]
e_60_69 = skupi[mask_60_69]
vec_ku_70 = skupi[mask_vec_kot_70]

starSkupine = [
    e_18_25['Starost'].count() / len(skupi),
    e_25_30['Starost'].count() / len(skupi),
    e_30_39['Starost'].count() / len(skupi),
    e_40_49['Starost'].count() / len(skupi),
    e_50_59['Starost'].count() / len(skupi),
    e_60_69['Starost'].count() / len(skupi),
    vec_ku_70['Starost'].count() / len(skupi)
] 
normalized_starSkupine = [value / sum(starSkupine) for value in starSkupine]

print("Normalized starSkupine:", normalized_starSkupine)
StarLabli = ["18 - 25 let", "25 - 30 let", "30 - 39 let", "40 - 49 let", "50 - 59 let", "60 - 69 let", "vec kot 70 let"]

plt.bar(StarLabli, normalized_starSkupine, color='grey')
plt.title('Količina PN po starostnih skupinah')
plt.xlabel('Starostne skupine')
plt.ylabel('količina')
plt.show()

M18_25 = e_18_25[e_18_25['Spol'].str.contains('MOŠKI')].count()
Z18_25 = e_18_25[e_18_25['Spol'].str.contains('ŽENSKI')].count()

mzPN = [M18_25['Spol'] / len(e_18_25), Z18_25['Spol'] / len(e_18_25)]
listic = ["Moški", "Ženske"]

# plt.bar(listic, mzPN, color='grey')
# plt.title('Količina PN po spolu v starostni skupini 18 - 25')
# plt.xlabel('Spol')
# plt.ylabel('količina')
# plt.show()


print("Moški vdeleženci v PN: ",M18_25['Spol'])
print("Ženske vdeleženke v PN: ",Z18_25['Spol'])



# | Leta izpita| procent nesreč|
# |-|-|
# | <1 | 0.047% |
# |1-2| 0.022%|
# | 2-5 | 0.072%|
# |5-10| 0.109%|
# |10-20| 0.19%|
# |20<| 0.556|

# |starostna skupina | procent nesreč|
# |-|-|
# | 18-25 | 0.179%|
# |25-30|0.095%|
# |30-39| 0.164%|
# |40-49| 0.179%|
# |50-59| 0.149%|
# |60-69| 0.116%|
# |70<| 0.115%|
