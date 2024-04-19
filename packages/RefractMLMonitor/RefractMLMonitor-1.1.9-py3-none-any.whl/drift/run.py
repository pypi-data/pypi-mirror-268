import os,json
import pandas as pd
from utility.constants import DataConnector, DriftType, ProblemType
from utility.drift_util import get_feature_drift_report, get_model_performance_drift_report, get_target_drift_report
from evidently.pipeline.column_mapping import ColumnMapping
from evidently.options.data_drift import DataDriftOptions
from utility import constants 
from utility.constants import ProblemType,DriftType,DataType

def get_data_source_type():
    basic_details = json.loads(os.getenv("basic_details"))
    soure_type = [item["field_value"] for item in basic_details if item["field_id"]=="data_source"][0]
    drift_type = [item["field_value"] for item in basic_details if item["field_id"]=="drift_type"][0]
    probelm_type = [item["field_value"] for item in basic_details if item["field_id"]=="problem_type"][0]

    problem_type_maps = {
        "binary_classification" : "Binary Classification",
        "multiclass_classification" : "Multiclass Classification",
        "multi_label_classification" : "Multilabel Classification",
        "regression" : "Regression"
    }
    probelm_type = probelm_type if not probelm_type in problem_type_maps else problem_type_maps[probelm_type]

    if not probelm_type in ["Binary Classification","Multiclass Classification","Multilabel Classification","Regression"]:
        raise Exception(f"Invalid problem_type {probelm_type} provided")

    return soure_type,drift_type,probelm_type

def main():
    # from test import set_env
    # set_env()
    print(f"Starting drift execution!")
    print(f'os.getenv("drift_type"): {os.getenv("drift_type")}')
    print(f'os.getenv("data_type"):  {os.getenv("data_type")}')
    print(f'os.getenv("problem_type") : {os.getenv("problem_type")}')
    print(f'os.getenv("default_container_size") : {os.getenv("default_container_size")}')
    print(f'os.getenv("data_source"): {os.getenv("data_source")}')
    print(f'os.getenv("reference_data_path") : {os.getenv("reference_data_path")}')
    print(f'os.getenv("reference_filter_condition"): {os.getenv("reference_filter_condition")}')
    print(f'os.getenv("current_data_path"): {os.getenv("current_data_path")}')
    print(f'os.getenv("current_filter_condition"): {os.getenv("current_filter_condition")}')
    print(f'os.getenv("categorical_features"): {os.getenv("categorical_features")}')
    print(f'os.getenv("categorical_features_stattest"): {os.getenv("categorical_features_stattest")}')
    print(f'os.getenv("categorical_features_threshold"): {os.getenv("categorical_features_threshold")}')
    print(f'os.getenv("numerical_features"): {os.getenv("numerical_features")}')
    print(f'os.getenv("numerical_features_stattest"): {os.getenv("numerical_features_stattest")}')
    print(f'os.getenv("numerical_features_threshold"): {os.getenv("numerical_features_threshold")}')
    print(f'os.getenv("prediction_col_name"): {os.getenv("prediction_col_name")}')
    print(f'os.getenv("target_col_name"): {os.getenv("target_col_name")}')
    from utility.connector import connector_factory
    source,drift_type,problem_type = get_data_source_type()
    connection = connector_factory.ConnectorFactory.getConnector(source)
    reference, current = connection.load_data()

    ## Testing
    # source,drift_type,problem_type=os.getenv("data_source"),os.environ["drift_type"],os.environ["problem_type"]
    # reference, current = pd.read_csv(os.getenv("reference_data_path")),pd.read_csv(os.getenv("current_data_path"))
    
    column_mapping = ColumnMapping()

    if drift_type == DriftType.FEATURE_DRIFT:
        cat_features_stattest = None ; categorical_features = "auto" ; categorical_features_threshold = "auto"
        num_features_stattest = None ; numerical_features = "auto" ; numerical_features_threshold = "auto"

        options = None

        categorical_features = os.getenv("categorical_columns")
        if categorical_features == "auto" or not categorical_features:
            categorical_features = "auto"
        else:
            categorical_features = eval(categorical_features)
            if len(categorical_features) == 1 and categorical_features[0] == "auto":
                categorical_features = "auto"
        cat_features_stattest = os.getenv("categorical_features_stattest")
        categorical_features_threshold = os.getenv("categorical_features_threshold")

        numerical_features = os.getenv("numeric_columns")
        if numerical_features == "auto" or not numerical_features:
            numerical_features = "auto"
        else:
            numerical_features = eval(numerical_features)
            if len(numerical_features) == 1 and numerical_features[0] == "auto":
                numerical_features = "auto"
        numerical_features_threshold = os.getenv("numerical_features_threshold")
        num_features_stattest = os.getenv("numerical_features_stattest")

        if categorical_features != "auto":
            column_mapping.categorical_features = categorical_features
        if numerical_features != "auto":
            column_mapping.numerical_features = numerical_features

        if categorical_features_threshold == "auto":
            categorical_features_threshold = None
        else:
            categorical_features_threshold = float(categorical_features_threshold)
        if numerical_features_threshold == "auto":
            numerical_features_threshold = None
        else:
            numerical_features_threshold = float(numerical_features_threshold)

        cat_features_stattest = None if cat_features_stattest=="auto" else cat_features_stattest
        num_features_stattest = None if num_features_stattest=="auto" else num_features_stattest

        custom_options = {
            "cat_stattest" :cat_features_stattest,
            "num_stattest" : num_features_stattest,
            "cat_stattest_threshold" :categorical_features_threshold,
            "num_stattest_threshold" :numerical_features_threshold
        }
        
        html_report_path = get_feature_drift_report(reference,current,column_mapping=column_mapping,custom_options=custom_options)
        
    elif drift_type == DriftType.MODEL_PERFORMANCE_DRIFT:
        from utility.constants import ProblemType
        prediction_col = os.getenv("prediction_col_name")
        target_col = os.getenv("target_col_name")
        prob = False
        try:
            if str(target_col).strip().startswith("[") and str(target_col).strip().endswith("]"):
                target_col = json.loads(str(target_col).replace("'",'"'))[0]

            if str(prediction_col).strip().startswith("[") and str(prediction_col).strip().endswith("]"):
                prediction_col = json.loads(str(prediction_col).replace("'",'"'))
                if len(prediction_col) > 1:
                    prob = True
                else:
                    prediction_col = prediction_col[0]
            else:
                prediction_col = str(prediction_col).strip().split(",")
                if len(prediction_col) > 1 :
                    prob = True
                else:
                    prediction_col = prediction_col[0]
                    prob = False
        except Exception as msg:
            print(msg)
            prob = False
        if prob:
            column_mapping.pos_label = prediction_col[0]
        elif not prob and  problem_type == ProblemType.BINARY_CLASSIFICATION:
            column_mapping.pos_label = 1

        column_mapping.target = target_col
        column_mapping.prediction = prediction_col
        html_report_path = get_model_performance_drift_report(reference,current,problem_type,column_mapping, prob=prob)

    elif drift_type == DriftType.PREDICTION_DRIFT:
        prediction_col = os.getenv("prediction_col_name")
        if str(prediction_col).strip().startswith("[") and str(prediction_col).strip().endswith("]"):
            prediction_col = json.loads(str(prediction_col).replace("'",'"'))[0]

        column_mapping.prediction = prediction_col
        column_mapping.target='None'
        html_report_path = get_target_drift_report(reference,current,problem_type,column_mapping)

    elif drift_type == DriftType.LABEL_DRIFT:
        target_col = os.getenv("target_col_name")
        if str(target_col).strip().startswith("[") and str(target_col).strip().endswith("]"):
            target_col = json.loads(str(target_col).replace("'",'"'))[0]

        column_mapping.prediction = 'None'
        column_mapping.target = target_col
        html_report_path = get_target_drift_report(reference,current,problem_type,column_mapping)

    elif drift_type == DriftType.CONCEPT_DRIFT:
        print("Concept drift yet to be implemented")
    else:
        print("Drift type not found. User provded : {}, expected one from [{},{},{},{},{}]".format(
            drift_type,DriftType.FEATURE_DRIFT,DriftType.LABEL_DRIFT,DriftType.MODEL_PERFORMANCE_DRIFT,DriftType.PREDICTION_DRIFT,DriftType.CONCEPT_DRIFT))
    return None


main()

