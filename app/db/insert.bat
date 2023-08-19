@echo off

curl -X POST -H "Content-Type: application/json" -d "{
    \"operand_one\": 5,
    \"operand_two\": 3,
    \"operator\": \"+\",
    \"result\": 8,
    \"date_of_creation\": \"2023-08-19\"
}" http://localhost:5555/insert
