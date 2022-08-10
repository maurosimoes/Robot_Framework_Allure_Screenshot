# Allure Screenshot fix | Robot Framework Selenium Library

***Language:EN-US***

1 - Install Python 3.7
        Windows OS: https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe

2 - Install Robot Framework
        `pip install robotframework`

3 - Install Selenium Library
        `pip install --upgrade robotframework-seleniumlibrary`

4 - Install Allure Reports
        `pip install allure-robotframework`

5 - Place the `SeleniumLibraryHelper.py` file inside a folder named `Helpers` in your project

6 - Call the Helper using Library sintaxe: `Library ./Helpers/SeleniumLibraryHelper.py`

You can run your project using the command: `robot -d ../Reports --listener allure_robotframework:../Reports ../Path_Your_Project_Folder_Here`, and run the reports using the command: `allure serve ../Reports`

***Language:PT-BR***

1 - Instale o Python versão 3.7
        Windows OS: https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe

2 - Instale o Robot Framework através do seguinte comando em seu terminal
        `pip install robotframework`

3 - Instale a Selenium Library através do seguinte comando em seu terminal
        `pip install --upgrade robotframework-seleniumlibrary`

4 - Instale o Allure Reports através do seguinte comando em seu terminal
        `pip install allure-robotframework`

5 - Coloque o arquivo `SeleniumLibraryHelper.py` dentro de uma pasta chamada `Helpers` no seu projeto

6 - Chame o Helper através da sintaxe Library: `Library ./Helpers/SeleniumLibraryHelper.py`

Você pode executar seu projeto através do seguinte comando: `robot -d ../Reports --listener allure_robotframework:../Reports ../Cole_o_Caminho_do_Projeto_Aqui`, e visualizar o Reports através do seguinte comando: `allure serve ../Reports`