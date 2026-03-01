# 🌿 Carbon Footprint Calculator

An interactive web application that helps companies calculate and visualize their Scope 1, 2, and 3 greenhouse gas emissions in line with the GHG Protocol — the same standard required under CSRD reporting frameworks.

## What it does

Input your company's operational data and the app instantly calculates your total carbon footprint broken down by scope, visualizes the emission sources as an interactive chart, and provides targeted reduction recommendations based on your highest emission area.

## Why it matters

The EU's Corporate Sustainability Reporting Directive (CSRD) requires companies to report Scope 1, 2, and 3 emissions. This tool simplifies that process using emission factors sourced from the GHG Protocol and DEFRA 2023 guidelines.

## The Three Scopes

Scope 1 covers direct emissions from sources owned or controlled by the company such as vehicles and heating. Scope 2 covers indirect emissions from purchased electricity. Scope 3 covers all other indirect emissions across the value chain including business travel, employee commuting, and waste.

## How to Run Locally

Install dependencies and run the app:

pip install -r requirements.txt
streamlit run app.py

![App Screenshot](screenshot.png)

## Tools Used
Python, Streamlit, Plotly, Pandas