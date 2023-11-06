import qrcode
from qrcode.constants  import ERROR_CORRECT_L
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi

def QRCode_generator(name):
    qr = qrcode.QRCode(
        version=3,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=5
    )

    qr.add_data('https://forms.office.com/Pages/ResponsePage.aspx?id=ICXHB0XmeUaPVdxhHJdaAgVVBT2VFj9PumthlDIpVhFUN1hUSExESTNQSVhDUVNZTTZERkc2R0s3Qy4u')
    qr.make(fit=True)

    img = qr.make_image(fill_color="White", back_color="Transparent", image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), color_mask=RadialGradiantColorMask(back_color=(242,242,244),edge_color=(147,0,255),center_color=(186,0,0))).convert("RGB")
    name = name.upper()
    file = "./static/img/QR_CODE_" + name + "_FORUM_CARRIERE_2023.png"
    img.save(file)
    return file

def QRCode_generator_logo(name, logo):
    qr = qrcode.QRCode(
        version=3,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=5
    )

    qr.add_data('https://forms.office.com/Pages/ResponsePage.aspx?id=ICXHB0XmeUaPVdxhHJdaAgVVBT2VFj9PumthlDIpVhFUN1hUSExESTNQSVhDUVNZTTZERkc2R0s3Qy4u')
    qr.make(fit=True)

    img = qr.make_image(fill_color="White", back_color="Transparent", image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), color_mask=RadialGradiantColorMask(back_color=(242,242,244),edge_color=(147,0,255),center_color=(186,0,0))).convert("RGB")

    logo_display = Image.open(logo)
    logo_display.thumbnail((60,60))
    log_pos = ((img.size[0]-logo_display.size[0])//2, (img.size[1]-logo_display.size[1])//2)
    img.paste(logo_display, log_pos)
    name = name.upper()
    file = "./static/img/QR_CODE_" + name + "_FORUM_CARRIERE_2023.png"
    img.save(file)
    return file

def printAllStudents(db_file, name):
    db = open(db_file, "r")
    excel_file = db.read()
    df_survey = pd.read_excel(excel_file)
    students = []
    time_start = []
    time_end = []
    for i in range(len(df_survey['Nom'])):
        if df_survey["Nom de l'entreprise"][i]==name:
            time_start.append(df_survey['Heure de début'][i])
            time_end.append(df_survey['Heure de fin'][i])
            students.append(df_survey["Nom"][i])
    df_student = pd.DataFrame(time_start, index=None, columns=['Heure de début'])
    df_student.insert(1, 'Heure de fin', time_end, True)
    df_student.insert(2, "Nom de l'élève", students, True)
    dfi.export(df_student, './static/img/all_visits.png', max_rows=-1)
    img = './static/img/all_visits.png'
    return img

def printTopEnteprise(db_file):
    db = open(db_file, "r")
    excel_file = db.read()
    top = ""
    if excel_file == '':
        return "No valid database", top
    df_survey = pd.read_excel(excel_file)
    all_enterprise = list(set(df_survey["Nom de l'entreprise"]))
    nb_visits = []
    for enterprise in all_enterprise:
        nb_students = 0
        for i in range(len(df_survey['Nom'])):
            if enterprise == df_survey["Nom de l'entreprise"][i]:
                nb_students += 1
        nb_visits.append(nb_students)
    df_top_enterprise = pd.DataFrame(all_enterprise, index=None, columns=['Entreprise'])
    df_top_enterprise.insert(1, 'Nombre de visites', nb_visits)
    df_top_enterprise = df_top_enterprise.sort_values(by='Nombre de visites', ascending=True)
    df_top_enterprise = df_top_enterprise.reset_index(drop=True)
    top = df_top_enterprise.iloc[(len(df_top_enterprise['Entreprise']) - 1):len(df_top_enterprise['Entreprise']),:]
    plt.switch_backend('Agg') 
    plt.figure(figsize=(8,6))
    plt.barh(df_top_enterprise['Entreprise'], df_top_enterprise['Nombre de visites'], color="#b37695")
    plt.title("Nombre de visites par stand entreprise")
    plt.xlabel("Entreprise")
    plt.ylabel("Nombre de visites")
    for i in range(len(df_top_enterprise['Entreprise'])):
        plt.text(df_top_enterprise['Nombre de visites'][i]/2, i, round(df_top_enterprise['Nombre de visites'][i], 2), color="white")
    plt.tight_layout()
    img = "./static/img/top_enterprise.png"
    plt.savefig(img)
    return img, top

def printAverage(db_file):
    db = open(db_file, "r")
    excel_file = db.read()
    if excel_file == '':
        return "No valid database"
    df_survey = pd.read_excel(excel_file)    
    all_enterprise = list(set(df_survey["Nom de l'entreprise"]))
    average = []
    for enterprise in all_enterprise:
        nb_students = 0
        note = 0
        for i in range(len(df_survey["Nom de l'entreprise"])):
            if enterprise == df_survey["Nom de l'entreprise"][i]:
                nb_students += 1
                note += int(df_survey['Indice de satisfaction suite à votre rencontre entreprise'][i].split(' ', 2)[0])
        average.append(note/nb_students)
    df_average = pd.DataFrame(all_enterprise, index=None, columns=['Entreprise'])
    df_average.insert(1, 'Moyenne appréciation', average, True)
    df_average = df_average.sort_values(by='Moyenne appréciation', ascending=False)
    df_average = df_average.reset_index(drop=True)
    plt.switch_backend('Agg') 
    plt.figure(figsize=(12,6))
    plt.barh(df_average['Entreprise'], df_average['Moyenne appréciation'], color="#b37695")
    plt.title("Moyenne des notes d’appréciation par entreprise")
    plt.xlabel("Entreprise")
    plt.ylabel("Moyenne des notes")
    plt.tight_layout()
    for i in range(len(df_average['Entreprise'])):
        plt.text(df_average['Moyenne appréciation'][i]/2, i, round(df_average['Moyenne appréciation'][i], 2), color="white")
    img = "./static/img/average_by_enterprise.png"
    plt.savefig(img)
    return img

def printPrcFreq(db_file):    
    db = open(db_file, "r")
    excel_file = db.read()
    if excel_file == '':
        return "No valid database"
    df_survey = pd.read_excel(excel_file)
    all_enterprise = list(set(df_survey["Nom de l'entreprise"]))
    all_visitors = list(set(df_survey['Nom']))
    nb_visitors = len(all_visitors)
    prc_freq = []
    for enterprise in all_enterprise:
        nb_visits = 0
        for i in range(len(df_survey['Nom'])):
            if enterprise == df_survey["Nom de l'entreprise"][i]:
                nb_visits += 1
        prc_freq.append(nb_visits/nb_visitors*100)
    df_prc_freq = pd.DataFrame(all_enterprise, index=None, columns=['Entreprise'])
    df_prc_freq.insert(1, 'Pourcentage de fréquentation', prc_freq, True)
    df_prc_freq = df_prc_freq.sort_values(by='Pourcentage de fréquentation')
    df_prc_freq = df_prc_freq.reset_index(drop=True)
    plt.switch_backend('Agg') 
    plt.figure(figsize=(12,6))
    plt.bar(df_prc_freq['Entreprise'], df_prc_freq['Pourcentage de fréquentation'], color="#b37695")
    plt.title("Pourcentage de fréquentation par entreprise")
    plt.xlabel("Entreprise")
    plt.ylabel("Pourcentage de fréquentation")
    plt.tight_layout()
    for i in range(len(df_prc_freq['Entreprise'])):
        plt.text(i, df_prc_freq['Pourcentage de fréquentation'][i]/2, str(round(df_prc_freq['Pourcentage de fréquentation'][i], 2)) + "%", ha='center', color="white")
    img = "./static/img/prcfreq_by_enterprise.png"
    plt.savefig(img)
    return img