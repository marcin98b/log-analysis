import pandas as pd
import os

#Stworzenie pliku merge.csv w teście - kombinacji wszystkich plików .csv testu, podstawą jest plik methods.csv
def merge_csv_files(path):
    # wczytanie plików CSV
    methods = pd.read_csv(path + 'methods.csv').dropna(inplace=False)
    stock = pd.read_csv(path + 'stock.csv').dropna(inplace=False)
    trading = pd.read_csv(path + 'trading.csv').dropna(inplace=False)
    traffic = pd.read_csv(path + 'traffic.csv').dropna(inplace=False)

    # modyfikacja methods
    endpoint_map = {
        'do-register': 0,
        'add-sell-offer': 1,
        'add-buy-offer': 2,
        'get-stock-data': 3,
        'add-company': 4,
        'get-stock-users-and-companies': 5

    }

    # zastosowanie mapowania na kolumnę endpointUrl
    methods['endpointUrl'] = methods['endpointUrl'].replace(endpoint_map)
    methods = methods.iloc[:, :-1]

    # stock.csv
    stock = stock.iloc[:, :-1]
    # trading.csv
    trading = trading.iloc[:, :-1]

    methods = methods.sort_values('timestamp')
    stock = stock.sort_values('timestamp')
    trading = trading.sort_values('timestamp')
    traffic = traffic.sort_values('timestamp')

    stock = stock.add_prefix('st_')
    stock.rename(columns={'st_timestamp': 'timestamp'}, inplace=True)

    trading = trading.add_prefix('trad_')
    trading.rename(columns={'trad_timestamp': 'timestamp'}, inplace=True)

    traffic = traffic.add_prefix('traf_')
    traffic.rename(columns={'traf_timestamp': 'timestamp'}, inplace=True)

    # połączenie plików
    merged = methods.copy()  # tworzenie kopii pierwszego pliku
    files = [stock, trading, traffic]

    for file in files:
        merged = pd.merge_asof(merged, file, on='timestamp', direction='nearest')

    merged.to_csv(path + 'merged.csv', index=True)

#Stworzenie pliku merge.csv w teście - kombinacji wszystkich plików .csv testu, podstawą jest plik stock.csv
def merge_csv_files2(path):
    # wczytanie plików CSV
    stock = pd.read_csv(path + 'stock.csv').dropna(inplace=False)
    methods = pd.read_csv(path + 'methods.csv').dropna(inplace=False)
    trading = pd.read_csv(path + 'trading.csv').dropna(inplace=False)
    traffic = pd.read_csv(path + 'traffic.csv').dropna(inplace=False)

    # modyfikacja methods
    endpoint_map = {
        'do-register': 0,
        'add-sell-offer': 1,
        'add-buy-offer': 2,
        'get-stock-data': 3,
        'add-company': 4,
        'get-stock-users-and-companies': 5
    }

    # zastosowanie mapowania na kolumnę endpointUrl
    methods['endpointUrl'] = methods['endpointUrl'].replace(endpoint_map)
    methods = methods.iloc[:, :-1]

    # stock.csv
    stock = stock.iloc[:, :-1]
    # trading.csv
    trading = trading.iloc[:, :-1]

    methods = methods.sort_values('timestamp')
    stock = stock.sort_values('timestamp')
    trading = trading.sort_values('timestamp')
    traffic = traffic.sort_values('timestamp')

    stock = stock.add_prefix('st_')
    stock.rename(columns={'st_timestamp': 'timestamp'}, inplace=True)

    trading = trading.add_prefix('trad_')
    trading.rename(columns={'trad_timestamp': 'timestamp'}, inplace=True)

    traffic = traffic.add_prefix('traf_')
    traffic.rename(columns={'traf_timestamp': 'timestamp'}, inplace=True)

    # połączenie plików
    merged = stock.copy()  # tworzenie kopii pierwszego pliku (stock.csv)
    files = [methods, trading, traffic]

    for file in files:
        merged = pd.merge_asof(merged, file, on='timestamp', direction='nearest')

    merged.to_csv(path + 'merged2.csv', index=True)

# Skrypt tworzący pliki merged.csv oraz merged2.csv w każdych testach
def merge_all():
    architectures = ['8CPU_20RAM', '12CPU_30RAM']
    tests_time = ['3600s', '10800s', '21600s', '32400s', '43200s']
    tests = ['2repl', '4repl', '5repl', '6repl',
             'A1_100-A2_100-A3_100', 'A1_200-A3_100', 'A2_200', 'A2_200-A3_100', 'A3_200',
             'req_250ms', 'req_500ms', 'req_1000ms', 'req_2000ms',
             'trans_60s', 'trans_120s', 'trans_180s', 'trans_240s', 'trans_300s']

    # Iteracja po wszystkich kombinacjach architektury, czasu testu i testów
    for arch in architectures:
        for time in tests_time:
            for test in tests:
                folder_path = arch + "/" + time + "/" + test + "/"
                # Sprawdzenie czy pliki merged.csv i merged2.csv istnieją, jeśli nie to ich utworzenie
                if "merged.csv" not in os.listdir(folder_path):
                    merge_csv_files(folder_path)
                    print("created merged.csv: " + folder_path)
                else:
                    print("merged.csv exists: " + folder_path)

                if "merged2.csv" not in os.listdir(folder_path):
                    merge_csv_files2(folder_path)
                    print("created merged2.csv: " + folder_path)
                else:
                    print("merged2.csv exists: " + folder_path)


# Skrypt tworzący pliki grupowe testów
def merge_group(group_name, group_members, tests_path):
    # Utwórz listę nazw plików, które chcemy połączyć
    file_names = ['methods.csv', 'stock.csv', 'trading.csv', 'traffic.csv', 'merged.csv', 'merged2.csv']

    # Wybierz listę ścieżek do folderów, w których znajdują się pliki
    folder_paths = group_members

    # Utwórz folder "replGroup", jeśli nie istnieje
    if not os.path.exists(tests_path + "/" + group_name):
        os.makedirs(tests_path + "/" + group_name)

    # Dla każdego pliku w liście nazw plików
    for file_name in file_names:

        # Utwórz pustą ramkę danych
        merged_df = pd.DataFrame()

        # Dla każdej ścieżki w liście ścieżek
        for folder_path in folder_paths:

            # Utwórz ścieżkę do pliku
            file_path = os.path.join(tests_path, folder_path, file_name)

            # Jeśli plik istnieje w tej ścieżce
            if os.path.exists(file_path):
                # Wczytaj plik do ramki danych
                df = pd.read_csv(file_path)

                # Dołącz ramkę danych do już połączonych
                merged_df = pd.concat([merged_df, df], ignore_index=True)

        # Usuń kolumny, które zawierają "Unnamed" w nazwie
        merged_df = merged_df.loc[:, ~merged_df.columns.str.contains('^Unnamed')]

        # Utwórz ścieżkę do pliku wynikowego
        merged_file_path = os.path.join(tests_path, group_name, file_name)

        print(f"Zapisywanie pliku {file_name}...")
        # Zapisz połączoną ramkę danych do pliku CSV, tylko pierwszy plik ma indeks
        if os.path.exists(merged_file_path):
            merged_df.to_csv(merged_file_path, index=False, mode='a', header=False)
        else:
            merged_df.to_csv(merged_file_path, index=False)

    print(f"Grupa {group_name} została utworzona!")
