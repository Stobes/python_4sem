from scraping_bilka import scrape_list
from ocr import img_to_list
from dataformat import clean_data
from datahandling import price_pr_unit
from dataframeing import pd_rep
from representation import grouped_barplot, sum_barplot, print_result
import pandas as pd

if __name__ == "__main__":

    foetex_data = [
        [['Bananer 4 pak øko', 2.25, 9.0],
        ['Bananer 6 pak øko', 2.00, 12.00]],

        [['Agurk', 8.50, 8.50],
        ['Agurk dansk øko', 10.00, 10.00],
        ['Agurk øko', 9.00, 9.00],
        ['Skoleagurker', 12.25, 4.08],
        ['Syltede agurker', 20.50, 107.89],
        ['Agurkesalat', 10.50, 25.86],
        ['Syltede drueagurker', 16.05, 30.28],
        ['Syltede drueagurker', 23.45, 78.17],
        ['Syltede cornichoner', 23.00, 135.29]],

        [['Grovhakket leverpostej', 17.90, 89.50],
        ['Grovhakket leverpostej', 30.50, 67.78],
        ['Leverpostej øko', 13.95, 69.75],
        ['Grov leverpostej', 12.00, 26.67],
        ['Fransk postej', 30.50, 67.78],
        ['Fransk postej', 17.90, 89.50],
        ['Baconleverpostej', 15.85, 79.25],
        ['Leverpostej', 11.95, 23.90],
        ['Kyllingepostej øko', 15.25, 76.25]],

        [['Skrabeæg S/M', 29.50, 1.97],
        ['Frilandsæg M/L', 18.75, 3.13],
        ['Æg M/L øko', 38.95, 3.90],
        ['Æg øko L/XL', 14.95, 3.74],
        ['Æg M/L øko', 27.95, 4.66],
        ['Skrabeæg M/L', 24.40, 3.05],
        ['Æg M/L øko', 33.95, 4.24],
        ['Æg L/XL øko', 27.50, 4.58],
        ['Skrabeæg L/XL', 23.40, 3.90]],

        [['Minimælk 0,4% fedt øko', 11.95, 11.95],
        ['Minimælk 0,4% fedt øko', 11.95, 11.95],
        ['Minimælk 0,5% fedt, laktosefri øko', 13.95, 13.95],
        ['Minimælk 0,4% fedt øko', 14.95, 14.95],
        ['Biodynamisk mælk 0,5% fedt øko', 15.25, 15.25],
        ['Minimælk 0,4% fedt i portionoer', 89, 44.50],
        ['Minimælk 0,4% fedt', 10.50, 10.50]],

        [['Arla ØKO, Økologisk smør 200g', 19.00, 95.00],
        ['Kærgården, Økologisk smørbart blandingsprodukt 72%, 200 g', 19.00, 95.00],
        ['Salling, Smør 250g', 20.95, 83.80],
        ['Bakkedal, Smørbart blandingsprodukt 75% 200g', 20.50, 102.50],
        ['Lurpak, Smørbart blandingsprodukt 78% 200g', 22.00, 110.00 ],
        ['Kærgården, Smørbart blandingsprodukt 72% 200g', 22.00, 110.00],
        ['Kærgården, Smørbart blandingsprodukt 72%', 20.00, 100.00],
        ['Smørbart blandingsprodukt 75% 250g', 16.95, 67.80],
        ['Naturli, Økologisk vegetabilsk blandingsprodukt 75% fedt 225g', 18.50, 82.22],
        ['Kærgården, Smørbart blandingsprodukt 57% 200g', 20.00, 100.00]],

        [['Bagepulver', 7.25, 51.79],
        ['Bagepulver øko', 13.25, 194.85],
        ['Bagepulver, Tørleffs', 11.95, 119.50],
        ['Brunt bagepulver med krydderi', 10.95, 608.33]]
    ]

    nemlig_data = [
        [['Bananer små øko.', 11.25, 11.25],
        ['Bananer små', 13.00, 1.86],
        ['Banan', 3.00, 3.00],
        ['Banan grøn øko', 3.5, 3.5],
        ['Plantain madbanan', 10.00, 10.00]],

        [['Agurk øko.', 9.00, 9.00],
        ['Agurk lille øko', 11.00, 11.00],
        ['Agutk', 8.5, 8.5],
        ['Madspildsagurker øko.', 12.00, 48.00],
        ['Skole agurker', 12.25, 4.08]],

        [['Grovhakket leverpostej', 20.00, 44.44],
        ['Leverpostej øko.', 11.21, 56.05],
        ['Grovhakket leverpostej', 17.90, 89.50],
        ['Leverpostej øko.', 19.95, 99.75],
        ['Leverpostej', 11.95, 23.90],
        ['Leverpostej øko.', 16.00, 58.18],
        ['Grovhakket leverpostej let', 16.00, 53.33]],

        [['Æg str. M/L øko.', 32.95, 3.30],
        ['Skrabeæg str. M/L', 29.50, 1.97],
        ['Skrabeæg str. M/L', 23.95, 2.40],
        ['Frilandsæg str. M/L', 30.25, 3.02],
        ['Frilandsæg str. M/L', 19.50, 3.25],
        ['Brunch æg str. L/XL øko.', 26.50, 6.13],
        ['Æg str. S/M øko.', 30.95, 3.87],
        ['Æg str. M/L øko.', 27.95, 4.66],
        ['Skrabe brunch æg str. L/XL', 32.95, 3.30]],

        [['Minimælk æko.', 11.95, 11.95],
        ['Letmælk øko.', 12.95, 12.95],
        ['Skummemælk øko.', 11.95, 11.95],
        ['Minimælk', 10.50, 10.50],
        ['Sødmælk', 11.50, 11.50],
        ['Minimælk', 11.50, 11.50],
        ['Letmælk', 10.75, 10.75]],

        [['Smør (saltet)', 20.95, 83.80],
        ['Smør øko.', 24.95, 123.75],
        ['Smør (saltet) øko.', 29.55, 147.75],
        ['Kuvertsmør (saltet)', 134.95, 168.69]],

        [['Bagepulver', 11.65, 51.78],
        ['Bagepulver', 12.25, 122.50],
        ['Bagepulver øko.', 29.95, 122.50],
        ['Bagepulver', 19.95, 142.50],
        ['Bagepulver øko.', 13.25, 194.85]]
    ]

    wordList = img_to_list("blocklistupdate3.png")

    print(wordList)

    scrapedList = scrape_list(wordList)

    cleaned_data = clean_data(scrapedList)

    foetex_unit_prices = price_pr_unit(foetex_data)
    foetex_df = pd_rep(foetex_unit_prices)
    foetex_df = (pd.DataFrame(foetex_df[0]).rename_axis('Føtex', axis=1), foetex_df[1])

    nemlig_unit_prices = price_pr_unit(nemlig_data)
    nemlig_df = pd_rep(nemlig_unit_prices)
    nemlig_df = (pd.DataFrame(nemlig_df[0]).rename_axis('Nemlig', axis=1), nemlig_df[1])

    bilka_unit_prices = price_pr_unit(cleaned_data)
    bilka_df = pd_rep(bilka_unit_prices)
    bilka_df = (pd.DataFrame(bilka_df[0]).rename_axis('Bilka', axis=1), bilka_df[1])

    dfs = [bilka_df, nemlig_df, foetex_df]
    
    grouped_barplot(wordList, bilka_df, foetex_df, nemlig_df)

    sum_barplot(bilka_df, foetex_df, nemlig_df)

    print_result(bilka_df, foetex_df, nemlig_df)

    #print('priser for Bilka: \n',bilka_df, '\n', 'priser for Nemlig: \n',nemlig_df,'\n', 'priser for Føtex: \n',foetex_df)


