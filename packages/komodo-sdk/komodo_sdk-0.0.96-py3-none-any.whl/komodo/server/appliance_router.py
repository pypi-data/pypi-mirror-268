import json
from pathlib import Path

from fastapi import Depends, APIRouter

from komodo.server.globals import get_appliance, get_email, get_user, get_version

router = APIRouter(
    prefix='/api/v1/appliance',
    tags=['Appliance']
)


@router.get('/description', response_model=dict, summary='Get appliance description',
            description='Get the description of the appliance.')
def get_appliance_description(appliance=Depends(get_appliance)):
    return {
        "shortcode": appliance.shortcode,
        "name": appliance.name,
        "company": appliance.company,
        "type": appliance.type.name,
        "features": ", ".join([f.name for f in appliance.features]),
        "version": get_version(),
        "purpose": appliance.purpose
    }


@router.get('/configuration', response_model=dict, summary='Get appliance configuration',
            description='Get the configuration of the appliance.')
def get_appliance_configuration(user=Depends(get_user), appliance=Depends(get_appliance)):
    return appliance.configuration(user)


@router.get('/index', summary='Index all data sources',
            description='Index all data sources for the appliance.')
def index_all_data_sources(appliance=Depends(get_appliance)):
    appliance.index(reindex=False)
    return {"status": "success"}


@router.get('/reindex', summary='Re-index all data sources.',
            description='Deletes all existing data and re-indexes all data sources for the appliance.')
def re_index_all_data_sources(appliance=Depends(get_appliance)):
    appliance.index(reindex=True)
    return {"status": "success"}


@router.get('/available-agents', summary='Get available agents',
            description='Get available agents for the appliance for a given feature.')
def get_available_agents(email=Depends(get_email), appliance=Depends(get_appliance)):
    agents = appliance.get_all_agents()
    return {"status": "success"}


@router.get('/firebase-config', response_model=dict, summary='Get firebase configuration',
            description='Get the firebase configuration related to the appliance.')
def get_firebase_configuration(user=Depends(get_user), appliance=Depends(get_appliance)):
    config = appliance.config
    if config is None:
        return {}

    config_file = config.get_firebase_config()
    if Path(config_file).exists():
        with open(config_file, 'r') as file:
            firebaseConfig = json.load(file)
            return firebaseConfig

    return {}
