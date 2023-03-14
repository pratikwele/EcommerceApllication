@ECHO OFF
Rem firefox

pytest -s -v -rA -m "sanity" --html=./Reports/report11.html TestCases/ --browser_name firefox
Rem pytest -s -v -rA -m "regression" --html=./Reports/report11.html TestCases/ --browser_name firefox
Rem pytest -s -v -rA -m "sanity or regression" --html=./Reports/report11.html  TestCases/ --browser_name firefox
Rem pytest -s -v -rA -m "sanity and regression" --html=./Reports/report11.html  TestCases/ --browser_name firefox

Rem chrome

Rem pytest -s -v -rA -m "sanity "--html=./Reports/report11.html TestCases/ --browser_name chrome
Rem pytest -s -v -rA -m "regression" --html=./Reports/report11.html TestCases/ --browser_name chrome
Rem pytest -s -v -rA -m "sanity or regression" --html=./Reports/report11.html  TestCases/ --browser_name chrome
Rem pytest -s -v -rA -m "sanity and regression" --html=./Reports/report11.html  TestCases/ --browser_name chrome








PAUSE