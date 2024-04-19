import json
import os
import numpy as np


import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

import config
from synch2jira.issue_csv import IssueCSV
from synch2jira.issue_json import IssueJSON

matplotlib.use('Agg')


def generate_issue_data_mining_csv(state1=config.workflow_status1, state2=config.workflow_status2):
    with open(config.json_issues_file, 'r') as file:
        json_data = json.load(file)
    issue_list = [IssueJSON.json_to_issue(issue_data, json_data, state1, state2) for issue_data in
                  json_data]
    IssueCSV.generate_csv_data(issue_list, config.csv_issue_file)


def csv_to_dataframe(file_path):
    df = pd.read_csv(file_path)
    return df

def correlation(dataframe):
    print(dataframe.corr(numeric_only=True))

    dataframe['statuscategorychangedate'] = pd.to_datetime(dataframe['statuscategorychangedate'], errors='coerce', utc=True).dropna().astype('int64') // 10**9
    dataframe['resolutiondate'] = pd.to_datetime(dataframe['resolutiondate'], errors='coerce', utc=True).dropna().astype('int64') // 10**9
    dataframe['created'] = pd.to_datetime(dataframe['created'], errors='coerce', utc=True).dropna().astype('int64') // 10**9
    dataframe['updated'] = pd.to_datetime(dataframe['updated'], errors='coerce', utc=True).dropna().astype('int64') // 10**9

    #dataframe.dropna(subset=['statuscategorychangedate', 'resolutiondate', 'created', 'updated'], inplace=True)

   
    correlation_matrix = dataframe.corr(numeric_only = True)

    print(correlation_matrix)
    return correlation_pairs(correlation_matrix,0.1,0.8)


def correlation_pairs(correlation, borne_inf, borne_supp):
    pairs = []
    for i in range(len(correlation.columns)):
        for j in range(i + 1, len(correlation.columns)):  
            value = correlation.iloc[i, j]
            if borne_inf <= value <= borne_supp:
                pairs.append((correlation.columns[i], correlation.columns[j], value))
                print((correlation.columns[i], correlation.columns[j], value))
                print()
    return pairs



def str_df_to_dt_df(dataframe, use_workflow=config.use_workflow):
    if use_workflow:
        dataframe['created'] = pd.to_datetime(dataframe['workflow_start_time'], utc=True)
        dataframe['resolutiondate'] = pd.to_datetime(dataframe['workflow_end_time'], utc=True)
        dataframe = dataframe.dropna(subset=['workflow_start_time', 'workflow_end_time'])
        return dataframe
    dataframe['created'] = pd.to_datetime(dataframe['created'], utc=True)
    dataframe['resolutiondate'] = pd.to_datetime(dataframe['resolutiondate'], utc=True)
    dataframe = dataframe.dropna(subset=['resolutiondate', 'created'])
    return dataframe


def genarate_creation_resolution_figure(dataframe):
    dataframe = str_df_to_dt_df(dataframe)
    dataframe.sort_values(by='created', inplace=True)

    plt.figure(figsize=(12, 6))
    plt.scatter(dataframe.index, dataframe['created'], label='Date de création', color='blue')
    plt.scatter(dataframe.index, dataframe['resolutiondate'], label='Date de résolution', color='green')
    plt.xlabel('ticket')
    plt.ylabel('dates creation_resolution')
    plt.title('Tendances creation_resolution des tickets ')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(config.image_directory + 'creation_resolution_by_issue_type.png')
    plt.show()


def genarate_creation_resolution_figure_by_issue_field(dataframe, field):
    dataframe = str_df_to_dt_df(dataframe)

    dataframe.sort_values(by='created', inplace=True)

    types_issues = dataframe[field].unique()

    fig, axes = plt.subplots(nrows=len(types_issues), ncols=1, figsize=(12, 6 * len(types_issues)))

    for i, issue_type in enumerate(types_issues):
        data_filtered = dataframe[dataframe[field] == issue_type]

        axes[i].scatter(data_filtered.index, data_filtered['created'], label='Date de création', color='blue')

        axes[i].scatter(data_filtered.index, data_filtered['resolutiondate'], label='Date de résolution', color='green')

        axes[i].set_xlabel('ticket')
        axes[i].set_ylabel('dates creation_resolution')
        axes[i].set_title(f'Tendances creation_resolution des tickets ({issue_type})')
        axes[i].legend()
        axes[i].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.savefig(config.image_directory + f'/creation_resolution_by_issue_{field}.png')
    plt.show()


def get_creation_resolution_time_statistics(dataframe):
    dataframe = str_df_to_dt_df(dataframe)
    dataframe['creation_resolution_time'] = dataframe.apply(lambda row: row['resolutiondate'] - row['created'], axis=1)
    # Différence de temps moyenne entre création et résolution
    average_resolution_time = dataframe['creation_resolution_time'].mean()
    return dataframe['creation_resolution_time'].describe()


def get_month_statistics(dataframe):
    dataframe = str_df_to_dt_df(dataframe)
    dataframe['created_month'] = dataframe['created'].dt.month
    dataframe['resolution_time'] = dataframe['resolutiondate'] - dataframe['created']  #
    dataframe = dataframe[['created_month', 'resolution_time']]
    statistics_by_month = dataframe.groupby('created_month')['resolution_time'].describe()
    return statistics_by_month


def get_period_statistics(dataframe, period):
    dataframe = str_df_to_dt_df(dataframe)
    dataframe['period'] = get_data_by_period(dataframe, period)
    dataframe['resolution_time'] = dataframe['resolutiondate'] - dataframe['created']
    dataframe = dataframe[['period', 'resolution_time']]
    statistics_by_period = dataframe.groupby('period')['resolution_time'].describe()
    return statistics_by_period


# def get_statistics_by_issue_type(dataframe):
#     dataframe = str_df_to_dt_df(dataframe)
#     dataframe['resolution_time'] = dataframe['resolutiondate'] - dataframe['created']
#     statistics_by_issue_type = dataframe.groupby('issuetypename')['resolution_time'].describe()
#
#     return statistics_by_issue_type


def get_statistics_by_field(dataframe, field):
    dataframe = str_df_to_dt_df(dataframe)
    dataframe['resolution_time'] = dataframe['resolutiondate'] - dataframe['created']
    statistics_by_issue_field = dataframe.groupby(field)['resolution_time'].describe()
    return statistics_by_issue_field


def get_double_group_by_statistics(dataframe, period):
    dataframe = str_df_to_dt_df(dataframe)
    dataframe['resolution_time'] = dataframe['resolutiondate'] - dataframe['created']
    dataframe['period'] = get_data_by_period(dataframe, period)

    statistics = dataframe.groupby(['period', "issuetypename"])['resolution_time'].describe()
    return statistics


def get_data_by_period(dataframe, period):
    if period == 'week':
        return dataframe['created'].dt.isocalendar().week
    elif period == 'month':
        return dataframe['created'].dt.month
    elif period == 'year':
        return dataframe['created'].dt.year
    else:
        raise ValueError("Période non valide. Veuillez spécifier 'day', 'month' ou 'year'.")


def get_number_issues_solved_within_preriod_graph(dataframe, period):
    dataframe = str_df_to_dt_df(dataframe)
    dataframe['resolution_time_days'] = (dataframe['resolutiondate'] - dataframe['created']).dt.days
    print(dataframe['resolution_time_days'].describe())
    # 3. Identify and visualize the proportion of issues resolved within 30 days
    dataframe['resolved_within'] = dataframe['resolution_time_days'] <= period

    resolution_proportion = dataframe['resolved_within'].value_counts(normalize=True) * 100
    plt.figure(figsize=(6, 6))
    resolution_proportion.plot(kind='pie', autopct='%1.1f%%', startangle=140,
                               labels=[f'en plus de  {period} jour', f'en moins de  {period} jour'],
                               colors=['lightgreen', 'lightcoral'])
    plt.ylabel('')
    plt.title(f'Proportion des tickets resolu en  {period} jour')
    plt.tight_layout()
    plt.savefig(config.image_directory + f'issues_resolved_within_{period}_days.png')
    plt.show()


def plot_issue_types_distribution(df):
    issue_counts = df['issuetypename'].value_counts()
    creer_histogramme(issue_counts, 'Répartition des Types d\'Issues', 'Type d\'Issue', 'Nombre d\'Issues')


def analyze_time_spent_on_issues(df):
    df['timespend_hours'] = df['timespend'] / 3600  # Convertir le temps passé en heures
    print(df['timespend_hours'].describe())
    average_time = df.groupby('issuetypename')['timespend_hours'].mean()
    creer_histogramme(average_time, 'Temps Moyen Passé par Type d\'Issue', 'Type d\'Issue', 'Temps Moyen (Heures)')


def tickets_clotures_en_mois(dataframe, annee, mois):
    dataframe = str_df_to_dt_df(dataframe)
    dataframe_mois_annee = dataframe[
        (dataframe['resolutiondate'].dt.year == annee) & (dataframe['resolutiondate'].dt.month == mois)]

    nombre_tickets_clotures = dataframe_mois_annee.shape[0]
    return nombre_tickets_clotures


def tickets_clotures_par_mois(dataframe, annee):
    dataframe = str_df_to_dt_df(dataframe)
    dataframe_annee = dataframe[dataframe['resolutiondate'].dt.year == annee]

    tickets_clotures = dataframe_annee['resolutiondate'].dt.month.value_counts().sort_index()
    creer_courbe(Serie=tickets_clotures, title_graphique='Nombre de tickets clôturés par mois pour l\'année {annee}',
                 title_x='Mois', title_y='Nombre de tickets clôturés', xticks_rotation='Mois')


###
def lead_time_par_mois(dataframe):
    dataframe = str_df_to_dt_df(dataframe)

    # Calculer le lead time pour chaque ticket et l'ajouter comme une nouvelle colonne
    dataframe['lead_time'] = (dataframe['resolutiondate'] - dataframe['created']).dt.days

    years = dataframe['created'].dt.year.unique()

    for annee in years:
        # Filtrer les données pour l'année spécifiée
        dataframe_annee = dataframe[dataframe['created'].dt.year == annee]

        # Calculer la moyenne du lead time par mois
        lead_time_moyen = dataframe_annee.groupby(dataframe_annee['created'].dt.month)['lead_time'].mean()
        creer_courbe(Serie=lead_time_moyen, title_graphique=f'Lead time moyen par mois pour toutes les années',
                     title_x='Mois', title_y='Lead time moyen (jours)', xticks_rotation='Mois')
    return True


# Remplacer les deux fonctions suivantes par une seule
def tickets_cloturés_crées_par_annee(dataframe, field='resolutiondate'):
    dataframe = str_df_to_dt_df(dataframe)
    tickets_clotures = dataframe[dataframe[field].notnull()][field].dt.year.value_counts().sort_index()
    type_ticket = "créés" if field == 'created' else "cloturés"
    creer_courbe(Serie=tickets_clotures, title_graphique=f'Nombre de tickets {type_ticket} par année', title_x='Année',
                 title_y=f'Nombre de tickets {type_ticket}')


# def tickets_clotures_par_annee(dataframe):
#     dataframe = str_df_to_dt_df(dataframe)
#     tickets_clotures = dataframe[dataframe['resolutiondate'].notnull()]['resolutiondate'].dt.year.value_counts().sort_index()
#
#     creer_courbe(Serie=tickets_clotures, title_graphique='Nombre de tickets clôturés par année', title_x='Année',
#                  title_y='Nombre de tickets clôturés')
    return True


###
# def tickets_cree_par_annee(dataframe):
#     dataframe = str_df_to_dt_df(dataframe)
#     tickets_clotures = dataframe[dataframe['created'].notnull()]['created'].dt.year.value_counts().sort_index()
#
#     creer_courbe(Serie=tickets_clotures, title_graphique='Nombre de tickets créés par année', title_x='Année',
#                  title_y='Nombre de tickets crées')
#     return True


###
def nombre_ticket_creer_cloture(dataframe):
    dataframe = str_df_to_dt_df(dataframe)

    tickets_crees = dataframe['created'].dt.year.value_counts().sort_index()
    tickets_clotures = dataframe[dataframe['resolutiondate'].notnull()][
        'resolutiondate'].dt.year.value_counts().sort_index()

    plt.figure(figsize=(10, 6))

    # courbe pour les tickets créés
    plt.plot(tickets_crees.index, tickets_crees.values, marker='o', label='Tickets créés')
    # courbe pour les tickets clôturés
    plt.plot(tickets_clotures.index, tickets_clotures.values, marker='o', label='Tickets clôturés')

    plt.xlabel('Année')
    plt.ylabel('Nombre de tickets')
    plt.title('Nombre de tickets créés et clôturés par année')
    plt.grid(True)
    plt.legend()
    plt.savefig('nombre_de_tickets_cree_et_clôturés_par_année.png')
    # Afficher le graphique
    plt.show()
    return True


def tickets_cloturés_ou_créés_par_mois_par_annee(dataframe, field='resolutiondate'):
    dataframe = str_df_to_dt_df(dataframe)
    annees = dataframe[field].dt.year.unique()
    type_ticket = "créés" if field == 'created' else "cloturés"
    for annee in annees:
        dataframe_annee = dataframe[dataframe[field].dt.year == annee]
        tickets_clotures_par_mois = dataframe_annee.groupby(dataframe_annee[field].dt.month).size()
        creer_courbe(tickets_clotures_par_mois, f'Nombre de tickets {type_ticket} pour l\'année {annee}',
                     'Mois', f'Nombre de tickets {type_ticket}', 'Mois')
    return True


def lead_time_par_annee(dataframe):
    dataframe = str_df_to_dt_df(dataframe)
    dataframe['lead_time'] = (dataframe['resolutiondate'] - dataframe['created']).dt.days
    lead_time_moyen = dataframe.groupby(dataframe['created'].dt.year)['lead_time'].mean()

    creer_courbe(Serie=lead_time_moyen, title_graphique='Lead time moyen par année', title_x='Année',
                 title_y='Lead time moyen (jours)')
    return True


def tickets_status_par_intervals_de_temps(status, dataframe, date_min, date_max):
    dataframe = str_df_to_dt_df(dataframe)
    date_resolution = dataframe[status]

    date_min = pd.Timestamp(date_min)
    date_max = pd.Timestamp(date_max)

    dataframe_intervals = dataframe[
        (date_resolution.dt.date >= date_min.date()) & (date_resolution.dt.date <= date_max.date())]

    tickets_clotures_par_date = dataframe_intervals.groupby(dataframe_intervals[status].dt.date).size()

    creer_courbe(tickets_clotures_par_date, f'Nombre de tickets clôturés du {date_min.date()} '
                                            f'au {date_max.date()}', 'Date',
                 'Nombre de tickets clôturés', 40)
    return True


def lead_time_par_intervals_de_temps(dataframe, date_min, date_max):
    dataframe = str_df_to_dt_df(dataframe)

    date_min = pd.Timestamp(date_min)
    date_max = pd.Timestamp(date_max)

    date_created = dataframe['created']
    date_resolution = dataframe['resolutiondate']

    # Data frame de notre intervals de temps
    dataframe_intervals = dataframe[
        (date_created.dt.date >= date_min.date()) & (date_resolution.dt.date <= date_max.date())]

    # Calculer le lead time pour chaque ticket et l'ajouter comme une nouvelle colonne
    dataframe_intervals['lead_time'] = (
            dataframe_intervals['resolutiondate'] - dataframe_intervals['created']).dt.days

    lead_time_moyen = dataframe_intervals.groupby(dataframe_intervals['created'].dt.date)['lead_time'].mean()

    # Créer le graphique
    creer_courbe(lead_time_moyen,
                 f'Lead time moyen par intervals du {date_min.date()} au {date_max.date()}',
                 'Date', 'Lead time moyen ', 40)
    return True


def creer_courbe(Serie, title_graphique='', title_x='', title_y='', xticks_rotation=40):
    if not os.path.exists(config.output_directory):
        os.makedirs(config.output_directory)
    plt.figure(figsize=(10, 6))
    if Serie is not None:
        plt.plot(Serie.index, Serie.values, marker='o')
    plt.xlabel(title_x)
    plt.ylabel(title_y)
    plt.title(title_graphique)
    plt.grid(True)
    if isinstance(xticks_rotation, int) is False:
        plt.xticks(range(1, 13),
                   ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc'])
    else:
        plt.xticks(rotation=xticks_rotation)
    plt.tight_layout()
    filename = os.path.join(config.output_directory, f'{title_graphique}.png')
    plt.savefig(filename)
    plt.grid(True)
    plt.show()


def creer_histogramme(values, title, x_title, y_title):
    if not os.path.exists(config.output_directory):
        os.makedirs(config.output_directory)
    values.plot(kind='bar')
    plt.title(title)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.xticks(rotation=12)
    filename = os.path.join(config.output_directory, f'{title}.png')
    plt.savefig(filename)
    plt.show()


def tickets_crees_par_mois_par_annee_pour_nombre_annee(dataframe, nb_dernieres_annees):
    dataframe = str_df_to_dt_df(dataframe)
    annees = dataframe['created'].dt.year.unique()

    dernieres_annees = sorted(annees)[-nb_dernieres_annees:]

    # if not os.path.exists(output_directory):
    #     os.makedirs(output_directory)
    #
    # plt.figure(figsize=(10, 6))

    for annee in dernieres_annees:
        dataframe_annee = dataframe[dataframe['created'].dt.year == annee]
        tickets_crees_par_mois = dataframe_annee.groupby(dataframe_annee['created'].dt.month).size()

        plt.plot(tickets_crees_par_mois.index, tickets_crees_par_mois.values, marker='o', label=f'Année {annee}')
    creer_courbe(None, f'Nombre de tickets créés par mois pour les {nb_dernieres_annees} dernières années',
                 'Mois', 'Nombre de tickets créés', 'Mois')
    # plt.xlabel('Mois')
    # plt.ylabel('Nombre de tickets créés')
    # plt.title(f'Nombre de tickets créés par mois pour les {nb_dernieres_annees} dernières années')
    # plt.grid(True)
    # plt.xticks(range(1, 13), ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc'])
    # plt.legend()
    #
    # # Enregistrer le graphique dans un fichier
    # filename = os.path.join(output_directory, f'tickets_crees_les_{nb_dernieres_annees}_dernieres_annees.png')
    # plt.savefig(filename)
    # plt.close()

    return True


def lead_time_moyen_par_mois_par_annee_pour_nombre_annee(dataframe, nb_dernieres_annees):
    dataframe = str_df_to_dt_df(dataframe)
    annees = dataframe['created'].dt.year.unique()
    dernieres_annees = sorted(annees)[-nb_dernieres_annees:]

    for annee in dernieres_annees:
        dataframe_annee = dataframe[dataframe['created'].dt.year == annee]
        dataframe_annee['lead_time'] = (dataframe_annee['resolutiondate'] - dataframe_annee['created']).dt.days
        lead_time_moyen_par_mois = dataframe_annee.groupby(dataframe_annee['created'].dt.month)['lead_time'].mean()
        plt.plot(lead_time_moyen_par_mois.index, lead_time_moyen_par_mois.values, marker='o', label=f'Année {annee}')
    creer_courbe(None, f'Lead time moyen par mois pour les {nb_dernieres_annees} dernières années',
                 'Mois', 'Lead time moyen (jours)', 'Mois')
    return True


def lead_time_moyen_par_mois_par_annee_pour_deux_annee(dataframe, annee1, annee2):
    dataframe = str_df_to_dt_df(dataframe)
    annees = [annee1, annee2]

    for annee in annees:
        dataframe_annee = dataframe[dataframe['created'].dt.year == annee]
        dataframe_annee['lead_time'] = (dataframe_annee['resolutiondate'] - dataframe_annee['created']).dt.days
        lead_time_moyen_par_mois = dataframe_annee.groupby(dataframe_annee['created'].dt.month)['lead_time'].mean()
        plt.plot(lead_time_moyen_par_mois.index, lead_time_moyen_par_mois.values, marker='o', label=f'Année {annee}')
    creer_courbe(None, f'Lead time moyen par mois pour les {annee1} et {annee2}',
                 'Mois', 'Lead time moyen (jours)', 'Mois')
    return True


def tickets_clotures_par_mois_par_annee_pour_nombre_annee(dataframe, nb_dernieres_annees):
    dataframe = str_df_to_dt_df(dataframe)
    annees = dataframe['resolutiondate'].dt.year.unique()
    dernieres_annees = sorted(annees)[-nb_dernieres_annees:]

    for annee in dernieres_annees:
        dataframe_annee = dataframe[dataframe['resolutiondate'].dt.year == annee]
        tickets_clotures_par_mois = dataframe_annee.groupby(dataframe_annee['resolutiondate'].dt.month).size()

        plt.plot(tickets_clotures_par_mois.index, tickets_clotures_par_mois.values, marker='o', label=f'Année {annee}')
    creer_courbe(None, f'Nombre de tickets clôturés par mois pour les {nb_dernieres_annees} dernières années',
                 'Mois', 'Nombre de tickets clôturés', 'Mois')
    return True


def lead_time_par_mois_par_annee(dataframe):
    dataframe = str_df_to_dt_df(dataframe)
    annees = dataframe['resolutiondate'].dt.year.unique()

    for annee in annees:
        dataframe_annee = dataframe[dataframe['resolutiondate'].dt.year == annee]
        tickets_clotures_par_mois = dataframe_annee.groupby(dataframe_annee['resolutiondate'].dt.month).size()
        creer_courbe(tickets_clotures_par_mois, f'Nombre de tickets clôturés par mois pour l\'andatetimenée {annee}',
                     'Mois', 'Nombre de tickets clôturés', 'Mois')
    return True


def tickets_per_month(dataframe):
    dataframe['created'] = pd.to_datetime(dataframe['created'], errors='coerce', utc=True)

    grouped = dataframe.groupby([dataframe['created'].dt.year, dataframe['created'].dt.month]).size().unstack(fill_value=0,level=0)

    month_names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                   7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    grouped = grouped.rename(columns=month_names)

    return grouped
