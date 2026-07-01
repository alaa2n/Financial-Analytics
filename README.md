# 📊 Financial Analytics Dashboard

## Overview

This project demonstrates an end-to-end Business Intelligence solution for financial reporting and performance analysis. Starting from raw financial data, an ELT pipeline was built using Python and DuckDB to transform data through Bronze, Silver, and Gold layers before creating an interactive Power BI dashboard.

The dashboard enables users to analyze Profit & Loss statements, monitor operational performance across stores and regions, and compare different business scenarios (Actual, Best Case, Worst Case) for decision-making.

---

# Objectives

* Build a modern ELT pipeline using the Medallion Architecture.
* Transform raw financial transactions into analytical star-schema tables.
* Create reusable financial KPIs using DAX.
* Analyze company profitability across multiple dimensions.
* Simulate business scenarios for strategic planning.

---

# Tech Stack

* **Python**
* **DuckDB**
* **SQL**
* **Power BI**
* **Power Query**
* **DAX**
* **Star Schema Modeling**

---

# ETL / ELT Process

### 1. Bronze Layer

Loaded raw financial datasets into DuckDB without applying business logic.

Included:

* GL Transactions
* Accounts
* Stores
* Geography
* Account Mapping

---

### 2. Silver Layer

Performed data cleaning and standardization.

Tasks included:

* Renaming columns
* Fixing data types
* Standardizing dates
* Removing inconsistencies
* Preparing dimensional tables

---

### 3. Gold Layer

Built business-ready analytical tables.

Fact Tables

* Fact GL Transactions
* Monthly Aggregated Transactions
* Scenario Analysis Fact Table (Actual / Best Case / Worst Case)

Dimension Tables

* Date
* Stores
* Accounts
* Account Mapping

---

# Data Model

A Star Schema was designed where:

Dimensions

* Date
* Store
* Account
* Account Mapping

Fact Tables

* Financial Transactions
* Monthly Financial Transactions
* Financial Scenarios

This model improves performance and simplifies DAX calculations.

---

# Dashboard Pages

## 1. Profit & Loss Dashboard

Analyzes the company's financial statements.

Includes

* Revenue by Month
* COGS Trend
* Operating Expenses Trend
* P&L Matrix
* Amount by PL Line
* Interactive slicers

Business Questions Answered

* How is revenue changing over time?
* Which cost category consumes the largest share?
* What are the monthly Profit & Loss trends?
* Which accounts contribute most to each financial statement line?

---

## 2. Operational Performance Dashboard

Focuses on store performance.

KPIs

* Revenue
* Gross Profit
* Operating Profit
* Operating Margin %

Visuals

* Operating Profit by Store
* Profit by Store Type
* Revenue vs Operating Margin
* Matrix by Region / Store Type

Business Questions Answered

* Which stores generate the highest operating profit?
* Which region performs best?
* Does store type affect profitability?
* How does operating margin change throughout the year?

---

## 3. Scenario Analysis Dashboard

Simulates multiple financial scenarios.

Scenarios

* Actual
* Best Case
* Worst Case

Logic Used

Revenue

* Best Case → +10%
* Worst Case → -10%

Expenses

* Best Case → 10% lower expenses
* Worst Case → 10% higher expenses

Visuals

* Revenue Comparison Cards
* Monthly Scenario Trend
* Revenue by Store
* Comparison Matrix

Business Questions Answered

* What happens if revenue increases by 10%?
* Which stores benefit the most in the best-case scenario?
* How much revenue could be lost in a worst-case situation?
* How does performance differ across scenarios?

---

# DAX Measures

Examples include

* Revenue
* COGS
* Gross Profit
* Operating Profit
* Operating Margin %
* Scenario Revenue
* Actual Revenue
* Best Case Revenue
* Worst Case Revenue
* Variance %
* Time Intelligence Measures

---

# Key Insights

### Profit & Loss

* Revenue fluctuates throughout the year with noticeable seasonal patterns.
* Operating Expenses represent the largest cost component.
* Revenue alone does not guarantee profitability because operating costs significantly impact the final result.

---

### Operational Performance

* Some stores consistently outperform others in operating profit.
* Physical stores contribute more operating profit than online stores.
* Operating Margin varies monthly, indicating changes in operational efficiency.

---

### Scenario Analysis

* A 10% increase in revenue produces a clear improvement across all stores.
* Revenue declines have a significant impact on overall business performance.
* Scenario analysis helps estimate financial risk before making strategic decisions.

---

# Project Workflow

```
Raw CSV Files
        │
        ▼
Python + DuckDB
(Bronze Layer)
        │
        ▼
Silver Layer
(Clean & Transform)
        │
        ▼
Gold Layer
(Fact & Dimension Tables)
        │
        ▼
Power BI
        │
        ▼
DAX Measures
        │
        ▼
Interactive Financial Dashboard
```

---
<img width="1920" height="967" alt="Screenshot (386)" src="https://github.com/user-attachments/assets/82f3b984-ed34-420c-953d-0424689db984" />
<img width="1743" height="773" alt="Screenshot (385)" src="https://github.com/user-attachments/assets/dffc1af3-9736-489d-91fa-3961febc13cb" />
<img width="1323" height="753" alt="Screenshot (382)" src="https://github.com/user-attachments/assets/fcb0430e-922c-4141-92b4-b0863c92270d" />
<img width="1325" height="750" alt="Screenshot (383)" src="https://github.com/user-attachments/assets/a4940e4b-cd9b-495e-8ac0-0f44522efa65" />
<img width="1318" height="741" alt="Screenshot (384)" src="https://github.com/user-attachments/assets/8bcaffbf-8f53-4fff-8529-eeec18c5d08f" />

---
