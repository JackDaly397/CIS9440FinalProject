# CIS9440 Group 4 Final Project

# Project Overview

## Information Architecture
![Information Architecture](https://drive.google.com/file/d/1y5xubyr-Es94vA1Yy3jjFblRPLzu-wPs/view?usp=sharing)

## Introduction

### Background:
The project aims to conduct an in-depth analysis of the Paycheck Protection Program (PPP) loans issued to small businesses during the COVID-19 pandemic. By leveraging data from various sources, including the U.S. Small Business Administration (SBA) and the U.S. Census Bureau, the project seeks to extract valuable insights to aid in understanding the distribution of loans, their impact on different sectors, and their correlation with economic indicators such as GDP.

## Business Problem

### Description:
Small businesses faced unprecedented challenges during the COVID-19 pandemic, necessitating government intervention through programs like the PPP. However, assessing the effectiveness and distribution of PPP loans requires thorough analysis to identify trends, challenges, and opportunities for improvement.

### Requirements:
- Total loan amounts by companies, states, and lenders.
- Classification of loans by NAICS codes to understand industry distribution.
- Comparison of PPP loan data with aggregate GDP data to assess economic impact.
- Identification of top lenders by state and analysis of loan distribution across industries.

## Business Impact

### Potential Benefits:
- Informed decision-making for policymakers and small business owners.
- Strategic planning for economic recovery efforts.
- Identification of sectors in need of additional support or resources.
- Insights into the effectiveness of government stimulus programs during times of crisis.

### Risks and Challenges:
- Data quality issues such as missing or inaccurate information.
- Interpretation biases that may arise from the analysis.
- External factors impacting loan distribution and economic recovery.

## Data

### Data Sources:
- **PPP Data**: Obtained from the U.S. Small Business Administration (SBA) Open Data portal.
- **NAICS Codes**: Retrieved from the U.S. Census Bureau's NAICS directory.
- **GDP Data**: Aggregate GDP data sourced from the U.S. Small Business Administration (SBA) Open Data.

### Metadata:
- **PPP Data**: Includes loan amounts, borrower information, and loan status.
- **NAICS Codes**: Provides classification codes for various industries.
- **GDP Data**: Offers insights into economic performance at the national and regional levels.

### Data Size:
- The PPP loan dataset consists of millions of records spanning multiple years.
- NAICS codes provide comprehensive industry classification data.
- Aggregate GDP data covers multiple years and regions.

### Strengths and Weaknesses:
- **Strengths**: Large dataset enabling detailed analysis, diverse sources provide comprehensive insights.
- **Weaknesses**: Data quality issues may require extensive cleaning and preprocessing.

## Dimensional Modeling

### PPP Dimensional Modeling
Dimensional modeling for PPP data involves creating a structure that facilitates analysis and reporting. This included defining dimensions such as borrower information, loan status, and industry classification, as well as measures such as loan amounts.

### GDP Dimensional Modeling
Dimensional modeling for GDP data involves structuring the data to enable analysis of economic performance at different levels, such as national, regional, and industry-specific. This included defining dimensions such as time, geography, and economic indicators, along with measures such as GDP growth rates.

## Methods

### Tools:
- **Python**: Utilized for data processing and analysis using libraries such as Pandas, NumPy, and Matplotlib.
- **Azure Services**: Azure Blob Storage used for data storage and retrieval.
- **Power BI**: Employed for creating interactive visualizations and dashboards.
- **DataGrip**: Used for database management and SQL scripting.
- **PostgresSQL**: Database management system for storing dimensional models and processed data.

### Data Tools:
- **Data Storage**: Azure Blob Storage for storing raw and processed data.
- **Data Processing**: Python scripts for cleaning, preprocessing, and integrating data.
- **Data Orchestration**: Workflow management tools for organizing and orchestrating data pipelines.

## Data Processing

### Steps:
1. **Data Extraction**: Raw data retrieved from SBA and Census Bureau portals.
2. **Data Cleaning**: Preprocessing involves handling missing values, standardizing formats, and resolving data inconsistencies.
3. **Data Integration**: PPP loan data integrated with NAICS codes and GDP data to create dimensional models for analysis.
4. Dimensional Modeling: Creation of dimensional models for PPP and GDP data to facilitate analysis and reporting.
5. Aggregation and Summarization: Aggregating data at different levels (e.g., by state, industry) and summarizing key metrics for analysis.
6. Feature Engineering: Generating new features from existing data to enhance analysis capabilities.
7. Data Transformation: Applying transformations such as normalization or scaling to prepare data for modeling.
8. Quality Assurance: Performing checks to ensure data accuracy, consistency, and completeness throughout the processing pipeline.


## Analysis and Insights

### Findings:
- Insights gained include total loan amounts by companies, states, and lenders.
- Classification by NAICS code provides insights into industry distribution of PPP loans.
- Visualizations highlight top lenders by state, total loan amounts per industry, and comparison with GDP data.

## Conclusion

### Impact and Recommendations:
- Insights from the analysis can inform decision-making and strategic planning for small businesses and policymakers.
- Further analysis could include exploring loan forgiveness rates and their correlation with economic indicators.
- Continuous monitoring and updating of data recommended to track long-term impacts on small businesses and the economy.

## Next Steps

### Future Directions:
- Explore additional datasets for a more comprehensive analysis.
- Implement machine learning models for predictive analysis and forecasting.
- Collaborate with stakeholders to address specific research questions or areas of interest.
