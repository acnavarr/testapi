para ejecutar el proyecto, recreamos un ambiente virtual

ejecutamos en consola:

python3.7 -m venv venv; \
source venv/bin/activate; \
pip install -r requirements.txt; \
pip install --upgrade pip; \



para ver los resultados con ayuda de allure

behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
allure serve %allure_result_folder%
