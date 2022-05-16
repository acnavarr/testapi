# testapi
el proyecto permite probar API´s, con la implementacion de la libreria request, los pasos estan pametrizados y se pueden reutilizar
en este caso contiene los casos de pruebas sobre los servicios de breeds en https://documenter.getpostman.com/view/5578104/RWgqUxxh#3cd6ebfd-338d-4a38-9929-f879a6bb0bd1

para ejecutar el proyecto, recreamos un ambiente virtual

ejecutamos en consola:

python3.7 -m venv venv; \
source venv/bin/activate; \
pip install -r requirements.txt; \
pip install --upgrade pip; \

ejecutar los escenario : make by_name name=breeds

para ver los resultados con ayuda de allure

behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
allure serve %allure_result_folder%
