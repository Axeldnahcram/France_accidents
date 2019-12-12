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

    
    ## On concatene les bases
    df_caracteristiques = pd.concat([df_caracteristiques_2018, df_caracteristiques_2017, df_caracteristiques_2016])
    df_lieux = pd.concat([df_lieux_2018, df_lieux_2017, df_lieux_2016])
    df_usagers = pd.concat([df_usagers_2018, df_usagers_2017, df_usagers_2016])
    df_vehicules = pd.concat([df_vehicules_2018, df_vehicules_2017, df_vehicules_2016])

     ## On drop les duplicates 
    df_caracteristiques = df_caracteristiques.drop_duplicates() 
    
    ## Reset index 
    df_caracteristiques = df_caracteristiques.reset_index(drop=True)
    df_lieux = df_lieux.reset_index(drop=True)
    df_usagers = df_usagers.reset_index(drop=True)
    df_vehicules = df_vehicules.reset_index(drop=True)
    
  
    
        ## Création d'une nouvelle variable Datetime 
    df_caracteristiques['an'] = [str(df_caracteristiques['an'][i]) for i in range(df_caracteristiques.shape[0])]
    df_caracteristiques['an'] = ["20" + df_caracteristiques['an'][i] for i in range(df_caracteristiques.shape[0])]
    df_caracteristiques['mois'] = [str(df_caracteristiques.mois[i]) for i in range(df_caracteristiques.shape[0])]
    df_caracteristiques['mois'] = [df_caracteristiques.mois[i].zfill(2) for i in range(df_caracteristiques.shape[0])]
    df_caracteristiques['jour'] = [str(df_caracteristiques.jour[i]) for i in range(df_caracteristiques.shape[0])]
    df_caracteristiques['jour'] = [df_caracteristiques.jour[i].zfill(2) for i in range(df_caracteristiques.shape[0])]
    df_caracteristiques['hrmn'] = [str(df_caracteristiques.hrmn[i]) for i in range(df_caracteristiques.shape[0])]
    df_caracteristiques['hrmn'] = [df_caracteristiques.hrmn[i].zfill(4) for i in range(df_caracteristiques.shape[0])]
    
    
    df_caracteristiques["Date"] = [df_caracteristiques.an[i] + "-" + df_caracteristiques.mois[i] + "-" + df_caracteristiques.jour[i]   + " " + df_caracteristiques.hrmn[i][:2] + ":" + df_caracteristiques.hrmn[i][2:4] for i in range(df_caracteristiques.shape[0])]
    df_caracteristiques.Date = pd.to_datetime(df_caracteristiques.Date, format='%Y-%m-%d %H:%M')
    
        ## Création des variables heure et jour de la semaine
    df_caracteristiques['jour_semaine'] = [df_caracteristiques.Date[i].weekday() for i in range(df_caracteristiques.shape[0])]   
    df_caracteristiques['heure'] = df_caracteristiques.Date.dt.hour

    
 
    if concat==True:
        return df_caracteristiques, df_lieux, df_usagers, df_vehicules

    
    else: ## Attention, données brut si pas de concaténation
        return df_caracteristiques_2018, df_caracteristiques_2017, df_caracteristiques_2016, df_usagers_2018, df_usagers_2017, df_usagers_2016, df_lieux_2018, df_lieux_2017, df_lieux_2016, df_vehicules_2018, df_vehicules_2017, df_vehicules_2016
    
 

    
