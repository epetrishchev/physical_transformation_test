# Physical_Transformation_test

Установка зависимостей

```
python -m pip install -r requirements.txt
```

Запуск всех тестов

```
python -m pytest
```

Запуск тестов отдельно взятого модуля

```
python -m pytest balance/tests/test_118_nodes.py
```

Запуск тестов с обновлением снепшотов

```
python -m pytest --snapshot-update
```

При вызове теста с флагом `-s` выводятся логи, созданные при помощи `print`

```
python -m pytest -s
```

Запуск тестов с замером времени их исполнения

```
python -m pytest --durations=0
```