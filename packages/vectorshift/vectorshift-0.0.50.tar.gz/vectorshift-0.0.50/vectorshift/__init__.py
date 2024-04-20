# __init__.py
import os

import vectorshift.deploy
import vectorshift.node
import vectorshift.pipeline
import vectorshift.vectorstore

api_key = os.environ.get('VECTORSHIFT_API_KEY')
public_key = os.environ.get('VECTORSHIFT_PUBLIC_KEY')
private_key = os.environ.get('VECTORSHIFT_PRIVATE_KEY')
