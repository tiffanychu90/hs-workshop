FROM jupyter/datascience-notebook:python-3.8.5

# Install conda requirements
COPY conda-requirements.txt /tmp/
RUN conda install --yes -c conda-forge --file /tmp/conda-requirements.txt

# Install pip requirements
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# This might prevent Docker container from building, so let's comment it out
# Make sure vega-cli are available for altair export
#RUN npm install -g --unsafe --force vega vega-cli vega-lite canvas