
#----------IMPORT LIBRARIES-----------#

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from datetime import datetime
import calendar
import plotly.express as px
from PIL import Image
import statistics as sta
import numpy as np
import plotly.graph_objects as go




# ------------PAGE SETTINGS---------

page_title = "PFMSystem"
page_icon = ":dollar:"
layout = "wide"
currency = "USD"+":dollar:"

st.set_page_config(page_title=page_title,page_icon=page_icon, layout=layout)

st.title(page_icon + "  " +" "+ "P.F.M.S")

st.write("---")

selected = option_menu(
        menu_title=None,
        options = ["Home", "Datasets", "Analysis", "About"],
        icons = ["house-fill", "distribute-vertical", "graph-up-arrow", "info-circle"],
        menu_icon = "command",
        default_index = 0,
        orientation = "horizontal",
         styles={
                "container": {"padding": "0!important","background-color": "#4d2f01"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "color": "#fff",
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#4d5101",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        
         )





#----------------STYLE--------

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css(".style/style.css")


st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    color: #4E0090;
}
</style>

""",  unsafe_allow_html=True)

st.markdown("""
<style>
.goal {
    font-size:15px !important;
    color: #0000FF;
}
</style>

""",  unsafe_allow_html=True)
#------analysis styling--------
st.markdown("""
<style>
.results {
    font-size:25px !important;
    color: #ff6347;
    font-weight: 300px;
}
</style>

""",  unsafe_allow_html=True)

st.markdown("""
<style>
.analysis {
    font-size:25px !important;
    color: #ff6347;
    font-weight: 300px;
}
</style>

""",  unsafe_allow_html=True)

#-----------------ASSETS-------------

phl = pd.read_csv("clean_data.csv").drop(['Unnamed: 0'], axis=1)
poverty_class = pd.read_csv("poverty_class.csv")

numerical_cols = phl[['food', 'clothing',
       'power', 'entertainment', 'house_items', 'Health', 'Transport',
       'Education', 'Communication', 'leisure', 'eats']]

numerical_cols_mean = numerical_cols.mean().reset_index(name='mean')


st.header("Personal Finance Management System")

st.write('---')
if selected == "Home":
    st.header("INTRODUCTION")
    st.write(
    """<p class="big-font"> Personal Finance Management System (PFMS) is a system developed to help people manage their finances.
        Most people tend to mismanage their income, either by impulse buying, wrong priorities, over-spending; this corners them
            not SAVE or INVEST. Thus leading to no growth financially.</p>""", unsafe_allow_html=True
    )
    st.write(
   """<p class="big-font"> The System also helps people/families(households) realize which economic classes they belong 
    and how to adjust to a higher economic class or how they can maintain in the prefered economic class.</p>

        """, unsafe_allow_html=True
      )
    st.write(
        """<p class="big-font"> 
        PFMS helps them relate/compare with best performing families, by their priorities, HOW & WHERE they spend their income:</p>
        """, unsafe_allow_html=True
      )  

    st.write("---")  

    pic1,text1,pic2,text2 = st.columns(4)
    with pic1:
        st.image(Image.open("images/robot.jpg"))
    with text1:
        st.write("##")
        st.caption("<p class='goal'> We get along list of Expenses but a short list of income.By that we struggle very hard on how to cover the whole expense list.</p>", unsafe_allow_html=True)
        st.caption("<p class='goal'>Create a budget that includes all sources of income and expenses.</p>", unsafe_allow_html=True)    
    with pic2:
        st.image(Image.open("images/vaccuum.jpg"))
    with text2:
        st.write("##")
        st.caption("""<p class='goal'>Data sourcing is very crucial to get to understand everything thats is a factor in
         expenditure and revenue generation. Since without the know how of what you spend and how to really earn your money it can be difficult 
         to know where to start.</p>""",unsafe_allow_html=True)
    text3,pic3,text4,pic4 = st.columns(4)     
    with text3:
        st.write('##')
        st.caption("<p class='goal'>Track your spending and make adjustments as needed to stay within your budget.</p>", unsafe_allow_html=True)
        st.caption("""<p class='goal'>Spend wisely: Carefully evaluate your spending habits and prioritize necessary expenses over discretionary spending.Stay informed:
         Keep up with the latest financial news and trends and seek out educational resources to help you make informed financial decisions. </p>""", unsafe_allow_html=True)
    with pic3:
        st.image(Image.open("images/search.jpg"))
    with text4:
        st.write('##')
        st.caption(":blue[**STRATEGY;**]")
        st.caption("""<p class='goal'> Budgeting is crucial, using the right budgeting tools, individuals can create visual representations of their 
        spending habits over time. This can help identify patterns, such as high spending months or 
        areas where spending can be reduced. </p>""", unsafe_allow_html=True)
    with pic4:
        st.image(Image.open("images/strategy.jpg"))
    
    st.write("##")
    st.write("##")
    st.header("Goal. Problem Statement")
    st.write("---")
    st.write("""<p class="big-font"> To develop a model that will help individuals manage their financial resources effectively and make informed financial decisions</p>""", unsafe_allow_html=True)
    st.write("""<p class="big-font"> The ultimate goal of P.F.M.S is to help individuals achieve their financial goals. It will also
     improve overall quality of life and assist individuals realize which economic class they belong to...</p>""", unsafe_allow_html=True)


    fig = {
    "data": [
    {
      "values": numerical_cols_mean['mean'],
      "labels": numerical_cols_mean['index'],
      "domain": {"x": [0, .5]},
      "name": "Basic Need",
      "hoverinfo":"label+percent+name",
      "hole": .3,
      "type": "pie"
    },],
    
   "layout": {
        "title":"Utilities Analysis",
        "annotations": [
            { "font": { "size": 20},
              "showarrow": False,
              "text": "Basic need",
                "x": 0.50,
                "y": 3
            },
         ]
        }
       }

    fig = go.Figure(fig)

    st.plotly_chart(fig)




#----------------DATASET DESCRIPTION----------

if selected == "Datasets":
    st.header("Details on the dataset")
    st.subheader("Title: Philippines Poverty Level Estimates")
    st.write(
                """<p class="big-font"> The Dataset used is from several municipalities in Philippines, which shows the expenditure of low-level households.
                It indicates how the families spend on different utilities. There are two categories economically, where there are ones who are stabler than others,
               where the factor is their expenditure.</p>

               """, unsafe_allow_html=True
             )
    st.write("Link Address:")
    st.write("https://data.world/am-red-cross/d9df3633-8775-435e-9362-6fa218bf4331/file/phl-cityandmunicipallevelpovertyestimates-csv-1.csv")
    st.subheader("Sources:")
    st.subheader("Red-Cross poverty level estimates")
    st.write(
             """link
         https://data.world/am-red-cross/d9df3633-8775-435e-9362-6fa218bf4331/discuss/d9df3633-8775-435e-9362-6fa218bf4331/ytuexfnx?type=comment""")

    st.write("Link: https://data.world/am-red-cross/d9df3633-8775-435e-9362-6fa218bf4331")
              

  
    st.subheader("Households of different Municipality-cities in Philippines")
    st.write("##")
    st.markdown('<p class="big-font"> Below is a dataset of how the the families spend their incomes</p>',unsafe_allow_html=True )
    st.write(phl.head())
   
    st.write("---")
    st.caption("""<p class="big-font">
    From the dataset, last column of the dataframe is a classification column between financially challanged and the stable families.<br> 
    From which its becomes our point of concern to get the insights that clasifies the families. This is characterised by how different families
    spend their money on various utilities.</p>""", unsafe_allow_html=True)
    

    
  
    st.write("##")
    
    #-----------poverty visualization--------------
    st.subheader("Expenditure of the two Economic Classes")
    st.bar_chart(data=poverty_class, x="index", y=['Class_0','Class_1'])
    

    col1,col2 = st.columns(2)
    with col1:
        numerical_ftrs = ['food', 'clothing',
       'power', 'entertainment', 'house_items', 'Health', 'Transport',
       'Education', 'Communication', 'leisure', 'eats']

        food_phl = phl.groupby('Region')['food'].mean().reset_index()

        st.subheader("Food Consumption Distribution")
        st.line_chart(data=food_phl, x="Region", y = "food", use_container_width=True)
        
        with col2:
            health_phl = phl.groupby("Region")['Health'].mean().reset_index()
            st.subheader("Health Insurance Distribution")
            st.area_chart(data=health_phl, x="Region", y = "Health", use_container_width=True)

#---------ANALYSIS PAGE-------------


if selected == "Analysis":
    years = [datetime.today().year, datetime.today().year+1, datetime.today().year+2, datetime.today().year+3]
    months = list(calendar.month_name[1:])
    incomes = ['Salary', 'Business' ,'Blogging', 'Divideds', 'Commisssions', 'Incentives']
    expenses = ['Rent', 'Transport', 'Food', 'Groceries',  'Utilities', 'School fees', 'Loan']

   
    

 #---------SIDEBAR ENTRY FORM-------          
    st.sidebar.header(f"Data Entry in {currency} ")
    st.sidebar.write('<p class="big-font"> -Key in your information in the entry form below for analysis.</p>', unsafe_allow_html=True)
    incomes_selected = st.sidebar.multiselect("Select your sources of income:", incomes)
    expenses_selected = st.sidebar.multiselect("Select your expenses:", expenses) 
    with st.sidebar.form("entry form", clear_on_submit =True):
        col1, col2 = st.columns(2)
        col1.selectbox("Select Month:", months, key='month' )
        col2.selectbox("Select Year:", years, key = "year")
       

        with st.expander("Income"):
            for income in incomes_selected:
                st.number_input(f"{income}:", min_value=2, format="%i", step=10, key=income)

       
        with st.expander("Expenses"):
            for expense in expenses_selected:
                st.number_input(f"{expense}:", min_value=1, format="%i", step=10, key=expense)

   
        submitted = st.form_submit_button("Save Data")
        if submitted:
            period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
            income_set = {income: st.session_state[income] for income in incomes_selected}
            expense_set = {expense: st.session_state[expense] for expense in expenses_selected}
            income_values = list(income_set.values())
            expense_values = list(expense_set.values())
            st.success("Data Saved")
            total_income = sum(income_set.values())
            total_expense = sum(expense_set.values())
            percent_more = round(((total_income - total_expense)/total_expense)*100)
            percent_expense = (total_expense/total_income)*100
            percent_remaining = (100 - percent_expense)
            remaining_income = (percent_remaining*total_income)/100
            investment = (65/100)*remaining_income
            savings = (35/100)*remaining_income
            std_investment = (35/100)*total_income
            std_savings = (15/100)*total_income
        else:
            st.write("Kindly fill in your data above")

  
    income_set = {income: st.session_state[income] for income in incomes_selected}
    expense_set = {expense: st.session_state[expense] for expense in expenses_selected}
   

    #--------- creating  a dataframe
    total_income = sum(income_set.values())
    total_expense = sum(expense_set.values())

    income_values = list(income_set.values())
    expense_values = list(expense_set.values())
    income_features = {"Income": incomes_selected,
                "Amount": income_values }

    expense_features = {"Expense": expenses_selected,
                        "Dollars": expense_values }
    income_df = pd.DataFrame(data=income_features)
   
    expense_df = pd.DataFrame(data=expense_features)

    totals = {"Channels": ["income", "expenses"],
            "Amount": [total_income, total_expense] }

    totals_df = pd.DataFrame(data = totals)
    #---------------analysis--------------
    st.success("In the sidebar to the left, kind input your data for analysis")
    st.write("---")   
    st.header(":blue[**ECONOMIC CLASSIFICATION**]")
    st.write("##")
    st.subheader("Reviews"+":clipboard:")
    st.write("")

   
    visual_income = st.checkbox("View your Income and Expenses tabulation")
    if visual_income:
        column1,column2 = st.columns(2)
        with column1:
            fig = px.bar(income_df, x = 'Income', y = 'Amount', color = 'Income', title = 'Monthly income'
            
                )
            fig.update_layout(
               font_family="Courier New",
                               font_color="blue",
                                       font_size=15,
                                             title_font_family="Times New Roman",
                         title_font_color="red",
                  title_font_size=35,
               legend_title_font_color="green",
                legend_title_font_size=20,
                   yaxis_title="Amount in Dollars '$'"
                   )
            st.plotly_chart(fig, use_container_width=True)
        with column2:
            fig = px.bar(expense_df, x = 'Expense', y = 'Dollars', color = 'Expense', title = 'Expenditure Distribution'
            
                   )
            fig.update_layout(
                   font_family="Courier New",
                   font_color="blue",
                     font_size=15,
                    title_font_family="Times New Roman",
                    title_font_color="red",
                     title_font_size=35,
                       legend_title_font_color="green",
                     legend_title_font_size=20,
                   xaxis_title="Monthly Expenses",
                       yaxis_title="Amount in Dollars '$'"
                    )
            st.plotly_chart(fig, use_container_width=True)
   
    st.subheader(":blue[**Analysis:**]")
    st.write(":red[Click after keying-in the inputs]")
    more = st.checkbox("Show more...")
    if more:
        total_income = sum(income_set.values())
        total_expense = sum(expense_set.values())
        percent_more = round(((total_income - total_expense)/total_income)*100)
        percent_expense = round((total_expense/total_income)*100)
        percent_remaining = (100 - percent_expense)
        remaining_income = round((percent_remaining*total_income)/100)
        investment = round((65/100)*remaining_income)
        savings = round((35/100)*remaining_income)
        std_investment = round((35/100)*total_income)
        std_savings = round((15/100)*total_income)
        
        c1,c2,c3,c4 = st.columns(4)
        c1.metric(label=":blue[Total Income]", value=total_income)
        c2.metric(label=":blue[Total expenses]", value=total_expense,delta=(str(percent_expense)+"%") )
        c3.metric(label=":blue[After Expenses]", value=(total_income-total_expense))
        c4.metric(label=":blue[Investable]", value=(str(percent_remaining)+"%"))
        st.write("##")
        analysis1,analysis2 = st.columns(2)
        with analysis1:
            fig = px.bar(totals_df, x = 'Channels', y = 'Amount', color = 'Channels', title = 'Income Vs Expenses'
            
                   )
            fig.update_layout(
                   font_family="Courier New",
                   font_color="red",
                     font_size=15,
                    title_font_family="Times New Roman",
                    title_font_color="red",
                     title_font_size=35,
                       legend_title_font_color="green",
                     legend_title_font_size=20,
                   xaxis_title="Money Channels",
                       yaxis_title="Amount in Dollars"
                    )
            st.plotly_chart(fig, use_container_width=True)
          
        with analysis2:
            if total_income > total_expense:
                remainder =(total_income-total_expense)
                totals_pie = {"sections": ["remainder", "expenses"],
                          "Amount": [remainder, total_expense] }
                pie_df = pd.DataFrame(data = totals_pie)
                fig = {
                    "data": [
                        {
                       "values": pie_df['Amount'],
                         "labels": pie_df['sections'],
                        "domain": {"x": [0, .5]},
                           "name": "Basic Need",
                              "hoverinfo":"label+percent+name",
                             "hole": .4,
                          "type": "pie"
                           },],
    
                "layout": {
                         "title":"Expense proportion in relation to the Total Income",
                             "annotations": [
                             { "font": { "size": 25},
                               "showarrow": False,
                             "text": "Analysis",
                             "x": 0.80,
                               "y": 3
                                 },
                              ]
                            }
                          }

                fig = go.Figure(fig)

                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error("Your Expenses surpass Income")
        

        st.success("In Conclusion")
        st.write("- Your Income is " +  str(percent_more)+"% more than Your Expenses")
        st.write("- "+str(percent_expense) + "% of your Income goes to your Expenses")
        st.write("- You are left with "+ str(percent_remaining)+ "% for Investments and Savings")
        st.write(":red[Based on Financial Model]")
        st.write("> According to your inputs, you can only invest "+ str(std_investment))
        st.write("> Statistically savings will be  " + str(std_savings))
    st.write("---")    
    st.subheader("Financial Health")
    st.write("""There few set of guidelines that one would follow for him/her to be financialy health. One does not need to be rich to be declared financially healthy.
    There are few tips one should know and follow to be able to manage money:
    """)
    st.write("- Income must be greater than Expenses")
    st.write("- Save before you Spend")
    st.write("- Recurring bills should be compressed maximumly")
    st.write("- Basic needs should be priotized always")

    st.write("##")
    st.header("Financial Model"+":diamond_shape_with_a_dot_inside:")
    st.write("---")
    met1,met2,met3 = st.columns(3)
    met1.metric("EXPENSES", "55%")
    met2.metric("INVESTMENT", "30%")    
    met3.metric("SAVING", "15%")
    st.write("---")


if selected == "About":
   
    st.image(Image.open('official-pic.png'))

    st.header('BENSON N NYOTA')

    st.info('Data Scientist | Stastitician')

    icon_size = 20
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.write('Github: ','https://github.com/Nyotabenson')
    with col2:
        st.write('youtube: ', "https://youtube.com/")
    with col3:
        st.write('medium: ', 'https://medium.com/')
    with col4:
        st.write('twitter: ', 'https://twitter.com/')
    with col5:
        st.write('linkedin: ', 'https://www.linkedin.com/in/nyota-benson752/')
    
    
    
    
    
   