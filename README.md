# stepik-final-project
final project for the Selenium course on Stepik


# create new environment and activate it
python -m venv your_new_environment 
# run activate script
{your_env_name}\Scripts\activate.bat

# Load needed packets from the conf file
pip install -r requirements.txt

# Test test_main_page.py
pytest -v --tb=line --language=en test_main_page.py

