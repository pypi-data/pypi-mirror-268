
import os

def set_env():
    os.environ["drift_type"] = "model_performance_drift"
    os.environ["data_type"] ="Tabular"
    os.environ["problem_type"] =  "Regression"
    os.environ["default_container_size"] = "da3f755d-7dab-4df4-9f48-5cce0f263454"
    os.environ["data_source"]= "Local data files"
    os.environ["reference_data_path"] = "reference_loan_defaulter.csv"
    os.environ["reference_filter_condition"]= ""
    os.environ["current_data_path"]= "current_loan_defaulter.csv"
    os.environ["current_filter_condition"]= ""
    os.environ["categorical_features"]= 'None'
    os.environ["categorical_features_stattest"]= "None"
    os.environ["categorical_features_threshold"]= "None"
    os.environ["numerical_features"]= "None"
    os.environ["numerical_features_stattest"]= "None"
    os.environ["numerical_features_threshold"]= "None"
    os.environ["prediction_col_name"]= "['PREDICTION']"
    os.environ["target_col_name"]= "['LOAN_STATUS']"
    os.environ['plugin'] = '[{"field_id": "plugin_type", "field_value": "PERFORMANCE_DRIFT"}]'
    os.environ['output_path'] = os.getcwd()
    os.environ['alert_configuration']= '''[[
        {
            "field_id": "parameter",
            "field_label": "Parameter",
            "field_mandatory": "yes",
            "field_options": [
                "Accuracy",
                "Precision",
                "Recall",
                "F1 Score"
            ],
            "field_type": "select",
            "field_value": "ME",
            "grid_value": 12
        },
        {
            "field_id": "min_threshold",
            "field_label": "Min. threshold",
            "field_mandatory": "yes",
            "field_type": "number",
            "field_value": "0",
            "grid_value": 12,
            "max": "1",
            "min": "0"
        },
        {
            "field_id": "max_threshold",
            "field_label": "Max. threshold",
            "field_mandatory": "yes",
            "field_type": "number",
            "field_value": "1",
            "grid_value": 12,
            "max": "1",
            "min": "0"
        },
        {
            "field_id": "severity",
            "field_label": "Severity",
            "field_mandatory": "yes",
            "field_options": [
                {
                    "icon": "red",
                    "label": "Red"
                },
                {
                    "icon": "amber",
                    "label": "Amber"
                }
            ],
            "field_type": "select",
            "field_value": "Red",
            "grid_value": 12
        }]]'''
    os.environ['model_configuration']='[{"field_id": "workflow_id", "field_value": "1245", "refract_source": "workflow"},{"field_id": "plugin_id", "field_value": "34r34rt", "refract_source": "workflow"}]'