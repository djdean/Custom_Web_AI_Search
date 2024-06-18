import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="generate_embedding", methods=[func.HttpMethod.GET, func.HttpMethod.POST])
def generate_embedding(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    try:
        processed_data = custom_processing_function(req_body)
        return func.HttpResponse(
                json.dumps(processed_data),
                status_code=200,
                mimetype="application/json"
            )
    except ValueError:
        return func.HttpResponse(
            "Invalid input",
            status_code=400
        )
def custom_processing_function(data):
    values = data["values"]
    output_values = {}
    output_values["values"] = []
    for record in values:
        output_record = {}
        output_record["recordId"] = record["recordId"]
        data = record["data"]
        content = data["text"]
        output_record["data"] = {"embedding": content}
        output_record["warnings"] = None
        output_record["errors"] = None
        output_values["values"].append(output_record)
    return output_values