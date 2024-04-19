from __future__ import annotations
from flask import Flask, request
from sqlglot.optimizer.qualify_tables import qualify_tables
from sqlglot.optimizer.qualify_columns import quote_identifiers
from sqlglot import exp
import sqlglot
import logging
import json
import os
import sys

app = Flask(__name__)
logger = logging.getLogger("sqlglot")
# Configure Logger
if getattr(sys, "frozen", False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

application_parent_path = os.path.dirname(application_path)
log_directory = os.path.join(application_parent_path, "log")
if not os.path.exists(log_directory):
    os.mkdir(log_directory)
log_file_path = os.path.join(log_directory, "audit.log")
logging.basicConfig(
    filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def transpile(sql_query, read, write, case_sensitive):
    global result, response_code
    # Check if the SQL contains DDL keywords
    ddl_keywords = ["CREATE", "ALTER", "DROP", "TRUNCATE", "COMMENT"]
    first_word = sql_query.strip().split()[0].upper()
    response_code = 0
    unknown_function = None
    if first_word in ddl_keywords:
        response_code = 1
        result = "DDL transformation is not supported. Only DML transformation is supported."
    else:
        try:
            result, unknown_function = transpile_text(
                sql_query, read=read, write=write, case_sensitive=case_sensitive
            )
        except Exception as e:
            response_code = 1
            result = f"Error transpiling query: {str(e).replace('sqlglot.', 'DorisSQLConvertor.')}"
    return result, unknown_function


def transpile_text(sql_query, read, write, case_sensitive):
    ast = sqlglot.parse_one(read=read, sql=sql_query)
    unknown_functions = []
    # identify unknown functions
    for unknown in ast.find_all(exp.Anonymous):
        unknown_functions.append(unknown.name)
    case = None if case_sensitive == "0" else True if case_sensitive == "1" else False
    ast_1 = quote_identifiers(ast, dialect="doris", identify=True)
    result = qualify_tables(ast_1, case_sensitive=case).sql(write)
    return result, unknown_functions


@app.post("/api/v1/convert")
def convert():
    data = request.data
    j_data = json.loads(data)
    version = j_data["version"]
    audit = j_data["sql_query"]
    transformedSQL, unknown_function = transpile(
        j_data["sql_query"], j_data["from"], j_data["to"], j_data["case_sensitive"]
    )

    # Record SQL statements to log file
    if response_code == 1:
        logging.error(
            f'Received SQL query: {audit},Version: {version},From {j_data["from"]},To {j_data["to"]}'
        )
    elif unknown_function:
        logging.warning(
            f"Unknown_function: {unknown_function}, Received SQL query: {audit},Version: {version},From {j_data['from']},To {j_data['to']}"
        )
    else:
        logging.info(
            f"Received SQL query: {audit},Version: {version},From {j_data['from']},To {j_data['to']}"
        )

    response = {
        "version": version,
        "data": transformedSQL,
        "code": response_code,
        "message": "success" if response_code == 0 else "Error transpiling query",
    }

    return json.dumps(response)
