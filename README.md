BitTorrent Sync
===============
Описание
--------
Образ Docker для [BitTorrent Sync](http://www.getsync.com/).

Параметры
---------
### Разделы
`/data/` – родительсткий каталог куда будет сохранена папка доступная по секретному ключу.

### Переменные
Обязательные переменные **выделенны**.  

* **`KEY`** – секретный ключ BtSync. 
* `FOLDER` – поддиректория в подключенной к контейнеру дирректории куда будет сохраненно содержимое доступное по секретному ключу. По умолчанию "FOLDER".

Запуск
------
Для синхронизации файлов по известному ключу запустите контейнер со следюущими параметрами:
	
	docker run -d --name="btsync" \
				--env KEY="MYKEY" \
				--env FOLDER="MYFOLDER" \
				--volume /home/user/data/:/data/ \
				maksim77/btsync

### Пример
Например вот параметры для синхронизации последних выпусков подкаста [Радио-Т](http://www.radio-t.com/) в дирректорию `/home/maksim/data/Radio-T`:

	docker run -d --name="btsync" \
				--env KEY="BGDUABD2AAF4H2A324AG4DIACY7CPYAK7" \
				--env FOLDER="Radio-T" \
				--volume /home/maksim/data:/data/ \
				maksim77/btsync