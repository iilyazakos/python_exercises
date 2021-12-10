import streamlit as st
import pandas as pd
import datetime
now = datetime.datetime.now()

data = pd.read_csv('https://raw.githubusercontent.com/iilyazakos/python_exercises/main/stud_project/data_1.csv')

st.set_page_config(layout = "wide")
st.header('Выбранный парметр')
with st.container() as parametr:
    one_par, two_par = st.columns(2)
    with one_par:
        one = st.selectbox('Тип БП', pd.unique(data['Тип БП']))
    with two_par:
        two = st.selectbox('Завод-изготовитель', pd.unique(data['Завод-изготовитель']))
with st.container() as table_one:
    st.write('Контрольная таблица')
    one_data = data[["№ п/п", "№ по учету", 'Тип БП', 'Завод-изготовитель']]
    one_data = one_data[(one_data['Тип БП'] == one) & (one_data['Завод-изготовитель'] == two)]
    st.write(one_data.head(4))
with st.container() as information_map:
    inf_map, number_1, number_2, number_3 =st.columns(4)
    with inf_map:
        st.write('Информационная карта')
    with number_1:
        num = st.selectbox("№ п/п", pd.unique(data["№ п/п"]))
    with number_2:
        st.write("№ по учету")
    with number_3:
        data_for_info = data[(data["№ п/п"] == num)]
        data_for_info = data_for_info["№ по учету"]
        data_for_info.reset_index()
        st.metric(label = '', value = data_for_info[num-1])
with st.container() as title_1:
    st.header('ОБЩИЕ ДАННЫЕ')
with st.container() as type_BP:
    title, metric = st.columns(2)
    with title:
        st.write("1. Тип боеприпаса")
    with metric:
        data_for_info = data[(data["№ п/п"] == num)]
        data_for_info = data['Тип БП']
        data_for_info.reset_index()
        st.metric(label = '', value = data_for_info[num-1])
with st.container() as zavod:
    title, metric = st.columns(2)
    with title:
        st.write('2. Завод-изготовитель')
    with metric:
        data_for_info = data[(data["№ п/п"] == num)]
        data_for_info = data['Завод-изготовитель']
        st.metric(label='', value=data_for_info[num - 1])
with st.container() as data_start:
    title, metric = st.columns(2)
    with title:
        st.write('3. Дата выпуска')
    with metric:
        data_for_info = data[(data["№ п/п"] == num)]
        data_for_info = data['Дата выпуска']
        st.metric(label = '', value = data_for_info[num - 1])
with st.container() as time:
    title, metric_1, metric_2 = st.columns(3)
    with title:
        st.write('6. Время на хранении')
    with metric_1:
        data_for_info = data[(data["№ п/п"] == num)]
        data_for_info = data['Дата выпуска']
        data_for_info.reset_index()
        date_condition = now.year - pd.to_datetime(data_for_info[num-1]).year
        st.metric(label = 'Количестов лет', value = date_condition)
    with metric_2:
        st.metric(label = 'Количестов месяцев', value = now.month - pd.to_datetime(data_for_info[num-1]).month)
with st.container() as category:
    title, categ = st.columns(2)
    with title:
        st.write('4. Степень годности')
    with categ:
        if date_condition < 10: st.write('I КАТЕГОРИЯ')
        if date_condition <= 10 and date_condition < 15: st.write('II КАТЕГОРИЯ')
        if date_condition <= 15 and date_condition < 20: st.write('III КАТЕГОРИЯ')
        if date_condition >= 20: st.write('ПОДЛЕЖИТ СПИСАНИЮ')
with st.container() as waight:
    title, mass = st.columns(2)
    with title:
        st.write('5. Полная масса б/п')
    with mass:
        data_for_info = data[(data["№ п/п"] == num)]
        st.metric(label='Масса в килиграммах', value = int(data_for_info['Количество, ящ'] * data_for_info['Масса одного ящика, кг']))
