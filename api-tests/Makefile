ifdef tag
    tag = :
else
	tag = login;
endif


ifdef name
    name = :
else
	name = 1-sign_in;
endif

ifdef folder
    folder = :
else
	folder = access;
endif

by_folder: venv
	$(VENV) behave features/${folder}/

by_name: venv
	$(VENV) behave features/${name}.feature
by_name_tag: venv
	$(VENV) behave features/${name}.feature --tags @${tag}


all: venv
	$(VENV) behave

report: venv
	$(VENV) allure serve allure_reports

install: setup activate

dev: venv
	$(VENV) install --dev

no-lock: venv
	$(VENV) install --skip-lock

clean: venv
	$(VENV) --rm

fresh: clean install

.DEFAULT_GOAL := help

help:
	cat Makefile

setup:
		 ( \
 			python3.7 -m venv venv; \
			source venv/bin/activate; \
			pip install -r requirements.txt; \
			pip install --upgrade pip; \
		 )

activate:
		bash --rcfile "venv/bin/activate" -i



