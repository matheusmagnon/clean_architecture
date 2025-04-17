-Criar venv
python3 -m venv venv

-Gera pylintrc
pylint --generate-rcfile > .pylintrc

-Install all requirements
venv/bin/pip3 install -r requirements.txt

pip3 install pre-commit

pre-commit install
