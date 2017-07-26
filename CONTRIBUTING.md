# Настройка рабочего окружения

## Скачивание репозитория

После [первичной настройки Git](https://github.com/lambdafrela/lambda-help/tree/master/lectures/git/lecture_1#итак-с-чего-же-начать) сделай Fork репозитория и склонируй себе командой:
```
git clone https://github.com/<your name>/lambdaweb.git
```
или, если в системе установлен SSH ключ:
```
git clone git@github.com:<your name>/lambdaweb
```

## Установка Python

__На продакшене используется Python версии 3.4.3__ . Скачать можно [отсюда](https://www.python.org/downloads/release/python-343/), но в большинстве популярных дистрибутивах (Ubuntu, Fedora) он присутствует по умолчанию и вызывается командой `python3`.  
Вести разработку и тестировать локально можно и в более свежих версиях, например, 3.5 или 3.6 , но учитывать обратную совместимость (например, новые способы форматирования литералов и вот такие `1_000_000` числа, добавленные в 3.6, на рабочем сервере не заведутся).

## Создание virtualenv

### Linux

```bash
# устанавливаем virtualenv
sudo pip3 install virtualenv virtualenvwrapper

# указываем на интерпретатор нужной версии и скрипт для удобной работы
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

# указываем на директорию, в которой будем хранить окружение
export WORKON_HOME=/path/to/directory

# создаем новое окружение
mkvirtualenv lambdaweb
```

### Windows | MacOS | Linux (easy way)

Установите Pycharm :sparkles: 

## Включение линтеров

Наш проект придерживается правил оформления кода `pep8`, поэтому во избежание всякого - используем flake8 в качестве линтера. Допускаем превышение длины строки более 79 символов, больше -- ни-ни :angry:  
```
# устанавливаем
$ pip install flake8
```
Для запуска использовать конфигурационный файл `tox.ini`, находящийся в корне репозитория:
```
$ flake8 --config=tox.ini .
```
__Правильным шагом__ будет интеграция flake8 с Pycharm и Git. Сделать это можно по инструкции, описанной  [тут](https://habrahabr.ru/company/dataart/blog/318776/) .

## GitFlow
Ветвить проекты надо с умом. Вся разработка в нашем проекте идет только в ветке `develop` и соответствующих от нее ответвлениях. Для удобства работы необходимо установить `git flow`. Установка и использование описаны [тут](http://danielkummer.github.io/git-flow-cheatsheet/index.ru_RU.html)


> Ввиду скорой упаковки проект в docker-контейнер, эта инструкция может сильно измениться.
