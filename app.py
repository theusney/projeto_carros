import streamlit as st 
import pandas as pd
#python -m streamlit run  app.py

#----------------------------------------------sidebar

st.sidebar.image("logo.png")
st.sidebar.title('visionário carros')


carros = ['BMW', 'MUSTANG', 'Porsche', 'Fusca', 'Toro', 'Jetta', 'Nivus']

opcao = st.sidebar.selectbox('Escolha o carro que você vai alugar', carros )



#----------------------------------------------Principal

st.title('Visionario - Aluguel de carros')

st.image(f'{opcao}.png')
st.markdown(f'##  Você alugou o modelo: {opcao}')
st.markdown('---')

dias =st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f' quantos Km voê rodou com a  {opcao}? ')

if opcao == 'BMW' :
    diaria = 450

elif opcao == 'MUSTANG' :
    diaria = 500

elif opcao == 'Porsche' :
    diaria = 300

elif opcao == 'Fusca' :
    diaria = 250

elif opcao == 'Toro' :
    diaria = 550

elif opcao == 'Jetta' :
    diaria = 600

elif opcao == 'Nivus' :
    diaria = 350


if st.button('Calcular'):
    dias= int(dias)
    km= float(km)

    todal_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = todal_dias+ total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. o valor total a pagar é R$ {aluguel_total:.2f}')