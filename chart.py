import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def chart_nochurn_vs_nochurn(dataframe):

    fig, ax = plt.subplots()
    sns.countplot(x='Churn', data=dataframe, palette="viridis", ax=ax)
    ax.set_title('Não ocorreu Churn x Ocorreu Churn')
    ax.set_xlabel('Ocorreu Churn?', fontsize = 12)
    ax.set_ylabel('Quantidade', fontsize = 12)

    st.pyplot(fig)

def plot_annotate(ax, title):
    for rect in ax.patches:
        ax.annotate(rect.get_height(),
                (rect.get_x() + rect.get_width()/2, rect.get_height()),
                ha='center', va='baseline', fontsize=12, color='black',
                xytext=(0, 1), textcoords="offset points")
    ax.set_title(title)

def churn_by_variable(dataframe, option):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x=option, data=dataframe, palette="viridis", hue="Churn")
    plot_annotate(ax, option)

    return fig

def churn_by_variable_boxplot(dataframe, option):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='Churn', y=option, data=dataframe, palette="viridis")

    return fig

def churn_by_variable_kdeplot(dataframe, option):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.kdeplot(dataframe[option][(dataframe["Churn"] == 'No')], color='Blue', fill=True, ax=ax)
    sns.kdeplot(dataframe[option][(dataframe["Churn"] == 'Yes')], color="DarkGreen", fill=True, ax=ax)
    ax.legend(["Not Churn", "Churn"], loc='upper right')

    return fig