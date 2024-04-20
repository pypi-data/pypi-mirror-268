# Cognite 3D Reveal Streamlit

This is a Streamlit library that can be used to show 3D models inside a Streamlit app. It works especially good when used inside Streamlit in Fusion, but can also be used in standalone Streamlit apps.

## How to install

You simply install it by running
`pip install cognite-streamlit-reveal`

## How to use

Here is an example app

```
import streamlit as st
import os
from cognite.streamlit import reveal
from cognite.client import CogniteClient

st.subheader("Cognite Reveal Streamlit example")
client = CogniteClient()
model_id = 123
revision_id = 234

selected_node_id = reveal(client, model_id, revision_id)
st.markdown("Selected node id: %d!" % int(selected_node_id))

```

## Local development

It's recommended to add a clean environment. You need `pip` and `node`.

Clone repo
`git clone https://github.com/cognitedata/hackathon-reveal-streamlit.git`

Install Python packages
`pip install streamlit`

Install NPM packages and start server

```
cd cognite/streamlit/reveal/frontend
yarn
HTTPS=true yarn start
```

Then open https://localhost:3001/ to accept bad certificate.

Open repo folder in another terminal. Install this package as development package
`pip install -e .`

Extract a token from Fusion, and start with

`COGNITE_TOKEN="TOKEN" streamlit run examples/example.py`

### Local development in fusion stlite

Make sure you have set (reveal/**init**.py:8)[reveal/__init__.py:8] to `_RELEASE = True`.

Step 1) Build front end component with `cd reveal/frontend && yarn && yarn build`
Step 2) Build streamlit component with `python -m build` (hint: `pip install build`)
Step 3) Start local server `python server.py`

Open Fusion, create a Streamlit app and add the following the installed package
`http://localhost:8000/dist/reveal_streamlit_component-0.0.1-py3-none-any.whl`

It will then load successfully inside Stlite.
