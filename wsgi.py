from flask import request
from flask_api import FlaskAPI, status, exceptions

from crp_api.crp_validation import CRPValidation
from conf import Config


app = FlaskAPI(__name__)
crpv = CRPValidation(Config)


@app.route("/api/crp", methods=['GET'])
def crp():
    try:
        cpf = request.data['cpf']
        crp = request.data['crp']

    except KeyError:
        return {'response': "'crp' and 'cpf' must be provided" }, status.HTTP_400_BAD_REQUEST

    valid_crp, user_data = crpv.validate_crp_register(crp, cpf)

    return {
        'valid_crp': valid_crp,
        'user_data': user_data
    }, status.HTTP_200_OK

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
