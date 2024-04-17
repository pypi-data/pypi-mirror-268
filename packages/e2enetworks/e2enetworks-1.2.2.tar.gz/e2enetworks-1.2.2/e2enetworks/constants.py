import os

BASE_URL_MODEL_API_CLIENT = os.environ.get("MODEL_API_CLIENT_HOST", "https://infer.e2enetworks.net/")
MY_ACCOUNT_LB_URL = os.environ.get("E2E_TIR_API_HOST", "https://api.e2enetworks.com/myaccount/")

GPU_URL = "api/v1/gpu/"
BASE_GPU_URL = f"{MY_ACCOUNT_LB_URL}{GPU_URL}"
VALIDATED_SUCCESSFULLY = "Validated Successfully"
INVALID_CREDENTIALS = "Validation Failed, Invalid APIkey or Token"
headers = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://thor-gpu.e2enetworks.net',
    'Referer': 'https://thor-gpu.e2enetworks.net/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
}
MANAGED_STORAGE = "managed"
E2E_OBJECT_STORAGE = "e2e_s3"
BUCKET_TYPES = [MANAGED_STORAGE, E2E_OBJECT_STORAGE]
BUCKET_TYPES_HELP = {
    MANAGED_STORAGE: "To Create New Bucket",
    E2E_OBJECT_STORAGE: " To Use Existing Bucket"
}
NOTEBOOK = "notebook"
INFERENCE = "inference_service"
PIPELINE = "pipeline"

FREE_USAGE = "free_usage"
PAID_USAGE = "paid_usage"
INSTANCE_TYPE = [FREE_USAGE, PAID_USAGE]
TRITON = "triton"
PYTORCH = "pytorch"
MODEL_TYPES = ['pytorch', 'triton', 'custom']
S3_ENDPOINT = "objectstore.e2enetworks.net"

WHISPER_DATA_LIMIT_BYTES = 50000000
WHISPER_LARGE_V3 = "whisper-large-v3"
LLAMA_2_13B_CHAT = "llama-2-13b-chat"
STABLE_DIFFUSION_2_1 = "stable-diffusion-2-1"
MIXTRAL_8X7B_INSTRUCT = "mixtral-8x7b-instruct"
CODELLAMA_13B_INSTRUCT = "codellama-13b-instruct"
E5_MISTRAL_7B_INSTRUCT = "e5-mistral-7b-instruct"