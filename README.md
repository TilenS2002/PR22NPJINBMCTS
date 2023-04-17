# POROČILO: Statistika okoliščin prometnih nesreč v Sloveniji v letu 2021 in 2022

**Problem:** Prometne nesreče so velik povzročitelj fizičnih poškodb in smrti v Sloveniji.

**Podatki:** Za bazo podatkov smo uporabili analizo prometne varnosti za leto 2022. V bazi so združeni vsi podatki o prometnih nesrečah in udeleženih osebah, katere so nastopale kot povzročitelj ali poškodovanec/žrtev. Baza zajema vse prometne nesreče katere si je ogledala in analizirala policija. V bazi podatkov, smo zasledili tudi nekaj napak pri vnosu, in sicer pri formatiranju določenih podatkov. Celotno ločevanje podatkov in popravljanje formatiranja podatkov smo opravili pred analizami in vizualizacijami.

### Ločevanje podatkov za obdelavo (`locevanje_tabel.py`):
Zaradi velike količine podatkov, smo celotno podatkovno bazo ločili na manjše, bolj obvladljive in modularne tabele. To smo naredili z razlogom olajšanja upravljanja s podatki in vizualizacijami podatkov. Podatke smo ločili z uporabo zgoraj navedene datoteke. Bazo smo ločili na 9 različnih tabel: 
- `Splosno.csv` (klasifikacija nesreče),  
- `Kraj.csv` (vsebuje glavne podatek o krajih), 
- `Cas.csv` (vsebuje datum in čas), 
- `Cesta.csv` (vrsta ceste naselja), 
- `Koordinate.csv`, 
- `Nesreca.csv` (vzrok in tip nesreče), 
- `FaktorCest.csv` (stanje prometa in vozišča, vrsta vozišča in vremenske okoliščine), 
- `FaktorOseb.csv` (uporaba varnostnega pasu, vsebnost alkohola, vrednost strokovnega pregleda),
- `Osebe.csv` (povzročitelj/udeleženec, starost, spol, državljanstvo, vrsta udeleženega, poškodba, vozni staz v mesecih). 
Pri vseh tabelah smo za Id uporabili VPN šifre, kajti te so edine unikatne.
Za bolj podrobno razlago kako se vse te stvari izvajajo si lahko preberete komentarje v `locevanje_tabel.py`.

### Izvedene analize:

<p><span style="color:red">Opomba: vsaka analiza je vsebovana v svoji datoteki!</span></p>

<!-- pogledu kaj so tipi posledic pri pn, določu barve, pobarvu lokacije tiste barve kukr je tip posledic -->
**posledice prometnih nesreč:** Pri tej analizi smo si ogledali kateri tipi posledic so kategorizirani pri prometnih nesrečah. 
Vsebovanih je 5 kategorij: 
- 0 - Brez poškodbe, 
- 1 - Lažja telesna poškodba, 
- 2 - Huda telesna poškodba, 
- 3 - Smrt, 
- 4 - Brez poškodbe-UZ (zelo podobno 0, uporabljata isto barvo)
Vsaki kategoriji smo določili svojo barvo, ter jih označili po lokacijah. Tako dobimo predstavo v katerih delih Slovenije je prišlo do lažjih/hujših prometnih nesreč.

<!-- uzeu use prometne in jih fuknu u eno mapo -->
**pogostost prometnih nesreč po sloveniji:** 

**vremenske okoliščine pri prometnih nesrečah:**

**Količina (procentualno) nesreč zjutraj, popoldne in zvečer:**

```python
# tle bo koda od analize podatkov
```

### Glavne ugotovitve in rezultati:
