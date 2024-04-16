import ctypes
import os
from ctypes import c_char_p, c_bool
from distutils.sysconfig import get_config_var
from pathlib import Path
from typing import BinaryIO

root = Path(__file__).absolute().parent
path = root / "libpss.so"
libpss = ctypes.cdll.LoadLibrary(path)

_template_root = str(root / "templates").encode("utf-8")
_set_template_root = libpss.SetTemplateRoot
_set_template_root.argtypes = [c_char_p]
_set_template_root(_template_root)

_check_exists = libpss.CheckExists
_check_exists.argtypes = [c_char_p, c_char_p]
_check_exists.restype = c_bool

_upload_file = libpss.UploadFile
_upload_file.argtypes = [c_char_p, c_char_p, c_char_p]
_upload_file.restype = c_bool

_generate_presigned_url = libpss.GeneratePresignedURL
_generate_presigned_url.argtypes = [c_char_p, c_char_p]
_generate_presigned_url.restype = c_char_p

_generate_pricing_sheet = libpss.GeneratePricingSheet
_generate_pricing_sheet.argtypes = [c_char_p]
_generate_pricing_sheet.restype = c_char_p

_generate_project_summary = libpss.GenerateProjectSummary
_generate_project_summary.argtypes = [c_char_p]
_generate_project_summary.restype = c_char_p

# TODO: deprecate
_invoke_lambda_function = libpss.InvokeLambdaFunction
_invoke_lambda_function.argtypes = [c_char_p, c_char_p, c_char_p]
_invoke_lambda_function.restype = c_bool


def check_exists(bucket: str, key: str) -> bool:
    """Check if a file exists on S3"""
    bucket = bucket.encode("utf-8")
    key = key.encode("utf-8")
    return _check_exists(bucket, key)


def upload_file(filename: str, bucket: str, key: str) -> bool:
    """Upload a file from disk to S3"""
    filename = filename.encode("utf-8")
    bucket = bucket.encode("utf-8")
    key = key.encode("utf-8")
    return _upload_file(filename, bucket, key)


def generate_presigned_url(bucket: str, key: str) -> str:
    """Generate a presigned URL for an S3 file"""
    bucket = bucket.encode("utf-8")
    key = key.encode("utf-8")
    return _generate_presigned_url(bucket, key).decode("utf-8")


def generate_pricing_sheet(data: str) -> str:
    """Generate the pricing sheet"""
    data = data.encode("utf-8")
    return _generate_pricing_sheet(data).decode("utf-8")


def generate_project_summary(data: str) -> str:
    """Generate the project summary"""
    data = data.encode("utf-8")
    return _generate_project_summary(data).decode("utf-8")


# TODO: deprecate
def invoke_lambda_function(endpoint: str, function_name: str, parameters: str) -> bool:
    """Invoke a Lambda function asynchronously"""
    endpoint = endpoint.encode("utf-8")
    function_name = function_name.encode("utf-8")
    parameters = parameters.encode("utf-8")
    return _invoke_lambda_function(endpoint, function_name, parameters)
