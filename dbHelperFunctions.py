def cleanDataFrame(df):
    print("Null Value Count:")
    print(df.isnull().sum().sum())
    print("Duplicate Row Count:")
    print(df.duplicated().sum())
    df.drop_duplicates(inplace=True)
    df.drop(columns=['Disaster Group', 'Dis No', 'Adm Level', 'Admin1 Code', 'Admin2 Code', "Reconstruction Costs ('000 US$)"], errors='ignore', inplace=True)

    # normalize country names by removing any trailing "(the)" from country names
    df['Country'] = df['Country'].str.replace(r'\s+\(the\)$','',regex=True)
    
    

def getDfInfo(df):
    print(df.info())
    print(df.describe())
    print(df.shape)