import pandas as pd
from m5_rules import m5_rules


def run_m5_rules_experiment():
    df = pd.read_csv('datasets/PV_secondRelease.csv')
    for index in range(len(df)):
        generated_power = m5_rules(df.iloc[index])
        print(generated_power)


if __name__ == '__main__':
    run_m5_rules_experiment()
