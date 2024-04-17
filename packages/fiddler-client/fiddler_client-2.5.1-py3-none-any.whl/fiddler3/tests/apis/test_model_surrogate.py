from http import HTTPStatus

import pytest
import responses

from fiddler3.entities.job import Job
from fiddler3.entities.model import Model
from fiddler3.exceptions import NotFound
from fiddler3.schemas.deployment_params import DeploymentParams
from fiddler3.tests.apis.test_model import API_RESPONSE_200
from fiddler3.tests.constants import JOB_ID, MODEL_ID, MODEL_NAME, URL

SURROGATE_202_RESPONSE = {
    'data': {
        'job': {
            'id': JOB_ID,
            'name': 'Add model surrogate - manual',
        }
    },
    'api_version': '3.0',
    'kind': 'NORMAL',
}

SURROGATE_JOB_API_RESPONSE_200 = {
    'api_version': '3.0',
    'kind': 'NORMAL',
    'data': {
        'name': 'Add model surrogate - manual',
        'id': JOB_ID,
        'status': 'SUCCESS',
        'progress': 100.0,
        'error_message': None,
        'error_reason': None,
    },
}

SURROGATE_JOB_API_RESPONSE_400 = (
    {
        'error': {
            'code': 400,
            'message': f'Model {MODEL_NAME}/'
            f'{MODEL_NAME} already has artifact. Please '
            f'use update_model_artifact or update_model_surrogate '
            f'instead',
            'errors': [
                {
                    'reason': 'BadRequest',
                    'message': f'Model {MODEL_NAME}/'
                    f'{MODEL_NAME} already has artifact. '
                    f'Please use update_model_artifact or '
                    f'update_model_surrogate instead',
                    'help': '',
                }
            ],
        },
        'api_version': '3.0',
        'kind': 'ERROR',
    },
)

API_RESPONSE_404 = {
    'error': {
        'code': 404,
        'message': 'Model not found for the given identifier',
        'errors': [
            {
                'reason': 'ObjectNotFound',
                'message': 'Model not found for the given identifier',
                'help': '',
            }
        ],
    }
}

DEPLOYMENT_PARAMS = {'deployment_type': 'MANUAL', 'cpu': 1000}


@responses.activate
def test_add_model_surrogate() -> None:
    responses.get(
        url=f'{URL}/v3/models/{MODEL_ID}',
        json=API_RESPONSE_200,
    )
    model = Model.get(id_=MODEL_ID)

    responses.post(
        url=f'{URL}/v3/models/{MODEL_ID}/deploy-surrogate',
        json=SURROGATE_202_RESPONSE,
    )

    responses.get(
        url=f'{URL}/v3/jobs/{JOB_ID}',
        json=SURROGATE_JOB_API_RESPONSE_200,
    )

    job_obj = model.add_surrogate(
        deployment_params=DeploymentParams(**DEPLOYMENT_PARAMS)
    )
    assert isinstance(job_obj, Job)


@responses.activate
def test_add_model_surrogate_no_model() -> None:
    responses.get(
        url=f'{URL}/v3/models/{MODEL_ID}',
        json=API_RESPONSE_200,
    )
    model = Model.get(id_=MODEL_ID)

    responses.post(
        url=f'{URL}/v3/models/{MODEL_ID}/deploy-surrogate',
        json=API_RESPONSE_404,
        status=HTTPStatus.NOT_FOUND,
    )

    with pytest.raises(NotFound):
        model.add_surrogate(deployment_params=DeploymentParams(**DEPLOYMENT_PARAMS))


@responses.activate
def test_update_model_surrogate() -> None:
    responses.get(
        url=f'{URL}/v3/models/{MODEL_ID}',
        json=API_RESPONSE_200,
    )
    model = Model.get(id_=MODEL_ID)

    responses.put(
        url=f'{URL}/v3/models/{MODEL_ID}/deploy-surrogate',
        json=SURROGATE_202_RESPONSE,
    )

    responses.get(
        url=f'{URL}/v3/jobs/{JOB_ID}',
        json=SURROGATE_JOB_API_RESPONSE_200,
    )

    job_obj = model.update_surrogate(
        deployment_params=DeploymentParams(**DEPLOYMENT_PARAMS)
    )
    assert isinstance(job_obj, Job)


@responses.activate
def test_update_model_surrogate_no_model() -> None:
    responses.get(
        url=f'{URL}/v3/models/{MODEL_ID}',
        json=API_RESPONSE_200,
    )
    model = Model.get(id_=MODEL_ID)

    responses.put(
        url=f'{URL}/v3/models/{MODEL_ID}/deploy-surrogate',
        json=API_RESPONSE_404,
        status=HTTPStatus.NOT_FOUND,
    )

    with pytest.raises(NotFound):
        model.update_surrogate(deployment_params=DeploymentParams(**DEPLOYMENT_PARAMS))
