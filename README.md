# dflow_interview

В папке `last_release` находится исполняемый файл симулятора `PyHyCarSim.exe`. Он запускается в паре с входным файлом вида `input.py`

Запуск симулятора производится в командной строке:

```bash
PyHyCarSim.exe input.py
```

## Задача 1
В форке проекта создайте систему автотестов на основе имеющихся входных файлов вида `input.py`.

Автотесты должны проверять успешный запуск и отработку симуляции для всех входных файлов.

Для запуска автотестов используйте `pytest`.

Автотесты должны выполняться в виртуальном окружении, запушьте в репозиторий `requirements.txt`

## Задача 2

В папке `json` хранятся файлы с данными движения потока по скважине.

Файл `flow.json` содержит записи по времени для участка скважины "left_boundary". Напишите скрипт, который строит для указанного участка графики изменения массового расхода в зависимости от времени, параметры:

* Mass_flow_liquid_lc
* Mass_flow_gas_lc
* Mass_flow_water_lc

Значения параметров принимать положительными, все три графика построить на одном поле.

## Задача 3

Файл `output.json` содержит записи по времени для всех участков скважины. Напишите скрипт, который строит трехмерный график изменения давления (параметр `pressure`) вдоль профиля скважины в зависимости от времени.

-------
Предоставьте решённые задачи в виде ссылки на репозиторий проекта.
