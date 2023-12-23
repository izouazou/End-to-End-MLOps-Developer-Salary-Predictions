import os
from mlProject.custom_logger import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def preprocess_data(self, data: pd.DataFrame) -> pd.DataFrame:
        selected_columns = ['Country', 'Age', 'EdLevel', 'Employment', 'RemoteWork', 
                            'DevType', 'OrgSize',  'YearsCodePro', 'ConvertedCompYearly']
        data = data[selected_columns]

        data['YearsCodePro'] = pd.to_numeric(data['YearsCodePro'], errors='coerce')
        data.rename(columns={'ConvertedCompYearly': 'Salary'}, inplace=True)
        data = data[data["Employment"]=="Employed, full-time"]
        data = data.drop("Employment", axis=1)
        data = data[data["Salary"].notnull()]
        data = data[~data['Age'].isin(['Prefer not to say'])]
        data = data[~data['OrgSize'].isin(['I don’t know'])]
        data = data.dropna()

        # Data Transformation
        def replace_column_values(column, value_mapping=None, threshold=None, replacement='other'):
            column = column.replace(value_mapping)

            if threshold is not None:
                value_counts = column.value_counts()
                to_replace = value_counts[value_counts < threshold].index
                column = column.replace(to_replace, replacement)

            return column

        YearsCodePro_mapping = {'More than 50 years': 50, 'Less than 1 year': 0.5}
        DevType_mapping = {'Other (please specify):': 'other'}
        EdLevel_mapping = {
                'Bachelor’s degree (B.A., B.S., B.Eng., etc.)': 'Bachelor’s degree',
                'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)': 'Master’s degree',
                'Professional degree (JD, MD, Ph.D, Ed.D, etc.)': 'Doctoral degree',
                'Associate degree (A.A., A.S., etc.)': 'Associate degree',
                'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)': 'Non-degree',
                'Some college/university study without earning a degree': 'Non-degree',
                'Primary/elementary school': 'Non-degree',
                'Something else': 'Non-degree',
        }
        OrgSize_mapping = {
                '2 to 9 employees': 'Small Business',
                '10 to 19 employees': 'Small Business',
                '20 to 99 employees': 'Small Business',
                '100 to 499 employees': 'Medium Business',
                '500 to 999 employees': 'Medium Business',
                '1,000 to 4,999 employees': 'Large Business',
                '5,000 to 9,999 employees': 'Large Business',
                '10,000 or more employees': 'Large Business',
                'Just me - I am a freelancer, sole proprietor, etc.': 'Freelancer'
        }

        data["Country"] = replace_column_values(data["Country"], threshold=50)
        data["DevType"] = replace_column_values(data["DevType"], DevType_mapping, threshold=50)
        data["EdLevel"] = replace_column_values(data["EdLevel"], EdLevel_mapping)
        data["YearsCodePro"] = replace_column_values(data["YearsCodePro"], YearsCodePro_mapping)
        data["OrgSize"] = replace_column_values(data["OrgSize"], OrgSize_mapping)

        def cap_outliers_by_group(data, y_column, x_column):
            # Group by 'x_column' and compute the 25th and 75th percentiles for 'y_column'
            summary_stats = data.groupby(x_column)[y_column].describe().reset_index()[[x_column, '25%', '75%']]

            # Merge the percentiles back into the original DataFrame
            df_with_stats = data.merge(summary_stats, on=x_column, how="left")

            # Replace outliers with corresponding percentiles
            mask_low = df_with_stats[y_column] < df_with_stats['25%']
            df_with_stats.loc[mask_low, y_column] = df_with_stats['25%']

            mask_high = df_with_stats[y_column] > df_with_stats['75%']
            df_with_stats.loc[mask_high, y_column] = df_with_stats['75%']

            # Drop the columns '25%' and '75%' from the DataFrame 
            df_with_stats.drop(['25%', '75%'], axis=1, inplace=True)

            return df_with_stats

        data = cap_outliers_by_group(data, 'Salary', 'Country')

        return data



    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)

            # Preprocess the data
            preprocessed_data = self.preprocess_data(data)

            # Save the preprocessed data to a new CSV file
            preprocessed_data.to_csv(self.config.preprocessed_data_csv, index=False)
            
            all_cols = list(preprocessed_data.columns)

            all_schema = self.config.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e

