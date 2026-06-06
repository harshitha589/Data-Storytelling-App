import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.title("What Makes a Country Happy?")
st.write("""
This data storytelling application explores the World Happiness Report 2023 dataset.
The aim of this project is to understand how different factors influence happiness across countries.
""")
df=pd.read_csv("WHR2023.csv")
df["Country name"]=df["Country name"].str.strip()
df=df.dropna()
df=df.drop_duplicates()
st.header("About the Dataset")
st.write("""
The World Happiness Report 2023 dataset contains happiness scores and several social and economic indicators for different countries around the world.
""")
st.write("Dataset Shape:",df.shape)
st.write("Number of Rows:",df.shape[0])
st.write("Number of Columns:",df.shape[1])
st.write("Dataset Columns:")
st.write(df.columns.tolist())
st.header("Dataset Overview")
st.write(df.head())
st.header("Exploratory Data Analysis")
st.subheader("Data Types")
st.write(df.dtypes)
st.subheader("Missing Values Analysis")
st.write(df.isnull().sum())
st.subheader("Statistical Analysis - Happiness Score")
st.write("Mean:",df["Ladder score"].mean())
st.write("Median:",df["Ladder score"].median())
st.write("Mode:",df["Ladder score"].mode()[0])
st.write("Standard Deviation:",df["Ladder score"].std())
st.write("Variance:",df["Ladder score"].var())
st.write("Minimum:",df["Ladder score"].min())
st.write("Maximum:",df["Ladder score"].max())
st.write("Range:",df["Ladder score"].max()-df["Ladder score"].min())
st.subheader("Statistical Analysis - GDP per Capita")
st.write("Mean:",df["Logged GDP per capita"].mean())
st.write("Median:",df["Logged GDP per capita"].median())
st.write("Mode:",df["Logged GDP per capita"].mode()[0])
st.write("Standard Deviation:",df["Logged GDP per capita"].std())
st.write("Variance:",df["Logged GDP per capita"].var())
st.subheader("Statistical Analysis - Social Support")
st.write("Mean:",df["Social support"].mean())
st.write("Median:",df["Social support"].median())
st.write("Mode:",df["Social support"].mode()[0])
st.write("Standard Deviation:",df["Social support"].std())
st.write("Variance:",df["Social support"].var())
st.subheader("Statistical Analysis - Freedom")
st.write("Mean:",df["Freedom to make life choices"].mean())
st.write("Median:",df["Freedom to make life choices"].median())
st.write("Mode:",df["Freedom to make life choices"].mode()[0])
st.write("Standard Deviation:",df["Freedom to make life choices"].std())
st.write("Variance:",df["Freedom to make life choices"].var())
st.header("Univariate Analysis")
st.subheader("Distribution of Happiness Scores")
fig=px.histogram(df,x="Ladder score",title="Distribution of Happiness Scores")
st.plotly_chart(fig)
st.write("Most countries fall within the medium to high happiness range.")
st.subheader("Distribution of GDP per Capita")
fig=px.histogram(df,x="Logged GDP per capita",title="Distribution of GDP per Capita")
st.plotly_chart(fig)
st.write("GDP levels vary across countries indicating different economic conditions.")
st.subheader("Distribution of Social Support")
fig=px.histogram(df,x="Social support",title="Distribution of Social Support")
st.plotly_chart(fig)
st.write("Many countries show moderate to high social support values.")
st.subheader("Happiness Score Box Plot")
fig=px.box(df,y="Ladder score",title="Happiness Score Box Plot")
st.plotly_chart(fig)
st.subheader("Freedom Box Plot")
fig=px.box(df,y="Freedom to make life choices",title="Freedom to Make Life Choices")
st.plotly_chart(fig)
st.header("Bivariate Analysis")
st.subheader("GDP vs Happiness")
fig=px.scatter(df,x="Logged GDP per capita",y="Ladder score",hover_name="Country name",title="GDP vs Happiness")
st.plotly_chart(fig)
st.write("Countries with higher GDP generally report higher happiness scores.")
st.subheader("Social Support vs Happiness")
fig=px.scatter(df,x="Social support",y="Ladder score",hover_name="Country name",title="Social Support vs Happiness")
st.plotly_chart(fig)
st.write("Social support appears to have a positive relationship with happiness.")
st.subheader("Freedom vs Happiness")
fig=px.scatter(df,x="Freedom to make life choices",y="Ladder score",hover_name="Country name",title="Freedom vs Happiness")
st.plotly_chart(fig)
st.write("People with greater freedom often report higher life satisfaction.")
st.subheader("Healthy Life Expectancy vs Happiness")
fig=px.scatter(df,x="Healthy life expectancy",y="Ladder score",hover_name="Country name",title="Healthy Life Expectancy vs Happiness")
st.plotly_chart(fig)
st.write("Countries with better health conditions generally show higher happiness levels.")
st.header("Multivariate Analysis")
st.subheader("Correlation Matrix")
correlation=df.select_dtypes(include=np.number).corr()
fig=px.imshow(correlation,text_auto=True,title="Correlation Matrix")
st.plotly_chart(fig)
st.subheader("Scatter Matrix")
fig=px.scatter_matrix(df,dimensions=["Ladder score","Logged GDP per capita","Social support","Healthy life expectancy","Freedom to make life choices"])
st.plotly_chart(fig)
st.header("Insights and Findings")
st.write("""
1. Most countries fall in the medium to high happiness range.

2. GDP per capita has a positive relationship with happiness.

3. Social support contributes significantly to well-being.

4. Healthy life expectancy is associated with higher happiness levels.

5. Freedom to make life choices positively influences happiness.

6. Happiness depends on multiple factors rather than a single factor.
""")
st.header("Recommendations")
st.write("""
1. Improve economic opportunities and living standards.

2. Strengthen social support systems and community networks.

3. Promote healthcare and healthy lifestyles.

4. Encourage policies that support freedom and individual choice.

5. Focus on overall well-being along with economic growth.
""")
st.header("Conclusion")
st.write("The analysis shows that happiness is influenced by economic, social and health-related factors. Countries with stronger economies, better social support and greater freedom generally report higher happiness scores. Understanding these factors can help create happier societies.")
