import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read dataset
    df = pd.read_csv("adult.data.csv")

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage of Bachelors
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4 & 5. Higher vs lower education
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    lower_education_rich = round(
        (df[~higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Min work hours
    min_work_hours = df['hours-per-week'].min()

    # 7. % rich among those who work min hours
    min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 8 & 9. Country with highest % of rich
    country_stats = df.groupby('native-country')['salary'].value_counts(normalize=True)

    country_rich = country_stats.loc[:, '>50K']

    highest_earning_country = country_rich.idxmax()
    highest_earning_country_percentage = round(country_rich.max() * 100, 1)

    # 10. Top occupation in India
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    # Print (optional)
    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich % among min workers:", rich_percentage)
        print("Top country:", highest_earning_country)
        print("Top country %:", highest_earning_country_percentage)
        print("Top occupation India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data()
