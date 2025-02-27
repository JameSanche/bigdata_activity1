import pandas as pd
import json

def main():
    with open('data.json' , 'r', encoding='utf-8') as f:
        data = json.load(f)

        if isinstance(data, dict):
            data = [data]

    df = pd.DataFrame(data)
    df.to_excel('data.xlsx', index=False)
    print("Archivo 'Data saved to data.xlsx'generado con éxito")

if __name__ == '__main__':
    main()