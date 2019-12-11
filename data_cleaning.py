import os 
import pandas as pd

def preparation_data(path,concat=True): 
    
    ## Dataframe des caractétistiques 
    df_caracteristiques_2018 = pd.read_csv(os.path.join(path, 'caracteristiques_2018.csv'), encoding="ISO-8859-1")
    df_caracteristiques_2017 = pd.read_csv(os.path.join(path, 'caracteristiques_2017.csv'), encoding="ISO-8859-1")
    df_caracteristiques_2016 = pd.read_csv(os.path.join(path, 'caracteristiques_2017.csv'), encoding="ISO-8859-1")
    
    ## Dataframe des usagers 
    df_usagers_2018 = pd.read_csv(os.path.join(path, 'usagers_2018.csv'))
    df_usagers_2017 = pd.read_csv(os.path.join(path, 'usagers_2017.csv'))
    df_usagers_2016 = pd.read_csv(os.path.join(path, 'usagers_2016.csv'))
    
    ## Dataframe des lieux 
    df_lieux_2018 = pd.read_csv(os.path.join(path, 'lieux_2018.csv'),encoding="ISO-8859-1")
    df_lieux_2017 = pd.read_csv(os.path.join(path, 'lieux_2017.csv'),encoding="ISO-8859-1")
    df_lieux_2016 = pd.read_csv(os.path.join(path, 'lieux_2016.csv'),encoding="ISO-8859-1")

    ## Dataframe des véhicules 
    df_vehicules_2018 = pd.read_csv(os.path.join(path, 'vehicules_2018.csv'))
    df_vehicules_2017 = pd.read_csv(os.path.join(path, 'vehicules_2017.csv'))
    df_vehicules_2016 = pd.read_csv(os.path.join(path, 'vehicules_2016.csv'))

    df_caracteristiques = pd.concat([df_caracteristiques_2018, df_caracteristiques_2017, df_caracteristiques_2016])
    df_lieux = pd.concat([df_lieux_2018, df_lieux_2017, df_lieux_2016])
    df_usagers = pd.concat([df_usagers_2018, df_usagers_2017, df_usagers_2016])
    df_vehicules = pd.concat([df_vehicules_2018, df_vehicules_2017, df_vehicules_2016])
 
    ## On drop les duplicates 
    df_caracteristiques = df_caracteristiques.drop_duplicates() 
    
    if concat==True:
        return df_caracteristiques, df_lieux, df_usagers, df_vehicules

    
    else: 
        return df_caracteristiques_2018, df_caracteristiques_2017, df_caracteristiques_2016, df_usagers_2018, df_usagers_2017, df_usagers_2016, df_lieux_2018, df_lieux_2017, df_lieux_2016, df_vehicules_2018, df_vehicules_2017, df_vehicules_2016
