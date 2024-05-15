Необходимо создать систему управления паролями, которая поможет пользователям генерировать, хранить и обновлять надежные пароли. В выполнении каждого из этапов проекта вам понадобятся знания и умения, которые вы освоили в рамках нашего курса.

Проект выполняется в группах по 3 - 4 человека. Вашей команде предстоит совместно разработать систему управления паролями, которая будет способна помогать пользователям создавать и хранить надежные пароли. Система должна реализовывать следующие функции:

1. Генерация паролей: Пользователи могут генерировать случайные пароли с заданными критериями безопасности.

2. Хранение паролей: Пользователи могут сохранять пароли в защищенном хранилище.

3. Управление паролями: Пользователи могут просматривать, обновлять и удалять свои пароли.

4. Обеспечение безопасности: Предусмотрите меры безопасности, чтобы защитить пароли от утечек и несанкционированного доступа.

Для эффективной работы вам нужно будет распределить между членами команды задачи каждого этапа проекта (отдельные его пункты). Это ускорит написание общей итоговой программы и обеспечит более высокое качество проекта.

Этапы реализации проекта

Этап 1

Планирование и проектирование системы

● Определите требования к системе и ее функциональности на основе задания. Определите функциональные и нефункциональные требования к системе управления паролями. Например, требования к генерации паролей, хранению, управлению и безопасности. (вы изучали это в теме 4.1 “Основы веб-разработки”)

● Разработайте структуру базы данных для хранения паролей и другой информации (если требуется). Выберете какую базу данных вы будете использовать (например, SQLite) и создайте соответствующую схему таблиц. Создайте таблицу "Passwords" с полями, такими как "id", "username", "password", "created_at",

"updated_at".(это тоже вам знакомо из темы 1.4 “Работа с файлами и обработка исключений”)

● Разработайте пользовательский интерфейс системы, учитывая требования пользователей. (с этим вы имели дело в рамках освоения темы 4.1 “Основы веб-разработки”)

Этап 2

Создание основных функций системы

● Создайте функцию для генерации случайных паролей с заданными критериями безопасности, используя модуль random в Python. Создайте функцию generate_password(length) для генерации пароля заданной длины (вы изучали это в теме 1.1 “Введение в Python”)

● Реализуйте функцию для сохранения паролей в защищенном хранилище, например, в базе данных с использованием модуля sqlite3. (это вам уже знакомо из темы 1.3 “Функции и модули”)

● Создайте функцию для просмотра, обновления и удаления паролей из хранилища. Создайте функции get_passwords(), update_password(id, new_password) и delete_password(id) для работы с паролями в базе данных. (это тоже вам известно, тема 1.3 “Функции и модули”)

Этап 3

Обеспечение безопасности

● Примените меры безопасности для защиты паролей, например, хэширование или шифрование паролей перед их сохранением, используя модуль hashlib в Python. Создайте функцию hash_password(password) для хэширования пароля (вы изучали это в теме 2.4 “Эксплуатация и защита от атак”)

● Защитите систему от распространенных атак, таких как инъекции SQL или межсайтовые скриптинг, соблюдая рекомендации безопасности. (это вам знакомо из темы 2.4 “Эксплуатация и защита от атак” и темы 3.3 “Защита сети и обнаружение атак” )

● Разработайте механизм аутентификации и авторизации пользователей, чтобы обеспечить доступ только авторизованным пользователям. (это вы также освоили в рамках темы 2.4 “Эксплуатация и защита от атак” и темы 3.3 “Защита сети и обнаружение атак”)