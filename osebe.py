import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

df = pd.read_csv('baze/manjse/Osebe.csv')

mask_povzrocitelj = (df['Povzrocitelj'] == 'POVZROČITELJ') & (df['MeseciIzpita'] > 0) & (df['MeseciIzpita'] < 1000)
povzrocitelj = df[mask_povzrocitelj]

mask_udelezenec = (df['Povzrocitelj'] == 'UDELEŽENEC')
udelezenec = df[mask_udelezenec]

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

# mask_leto_izpita = (povzrocitelj['MeseciIzpita'] > 0) & (povzrocitelj['MeseciIzpita'] <= 12)
# mask_leti2_voznik = (povzrocitelj['MeseciIzpita'] > 12) & (povzrocitelj['MeseciIzpita'] <= 24)
# mask_med_2_in_5 = (povzrocitelj['MeseciIzpita'] > 24) & (povzrocitelj['MeseciIzpita'] <= 60)
# mask_med_5_in_10 = (povzrocitelj['MeseciIzpita'] > 50) & (povzrocitelj['MeseciIzpita'] <= 120)
# mask_med_10_in_20 = (povzrocitelj['MeseciIzpita'] > 120) & (povzrocitelj['MeseciIzpita'] <= 240)
# mask_vec_kot_20 = povzrocitelj['MeseciIzpita'] > 240

# leto_izpita = povzrocitelj[mask_leto_izpita]
# leti2_voznik = povzrocitelj[mask_leti2_voznik]
# med_2_in_5 = povzrocitelj[mask_med_2_in_5]
# med_5_in_10 = povzrocitelj[mask_med_5_in_10]
# med_10_in_20 = povzrocitelj[mask_med_10_in_20]
# vec_kot_20 = povzrocitelj[mask_vec_kot_20]

# print("Length of leto_izpita:", len(leto_izpita))
# print("Length of leti2_voznik:", len(leti2_voznik))
# print("Length of med_2_in_5:", len(med_2_in_5))
# print("Length of med_5_in_10:", len(med_5_in_10))
# print("Length of med_10_in_20:", len(med_10_in_20))
# print("Length of vec_kot_20:", len(vec_kot_20))

meseci_izpita_counts = povzrocitelj['MeseciIzpita'].value_counts().sort_index()
#print(meseci_izpita_counts)


# korelacijski koeficient in vrednost-P
corr_coef, p_value = pearsonr(meseci_izpita_counts, meseci_izpita_counts.index)
print(f"Correlation coefficient: {corr_coef:.2f}")
print('P-value:',p_value)



#graf dobljenih rezultatov
sns.set_style('whitegrid')
sns.regplot(x=meseci_izpita_counts.index, y=meseci_izpita_counts,scatter_kws={'color': 'grey'}, line_kws={'color': 'orange'})
plt.title('Razmerje med meseci izpita povzročitelja in številom nesreč')
plt.xlabel('Meseci izpita')
plt.ylabel('Stevilo nesrec')

plt.annotate('r = {:.2f}'.format(corr_coef), xy=(0.65, 0.94) , xycoords='axes fraction', fontsize=12)
plt.annotate('p = {:.2e}'.format(p_value), xy=(0.65, 0.88) , xycoords='axes fraction', fontsize=12)

plt.show()




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

colors = ['#FF8533','grey', '#FF983E', '#FFAA48', '#FFB34D',  '#FFBC52','#FFCE5C' ]
explode = [0.1 if size > sum(sizes)*0.03 else 0 for size in sizes] # explode only if size is greater than 3%

fig, ax = plt.subplots(figsize=(10, 6))
ax.pie(sizes, labels=labels,autopct=my_autopct, colors=colors, startangle=90, explode=explode, pctdistance=0.8) # type: ignore
ax.axis('equal') # equal aspect ratio ensures that pie is drawn as a circle
ax.set_title('Udeleženci v prometni nesreči',y=1.08)

# adjust the spacing between subplots to move the pie chart to the left
plt.subplots_adjust(top=0.85)


plt.show()
