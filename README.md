# Camino de Santiago - Statistics Analysis

## 🧪 Project Overview

This project analyzes the "The Santiago Way" statistics to uncover trends and insights regarding pilgrims' journeys to Santiago de Compostela. The analysis utilizes a dataset spanning nearly two decades to evaluate key questions proposed in the initial research scope.

The core objectives of this analysis are to determine:
- **Growth Trends**: Whether the total number of pilgrims is increasing year-over-year and if there's a post-pandemic acceleration.
- **Demographic Shifts**: Analysis of gender ratios (e.g., increase in female pilgrims) and age distribution (e.g., is the average pilgrim getting younger?).
- **Route Popularity**: Dominance of the French Way vs. growth of secondary routes like the Portuguese or Primitive ways.
- **Nationality Insights**: Comparison of European vs. non-European pilgrim behaviors.
- **Seasonality & Mode**: Impact of summer months and the prevalence of foot vs. bicycle pilgrims.

This repository bridges raw data processing with SQL modeling and Python-based exploratory data analysis (EDA) to answer these questions.

## 🛠️ Tools

*   **Python**: `pandas` for data manipulation, cleaning, and initial analysis.
*   **SQL**: Database schema creation and queries for structured analysis (MySQL/MariaDB syntax).
*   **Tableau**: Used for interactive visualizations (Workbook files included).
*   **Jupyter Notebook**: For documenting the workflow from raw data availability to final statistical insights.
*   **Git & GitHub**: Version control and project management.

## 📁 Repository Structure

The repository is organized as follows:

*   **`data: Contains the CSV datasets.
*   **`notebooks:`camino_main.ipynb`: The central notebook containing data loading, cleaning, merging logic, and Python-based EDA.
*   **`SQL: `camino.sql`: SQL script for creating the database schema (`camino_santiago`) and defining tables (`df_routes`, `df_gender`, etc.) along with key analytical queries.
*   **`figures: Stores generated charts and visual assets used in presentations.
*   **`slides: Presentation materials summarizing the findings.

## 📅 Project Log

**Day 1 – Dataset Discovery & Setup**
*   Identified the "Santiago Way" dataset from Kaggle.
*   Defined 10 key research questions (Growth, Demographics, Routes, Seasonality).
*   Loaded initial CSV files (`camino_origin.csv`, `camino_routes.csv`, etc.) into Python.

**Day 2 – Data Cleaning & Preprocessing**
*   Handled missing values and standardized column names (e.g., identifying 'Pie' as 'Foot', 'Bicicleta' as 'Bicycle').
*   Aggregated "Other" categories for transportation and routes to simplify analysis.
*   Translated country and route names to English for consistency (e.g., 'Alemania' -> 'Germany').

**Day 3 – Relational Database Design (SQL)**
*   Designed the `camino_santiago` database schema.
*   Created tables for normalized data: `df_routes`, `df_groups`, `df_countries`, `df_motives`, etc.
*   Defined Foreign Keys to establish relationships between the main `df_pilgrins` table and dimension tables.

**Day 4 – Exploratory Analysis (SQL & Python)**
*   Executed SQL queries.
*   Validated the "French Way" dominance hypothesis (>60%).

**Day 5 – Visualization & Reporting**
*   Exported cleaned datasets (`df_routes_tableau_map.csv`, `df_trans_tableau_side.csv`) for Tableau.
*   Created Tableau visualization workbooks (`.twbr`) to map pilgrim origins and route density.
*   Synthesized findings into the final presentation.

**Day 6 – Final Review**
*   Cleaned up code in `camino_main.ipynb`.
*   Finalized `README.md` and repository structure.
