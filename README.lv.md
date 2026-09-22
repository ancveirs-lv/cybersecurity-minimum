# Kiberdrošības minimums ikvienam

**Latviski** · [English](README.md)

**25 praktiski noteikumi kontu, ierīču, datu un naudas aizsardzībai.**

Šis ir praktisks sabiedrības kiberdrošības minimums ikdienai. **Angļu versija ir globāla** un nebalstās Latvijas institūcijās vai pakalpojumos. Latviešu versijā saglabāti tie paši 25 kontroles ID, bet atsevišķi ieviešanas elementi lokalizēti Latvijai — tostarp CERT.LV incidentu ziņošana un CERT.LV/NIC.LV DNS ugunsmūris.

> **Universālais princips:** neļauj citiem vadīt tavu pieslēgšanos, ierīces vai naudas darījumus.

## Universālais lēmuma algoritms

`STOP → pārbaudi avotu → pats atver oficiālo pakalpojumu → pārbaudi citā veidā → tikai tad rīkojies`

## 25 noteikumu minimums

### 01–06 · Domā pirms rīkojies

- 01. Svarīgas darbības sāc pats.
- 02. Pirms maksājuma pārbaudi saņēmēju.
- 03. Steidzamība nozīmē pauzi.
- 04. Aizdomīgu pieprasījumu pārbaudi citā veidā.
- 05. Ziņa nepierāda, kas to sūtījis.
06. Ja šaubies — vispirms pārbaudi.

### 07–14 · Sargā kontus

- 07. Nekad nevienam nesūti paroles, PIN vai vienreizējos kodus.
- 08. Katram kontam sava parole.
- 09. Izmanto garu paroļu frāzi vai ģenerētu paroli.
- 10. Glabā paroles droši.
- 11. Ieslēdz passkey vai divu soļu apstiprināšanu.
- 12. Īpaši sargā galveno e-pastu.
- 13. Pārskati svarīgo kontu drošības iestatījumus.
14. Atvieno vecās ierīces un nevajadzīgas piekļuves.

### 15–20 · Sargā ierīces un tīklu

- 15. Bloķē telefonu un datoru.
- 16. Regulāri atjaunini ierīces un programmas.
- 17. Pārbaudi, vai ierīces aizsardzība ir ieslēgta.
- 18. Sargā mājas Wi‑Fi un rūteri.
- 19. Veido rezerves kopijas, kuras vari atjaunot.
20. Papildini aizsardzību ar CERT.LV/NIC.LV DNS ugunsmūri.

### 21–24 · Atpazīsti krāpšanu

- 21. Neatver negaidītus vai aizdomīgus pielikumus un QR kodus.
- 22. Neinstalē programmas pēc sveša cilvēka norādes.
- 23. Glīts dizains nepierāda uzticamību.
24. Sargies no pārāk labiem piedāvājumiem un emocionāliem stāstiem.

### 25 · Zini, ko darīt

25. Ziņo un rīkojies uzreiz.

Pilnie skaidrojumi: [Kiberdrošības minimums — detalizēti](docs/lv/kiberdrosibas-minimums.md).

## Lokalizācijas modelis

`globālais kontroles ID → globālā vadlīnija → lokālā ieviešanas piezīme`

EN un LV saglabā tos pašus 25 kontroles ID. Lokālās detaļas drīkst atšķirties, ja konkrētā institūcija, ziņošanas kanāls vai aizsardzības pakalpojums ir jurisdikcijas specifisks. Projekts **neuzdod Latvijas pakalpojumu par globālu standartu**.

## Pierādījumu modelis

`avots → kontrole → lokalizēta vadlīnija → validācija`

Mašīnlasāmie noteikumi ir `data/minimum.en.json` un `data/minimum.lv.json`; avoti — `data/sources.json`. CI pārbauda ID paritāti, avotu atsauces un lokalizācijas robežas.

## Avoti

Globālais pamats izmanto ENISA, CISA, UK NCSC un NIST. Latviešu lokalizācija papildus izmanto CERT.LV vietējai incidentu ziņošanai un DNS aizsardzībai.

## Tvērums

Šis ir praktisks sabiedrības materiāls, nevis organizācijas drošības programmas, incidentu plāna, juridiska atzinuma vai nozares regulējuma aizstājējs.

## Autors

**Zigmārs Ancveirs** — tehnoloģiju vadītājs, programmatūras inženieris un neatkarīgs kiberdrošības pētnieks.

## Licence

Dokumentācija un dati: **CC BY 4.0**. Kods un automatizācija: **MIT**. Skat. [LICENSE.md](LICENSE.md).
