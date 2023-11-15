# Customer Churn Prediction using Azure Databricks

![Azure Databricks Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Databricks_Logo.png/320px-Databricks_Logo.png)

## Overview
This project demonstrates how to predict customer churn using Azure Databricks, a powerful analytics platform. It leverages Spark, Python, and Machine Learning to process large datasets and build predictive models.

## Features
- End-to-end data pipeline for processing customer data
- ML models for churn prediction with high accuracy
- Scalable architecture leveraging Azure Databricks and PySpark
- Data visualization and model performance metrics

## Project Structure
```plaintext
azure-databricks-churn-prediction/
│
├── data/
│   ├── raw/                 # Raw input data files (CSV, JSON, etc.)
│   ├── processed/           # Processed data ready for analysis
│   └── output/              # Model output, predictions, or reports
│
├── notebooks/
│   ├── 1_data_ingestion.py  # Data ingestion and preparation notebook
│   ├── 2_data_preprocessing.py  # Data cleaning and transformation
│   ├── 3_model_training.py  # Machine learning model training
│   ├── 4_model_evaluation.py  # Model evaluation and metrics
│   └── 5_model_deployment.py  # Model deployment scripts
│
├── utils/
│   ├── data_loader.py       # Functions to load and save data
│   ├── preprocess.py        # Functions for data cleaning
│   └── model_utils.py       # Model training, evaluation utilities
│
├── .gitignore               # Git ignore file
├── LICENSE                  # License for the project
├── README.md                # Project description and setup guide
├── requirements.txt         # Python dependencies
└── setup_environment.sh     # Script to set up the Azure Databricks environment

```

![Azure Databricks](https://github.com/user-attachments/assets/4abf4541-55c3-40be-879a-aa3f9a9345dc)

## Setup Instructions

### Prerequisites
1. An active [Azure account](https://azure.microsoft.com/).
2. Azure Databricks workspace.
3. Install Python 3.8+ and the necessary dependencies.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/azure-databricks-churn-prediction.git
   cd azure-databricks-churn-prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Upload the project to your Databricks workspace:
   - Navigate to the **Data** section to upload raw files from the `data/raw` directory.
   - Upload notebooks to Databricks using the **Workspace** section.

4. Run the notebooks in order:
   - **1_data_ingestion.py** > **2_data_preprocessing.py** > **3_model_training.py** > **4_model_evaluation.py** > **5_model_deployment.py**

5. Deploy the model using `5_model_deployment.py`.

## Technology Stack
- **Azure Databricks**: Distributed analytics and ML
- **PySpark**: Data processing
- **MLlib**: Machine learning
- **Python**: Core programming
- **pandas**, **scikit-learn**: Auxiliary libraries

## Results
- **Accuracy**: 92%
- **Precision**: 91%
- **Recall**: 89%

## Contribution
Contributions are welcome. Please create a pull request with relevant detail.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

## Author
[eagleanurag](https://www.google.com/search?q=eagleanurag)



```


