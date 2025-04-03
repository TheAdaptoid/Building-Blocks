clear

echo -e "\nFormatting..."
black essential_building_blocks/

echo -e "\nLinting..."
pylint essential_building_blocks/

echo -e "\nTypechecking..."
mypy essential_building_blocks/

echo -e "\nTesting..."
pytest tests/ --cov=essential_building_blocks/