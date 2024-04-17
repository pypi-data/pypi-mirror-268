from copy import deepcopy
import string
import random
from e2enetworks.constants import BASE_URL_MODEL_API_CLIENT
from e2enetworks.cloud.tir.constants import MODEL_NAME_TO_URL_PATH_MAPPING, MODEL_API_DEFAULT_DATA, MODELS_API_DATA_FORMATS


def get_random_string(N):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))


def cpu_plan_short_code(sku):
    return f"{sku.get('series')}-{sku.get('sku_type').split('-')[0]}-{sku.get('cpu')}-" \
           f"{sku.get('memory')}-{sku.get('gpu') if sku.get('gpu') else 0}"


def gpu_plan_short_code(sku):
    return f"{sku.get('series')}-{sku.get('sku_type').split('.')[1]}-{sku.get('cpu')}-" \
           f"{sku.get('memory')}-{sku.get('gpu') if sku.get('gpu') else 0}"


def plan_to_sku_id(skus, plan):
    if plan.startswith("CPU"):
        for sku in skus["CPU"]:
            if cpu_plan_short_code(sku) == plan:
                return sku.get("sku_id")
    else:
        for sku in skus["GPU"]:
            if gpu_plan_short_code(sku) == plan:
                return sku.get("sku_id")
    return False


def plan_name_to_sku_item_price_id(skus, sku_unique_name):
    if sku_unique_name.startswith("CPU"):
        for sku in skus["CPU"]:
            if not sku["is_free"] and cpu_plan_short_code(sku) == sku_unique_name:
                for plan in sku["plans"]:
                    if plan["committed_days"] == 0:
                        return plan.get("sku_item_price_id")
    else:
        for sku in skus["GPU"]:
            if not sku["is_free"] and gpu_plan_short_code(sku) == sku_unique_name:
                for plan in sku["plans"]:
                    if plan["committed_days"] == 0:
                        return plan.get("sku_item_price_id")
    return False

def get_model_url(model_name, namespace):
    if model_name not in MODEL_NAME_TO_URL_PATH_MAPPING:
        return False, model_name
    url = BASE_URL_MODEL_API_CLIENT + MODEL_NAME_TO_URL_PATH_MAPPING[model_name].format(namespace=namespace)
    return True, url

def get_formated_data_for_model(model_name, parameters):
    extra_keys = []
    fromatted_data = deepcopy(MODEL_API_DEFAULT_DATA)
    model_formatted_data = deepcopy(MODELS_API_DATA_FORMATS).get(model_name)
    for input_key in parameters:
        if input_key in model_formatted_data:
            key_data = model_formatted_data.get(input_key)
            key_data["data"].append(parameters.get(input_key))
            fromatted_data["inputs"].append(key_data)
        else:
            extra_keys.append(input_key)
    if len(extra_keys):
        return False, extra_keys
    return True, fromatted_data
